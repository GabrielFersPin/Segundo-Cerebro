---
tags: [clase, prompt-engineering, LLM, AI]
deck: Obsidian::Prompt Engineering
created: 2026-05-11 10:00
modified: 2026-05-11 10:00
status: 🟡
tipo_nota: clase
profesor: No especificado
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
cards-deck: ""
---

# 📝 Prompt Engineering - Técnicas y mejores prácticas

> [!info] Metadata de la clase
> **Fecha**: 2026-05-11
> **Hora**: 10:00
> **Profesor**: No especificado
> **Estado**: 🟡 Por procesar

---

## 🎯 Objetivo de la clase

Entender qué es prompt engineering, las técnicas fundamentales para optimizar prompts y cómo diseñar instrucciones efectivas para modelos de lenguaje.

---

## 📊 Captura Rápida

### ⚡ Notas Rápidas

- Prompt engineering es el arte de diseñar instrucciones para obtener mejores respuestas de LLMs.
- Un buen prompt define claramente el contexto, rol, tarea y formato esperado.
- Las técnicas incluyen: few-shot learning, chain-of-thought, role-playing y temperatura.
- El mismo prompt puede dar resultados muy diferentes según parámetros y estructura.

### 🔑 Conceptos Clave

- **Prompt**: instrucción o pregunta que das a un LLM.
- **Few-shot learning**: proporcionar ejemplos para guiar la respuesta.
- **Chain-of-thought**: pedir razonamiento paso a paso.
- **Temperature**: controla la creatividad (0 = determinístico, 1 = creativo).
- **Token limit**: restricción de longitud de entrada/salida.

### ❓ Dudas

- ¿Por qué un pequeño cambio de wording cambia tanto la respuesta?
- ¿Cómo sé si mi prompt es óptimo?
- ¿Existen técnicas para evitar alucinaciones?

### 💡 Insights

- El prompt engineering es casi un arte: no hay recetas definitivas, requiere experimentación.
- Los mejores prompts son específicos, contextuales y con ejemplos claros.
- La claridad y la estructura son más importantes que la extensión.

### ⚠️ Importante

- No confundir prompt engineering con manipulación: debe ser ético y transparente.
- Los prompts óptimos para un modelo pueden no funcionar igual en otro.
- El "jailbreaking" no es prompt engineering legítimo.

---

## 📝 Notas Detalladas

### ¿Qué es Prompt Engineering?

Prompt engineering es la práctica de diseñar y optimizar instrucciones (prompts) para obtener respuestas precisas, relevantes y de alta calidad de modelos de lenguaje. Es la interfaz entre el usuario y el modelo.

Un buen prompt:

- Define claramente la tarea.
- Proporciona contexto suficiente.
- Especifica el formato de salida esperado.
- Usa lenguaje preciso y sin ambigüedades.

### Estructura básica de un prompt efectivo

```
[CONTEXTO] + [ROL/PERSONA] + [TAREA] + [RESTRICCIONES] + [FORMATO]
```

**Ejemplo débil:**

```
¿Qué es machine learning?
```

**Ejemplo efectivo:**

```
Eres un experto en ciencia de datos. Explica qué es machine learning en 2-3 párrafos, 
enfocándote en aplicaciones prácticas. Usa ejemplos concretos.
```

### Técnicas principales

#### 1. **Few-Shot Learning**

Proporcionar ejemplos de entrada-salida para guiar el modelo.

```
Traduce al inglés:
- "Hola" → "Hello"
- "¿Cómo estás?" → "How are you?"
- "Buenos días" → ?
```

#### 2. **Chain-of-Thought (CoT)**

Pedir al modelo que razone paso a paso antes de responder.

```
Resuelve este problema paso a paso:
Si un tren viaja a 60 km/h durante 2 horas, ¿cuántos km recorre?
Primero, identifica los datos. Luego, aplica la fórmula. Finalmente, calcula.
```

#### 3. **Role-Playing**

Asignar un rol específico al modelo para enmarcar la respuesta.

```
Eres un abogado especialista en derecho civil. Un cliente pregunta sobre derechos 
de propiedad. Responde de manera profesional y clara.
```

#### 4. **Temperature y Parámetros**

- **Temperature 0**: respuestas determinísticas, ideales para tareas precisas.
- **Temperature 0.7**: balance entre coherencia y creatividad (típico).
- **Temperature 1+**: muy creativo, útil para brainstorming.

#### 5. **Negation Framing**

Indicar qué NO hacer ayuda al modelo a enfocar mejor.

```
Escribe un artículo sobre IA. NO incluyas especulación futura. 
Cita solo hechos verificables. NO uses lenguaje sensacionalista.
```

### Errores comunes

- ❌ **Ser vago**: "Hazme un texto" vs ✅ "Escribe 500 palabras sobre X para Y audiencia"
- ❌ **Múltiples tareas mezcladas**: ✅ numera o separa claramente
- ❌ **Olvidar contexto**: ✅ siempre proporciona background
- ❌ **Expectativas poco realistas**: el modelo tiene limitaciones de conocimiento y razonamiento
- ❌ **No iterar**: mejora el prompt si el resultado no es ideal

### Relación con agentes y MCP

En sistemas de agentes (como CrewAI), el prompt engineering define:

- Las instrucciones del agente (role, goal, backstory).
- El formato de herramientas y cómo se invocan.
- La forma en que el agente razona sobre problemas.

En FastMCP, los prompts guían cómo los LLMs deciden usar herramientas disponibles.

---

## 🔄 Procesamiento Post-Clase

### 📋 Checklist de Procesamiento

- [ ] Revisar y practicar las técnicas principales.
- [ ] Experimentar con different temperatures.
- [ ] Crear ejemplos personalizados de few-shot.
- [ ] Documentar prompts efectivos.
- [ ] Conectar con agentes y sistemas LLM.
- [ ] Identificar gaps de conocimiento.

### 🎯 Acciones Prioritarias

1. Desarrollar una biblioteca de prompts reutilizables.
2. Practicar chain-of-thought en problemas complejos.
3. Entender cómo prompt engineering se aplica a agentes.

### 🔗 Conexiones

- [[A2A - Agent-to-Agent]]
- [[CrewAI]]
- [[FastMCP - Ejemplo de implementación]]
- [[FastAPI vs FastMCP]]
- [[async - Programación asincrónica]]

---

## 🎴 Flashcards Rápidas

¿Qué es prompt engineering?::Diseño y optimización de instrucciones para obtener mejores respuestas de LLMs. #card
¿Cuál es la estructura básica de un prompt efectivo?::Contexto + Rol + Tarea + Restricciones + Formato esperado. #card
¿Qué es Chain-of-Thought?::Técnica que pide al modelo razonar paso a paso antes de responder. #card
¿Cuándo usar temperature alta vs baja?::Temperature baja (0-0.3) para tareas precisas; temperatura alta (0.7+) para creatividad. #card
