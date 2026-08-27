---
created: 2026-08-26
modified: 2026-08-26
area: "Data Studies/Cloud/AWS"
tipo_nota: "captura_rapida"
status: "🌱"
nivel-comprension: "Básico"
proxima-revision: "2026-08-29"
ultima-revision: "2026-08-26"
veces-revisado: 0
tiempo-repaso: "5min"
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
- [ ] Crear flashcards si es necesario
- [ ] Hacer ejercicios relacionados
- [ ] Conectar con otras notas ([[]])
- [ ] Actualizar nivel de comprensión
- [ ] Mover a vault definitivo / Cambiar status a 🌿

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
