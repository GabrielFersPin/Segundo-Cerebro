---
cards-deck: Azure Data Engineer
created: 2026-02-09
modified: 2026-02-09
status: 🌱
tipo_nota: ""
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
---

# Data Lake

> [!abstract] Objetivo
> Definition of data lake

---

## 🎓 Contexto Académico

**Asignatura/Curso**: Azure Data Engineer
**Relevancia para**: Certificación
**Dificultad percibida**: ⭐☆☆☆☆
---

## 📝 Definición

Data lake is a repository that is stored in its natural format, usually as blobs or files.

---

## ⚙️ Conceptos Clave

### 📌 Benefits

**Tipo**: Definición

**Características**:
- Data lake is design to deal with this variety and volume of data at exabyte scale while securely handling hundreds of gigabytes of throughtput.

**Relacionado**: [[Data Lake]]

### 📌 Hadoop

**Tipo**: Herramienta

**Características**:
- The data lake can be accessed the data with Hadoop Diatribuited File System (HDFS). With this feature you can store the data in one place and access with plenty of technologies.

**Relacionado**: [[Hadoop]]

### 📌 Security

**Tipo**: Benefits

**Características**:
- Data Lake Storage support control lists (ACLs) and Portable Operating System Interface (POSIXS) permissions that don't inherit the permissions of the parent directory.

**Relacionado**: [[Data Lake]]

### 📌 Performance

**Tipo**: Benefits

**Características**:
- Data lake storage organizes the stored data into a hierarchy of directories and subdirectories, much like a file system, for easier navigation.

**Relacionado**: [[Data Lake]]

### 📌 Stages of Processing

**Tipo**: Benefits

**Características**:
- **Ingest**: This data can come from files, logs, and other types of unstructured data that must be put into the data lake
- The technology that is used will vary depending on the frequency that the data is transferred. For example, for batch movement of data, pipelines in [[Azure Synapse Analytics]] or [[Azure Data Factory]] may be the most appropriate technology to use. For real-time ingestion of data, [[Apache Kafka]] for HDInsight or [[Stream Analytics]] may be an appropriate choice.
- **Store**: The store phase identifies where the ingested data should be placed. [[Azure Data Lake Storage Gen2]]provides a secure and scalable storage solution that is compatible with commonly used big data processing technologies.
- **Prep  and Train**: The prep and train phase identifies the technologies that are used to perform data preparation and model training and scoring for machine learning solutions. Common technologies that are used in this phase are Azure [[Synapse Analytics]], [[Azure Databricks]], [[Azure HDInsight]], and [[Azure Machine Learning]].
- **Model and Serve**: Finally, the model and serve phase involves the technologies that will present the data to users. These technologies can include visualization tools such as [[Microsoft Power BI]], or analytical data stores such as [[Azure Synapse Analytics]]. Often, a combination of multiple technologies will be used depending on the business requirements. 

**Relacionado**: [[Data Lake]]

---

## 💻 Ejemplo Práctico

_No se incluyó ejemplo en esta nota_
---

## 💭 Reflexiones & Conexiones

Data engineer have to be proactive to transform a data lake accessible and usefull using the right data governance and security features.

---

## 🎴 Flashcards

_Flashcards pendientes de crear_

> 💡 **Formato recomendado**:
> - Inline: `¿Pregunta?::Respuesta #tags`
> - Reversa: `Término:::Definición #tags`
> - Cloze: `Texto con ==palabra== oculta`
---

## 📚 Referencias & Enlaces

**Enlaces internos**: 
**Referencias externas**: 
**Fuente**: 

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2026-02-09
- **Próxima revisión**: 2026-02-12
- **Veces revisado**: 0
- **Nivel de comprensión**: 💡
- **Tiempo estimado de repaso**: 5min
---

> [!tip] 💡 Próximos pasos
> _Cuando revises esta nota, actualiza el contador de revisiones y ajusta la próxima fecha según tu comprensión_