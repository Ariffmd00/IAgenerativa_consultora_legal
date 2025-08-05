---


---

<h1 id="caso-2---asesor-legal-para-consulta-historia-de-demandas">Caso 2 - Asesor legal para consulta historia de demandas</h1>
<h2 id="explicación-del-caso">Explicación del caso</h2>
<p>Un consultor legal está buscando automatizar procesos de búsqueda de demandas pasadas, para presentarlas a los clientes. Por ello, se plantea utilizar una inteligencia artificial generativa, para automatizar las respuestas y búsquedas de casos para ayudar a dar respuesta a los clientes.</p>
<h2 id="supuestos">Supuestos</h2>
<p>1.-No se necesita información adicional.<br>
2.- Las respuestas son simples y concisas.<br>
3.- Se espera que tanto las preguntas como las respuestas sean en lenguaje natural.</p>
<h2 id="formas-de-resolver-el-caso-y-opción-tomada-en-esta-prueba">Formas de resolver el caso y opción tomada en esta prueba</h2>
<p>La idea principal para resolver el caso fue utilizar un NLP(procesamiento de lenguaje natural), el cual recibe una pregunta y busca en los documentos el que más se parezca. Se siguió el proceso:<br>
1.- Lectura de datos<br>
2.- Concatenar las columnas para un análisis más sencillo<br>
3.- Se utiliza un embeddings con la librería SentenceTransformer para convertir los datos en vectores numéricos<br>
4.- Se empleo FAISS para crear un índice semántico para encontrar un documento más parecido a la pregunta.<br>
4.- Se cargó un modelo de preguntas y respuestas <code>( deepset/roberta-base-squad2)</code> para dar una respuesta usando la fuente de datos<br>
5.- Con la función <strong>responder pregunta</strong> se reciben las preguntas, busca el documento más parecido y responde en lenguaje natural.</p>
<h2 id="resultado-del-análisis-de-datos-y-de-los-modelos">Resultado del análisis de datos y de los modelos</h2>
<p>Después de ejecutar todo el proceso de limpieza, transformación, vectorización y preparación de los datos para el sistema de preguntas coloquiales. El sistema lograr identificar los textos más cercanos(esto por el modelo all-mpnet-base-v2 y la búsqueda semántica FAISS) sin embargo, el rendimiento del modelo de respuesta, no está funcionando de la forma esperada.<br>
Observaciones:</p>
<ul>
<li>Posiblemente, no se logra entender al 100% el contexto  de los textos por su longitud.</li>
<li>Se intentó aumentar el rango K (número de documentos de consulta) pero esto no hizo cambios significativos en la respuesta.</li>
<li>Las respuestas obtenidas son  irrelevantes.<br>
Como resultado de este análisis,  la primera parte de identificación de similitudes funciona correctamente, pero las respuestas necesitan  mejoras.</li>
</ul>
<h2 id="futuros-ajustes-o-mejoras">Futuros ajustes o mejoras</h2>
<p>Dado que no se obtuvieron los resultados esperados, se plantean ideas y mejoras para aumentar la calidad del sistema:</p>
<ul>
<li>Dado que el sistema dé respuestas no funciona de la forma esperada, es posible cambiar a otros modelos como <strong>flan-t5</strong>  o **utilizar una API de ChatGPT  ** para obtener mejores respuestas.</li>
<li>Agregar una interfaz para ser más amigable para los usuarios</li>
<li>Limitar el contenido de las columnas a solo un par de ellas.</li>
</ul>
<h2 id="apreciaciones-y-comentarios-del-caso">Apreciaciones y comentarios del caso</h2>
<p>Realizar este ejercicio me ayudó a entender un poco más de la importancia de la utilización de inteligencia artificial generativa con respecto a los datos  en casos reales. El principal reto fue la investigación,  el tipo de inteligencias artificiales generativas con sus beneficios y determinar cuál podría ayudarme para este caso.<br>
Aun así, considero que el aprendizaje fue muy bueno y muy enriquecedor, ya que apliqué:</p>
<ul>
<li>Limpieza de datos</li>
<li>Conversión de textos a vectores con <strong>sentence-transformers</strong></li>
<li>Utilizar  FAISS para crear un índice semántico para crear un pipeline de preguntas</li>
</ul>

