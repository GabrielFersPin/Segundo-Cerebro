---
cards-deck: DataScience
created: 2026-04-27
modified: 2026-04-27
status: 🌱 Semilla
tipo_nota: tecnica
area: Databricks
nivel-comprension: 🤔
proxima-revision: 2026-04-30
ultima-revision: 2026-04-27
veces-revisado: 0
tiempo-repaso: 15min
---

# 📌 Data Lakehouse

> [!abstract] Objetivo
> 🎯 Comprender el concepto de Data Lakehouse, su arquitectura, y sus ventajas frente a los tradicionales Data Lakes y Data Warehouses, especialmente en el ecosistema de Databricks.

---

## 🎓 Contexto Académico

**Asignatura/Curso**: Databricks
**Relevancia para**: Databricks / Data Engineering
**Dificultad percibida**: ⭐⭐⭐☆☆ Medio

---

## 📝 Definición

✏️ Un **Data Lakehouse** es una arquitectura de gestión de datos moderna que combina la flexibilidad, el bajo costo y la escalabilidad de los **Data Lakes** con la gestión de datos, la confiabilidad y las transacciones ACID de los **Data Warehouses**. 

Permite almacenar grandes volúmenes de datos estructurados, semiestructurados y no estructurados (típico de un Data Lake), mientras se mantiene una capa de gestión que permite hacer consultas complejas y BI directamente sobre estos datos con alto rendimiento.

En el ecosistema de Databricks, esta arquitectura suele implementarse sobre **Delta Lake**, un formato de almacenamiento de código abierto que aporta transacciones ACID, manejo de metadatos escalable y procesamiento unificado de datos en streaming y batch.

---

## ⚙️ Conceptos Clave

### 📌 Transacciones ACID
**Tipo**: Característica Técnica

**Características**:
- Garantiza la integridad de los datos ante lecturas y escrituras concurrentes.
- Permite operaciones de actualización, eliminación y fusión (merge) fiables.
- Evita la lectura de datos parciales o corruptos en procesos concurrentes.

**Relacionado**: [[Data Warehousing]], [[Data Lake]]

### 📌 Unificación de BI y ML
**Tipo**: Ventaja Arquitectónica

**Características**:
- Los analistas de BI pueden consultar los mismos datos que los científicos de datos.
- Reduce la necesidad de mover o copiar datos entre sistemas (ETL innecesarios).
- Soporta tanto SQL para dashboards como Python/R/Scala para Machine Learning.

**Relacionado**: [[Databricks]], [[Spark]]

### 📌 Gobernanza y Seguridad
**Tipo**: Característica de Gestión

**Características**:
- Permite aplicar controles de acceso detallados sobre los datos (RBAC).
- Facilita el cumplimiento de normativas de privacidad (ej. GDPR) al permitir eliminar registros específicos fácilmente.
- Provee un catálogo unificado de metadatos (ej. Unity Catalog en Databricks).

---

## 💻 Ejemplo Práctico

Imagina una empresa de retail que tiene datos de ventas en bases de datos relacionales (estructurados), logs de navegación web en JSON (semiestructurados) e imágenes de productos (no estructurados). 

Antes del Lakehouse, la empresa almacenaba los logs e imágenes en un Data Lake barato para ML, y copiaba los datos de ventas a un Data Warehouse caro para BI. Había silos de datos, retrasos e inconsistencias. 

Con un Data Lakehouse (ej. en Databricks con Delta Lake), la empresa almacena **todos** los datos en un almacenamiento en la nube de bajo costo (ej. AWS S3 o Azure Data Lake Storage). Sobre este almacenamiento, la capa Delta proporciona la estructura para que Tableau/PowerBI consulte las ventas rápidamente usando SQL, mientras que los modelos de ML en Python acceden a las imágenes y logs en el mismo lugar y al mismo tiempo.

---

## 💭 Reflexiones & Conexiones

🧠 El Data Lakehouse elimina la dicotomía tradicional entre Data Lakes (para ML/AI) y Data Warehouses (para BI). Databricks es uno de los principales impulsores de esta arquitectura. Es crucial entender que el Lakehouse no es un producto físico, sino un *paradigma arquitectónico* habilitado por tecnologías como Delta Lake, Apache Iceberg o Apache Hudi.

---

## 🎴 Flashcards

> 💡 **Formato**: Usa `Pregunta::Respuesta` para flashcards inline

¿Qué es un Data Lakehouse?::Es una arquitectura que combina la flexibilidad y escalabilidad de los Data Lakes con las transacciones ACID y confiabilidad de los Data Warehouses. #DataLakehouse #Arquitectura

¿Cuál es la principal desventaja que resuelve el Data Lakehouse frente a tener un Data Lake y un Data Warehouse separados?::Resuelve el problema de los silos de datos, la duplicación (tener que hacer procesos ETL para mover datos del Lake al Warehouse) y la falta de gobernanza en el Data Lake. #DataLakehouse

¿Qué formato de almacenamiento suele habilitar la arquitectura Data Lakehouse en Databricks?::Delta Lake (aporta transacciones ACID, time travel y esquema estricto sobre datos en la nube). #Databricks #DeltaLake

Data Lakehouse:::Arquitectura que unifica Business Intelligence (BI) y Machine Learning (ML) sobre una única plataforma de datos escalable, soportando transacciones ACID sobre almacenamiento barato. #DataLakehouse

El componente que añade transacciones ACID a un Data Lake para convertirlo en un Lakehouse en Databricks se llama ==Delta Lake== #Databricks #DeltaLake

¿Qué tipos de datos soporta un Data Lakehouse de forma nativa?::Datos estructurados, semiestructurados y no estructurados. #DataLakehouse

---

## 📚 Referencias & Enlaces

**Enlaces internos**: [[Databricks]], [[Data Lake]], [[Data Warehousing]]
**Referencias externas**: [Databricks - What is a Data Lakehouse?](https://www.databricks.com/glossary/data-lakehouse)
**Fuente**: Curso de Databricks

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2026-04-27
- **Próxima revisión**: 2026-04-30
- **Veces revisado**: 0
- **Nivel de comprensión**: 🤔
- **Tiempo estimado de repaso**: 15min

---

> [!tip] 💡 Próximos pasos
> _Cuando revises esta nota, actualiza el contador de revisiones y ajusta la próxima fecha según tu comprensión_