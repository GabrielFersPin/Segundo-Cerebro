---
cards-deck: Nube::AWS vs. Azure
created: 2026-01-22
modified: 2026-01-22
status: 🌿 Creciendo
tipo_nota:
tecnica asignatura: Infraestructura-Nube
nivel-comprension: 💡 Entiendo bien
proxima-revision: 2026-01-29
ultima-revision: 2026-01-22
veces-revisado: 0
tiempo-repaso: 15min
---
# 📌 Arquitectura de Cómputo: IaaS vs. Serverless (AWS/Azure)

> [!abstract] Objetivo
> 
> 🎯 Dominar la equivalencia de servicios entre AWS (Teoría/Uni) y Azure (Práctica/Entrevista) y saber justificar cuándo usar Máquinas Virtuales (EC2) frente a Serverless (Lambda/Functions) basándose en costes y escalabilidad.

---

## 🎓 Contexto Académico

Asignatura/Curso: Infraestructura Nube

Relevancia para: Examen Final (Preguntas de teoría de escalado) y Entrevista Técnica Accenture (Justificación de proyecto EduInnovatech/Coworking).

Dificultad percibida: ⭐⭐⭐☆☆ Medio

---

## 📝 Definición

El cómputo en la nube se divide principalmente en modelos de responsabilidad compartida. Desde **IaaS** (Infrastructure as a Service), donde gestionamos el SO y el hardware virtual (ej. AWS EC2), hasta **FaaS/Serverless** (Function as a Service), donde abstraemos totalmente el servidor y solo subimos código que se ejecuta por eventos (ej. AWS Lambda).

Para la entrevista, es vital entender que **Serverless no significa "sin servidores"**, sino que la gestión, el parcheo y el escalado de esos servidores son responsabilidad del proveedor (AWS/Azure), permitiendo un modelo de costes "Pay-as-you-go" (pago por uso real).

---

## ⚙️ Conceptos Clave

### 📌 1. Equivalencia de Servicios (El Diccionario Accenture)

**Tipo**: Definición / Comparativa

**Características**:

- **Máquinas Virtuales (IaaS)**: En la Uni estudiamos **AWS EC2**. En mis proyectos (y Accenture) el equivalente es **Azure Virtual Machines**.
    
- **Serverless (FaaS)**: En la Uni estudiamos **AWS Lambda**. En mi proyecto EduInnovatech usé **Azure Functions**.
    
- **Almacenamiento Objetos**: En la Uni estudiamos **Amazon S3**. En mis proyectos uso **Azure Blob Storage**.
    

**Relacionado**: [[Modelos de Responsabilidad Compartida]] • [[FinOps]]

### 📌 2. Escalabilidad (La pregunta de examen y entrevista)

**Tipo**: Técnica / Arquitectura

**Características**:

- **Escalado Vertical (Scale Up)**: Añadir más RAM/CPU a la misma máquina. (Típico de bases de datos antiguas o monolitos). Tiene límite físico y requiere reinicio (downtime).
    
- **Escalado Horizontal (Scale Out)**: Añadir _más máquinas_ o instancias. Es el modelo nativo de la nube. Serverless lo hace automático.
    
- **Elasticidad**: La capacidad de crecer (Scale Out) y decrecer (Scale In) automáticamente según la demanda.
    

### 📌 3. Cold Start (Arranque en Frío)

**Tipo**: Concepto Técnico (Nivel Pro)

**Características**:

- Es el tiempo de latencia que ocurre cuando una función Serverless se ejecuta por primera vez después de un tiempo de inactividad.
    
- El proveedor tiene que "encender" el contenedor por debajo.
    
- **Defensa en entrevista**: "En mi proyecto EduInnovatech acepté este pequeño retraso inicial a cambio de tener coste cero cuando nadie usa la app".
    

---

## 💻 Ejemplo Práctico

### 📊 Caso práctico: Migración de EduInnovatech (Entrevista)

