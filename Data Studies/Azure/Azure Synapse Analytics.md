---
cards-deck: Nube
created: 2026-02-18
modified: 2026-02-18
status: 🌱
tipo_nota: ""
---

# Azure Synapse Analytics

> [!abstract] Objetivo
> Know how it works

---

## 🎓 Contexto Académico

**Asignatura/Curso**: Data Engineer
**Relevancia para**: Certificación
**Dificultad percibida**: ⭐⭐☆☆☆
---

## 📝 Definición

Azure Synapse Analytics is a real-time data capture service that perpetually filtered and aggregate

---

## ⚙️ Conceptos Clave

### 📌 Data Warehouse 

**Tipo**: Definición

**Características**:
- It provides dedicated SQL pools that you can use to implement enterprise-scale relational data warehouses.
- To ingest real-time data into a relational data warehouse,  [[Azure Stream Analytics]] query must write its results to an output that references the table into wich you want to load the data.

**Relacionado**: [[Cloud Computing]]

### 📌 Data Lake

**Tipo**: Técnica

**Características**:
- Azure Synapse Analytics typically includes at least one storage service that is used as a data lake.
- When ingesting real-time data into a data lake, [[Axure Stream Analytics]] query must write iits results to an uotput that references the location in the [[Azure Data Lake Gen2]] storage container where you want to save the data files.

**Relacionado**: [[Cloud Computing]]

### 📌 Configure inputs and outputs

**Tipo**: Técnica

**Características**:
- Streaming data inputs
- 
- 

**Relacionado**: [[Cloud Computing]]

### 📌 Streaming data inputs

**Tipo**: Técnica

**Características**:
- Depending on the specific unpit type, the data for each streamed event includes the event's data fields as well as input-specific metadata fields.

**Relacionado**: [[Cloud Computing]]

### 📌 Azure Synapse Analytics outputs

**Tipo**: Técnica

**Características**:
- The output configuration includes the identity of the dedicated SQL pool in Azure Synapse workspace, datails of how the azure Stream Analytics job should establish an authenticated connection to it, and the existing thable into wich the data should be loaded

**Relacionado**: [[Cloud Computing]]

### 📌 Azure Data Lake Storage Gen2 outputs

**Tipo**: Téncinca

**Características**:
- To write the results of stream processing to [[Azure Data Lake Storage Gen2]] container that hosts a data lake in Azure Synapse Analytics workspace, us a [[Blob storage]]/[[ADLS Gen2]] output. The output configuration includes details of the storage accounts in which the container is defined, authentication settings to connect to it, and details of the files to be created.
- It can specify minimun and maximun row counts for each batch, wich determines the number of outputs files generated. You can also configure the write mode to control when the data is written for a time window.

**Relacionado**: [[Cloud Computing]]

---

## 💻 Ejemplo Práctico

### Selecting input fields

The simplest approach to ingesting streaming data into Azure Synapse Analytics is to capture the required field values for every event using a **SELECT...INTO** query, as shown here:

```sql
SELECT     EventEnqueuedUtcTime AS ReadingTime,     SensorID,     ReadingValue 
INTO     [synapse-output] 
FROM     [streaming-input] TIMESTAMP BY EventEnqueuedUtcTime
```

### Filtering event data

In some cases, you might want to filter the data to include only specific events by adding a **WHERE** clause. For example, the following query writes data only for events with a negative **ReadingValue** field value.

```SQL
SELECT
    EventEnqueuedUtcTime AS ReadingTime,
    SensorID,
    ReadingValue
INTO
    [synapse-output]
FROM
    [streaming-input] TIMESTAMP BY EventEnqueuedUtcTime
WHERE ReadingValue < 0
```

### Aggregating events over temporal windows

A common pattern for streaming queries is to aggregate event data over temporal (time-based) intervals, or _windows_. To accomplish this, you can use a **GROUP BY** clause that includes a Window function defining the kind of window you want to define (for example, _tumbling_, _hopping_, or _sliding_)

The **HAVING** clause filters the results to include only windows where at least one event occurred.

```SQL
SELECT
    DateAdd(second, -60, System.TimeStamp) AS StartTime,
    System.TimeStamp AS EndTime,
    SensorID,
    MAX(ReadingValue) AS MaxReading
INTO
    [synapse-output]
FROM
    [streaming-input] TIMESTAMP BY EventEnqueuedUtcTime
GROUP BY SensorID, TumblingWindow(second, 60)
HAVING COUNT(*) >= 1
```

## Run a job to ingest data

### Querying data in a relational data warehouse

For example, the following SQL code could be used to query a table named **factSensorReadings** that contains the results of stream processing, and combine it with a **dimDate** table containing detailed data about the dates on which readings were captured.

```SQL
SELECT d.Weekday, s.SensorID, AVG(s.SensorReading) AS AverageReading
FROM factSensorReadings AS s
JOIN dimDate AS d
    ON CAST(s.ReadingTime AS DATE) = d.DateKey
GROUP BY d.Weekday, s.SensorID
```

### Querying data in a data lake

As streaming data is ingested into files in a data lake, you can query those files by using a serverless SQL pool in Azure Synapse Analytics. For example, the following query reads all fields from all Parquet files under the **sensors** folder in the **data** file system container.

```SQL
SELECT *
FROM OPENROWSET(
    BULK 'https://mydatalake.blob.core.windows.net/data/sensors/*',
    FORMAT = 'parquet') AS rows
```

You can also query the data lake by using code running in an Apache Spark pool, as shown in this example:

```python
%%pyspark
df = spark.read.load('abfss://data@datalake.dfs.core.windows.net/sensors/*', format='parquet'
)
display(df)
```

**Explicación**: 
---

## 💭 Reflexiones & Conexiones

It's a service that can aggregate and filter data from a data warehouse and data lake.

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
- **Última revisión**: 2026-02-19
- **Próxima revisión**: 2026-02-22
- **Veces revisado**: 0
- **Nivel de comprensión**: 🤔
- **Tiempo estimado de repaso**: 5min
---

> [!tip] 💡 Próximos pasos
> _Cuando revises esta nota, actualiza el contador de revisiones y ajusta la próxima fecha según tu comprensión_