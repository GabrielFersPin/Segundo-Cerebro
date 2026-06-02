---
tags: [AWS, certificacion, AI-Practitioner, AI, ML]
deck: AWS::AI_Practitioner
created: 2026-06-01 14:56
status: 🟢 Procesada
---

# 📝 AWS AI Practitioner - Servicios Clave

> [!info] Metadata
> **Certificación**: AWS Certified AI Practitioner (AIF-C01)
> **Objetivo**: Memorizar los servicios principales de IA/ML de AWS para el examen.

---

## 1. 🧠 Inteligencia Artificial Generativa y Asistentes
Estos servicios son el núcleo de la estrategia moderna de IA en AWS.

- **Amazon Bedrock**: Servicio gestionado para acceder a Foundation Models (FMs) de terceros y de Amazon a través de una API. Permite construir y escalar aplicaciones de IA generativa de forma segura.
- **Amazon Q**: Asistente impulsado por IA generativa.
  - **Amazon Q Business**: Para responder preguntas, redactar contenido y realizar tareas basadas en los datos empresariales.
  - **Amazon Q Developer**: Asistente de codificación y desarrollo (evolución de CodeWhisperer).
- **Guardrails for Amazon Bedrock**: Herramienta para implementar salvaguardas, filtrar contenido dañino y aplicar políticas de IA responsable.
- **AWS AI Service Cards**: Documentación pública de AWS que proporciona transparencia sobre cómo funcionan sus servicios de IA (casos de uso, limitaciones, consideraciones éticas).

## 2. ⚙️ Plataforma de Machine Learning (SageMaker)
SageMaker proporciona herramientas para construir, entrenar y desplegar modelos a escala.

- **Amazon SageMaker**: Servicio completo para todo el ciclo de vida del ML.
- **SageMaker JumpStart**: Hub de ML que ofrece FMs pre-entrenados y soluciones integradas listas para usar.
- **SageMaker Canvas**: Interfaz visual sin código (no-code) para que analistas de negocio construyan modelos de ML y generen predicciones.
- **SageMaker Clarify**: Herramienta para detectar sesgos en datos/modelos y explicar predicciones (IA responsable).
- **SageMaker Feature Store**: Repositorio centralizado para almacenar, descubrir y compartir variables (features) de ML.
- **SageMaker Model Monitor**: Monitorea continuamente la calidad de los modelos en producción (detecta *data drift* y *model drift*).
- **SageMaker Ground Truth**: Servicio para etiquetar (label) grandes volúmenes de datos de entrenamiento usando fuerza de trabajo humana o IA.

## 3. 👁️ Servicios de IA Cognitivos (API Services)
Servicios pre-entrenados listos para usar que no requieren experiencia en Machine Learning.

### Visión y OCR
- **Amazon Rekognition**: Análisis de imágenes y video (detección de rostros, objetos, texto, contenido inapropiado).
- **Amazon Textract**: Extracción de texto, escritura a mano y datos estructurados de documentos escaneados y PDFs.

### Lenguaje de Texto (NLP)
- **Amazon Comprehend**: Procesamiento de lenguaje natural (NLP) para descubrir insights, entidades y sentimientos en texto.
- **Amazon Translate**: Traducción automática de idiomas precisa y en tiempo real.
- **Amazon Lex**: Construcción de interfaces conversacionales (chatbots) usando voz y texto.

### Búsqueda y Recomendación
- **Amazon Kendra**: Motor de búsqueda inteligente impulsado por ML para encontrar información en bases de conocimiento empresariales.
- **Amazon Personalize**: Crea experiencias personalizadas y recomendaciones de productos para los usuarios.

### Voz y Audio
- **Amazon Transcribe**: Convierte voz a texto (Speech-to-Text).
- **Amazon Polly**: Convierte texto en habla que suena natural (Text-to-Speech).

### Análisis Específicos
- **Amazon Forecast**: Predicción de series temporales (ej. demanda, ventas, inventario) usando algoritmos de ML.

## 4. 🖥️ Infraestructura de Hardware (Chips personalizados)
Chips diseñados específicamente por AWS para optimizar cargas de trabajo de ML.

- **AWS Inferentia**: Aceleradores de silicio diseñados para **inferencia** de alto rendimiento y bajo costo.
- **AWS Trainium**: Aceleradores de silicio optimizados específicamente para **entrenar** modelos de deep learning de forma más económica.


