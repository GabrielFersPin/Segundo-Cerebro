---
tags: [clase, FastMCP, ejemplo, arxiv]
deck: Obsidian::FastMCP
created: 2026-05-06 15:10
modified: 2026-05-06 15:10
status: 🟡
tipo_nota: clase
profesor: No especificado
---

# 📝 FastMCP - Ejemplo de implementación

> [!info] Metadata de la clase
> **Fecha**: 2026-05-06
> **Hora**: 15:10
> **Profesor**: No especificado
> **Estado**: 🟡 Por procesar

---

## 🎯 Objetivo de la clase

Registrar el patrón de uso de FastMCP con funciones decoradas y entender cómo se usa en un ejemplo real de búsqueda de papers.

---

## 📊 Captura Rápida

- Se define un servidor `FastMCP("research")`.
- Las herramientas se declaran con `@mcp.tool()`.
- `search_papers(topic, max_results)` busca en arXiv y guarda resultados en JSON.
- `extract_info(paper_id)` recorre las carpetas y devuelve información del paper.
- El servidor se arranca con `mcp.run(transport='stdio')`.

---

## 📝 Notas detalladas

### Patrón principal
1. Importar `FastMCP`.
2. Crear la instancia del MCP.
3. Definir funciones de herramienta con `@mcp.tool()`.
4. Usar type hints y docstrings para la generación automática de schemas.
5. Inicializar el servidor con el transporte adecuado.

### Ejemplo de herramientas
- `search_papers(topic: str, max_results: int = 5) -> List[str]`
  - Busca artículos en arXiv.
  - Guarda los datos en `papers_info.json`.
  - Devuelve lista de IDs de papers.

- `extract_info(paper_id: str) -> str`
  - Lee los JSON guardados.
  - Busca el paper solicitado.
  - Devuelve información en formato JSON o un mensaje de error.

### Detalles importantes
- Se crea la ruta `papers/<topic>` y se guarda `papers_info.json`.
- Se maneja `FileNotFoundError` y `json.JSONDecodeError` para evitar fallos.
- FastMCP convierte estos métodos en herramientas usables por el LLM.

---

## 🔗 Conexiones
- [[MCP - Model Context Protocol]]
- [[FastMCP vs FastAPI]]

---

## 🎴 Flashcards
- **¿Cómo se declara una herramienta FastMCP?**
  - Con `@mcp.tool()` sobre una función.
- **¿Qué hace `mcp.run(transport='stdio')`?**
  - Arranca el servidor MCP usando stdio como transporte.
- **¿Por qué usar docstrings en FastMCP?**
  - Para que el framework genere automáticamente los esquemas de herramienta.
