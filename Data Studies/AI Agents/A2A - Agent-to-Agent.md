---
cards-deck:
created: 2026-05-06
modified: 2026-05-06
status: 🌱
tipo_nota: tecnica
area: IA / Agentes
procesamiento: CAPTURA-RAPIDA
prioridad: FUNDACIONAL
tipo-captura: concepto
fecha-examen: ""
proxima_revision: 2026-05-13
complejidad: ⭐
tiempo-estimado: ""
origen: Estudio personal
urgente: false
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
---

# A2A - Agent-to-Agent

> [!info] Contexto captura
> **Fecha**: 2026-05-06
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 🧠 Definición

A2A (Agent-to-Agent) describe la interacción directa entre agentes inteligentes autónomos. En este paradigma, un agente puede:
- comunicarse con otro agente,
- delegar tareas,
- compartir hallazgos,
- coordinar planes, y
- retroalimentarse mutuamente para lograr objetivos complejos.

A2A no es solo "mensaje entre agentes"; es un patrón de colaboración en el que cada agente razona sobre el estado, roles y resultados de sus pares.

---

## 🌟 Importancia

- Permite sistemas distribuidos más escalables y resilientes.
- Facilita la división de trabajo entre agentes especializados.
- Mejora la capacidad de resolver problemas multietapa sin intervención humana directa.
- Reduce la carga cognitiva de cada agente al delegar subtareas a compañeros más adecuados.
- Abre la puerta a la orquestación de ecosistemas de agentes heterogéneos.

> En la práctica, A2A transforma un conjunto de agentes aislados en un sistema colectivo con coordinación emergente.

---

## 🧩 Ejemplos

### Ejemplo 1: Escritor y editor
- Agente A: genera borradores de contenido.
- Agente B: revisa, corrige y sugiere mejoras.
- Flujo A2A: A envía texto a B, B responde con cambios y comentarios, A ajusta el borrador.

### Ejemplo 2: Planificador y ejecutor
- Agente Planificador: define pasos, prioridades y dependencias.
- Agente Ejecutor: realiza cada acción usando herramientas externas.
- Flujo A2A: el planificador delega tareas; el ejecutor reporta estado y solicita clarificaciones.

### Ejemplo 3: Monitor y reparador
- Agente Monitor: detecta anomalías en datos o servicios.
- Agente Reparador: aplica correcciones o reinicia procesos.
- Flujo A2A: el monitor envía alerta, el reparador responde con diagnóstico y ejecuta la solución.

---

## 🔗 Enlaces relacionados

- [[CrewAI]]
- [[DataX]]
- [[LangGraph]]
- [[Agentes_Documento_Completo]]

---

## 🏷️ Keywords

- A2A
- Agent-to-Agent
- coordinación de agentes
- delegación
- comunicación entre agentes
- orquestación
- sistemas multiagente
- agentes autónomos
- colaboración agentic
- ecosistema de agentes

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## ❓ Preguntas / Dudas pendientes

- [ ] ¿Qué formatos de mensaje A2A son más eficaces?
- [ ] ¿Cómo manejar conflictos de autoridad entre agentes?
- [ ] ¿Qué guardrails son necesarios para evitar bucles de delegación?

---

## ✅ Checklist procesamiento

- [ ] Revisar y expandir ejemplos con casos prácticos
- [ ] Añadir diagramas de flujo de comunicación
- [ ] Crear flashcards sobre patrones A2A
- [ ] Conectar con notas de coordinación y orquestación

---

## 💭 Notas adicionales / Ideas rápidas

- Incluir referencia a sistemas multi-agente reales y protocolos de mensajería.
- Pensar en A2A como base para agentes especializados que comparten resultados semánticos.

---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-05-06 |
| Asignatura | IA / Agentes |
| Prioridad | FUNDACIONAL |
| Estado | Captura rápida → Pendiente procesamiento |
| Revisión | 2026-05-13 |

---

#pendiente-procesar #captura-rapida
