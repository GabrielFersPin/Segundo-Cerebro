---
cards-deck:
created: 2026-03-24 15:46
modified: 2026-03-24 15:46
status: 🌱
tipo_nota: tecnica
asignatura:
procesamiento: CAPTURA-RAPIDA
prioridad: FUNDACIONAL
tipo-captura: concepto
fecha-examen: ""
proxima-revision: 2026-03-31
complejidad: ⭐
tiempo-estimado: ""
origen: Curso
urgente: false
---

# CrewAI

> [!info] Contexto captura
> **Fecha**: 2026-03-24 15:46
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> *Escribe aquí la idea principal o el concepto clave en 1-2 frases*


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->

> How to create an Agent:
	 role=
	 goal=
	 backstory=
	 allow_delegation=False
	 Verbose=True -> To see what it's doing

>Agent: Planner
>The benefit os using multiple strings:
 >	vername = "line 1 of text"
>		   	"line 2 of text"

### Create a Task
```
plan = Task (
 	  description=(
 	  )
     expected_output=" ",
     agent=planner, # put the agent to complete this task
 )
```
### Create the crew 
```
crew = Crew(
	agents=[planner, writer, editor]
	tasks=[plan, write, edit],
	verbose = 2
	)	
```

### Execute the crew
```
topic = 'Your Topic here'
result = crew.kickoff(inputs=('topic':'Artificial Intelligence'))
```

### Key elements
>	Focus
>	Choose the tools that your agent will do
>	Role Playing
>	Cooperation: Ability to cooperate on producing ideas 
>	Guardrails: Prevent the agent to allucinate and make the results consistent
>	Memory: The ability to the agent to remember what was done
>	Long Term Memory: Store in the database locals, self-critique itself to get better

### Support Automation 
>Allow delgation
>	allow_delegation=False
>Add Q&A agent: review task

### Mental Framework
>What would be the people that they would hire to do this job for them

### Key elements of agent tools
>Versitile
>	A tool need to be able to accept different kin of requests
>Fail Gracefully
>	If something goes wrong they can self-heal. CrewAI implements that by default.
>	Ask agent to retry given the error message
>Caching
>	caching layer that prevents the unnacessaary requests.
>	Cross-agent caching: If one agent tried to use a tool with a given set of arguments, and another agent try to use the same tool, with the same set of arguments, even if they are different agents, they're actually use a cache layer. So the second time they try to use a tool, they not going to do that API call
>Tools examples:
>	search the internet
>	scrape a website
>	connect to a database
>	call an API
>	send notifications


### Tasks

>A clear description of what is the task
>Set a clear and concise expectation
>Set a context
>Set a callback
>Override Agent tools with specific task tools
>Force human input before and of task


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
| Capturado | 2026-03-24 15:46 |
| Asignatura | `= this.asignatura` |
| Prioridad | `= this.prioridad` |
| Estado | Captura rápida → Pendiente procesamiento |
| Revisión | `= this.proxima-revision` |

---

#pendiente-procesar #captura-rapida
