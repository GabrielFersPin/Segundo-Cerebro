---
created: 2026-03-24 19:54
modified: 2026-03-24 19:54
area: 
tipo_nota: tecnica
status: 🔴 Por procesar
nivel-comprension: "❓"
proxima-revision: 2026-03-31
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
cards-deck: 
procesamiento: CAPTURA-RAPIDA
prioridad: FUNDACIONAL
tipo-captura: concepto
complejidad: ⭐
origen: Curso
urgente: false
---

# LangGraph

> [!info] Contexto captura
> **Fecha**: 2026-03-24 19:54
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> *Escribe aquí la idea principal o el concepto clave en 1-2 frases*


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->

### ReAct (Reason + Act)
>LLM first thinks what to do and them decides an action to take
>The action is execute in a environment and an observation is returned
>Create a class Agent to build the agent

### Creating the agent
> ```python
> class Agent:
> 	def __init__ (self, system=""): # The agent is parameterize by a system message
> 		self.system = system # atribute message
> 		self.messages = []
> 		if self.system:
> 			self.messagens.append({}"role":"system", "content": system})
> 	
> 	def __call_(self, message): # The message is take by the user and than give it back from the assistant
> 		self.messages.append({"role", "user", "content": message})
> 		result = self.execute()
> 		self.messages.append({"role", "assistant", "content": result})
> 		return result

### Graphs
> Nodes: Agents or functions
> Edges: Connect nodes
> Conditional Edges: Decisions
> 


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
| Capturado | 2026-03-24 19:54 |
| Asignatura | `= this.asignatura` |
| Prioridad | `= this.prioridad` |
| Estado | Captura rápida → Pendiente procesamiento |
| Revisión | `= this.proxima-revision` |

---

#pendiente-procesar #captura-rapida
