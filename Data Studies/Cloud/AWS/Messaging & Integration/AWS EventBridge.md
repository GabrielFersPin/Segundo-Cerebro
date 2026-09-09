---
created: 2026-09-07
modified: 2026-09-07
area: ""
tipo_nota: captura_rapida
status: 🌱
nivel-comprension: ""
proxima-revision: 2026-09-09
ultima-revision: 2026-09-07
veces-revisado: 0
tiempo-repaso: 5min
cards-deck: Nube::Messaging-Integration
---

# AWS EventBridge

> [!info] Contexto captura
> **Fecha**: 2026-09-07 13:09
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> Amazon EventBridge es un servicio serverless para recibir, filtrar y dirigir eventos entre aplicaciones y servicios de AWS.


### 🎯 Detalles / Contenido

Permite reaccionar cuando ocurre algo, por ejemplo:

- Se crea un objeto en S3.
- Termina un proceso de SageMaker.
- Se modifica una instancia EC2.
- Se registra una acción en otra aplicación.
- Llega un evento desde un servicio externo.

Su funcionamiento básico es:

> Evento → regla o filtro → destino

Los destinos pueden ser:

- AWS Lambda.
- Step Functions.
- SQS o SNS.
- ECS.
- Kinesis.
- Otros servicios de AWS o endpoints HTTP.

Ejemplo:

> Cuando termina un entrenamiento de SageMaker, EventBridge detecta el evento y activa una Lambda que valida el modelo y envía una notificación.

A diferencia de Airflow, EventBridge suele reaccionar a eventos concretos y desacoplar servicios. Airflow está más orientado a orquestar flujos completos de tareas con dependencias y ejecuciones programadas.




---

## 🔑 Keywords / Conceptos clave

`AWS`, `EventBridge`, `event-driven`, `serverless`, `reglas`, `event bus`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

¿Qué es Amazon EventBridge?::Es un servicio serverless que recibe, filtra y dirige eventos entre aplicaciones y servicios de AWS. #aws #eventbridge #serverless

¿Cuál es el flujo básico de EventBridge?::Evento → regla o filtro → destino. #aws #eventbridge #eventdriven

¿Qué puede actuar como evento de entrada en EventBridge?::Acciones de servicios AWS, cambios en recursos, eventos de aplicaciones propias o eventos de servicios externos. #aws #eventbridge

¿Qué es una regla en EventBridge?::Es una condición o patrón que filtra los eventos y determina cuándo debe ejecutarse una acción. #aws #eventbridge

¿Qué destinos puede invocar EventBridge?::Por ejemplo Lambda, Step Functions, SQS, SNS, ECS, Kinesis u otros servicios y endpoints HTTP compatibles. #aws #eventbridge

¿Cuál es un caso real de uso de EventBridge con SageMaker?::Cuando termina un entrenamiento, una regla detecta el evento y activa una Lambda para validar el modelo y enviar una notificación. #aws #eventbridge #sagemaker

¿Qué ventaja aporta EventBridge a una arquitectura?::Desacopla los servicios, porque el productor publica un evento sin tener que conocer directamente a los consumidores. #aws #eventbridge #architecture

¿Qué diferencia hay entre EventBridge y Airflow?::EventBridge reacciona principalmente a eventos concretos; Airflow orquesta flujos completos de tareas con dependencias y ejecuciones programadas. #aws #eventbridge #airflow

> 💡 **Formato recomendado**:
> - Inline: `¿Pregunta?::Respuesta #tags`
> - Reversa: `Término:::Definición #tags`
> - Cloze: `Texto con ==palabra== oculta`
---

## ❓ Preguntas / Dudas pendientes

- [ ] ¿Qué diferencia hay entre EventBridge y SNS para distribuir eventos?
- [ ] ¿Cuándo conviene usar EventBridge Scheduler?

---

## 🧩 Conexiones potenciales

<!-- ¿Con qué otros temas se relaciona? Escribe rápido, ya harás los links después -->

- [[AWS Lambda]]
- [[Amazon SNS]]
- [[Amazon SQS]]
- [[Amazon SageMaker Pipelines]]

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

<!-- Zona libre para cualquier cosa que quieras capturar rápido -->

EventBridge es especialmente útil cuando varios servicios deben reaccionar al mismo evento sin crear integraciones directas entre cada componente.



---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-09-07 13:09 |
| Área/Tema | `= this.area` |
| Estado | `= this.status` |
| Prioridad | `= this.prioridad` |
| Revisión | `= this.proxima-revision` |
| Nivel de comprensión | `= this.nivel-comprension` |

---

#pendiente-procesar #captura-rapida
