---
tags: [clase, comparación, FastMCP, FastAPI]
deck: Obsidian::Comparación
created: 2026-05-06 15:05
modified: 2026-05-06 15:05
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

# 📝 FastMCP vs FastAPI

> [!info] Metadata de la clase
> **Fecha**: 2026-05-06
> **Hora**: 15:05
> **Profesor**: No especificado
> **Estado**: 🟡 Por procesar

---

## 🎯 Objetivo de la clase

Comparar las características y usos de FastMCP y FastAPI para saber cuándo conviene usar cada tecnología.

---

## 📊 Captura Rápida

### 🔑 Diferencia central
- FastMCP: protocolo de integración para modelos de lenguaje y herramientas.
- FastAPI: framework HTTP para construir APIs web y microservicios.

### ⚡ Puntos clave
- FastMCP usa `@mcp.tool()` y type hints para generar esquemas.
- FastAPI usa Pydantic y OpenAPI para validar datos y documentar rutas.
- FastMCP típicamente se ejecuta con transporte especializado (por ejemplo `stdio`).
- FastAPI se ejecuta como servidor web (Uvicorn, Hypercorn, etc.).

### ❓ Preguntas útiles
- ¿Necesito una API web abierta a clientes humanos o una interfaz de herramientas para un LLM?
- ¿Quiero exponer endpoints HTTP o necesito un protocolo de herramientas para agentes?
- ¿Necesito documentación automática OpenAPI o un esquema de herramienta LLM?

---

## 📝 Comparación detallada

### FastMCP
- Propósito: conectar un modelo de lenguaje con herramientas externas.
- Modelo: definiciones de funciones como herramientas.
- Generación de esquema: automática con type hints y docstrings.
- Transporte: puede usar `stdio`, otros protocolos, y posiblemente adaptadores.
- Ideal para: agentes, asistentes basados en LLM, herramientas que ejecutan lógica de negocio desde prompts.

### FastAPI
- Propósito: exponer APIs HTTP de forma rápida y tipada.
- Modelo: rutas HTTP con decoradores `@app.get()`, `@app.post()`, etc.
- Generación de esquema: OpenAPI/Swagger automáticos.
- Transporte: HTTP/HTTPS.
- Ideal para: servicios web, microservicios, APIs REST para clientes web y móviles.

---

## 🔍 Tabla comparativa

| Característica | FastMCP | FastAPI |
|---|---|---|
| Enfoque | Integración LLM/herramientas | API web general |
| Transporte típico | `stdio`, protocolo interno | HTTP/HTTPS |
| Esquemas | Auto-generados desde type hints | OpenAPI + Pydantic |
| Uso principal | Agentes y herramientas de LLM | Servicios web y APIs REST |
| Seguridad | Depende del protocolo / control de herramientas | Seguridad HTTP estándar |
| Documentación | Implícita en herramientas | Documentación Swagger automática |

---

## 🔗 Conexiones
- [[MCP - Model Context Protocol]]
- [[FastMCP - Ejemplo de implementación]]
- [[FastAPI]]

---

## 🎴 Flashcards
- **¿Para qué sirve FastMCP?**
  - Para exponer herramientas como funciones a un LLM.
- **¿Para qué sirve FastAPI?**
  - Para crear APIs HTTP rápidas y tipadas.
- **¿Qué diferencia el transporte de FastMCP del de FastAPI?**
  - FastMCP usa transporte especializado/stdio mientras FastAPI usa HTTP.
