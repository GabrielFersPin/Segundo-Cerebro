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
---

# Amazon SQS (Simple Queue Service)

> [!info] Contexto captura
> **Fecha**: 2026-09-07 13:16
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> Amazon SQS (Simple Queue Service) es un servicio de colas de mensajes que permite desacoplar aplicaciones y procesar tareas de forma asíncrona.


### 🎯 Detalles / Contenido

Funcionamiento básico:

> Productor → cola SQS → consumidor

Ejemplo:

1. Una aplicación recibe un pedido.
2. Envía un mensaje a SQS.
3. Un worker o una Lambda lee el mensaje.
4. Procesa el pedido.
5. El mensaje se elimina de la cola.

Ventajas:

- Evita que los servicios tengan que estar disponibles al mismo tiempo.
- Absorbe picos de tráfico.
- Permite reintentos si el procesamiento falla.
- Ayuda a desacoplar componentes.
- Puede enviar mensajes fallidos a una Dead-Letter Queue (DLQ).

Tipos principales:

- Standard Queue: alto rendimiento, pero puede entregar mensajes duplicados o fuera de orden.
- FIFO Queue: conserva el orden y evita duplicados dentro de ciertas condiciones, aunque ofrece menor capacidad que Standard.

Comparación rápida:

- SQS: almacena mensajes hasta que un consumidor los procesa.
- [[Amazon SNS]]: distribuye mensajes a varios suscriptores.
- [[AWS EventBridge]]: enruta eventos según reglas y patrones.


---

## 🔑 Keywords / Conceptos clave

`AWS`, `SQS`, `Messaging`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

_Flashcards pendientes de crear_

> 💡 **Formato recomendado**:
> - Inline: `¿Pregunta?::Respuesta #tags`
> - Reversa: `Término:::Definición #tags`
> - Cloze: `Texto con ==palabra== oculta`
---

## ❓ Preguntas / Dudas pendientes

- [ ]
- [ ]

---

## 🧩 Conexiones potenciales

<!-- ¿Con qué otros temas se relaciona? Escribe rápido, ya harás los links después -->

-
-

---

## ✅ Checklist procesamiento

- [ ] Revisar y expandir contenido
- [ ] Crear flashcards si es necesario
- [ ] Hacer ejercicios relacionados
- [ ] Conectar con otras notas ([[]])
- [ ] Actualizar nivel de comprensión
- [ ] Mover a vault definitivo / Cambiar status a 🌿

---

## 💭 Notas adicionales / Ideas rápidas

<!-- Zona libre para cualquier cosa que quieras capturar rápido -->

SQS es una cola que permite enviar tareas entre servicios de forma segura, asíncrona y desacoplada.


---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-09-07 13:16 |
| Área/Tema | `= this.area` |
| Estado | `= this.status` |
| Prioridad | `= this.prioridad` |
| Revisión | `= this.proxima-revision` |
| Nivel de comprensión | `= this.nivel-comprension` |

---

#pendiente-procesar #captura-rapida