El Problema: Tenía una aplicación monolítica que costaba dinero incluso de noche cuando ningún alumno la usaba.

La Solución (Arquitectura): Migrar de un modelo IaaS (VM fija) a un modelo Serverless.

La Implementación:

1. **Backend**: Pasé de un servidor Python siempre encendido a **Azure Functions** (equiv. AWS Lambda) que solo se activa con peticiones HTTP.
    
2. Base de Datos: Migré a Azure SQL Serverless (equiv. AWS Aurora Serverless). Se pausa si no hay queries.
    
    El Resultado: Reducción de costes del 90% en entorno de desarrollo.
    

---

## 💭 Reflexiones & Conexiones

🧠 Insight para la entrevista:

Cuando me pregunten "¿Por qué Azure y no AWS?", la respuesta académica es "son lo mismo". La respuesta de ingeniero es: "Los patrones de arquitectura (Event-driven, Microservicios) son idénticos. Solo cambia la sintaxis de la consola. Mi transición de Azure a AWS en Accenture sería inmediata porque entiendo el concepto, no solo la herramienta".

🧠 Conexión con Examen:

En el examen preguntarán por "Alta Disponibilidad". En Serverless, la alta disponibilidad viene "de serie" (multi-AZ) sin configurar nada extra. En EC2/VM tienes que configurar tú el Load Balancer y el Auto Scaling Group.

---

## 🎴 Flashcards

> 💡 **Formato**: Usa `Pregunta::Respuesta` para flashcards inline

[1] 📝 Pregunta:

¿Cuál es el equivalente de AWS Lambda en el ecosistema de Microsoft Azure?::Azure Functions. Ambas son servicios FaaS (Serverless). #entrevista #azure

[2] 📝 Pregunta:

En términos de escalabilidad, ¿cuál es la diferencia entre Escalado Vertical y Horizontal?

?

Escalado Vertical (Up/Down): Aumentar la potencia (RAM/CPU) de una sola máquina.

Escalado Horizontal (Out/In): Aumentar el número de máquinas/instancias que trabajan en paralelo. (Preferido en Cloud). #examen #arquitectura

[3] 🔄 Término/Concepto:

S3 (Simple Storage Service):::Es el servicio de almacenamiento de objetos de AWS. Su equivalente directo en Azure es Blob Storage. Ambos sirven para guardar datos no estructurados (imágenes, CSVs, logs) en un Data Lake. #entrevista #aws

[4] 🧩 Texto con partes ocultas (usa == ==):

El modelo de costes de Serverless se basa en ==pago por uso (tiempo de ejecución y memoria)==, mientras que en IaaS (EC2/VM) pagas por ==tiempo de aprovisionamiento (mientras la máquina esté encendida)==, aunque no esté procesando nada. #finops #examen

[5] 📝 Pregunta:

Si el entrevistador pregunta "¿Cómo manejas picos de tráfico de 100 usuarios a 100.000?", ¿qué concepto debes mencionar?::Auto Scaling (Escalado Automático) y el diseño Stateless (sin estado) de la aplicación, para que se puedan crear copias horizontales sin perder datos. #entrevista

---

## 📚 Referencias & Enlaces

Enlaces internos: [[Proyecto Coworking AI]], [[Proyecto EduInnovatech]]

Referencias externas: Documentación AWS EC2 vs Lambda.

---

## 📋 Metadata

- **Estado**: 🌿 Creciendo
    
- **Última revisión**: 2026-01-22
    
- **Próxima revisión**: 2026-01-29
    
- **Veces revisado**: 0
    
- **Nivel de comprensión**: 💡 Entiendo bien
    
- **Tiempo estimado de repaso**: 15min
    

---

> [!tip] 💡 Próximos pasos
> 
> Cuando revises esta nota, intenta recitar el "Ejemplo Práctico" en voz alta como si estuvieras respondiendo al Manager de Accenture.