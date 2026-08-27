---
created: 2026-05-06
modified: 2026-08-22
area: IA / Agentes
tipo_nota: tecnica
status: 🌿 Creciendo
nivel-comprension: 💡
proxima-revision: 2026-11-30
ultima-revision: 2026-08-22
veces-revisado: 3
tiempo-repaso: 15min
cards-deck:
procesamiento: COMPLETO
prioridad: FUNDACIONAL
tipo-captura: concepto
complejidad: ⭐
origen: Estudio personal
urgente: false
proxima_revision: 2026-05-13
tiempo-estimado: 20min
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
- Suele ser JSON
- [ ] ¿Cómo manejar conflictos de autoridad entre agentes?
- Los conflictos de autoridad entre agentes se manejan mejor definiendo de antemano quién puede decidir qué. No conviene que dos agentes tengan autoridad absoluta sobre el mismo recurso o acción.

Un modelo básico sería:

1. Asignar dominios de autoridad
    
    - Agente financiero: pagos y presupuestos.
    - Agente técnico: configuración del sistema.
    - Agente de soporte: respuestas al cliente.
    - Un agente solo puede actuar dentro de sus permisos.
- [ ] ¿Qué guardrails son necesarios para evitar bucles de delegación?
- Para evitar bucles de comprobación entre agentes, necesitas limitar tanto el tiempo como el número de intentos y detectar cuándo no hay progreso.

---

## ✅ Checklist procesamiento

- [x] Revisar y expandir ejemplos con casos prácticos ✅ 2026-08-22
- [ ] Añadir diagramas de flujo de comunicación
- [ ] Crear flashcards sobre patrones A2A
- [ ] Conectar con notas de coordinación y orquestación

---

## 💭 Notas adicionales / Ideas rápidas

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

# pendiente-procesar #captura-rapida


---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Tarea para aclarar una duda de concepto. Usa #mejora-concepto
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia
