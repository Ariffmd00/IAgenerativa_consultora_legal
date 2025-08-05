import pandas as pd 
from sentence_transformers import SentenceTransformer
import faiss
from transformers import pipeline
import numpy as np

# 1. Cargar el archivo Excel
df = pd.read_excel('Datos/sentencias_pasadas.xlsx', sheet_name='Hoja1')

# 2. Concatenar las columnas para un análisis más sencillo
df["documento"] = (
    "Caso: " + df["#"].astype(str) + " " + df["Providencia"].astype(str) +
    " - " + df["Tema - subtema"].astype(str) + ".  " +
    "Síntesis: " + df["sintesis"].astype(str) + ".  " +
    "Resolución: " + df["resuelve"].astype(str)
)

documentos = df["documento"].tolist()


# 3. Crear embeddings con modelo de lenguaje
modelo = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = modelo.encode(documentos, convert_to_numpy=True)

# 4. Crear índice de búsqueda semántica con FAISS
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

# 5. Cargar modelo de preguntas y respuestas
qa = pipeline("question-answering", model="deepset/roberta-base-squad2")

# 6. Función para responder preguntas
def responder_pregunta(pregunta):
    pregunta_embedding = modelo.encode([pregunta], convert_to_numpy=True)
    D, I = index.search(pregunta_embedding, k=10)

    # Concatenar los 3 documentos más similares
    contexto = " ".join([documentos[idx] for idx in I[0]])

    respuesta = qa({
        'question': pregunta,
        'context': contexto
    })

    print("Pregunta:", pregunta)
    print("Contexto (truncado):", contexto[:500], "...")
    print("Respuesta:", respuesta['answer'])


# 7. Preguntas de ejemplo
preguntas = [
    "¿Cuáles son las sentencias de 3 demandas?",
    "¿De qué se trataron las 3 demandas anteriores?",
    "¿Cuál fue la sentencia del caso que habla de acoso escolar?",
    "¿Diga el detalle de la demanda relacionada con acoso escolar?",
    "¿Existen casos que hablan sobre el PIAR, indique de qué trataron los casos y cuáles fueron sus sentencias?"
]

# Ejecutar preguntas
for pregunta in preguntas:
    responder_pregunta(pregunta)
