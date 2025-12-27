---
cards-deck: <% await tp.system.suggester(["Algoritmos", "Nube", "DataScience", "Arquitectura"], ["Algoritmos", "Nube", "DataScience", "Arquitectura"]) %>
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
modified: <% tp.date.now("YYYY-MM-DD HH:mm") %>
status: 🌱
tipo_nota: tecnica
asignatura: <% await tp.system.suggester(["Algoritmos", "Arquitectura", "Infraestructura-Nube", "Fundamentos-DS"], ["Algoritmos", "Arquitectura", "Infraestructura-Nube", "Fundamentos-DS"]) %>
procesamiento: CAPTURA-RAPIDA
prioridad: <% await tp.system.suggester(["EXAMEN-PROXIMO", "EXAMEN-MEDIO", "EXAMEN-LEJANO", "EJERCICIO", "FUNDACIONAL"], ["EXAMEN-PROXIMO", "EXAMEN-MEDIO", "EXAMEN-LEJANO", "EJERCICIO", "FUNDACIONAL"]) %>
tipo-captura: <% await tp.system.suggester(["💡 Concepto", "❓ Pregunta", "🔧 Ejercicio", "📖 Lectura", "🐛 Duda", "💭 Idea"], ["concepto", "pregunta", "ejercicio", "lectura", "duda", "idea"]) %>
fecha-examen: ""
proxima-revision: <% tp.date.now("YYYY-MM-DD", 7) %>
complejidad: ⭐
tiempo-estimado: ""
origen: <% await tp.system.prompt("📍 Fuente/Contexto (clase, libro, video, etc):") %>
urgente: false
---

# <% await tp.system.prompt("📌 Título del concepto:") %>

> [!info] Contexto captura
> **Fecha**: <% tp.date.now("YYYY-MM-DD HH:mm") %>
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> *Escribe aquí la idea principal o el concepto clave en 1-2 frases*


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->




---

## 🔑 Keywords / Conceptos clave

`keyword1`, `keyword2`, `keyword3`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después


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




---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | <% tp.date.now("YYYY-MM-DD HH:mm") %> |
| Asignatura | `= this.asignatura` |
| Prioridad | `= this.prioridad` |
| Estado | Captura rápida → Pendiente procesamiento |
| Revisión | `= this.proxima-revision` |

---

#pendiente-procesar #captura-rapida
