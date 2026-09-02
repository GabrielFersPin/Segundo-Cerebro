---
created: 2026-08-26
modified: 2026-09-01
area: Data Studies/Cloud/AWS
tipo_nota: captura_rapida
status: 🌿 Creciendo
nivel-comprension: 💡
proxima-revision: 2026-10-01
ultima-revision: 2026-09-01
veces-revisado: 1
tiempo-repaso: 5min
tiempo-estimado: 10min
---

# Amazon Lambda

> [!info] Contexto captura
> **Fecha**: 2026-08-26 09:15
> **Origen**: AWS / Serverless computing
> **Tipo**: Concepto / servicio de computación sin servidor

---

## 📝 Captura principal

> [!tip] Lo más importante
> Amazon Lambda permite ejecutar código sin provisionar ni gestionar servidores, respondiendo a eventos y escalando automáticamente según la carga.

### 🎯 Detalles / Contenido

AWS Lambda es un servicio de computación serverless. El usuario sube su código en funciones y AWS se encarga de ejecutar ese código bajo demanda, sin necesidad de reservar instancias ni mantener infraestructura.

Casos de uso típicos:

- Procesamiento de eventos y archivos
- APIs REST mediante API Gateway
- Automatización de procesos y workflows
- Transformación de datos en streaming
- Integración entre servicios de AWS

Características clave:

- Pago por uso: solo se cobra por tiempo de ejecución y cantidad de invocaciones
- Escalado automático: se multiplica según la demanda
- Soporte para varios lenguajes: Python, Node.js, Java, Go, .NET y más
- Integración nativa con otros servicios de AWS
- Modelo basado en eventos: S3, DynamoDB, EventBridge, SNS, SQS, API Gateway, etc.

La arquitectura es muy útil para arquitecturas event-driven, donde cada acción dispara una función. Por ejemplo, al subir un archivo a S3 se puede invocar una Lambda para procesarlo, generar thumbnails, transformarlo o notificar a otra aplicación.

Una Lambda se compone normalmente de:

- trigger o evento de entrada
- función de código
- runtime y permisos IAM
- configuración de memoria, tiempo de ejecución y entorno

El mayor beneficio es la reducción de ops, aunque hay que tener en cuenta límites como duración máxima de ejecución, cold starts, dependencias y diseño de aplicaciones sin servidor.

---

## 🔑 Keywords / Conceptos clave

`Amazon Lambda`, `serverless`, `event-driven`, `FaaS`, `AWS`, `funciones`, `trigger`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## ❓ Preguntas / Dudas pendientes

- [ ] ¿Qué diferencia hay entre Lambda y EC2 para ejecutar código?
- Una Lambda ejecuta una tarea cuando es activada, ya EC2 mantiene un proceso rodando aunque no estés ejecutando la tarea.
- [ ] ¿Cuándo conviene Lambda frente a contenedores o servicios gestionados?
- [ ] ¿Cómo afecta el cold start a la latencia de una API?

---

## 🧩 Conexiones potenciales

- Amazon API Gateway
- Amazon S3
- Amazon DynamoDB
- Amazon EventBridge
- Amazon SQS
- Amazon SNS

---

## ✅ Checklist procesamiento

- [x] Revisar y expandir contenido
- [x] Crear flashcards si es necesario
- [x] Hacer ejercicios relacionados ✅ 2026-09-01
- [ ] Conectar con otras notas ([[]])
- [ ] Actualizar nivel de comprensión
- [ ] Mover a vault definitivo / Cambiar status a 🌿

---

## 🎴 Flashcards

¿Qué es Amazon Lambda?::Es un servicio serverless que ejecuta código bajo demanda sin provisionar ni gestionar servidores. #aws #lambda #serverless

¿Qué significa que Lambda sea serverless?::Que AWS gestiona la infraestructura y el escalado, y tú solo te encargas del código y la lógica de negocio. #aws #lambda

¿Cuándo conviene usar Lambda?::Cuando necesitas procesar eventos, automatizar tareas o responder a cambios en S3, DynamoDB, SNS, SQS o API Gateway. #aws #lambda

¿Qué es un trigger en Lambda?::Es el evento que dispara la ejecución, como la subida de un archivo a S3 o un mensaje en SQS. #aws #lambda

¿Qué es el modelo event-driven de Lambda?::Es un patrón donde cada evento activa una función que ejecuta una acción específica. #aws #lambda

¿Por qué Lambda es útil para APIs?::Porque puede exponer lógica backend en respuesta a peticiones HTTP mediante API Gateway sin mantener servidores siempre activos. #aws #lambda

¿Qué ventaja principal tiene Lambda en coste?::Pagas solo por el tiempo de ejecución y por las invocaciones realmente usadas. #aws #lambda

¿Qué es cold start en Lambda?::Es el tiempo inicial de preparación del entorno cuando la función se ejecuta por primera vez o tras un periodo de inactividad. #aws #lambda

¿Cuál es un caso real de uso para Lambda con S3?::Al subir una imagen a S3, una Lambda puede generar una miniatura, convertir el formato o enviar una notificación. #aws #lambda

¿Cuál es un caso real de uso para Lambda con DynamoDB?::Cuando se inserta un registro, una Lambda puede enviar un evento, actualizar otros datos o realizar validaciones. #aws #lambda

¿Qué limita Lambda en comparación con EC2?::Tiene límites de tiempo, memoria, duración y está optimizada para tareas cortas y eventos puntuales. #aws #lambda

> 💡 **Formato recomendado**:
> - Inline: `¿Pregunta?::Respuesta #tags`
> - Reversa: `Término:::Definición #tags`
> - Cloze: `Texto con ==palabra== oculta`

---

## 💭 Notas adicionales / Ideas rápidas

Lambda es una pieza clave dentro de AWS para construir sistemas altamente desacoplados y escalables. Su principal ventaja es la abstracción de la infraestructura, permitiendo centrarse en la lógica de negocio.

Es ideal para automatización, integración y funciones muy cortas o con tráfico variable.

---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-08-26 09:15 |
| Área/Tema | Data Studies/Cloud/AWS |
| Estado | 🌱 |
| Prioridad |  |
| Revisión | 2026-08-29 |
| Nivel de comprensión | Básico |

---

#pendiente-procesar #captura-rapida


---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Tarea para aclarar una duda de concepto. Usa #mejora-concepto
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia
