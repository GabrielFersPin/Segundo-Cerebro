---
created: 2026-05-20 01:02
modified: 2026-05-20 01:02
area: "Machine Learning"
tipo_nota: captura_rapida
status: 🔴 Por procesar
nivel-comprension: "❓"
proxima-revision: 2026-05-27
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
cards-deck: AWS::SageMaker_AI
tags: [captura_rapida, 2026-05-20]
---

# SageMaker AI

> [!info] Metadata
> **Fecha**: 2026-05-20
> **Área**: Machine Learning

---

# SageMaker AI

SageMaker is a fully managed service that provides all the tools and infrastructure needed to build, train, and deploy machine learning models at scale. It abstracts away the complexities of managing infrastructure, allowing data scientists to focus on model development and experimentation. SageMaker offers a comprehensive suite of services for every stage of the machine learning workflow.

Provides:

- Deployment with one click or a single API call
- Automatic scaling
- Model hosting services
- HTTPS endpoints for secure model access

You can use SageMaker to deploy a model to get predictions in several ways:

### Real Time

Real time inference is ideal for inference workloads where you have real-time interactive, and low latency requirements

### Batch Transform

Batch Transform is ideal for inference workloads where you have large amounts of data to process and you don't need real-time predictions

### Asynchronous

SageMaker AI asynchronous inference is a capability in SageMaker AI that queues incoming requests and processes them asynchronously.

### Serverless

On-demand serverless inference is a capability in SageMaker AI that provides serverless inference for machine learning models.

## Sagemaker JumpStart

Is a feature of Sagemaker AI that provides pre-trained, open source models for you to use. SageMaker JumpStart offers FMs that you can use for summarization use cases.

## Sagemanker Canvas

- Create data flows feature engineering workflows that use little to no coding.

- You can use Jupter Lab

## Amazon SageMaker Studio Classic

- Provides a built-in integration with Amazon EMR (Elastic Mapreduce) - Diseñado para el procesamiento de datos a gran escala.

## Amazon SageMaker Feature Store 

- feature descovery and storage, 
- Provide a centralized repository to store feature data in a standardized format.

## Amazon SageMaker Clarify

- Analize your data and detect potential biases across multiple facets.
- Helps you detect whether your trainning data contains imbalanced representations or labeling biases between groups such as gender, race or age.

## Amazon Ground Truth

- Automate the labeling of the data
- 

## Amazon SageMaker Serverless Inferencing

- Requires little managment to host the model

## Amazon SageMaker Model Monitor

- Monitor data quality
- Compares the model and the data with the baselines
- It generates statistics and metrics that are visible in SageMaker Studio

## SageMaker Model Registry

- Store models catalog

## SageMaker Model Cards

- Document, Retrieve and share essential model information from conception to deplyoment
- Model cards can be exports to PDF to share with stakeholders






## 🎴 Flashcards

¿Qué es SageMaker AI?::Es un servicio completamente administrado que proporciona herramientas e infraestructura para construir, entrenar y desplegar modelos de machine learning a escala. #card <!--SR:!2026-06-02,1,230-->
¿Cuáles son las 4 formas de desplegar un modelo para inferencia en SageMaker?::Real Time, Batch Transform, Asynchronous y Serverless. #card <!--SR:!2026-06-02,1,230-->
¿Qué es SageMaker JumpStart?::Una característica que proporciona modelos de código abierto pre-entrenados listos para usar (ej. Foundation Models para resúmenes). #card <!--SR:!2026-06-02,1,230-->
¿Para qué sirve Amazon SageMaker Canvas?::Para crear flujos de datos y de ingeniería de características con poco o ningún código. #card <!--SR:!2026-06-02,1,230-->
¿Cuál es la función de Amazon SageMaker Feature Store?::Proporcionar un repositorio centralizado para descubrir y almacenar datos de características (features) en un formato estandarizado. #card <!--SR:!2026-06-02,1,230-->
¿Qué permite hacer Amazon SageMaker Clarify?::Analizar los datos y detectar posibles sesgos (ej. de género, raza o edad) y representaciones desbalanceadas. #card <!--SR:!2026-06-02,1,230-->
¿Qué servicio se utiliza para etiquetar datos en el ecosistema de SageMaker?::Amazon Ground Truth. #card <!--SR:!2026-06-02,1,230-->
¿Qué hace Amazon SageMaker Model Monitor?::Monitorea la calidad de los datos comparando el modelo y los datos con líneas base, generando métricas visibles en SageMaker Studio. #card <!--SR:!2026-06-02,1,230-->
¿Para qué sirve SageMaker Model Registry?::Para almacenar y catalogar modelos. #card <!--SR:!2026-06-02,1,230-->
¿Qué son las SageMaker Model Cards?::Documentan, recuperan y comparten información esencial del modelo desde su concepción hasta su despliegue (exportables a PDF). #card <!--SR:!2026-06-02,1,230-->
