---
cards-deck: Nube
created: 2026-02-19
modified: 2026-02-19
status: 🌱
tipo_nota: tecnica
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
---

# Azure Stream Analytics

> [!abstract] Objetivo
> Understand data streams and event processing using Azure Stream Analytics.

---

## 🎓 Contexto Académico

**Asignatura/Curso**: Azure Data Engineer
**Relevancia para**: Certificación (DP-203)
**Dificultad percibida**: ⭐⭐☆☆☆

---

## 📝 Definición

Azure Stream Analytics is a platform-as-a-service (PaaS) solution for complex event processing and analysis of streaming data. It is used to ingest data from an input (like Azure Event Hubs or IoT Hub), process it using a query (SQL-based), and write the results to an output (like Azure SQL Database or Power BI).

It guarantees **exactly once** event processing and **at-least-once** event delivery, ensuring events are never lost. It provides built-in checkpointing for state maintenance and repeatable results.

---

## ⚙️ Conceptos Clave

### 📌 Data Stream Characteristics

**Tipo**: Concepto

**Características**:

- **Unbounded**: Data is added to the stream perpetually.
- **Temporal**: Each record includes time-based data indicating when the event occurred.
- **Windows**: Aggregation is performed over temporal windows (e.g., posts per minute).

![A diagram showing a stream of data including a date and time field being processed, aggregated by day, and visualized and stored.](https://learn.microsoft.com/en-us/training/data-ai-cert/introduction-to-data-streaming/media/stream-processing.png)

**Relacionado**: [[Azure Event Hubs]] • [[Azure IoT Hub]]

### 📌 Stream Analytics Jobs vs. Clusters

**Tipo**: Arquitectura

**Características**:

- **Job**: The easiest way to use Stream Analytics. Runs in an Azure subscription with configured inputs, outputs, and query.

![Diagram that shows a Stream Analytics job with inputs, a query, and outputs](https://learn.microsoft.com/en-us/training/data-ai-cert/introduction-to-data-streaming/media/stream-analytics.png)

- **Cluster**: For complex or resource-intensive requirements. Uses the same engine but in a dedicated tenant with configurable scalability.

### 📌 Window Functions

**Tipo**: Función

**Características**:

- **Tumbling**: Fixed-size, non-overlapping time segments.

![A diagram illustrating a stream with a series of events mapped into 1-minute tumbling windows.](https://learn.microsoft.com/en-us/training/data-ai-cert/introduction-to-data-streaming/media/tumble-window.png "Tumbling windows")

- **Hopping**: Fixed-size, overlapping windows that jump forward by a fixed period.

![The diagram illustrates a stream with a series of events captured in 60 second hopping windows that occur every 30 seconds.](https://learn.microsoft.com/en-us/training/data-ai-cert/introduction-to-data-streaming/media/hop-window.png "Hopping windows")

- **Sliding**: Windows that generate events only when the content changes (event enters/exits).

![The diagram illustrates a stream with a series of events mapped into sliding windows of 1 minute.](https://learn.microsoft.com/en-us/training/data-ai-cert/introduction-to-data-streaming/media/slide-window.png "Sliding windows")

- **Session**: Clusters events that arrive at similar times, filtering out periods with no data.

![The diagram illustrates a stream with a series of events mapped into session windows with a 20-second timeout and a maximum duration of 60 seconds.](https://learn.microsoft.com/en-us/training/data-ai-cert/introduction-to-data-streaming/media/session-window.png "Session windows")

- **Snapshot**: Groups events by identical timestamp values.

![The diagram illustrates a stream with a series of events mapped into snapshot windows.](https://learn.microsoft.com/en-us/training/data-ai-cert/introduction-to-data-streaming/media/snapshot-window.png "Snapshot windows")

**Relacionado**: [[SQL Window Functions]]

---

## 💻 Ejemplo Práctico

### Basic Query Structure

Query to filter events with temperature < 0.

```sql
SELECT observation_time, weather_station, temperature
INTO cold-temps
FROM weather-events TIMESTAMP BY observation_time
WHERE temperature < 0
```

### Tumbling Window

Find max reading in every 1-minute window.

```sql
SELECT DateAdd(minute,-1,System.TimeStamp) AS WindowStart,
       System.TimeStamp() AS WindowEnd,
       MAX(Reading) AS MaxReading
INTO [output]
FROM [input] TIMESTAMP BY EventProcessedUtcTime
GROUP BY TumblingWindow(minute, 1)
```

### Hopping Window

Window size 60s, hop 30s.

```sql
SELECT DateAdd(second,-60,System.TimeStamp) AS WindowStart,
       System.TimeStamp() AS WindowEnd,
       MAX(Reading) AS MaxReading
INTO [output]
FROM [input] TIMESTAMP BY EventProcessedUtcTime
GROUP BY HoppingWindow(second, 60, 30)
```

### Sliding Window

Max reading in 1-minute window, outputting only when events enter/exit.

```sql
SELECT DateAdd(minute,-1,System.TimeStamp) AS WindowStart,
       System.TimeStamp() AS WindowEnd,
       MAX(Reading) AS MaxReading
INTO [output]
FROM [input] TIMESTAMP BY EventProcessedUtcTime
GROUP BY SlidingWindow(minute, 1)
```

---

## 💭 Reflexiones & Conexiones

Streaming data analytics is crucial for understanding change over time, such as sentiment analysis on social media or monitoring IoT sensors. The alignment with other Azure services (Event Hubs, Blob Storage, Power BI) makes it a central piece of the Azure real-time analytics ecosystem.

---

## 🎴 Flashcards

What does Azure Stream Analytics guarantee regarding event processing?::It guarantees **exactly once** event processing and **at-least-once** event delivery. #Azure #StreamAnalytics

What are the three main components of a Stream Analytics job?::Input, Query, and Output. #Azure #StreamAnalytics

Which window function creates fixed-size, non-overlapping time segments?::Tumbling Window #Azure #StreamAnalytics

Which window function clusters events that arrive at similar times and filters out periods with no data?::Session Window #Azure #StreamAnalytics

What is the difference between a Hopping and a Sliding window?::Hopping windows jump forward by a fixed period, while Sliding windows output events only when an event enters or exits the window. #Azure #StreamAnalytics

---

## 📚 Referencias & Enlaces

**Enlaces internos**: [[Azure Data Engineer]] [[Azure Synapse Analytics]]
**Referencias externas**: [Introduction to Azure Stream Analytics](https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction)
**Fuente**: Microsoft Learn

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2026-02-19
- **Próxima revisión**: 2026-02-22
- **Veces revisado**: 0
- **Nivel de comprensión**: 🤔 Entiendo parcialmente
- **Tiempo estimado de repaso**: 15min

---

> [!tip] 💡 Próximos pasos
> _Cuando revises esta nota, actualiza el contador de revisiones y ajusta la próxima fecha según tu comprensión_
