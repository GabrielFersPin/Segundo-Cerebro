---
tags: [clase, MCP, FastMCP, FastAPI]
deck: Obsidian::MCP
created: 2026-05-06 15:00
modified: 2026-05-06 15:00
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

# 📝 MCP - Model Context Protocol

> [!info] Metadata de la clase
> **Fecha**: 2026-05-06
> **Hora**: 15:00
> **Profesor**: No especificado
> **Estado**: 🟡 Por procesar

---

## 🎯 Objetivo de la clase

Entender qué es MCP, distinguir entre implementación de bajo nivel y alto nivel, y conectar el concepto con FastMCP y su comparación frente a FastAPI.

---

## 📊 Captura Rápida

### ⚡ Notas Rápidas

- MCP define cómo un LLM se conecta con fuentes externas de forma segura.
- Existen dos formas de implementar un MCP: bajo nivel y alto nivel.
- FastMCP es una implementación de alto nivel que usa funciones decoradas como herramientas.
- FastMCP genera esquemas automáticamente a partir de type hints y docstrings.

### 🔑 Conceptos Clave

- MCP = Model Context Protocol.
- Low-level: control total de las peticiones, más trabajo manual.
- High-level: define herramientas como funciones, FastMCP se encarga de la infraestructura.
- FastAPI es un framework HTTP para APIs, mientras FastMCP es un protocolo especializado para LLM.

### ❓ Dudas

- ¿Cómo se asegura la seguridad en un MCP cuando se conectan fuentes externas?
- ¿FastMCP soporta transporte HTTP además de stdio?
- ¿Cuál es la frontera entre un servicio web tradicional y un protocolo de herramientas para LLM?

### 💡 Insights

- La comparación entre FastMCP y FastAPI ayuda a entender cuándo conviene usar un framework general versus una solución especializada.
- Un MCP puede ser un puente entre un LLM y datos externos sin exponer directamente la lógica de negocio.

### ⚠️ Importante

- FastMCP no es simplemente otra API web: es un conjunto de herramientas orientado a la integración con modelos.
- El high-level implementation de FastMCP reduce el boilerplate y acelera el desarrollo.

### 📚 Referencias Mencionadas

- FastMCP
- FastAPI
- arxiv

---

## 📝 Notas Detalladas

### ¿Qué es MCP?

MCP (Model Context Protocol) describe cómo un modelo de lenguaje interactúa con fuentes externas, usando un protocolo seguro para las solicitudes y respuestas. El objetivo es que el LLM no tenga que gestionar directamente toda la conectividad ni la lógica de I/O.

### Implementación de bajo nivel

En una implementación de bajo nivel se define y maneja manualmente cada tipo de petición. Esta aproximación ofrece control completo sobre la comunicación, pero requiere más trabajo y mayor complejidad.

### Implementación de alto nivel con FastMCP

FastMCP permite construir MCPs más rápido. La idea clave es que el desarrollador define herramientas como funciones decoradas con `@mcp.tool()` y el framework genera automáticamente los esquemas necesarios en base a los type hints y docstrings.

#### Ventajas de FastMCP

- Reducción de código repetitivo.
- Auto-generación de schemas.
- Mejor integración con modelos de lenguaje.
- Soporte para herramientas con parámetros tipados.

#### Ejemplo resumido

El ejemplo usa un servidor FastMCP llamado `research`, define herramientas `search_papers` y `extract_info`, y guarda información de artículos en JSON. El servidor se inicia con `mcp.run(transport='stdio')`.

---

## 🔄 Procesamiento Post-Clase

### 📋 Checklist de Procesamiento

- [ ] Revisar y organizar notas rápidas.
- [ ] Clarificar conceptos confusos sobre MCP.
- [ ] Resolver dudas pendientes sobre transporte y seguridad.
- [ ] Crear notas atómicas de conceptos clave.
- [ ] Generar flashcards de lo importante.
- [ ] Conectar con conocimiento previo sobre APIs y agentes.
- [ ] Identificar gaps de conocimiento.
- [ ] Planificar repaso con Active Recall.

### 🎯 Acciones Prioritarias

1. Definir claramente la diferencia entre FastMCP y FastAPI.
2. Investigar cómo FastMCP gestiona el transporte y la seguridad.
3. Crear una nota comparativa específica para FastMCP vs FastAPI.

### 🔗 Conexiones con otras notas

- [[FastMCP vs FastAPI]]
- [[FastAPI]]
- [[MCP - Model Context Protocol]]
- [[FastMCP - Ejemplo de implementación]]

---

## 🎴 Flashcards Rápidas

¿Qué es MCP?::Protocolo para conectar un LLM con fuentes externas de forma segura. #card
¿Cuál es la ventaja principal de FastMCP?::Permite definir herramientas como funciones y genera esquemas automáticamente. #card
¿En qué se diferencia FastMCP de FastAPI?::FastMCP es especializado en integración LLM/herramientas, FastAPI es un framework HTTP para APIs generales. #card