### 5. Seguridad, Compliance y Gobernanza

- **Amazon Fraud Detector**: Es un servicio que usa ML para identificar potenciales actividades fraudulentas.
---

## 🎴 Flashcards

¿Qué servicio de AWS ofrece acceso a diversos Foundation Models mediante una API unificada?::Amazon Bedrock #card <!--SR:!2026-06-05,4,270-->
¿Cuál es la diferencia principal entre AWS Trainium y AWS Inferentia?::Trainium se usa para el ==entrenamiento== de modelos, mientras que Inferentia está optimizado para la ==inferencia== (despliegue) de menor costo. #card
Amazon Bedrock:::Servicio gestionado de AWS para consumir y crear aplicaciones de IA Generativa con modelos fundacionales (FMs). #card <!--SR:!2026-06-04,3,250!2026-06-02,1,230-->
¿Para qué sirve Amazon SageMaker Canvas?::Para que analistas de negocio puedan crear modelos de ML y generar predicciones mediante una interfaz visual **sin necesidad de programar** (no-code). #card
¿Qué servicio extrae texto, escritura a mano y datos estructurados de documentos y formularios escaneados?::Amazon Textract #card <!--SR:!2026-06-05,4,270-->
¿Qué herramienta de SageMaker utilizarías para detectar sesgos (bias) en tus datos de entrenamiento y entender las predicciones de tu modelo?::Amazon SageMaker Clarify #card
Amazon Rekognition:::Servicio de análisis de imagen y video impulsado por IA para identificar objetos, personas, texto y contenido inapropiado. #card <!--SR:!2026-06-05,4,270!2000-01-01,1,250-->
¿Qué hace Amazon Polly?::Convierte texto a voz natural (Text-to-Speech). #card <!--SR:!2026-06-02,1,230-->
Amazon Transcribe:::Servicio que convierte voz a texto (Speech-to-Text). #card <!--SR:!2026-06-02,1,230!2026-06-04,3,250-->
¿Qué servicio usarías para añadir una búsqueda inteligente empresarial a tus bases de conocimiento interno?::Amazon Kendra #card
¿Qué es Amazon Q?::Un asistente impulsado por IA generativa. Tiene variantes como Q Business (empresas) y Q Developer (programación). #card <!--SR:!2026-06-02,1,230-->
¿Para qué se utiliza Amazon Personalize?::Para añadir recomendaciones personalizadas en tiempo real a las aplicaciones. #card <!--SR:!2026-06-02,1,230-->
Amazon Lex:::Servicio para crear interfaces conversacionales (chatbots) integrando voz y texto. #card <!--SR:!2026-06-02,1,230!2026-06-04,3,250-->
¿Qué son las AWS AI Service Cards?::Documentación transparente creada por AWS que explica el uso previsto, limitaciones y consideraciones de IA responsable para sus servicios de inteligencia artificial. #card
¿Qué herramienta se usa para monitorear modelos de ML en producción y detectar desviaciones de datos (data drift)?::Amazon SageMaker Model Monitor #card <!--SR:!2026-06-02,1,230-->
Amazon Comprehend:::Servicio de NLP que extrae información, entidades clave y sentimientos de textos no estructurados. #card <!--SR:!2026-06-04,3,250!2026-06-02,1,230-->
¿Qué servicio automatiza la traducción de grandes volúmenes de texto con alta precisión?::Amazon Translate #card
SageMaker JumpStart:::Hub de machine learning en AWS que proporciona FMs de código abierto y soluciones pre-entrenadas listas para desplegar. #card <!--SR:!2000-01-01,1,250!2026-06-02,1,230-->
¿Qué herramienta implementa salvaguardas personalizadas y filtra contenido dañino en aplicaciones construidas sobre Foundation Models?::Guardrails for Amazon Bedrock #card <!--SR:!2026-06-04,3,250-->
Amazon Forecast:::Servicio de IA que utiliza datos históricos para predecir métricas futuras (series temporales), como la demanda de productos o inventario. #card <!--SR:!2026-06-04,3,250!2026-06-02,1,230-->
¿Qué servicio utilizarías si necesitas que humanos etiqueten grandes volúmenes de datos (data labeling) para entrenar tus modelos?::Amazon SageMaker Ground Truth #card
