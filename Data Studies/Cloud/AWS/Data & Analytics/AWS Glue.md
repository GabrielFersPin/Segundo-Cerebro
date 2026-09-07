---
created: 2026-06-01
modified: 2026-09-07
area: Nube
tipo_nota: captura_rapida
status: 🌿 Creciendo
nivel-comprension: 💡
proxima-revision: 2026-09-21
ultima-revision: 2026-09-07
veces-revisado: 1
tiempo-repaso: 5min
cards-deck: Nube
tiempo-estimado: 10min
---

# AWS Glue

> [!info] Contexto captura
> **Fecha**: 2026-06-01
> **Origen**: AWS / Data & Analytics
> **Tipo**: Servicio administrado de ETL y calidad de datos

---

## 📝 Captura principal

> [!tip] Lo más importante
> AWS Glue es un servicio administrado de extracción, transformación y carga (ETL) que facilita preparar y mover datos para análisis.

### 🎯 Detalles / Contenido

AWS Glue incluye herramientas para descubrir metadatos, transformar datos y comprobar su calidad:

- **AWS Glue Data Catalog**: almacena metadatos de las fuentes de datos, como ubicación, esquemas, tipos de datos y definiciones de tablas.
- **AWS Glue Crawler**: escanea automáticamente las fuentes de datos para rellenar o actualizar el Data Catalog.
- **AWS Glue Data Quality**: evalúa objetos del Data Catalog mediante reglas no-code y usa machine learning para detectar anomalías.
- Los resultados de las reglas permiten revisar qué controles de calidad pasan y cuáles fallan.

### 💡 Ejemplo práctico

Un Crawler descubre archivos en S3 y registra sus metadatos en el Data Catalog. Después, un proceso ETL transforma los datos y Glue Data Quality valida el resultado antes de utilizarlo para análisis.

---

## 🔑 Keywords / Conceptos clave

`AWS Glue`, `ETL`, `Data Catalog`, `Crawler`, `Data Quality`, `data engineering`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

¿Qué es AWS Glue?::Es un servicio administrado de ETL que extrae, transforma y carga datos para prepararlos para análisis. #aws #glue #etl #card 

¿Qué problema resuelve AWS Glue?::Facilita preparar y mover datos entre fuentes y destinos sin tener que gestionar toda la infraestructura de los procesos ETL. #aws #glue #dataengineering #card 

¿Para qué sirve AWS Glue Data Catalog?::Para almacenar metadatos sobre las fuentes de datos, como su ubicación, esquemas, tipos de datos y definiciones de tablas. #aws #glue #datacatalog #card 

¿Qué hace un AWS Glue Crawler?::Escanea automáticamente las fuentes de datos y utiliza lo que descubre para rellenar o actualizar el Data Catalog. #aws #glue #crawler #card 

¿Cuándo usarías un Glue Crawler?::Cuando recibes archivos o tablas nuevas y quieres descubrir su esquema automáticamente en lugar de registrarlo de forma manual. #aws #glue #etl #card 

¿Qué es AWS Glue Data Quality?::Es una herramienta que permite definir y ejecutar reglas para evaluar la calidad de los datos registrados en el AWS Data Catalog. #aws #glue #dataquality #card 

¿Qué ventaja ofrece Glue Data Quality a usuarios que no programan?::Permite implementar reglas de calidad mediante una interfaz no-code. #aws #glue #dataquality #card 

¿Cómo detecta anomalías AWS Glue Data Quality?::Utiliza machine learning, además de reglas de calidad, para identificar comportamientos o valores anómalos en los datos. #aws #glue #machinelearning #card 

¿Cuál sería un flujo real usando AWS Glue?::Un Crawler descubre archivos en S3, registra sus metadatos en Data Catalog, un proceso ETL los transforma y Data Quality valida el resultado antes del análisis. #aws #glue #dataengineering #card 

---

## ❓ Preguntas / Dudas pendientes

- [ ] ¿Qué diferencia hay entre Glue ETL y un SageMaker Processing Job?
- [ ] ¿Cómo se conecta Glue con Athena y S3?

---

## 🧩 Conexiones potenciales

- [[Amazon S3]]
- [[Amazon Athena]]
- [[AWS SageMaker Processing job]]

---

## ✅ Checklist procesamiento

- [x] Revisar y expandir contenido
- [x] Crear flashcards si es necesario
- [ ] Hacer ejercicios relacionados
- [x] Conectar con otras notas ([[]])
- [ ] Actualizar nivel de comprensión
- [ ] Mover a vault definitivo / Cambiar status a 🌿

---

## 💭 Notas adicionales / Ideas rápidas

AWS Glue centraliza el descubrimiento, la preparación y la validación de datos antes de que estos lleguen a herramientas de análisis o machine learning.

---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-06-01 |
| Área/Tema | Nube |
| Estado | 🌱 |
| Prioridad | Certificación |
| Revisión | 2026-06-04 |
| Nivel de comprensión |  |

---

#pendiente-procesar #captura-rapida

---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Tarea para aclarar una duda de concepto. Usa #mejora-concepto
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia
