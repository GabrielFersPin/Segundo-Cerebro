---
created: 2026-05-20 11:25
modified: 2026-08-22
area: Machine Learning
tipo_nota: captura_rapida
status: 🌿 Creciendo
nivel-comprension: 💡
dias-para-revision: 2
ultima-revision: 2026-08-22
veces-revisado: 3
tiempo-repaso: ""
cards-deck: ""
tags:
  - captura_rapida
  - 2026-05-20
proxima-revision: 2026-08-25
tiempo-estimado: 20min
---

# AWS Services for MLOps

> [!info] Metadata
> **Fecha**: 2026-05-20
> **Área**: Machine Learning

---

# AWS Sagemaker Services

## Data Preparation

**Prepare Data**

[[AWS SageMaker Data Wrangler]]: a tool for data preparation and feature engineering

[[AWS SageMaker Processing job]]: a tool for data processing and feature engineering

**Curate features**

[[AWS SageMaker Feature Store]]: a tool for feature storage and retrieval

## Training and Tuning

**Experiment tracking**

[[AWS SageMaker Experiments]]: a tool for tracking ML experiments

**Train models**

[[AWS SageMaker Trainning Jobs]]: a tool for training ML models

**Evaluate model**

Sagemaker Processing Job: a tool for evaluating ML models

**Register models**

Sagemaker Model Registry: a tool for registering ML models

## Deploy and manage

**Deploy models**

[[AWS SageMaker JumpStart]]: A hub of pre-built models to easy deploy

[[AWS SageMaker Endpoints]]: a tool for deploying ML models

**Inferece**

[[AWS SageMaker Inference]]: a tool for inference with ML models

**MLOps Pipelines**

[[AWS SageMaker Pipelines]]: a tool for orchestrating ML workflows

**Model Monitoring**

[[AWS SageMaker Model Monitor]]: a tool for monitoring ML model performance

**AutoML**

[[AWS SageMaker Autopilot]]: a tool for automated machine learning

## Governance and security

**Explain models**

[[AWS SageMaker AI Clarify]]: a tool for model explainability and bias detection

**Track model lineage**

[[AWS SageMaker Lineage]]]: a tool for tracking model lineage

**Audit models**

[[AWS SageMaker Model Cards]]: a tool for model documentation and auditing

---

## 🎴 Flashcards

¿Cuándo usarías SageMaker Data Wrangler?::Para limpiar un dataset de ventas, unir tablas, transformar columnas y preparar features antes de entrenar un modelo de churn. #card #mlops #datascience
¿Cuándo usarías SageMaker Processing Job?::Cuando quieres ejecutar un preprocesamiento por lotes, crear features nuevas o evaluar un dataset antes del entrenamiento sin entrar en un pipeline completo. #card #mlops #preprocessing
¿Para qué sirve SageMaker Feature Store?::Para guardar features reutilizables como “historial de compras del cliente” y usarlas tanto en entrenamiento como en inferencia de forma consistente. #card #mlops #features
¿Cuándo usarías SageMaker Experiments?::Cuando estás comparando varios modelos de clasificación con distintos hiperparámetros y quieres mantener un registro del rendimiento. #card #mlops #experiments
¿Para qué sirve un Training Job en SageMaker?::Para entrenar un modelo con un conjunto de datos y ajustar pesos/hiperparámetros en un entorno escalable y gestionado. #card #mlops #training
¿Cuándo usarías SageMaker Model Registry?::Cuando ya tienes un modelo ganador y quieres registrarlo, versionarlo y mantener seguimiento antes de desplegarlo en producción. #card #mlops #modelregistry
¿Para qué se usa SageMaker JumpStart?::Para arrancar rápido con modelos ya entrenados o plantillas listas, por ejemplo un clasificador de texto o una visión preentrenada. #card #mlops #jumpstart
¿Cuándo usarías un SageMaker Endpoint?::Cuando necesitas poner un modelo en producción para responder predicciones en tiempo real, como riesgo crediticio o clasificación de fraude. #card #mlops #deployment
¿Para qué sirve SageMaker Pipelines?::Para automatizar todo el flujo: limpieza de datos, entrenamiento, validación y despliegue en un pipeline reproducible. #card #mlops #pipeline
¿Cuándo usarías SageMaker Model Monitor?::Para detectar degradación en un sistema de recomendación o detección de fraude cuando los datos de entrada cambian con el tiempo. #card #mlops #monitoring
¿Para qué sirve SageMaker Clarify?::Para revisar si un modelo de préstamos está sesgado por género o edad antes de ponerlo en producción. #card #mlops #governance
¿Cuándo usarías SageMaker Model Cards?::Cuando quieres documentar el propósito, limitaciones, riesgos y resultados de un modelo para auditoría o revisión interna. #card #mlops #governance
¿Para qué sirve SageMaker Autopilot?::Para automatizar la búsqueda de modelos y experimentación cuando quieres una solución rápida sin programar mucho. #card #mlops #automl
¿Dónde encaja Amazon Ground Truth?::En la preparación de datos etiquetados, por ejemplo marcar imágenes de coches, personas o defectos para entrenar un modelo de visión. #card #mlops #annotation
¿Cuándo usarías SageMaker Feature Store en un escenario real?::Para una plataforma de recomendación donde necesitas usar la misma feature de “usuario activo en los últimos 7 días” tanto en entrenamiento como en predicción. #card #mlops #features

---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Tarea para aclarar una duda de concepto. Usa #mejora-concepto
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia
