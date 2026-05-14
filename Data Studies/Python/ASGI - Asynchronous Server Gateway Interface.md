---
tags: [clase, ASGI, web, servidor]
deck: Obsidian::Python
created: 2026-05-06 15:35
modified: 2026-05-06 15:35
status: 🟡
tipo_nota: clase
profesor: No especificado
---

# 📝 ASGI (Asynchronous Server Gateway Interface)

> [!info] Metadata de la clase
> **Fecha**: 2026-05-06
> **Hora**: 15:35
> **Profesor**: No especificado
> **Estado**: 🟡 Por procesar

---

## 🎯 Objetivo de la clase

Entender qué es ASGI, cómo funciona, y por qué es fundamental para los servidores web modernos en Python.

---

## 📊 Captura Rápida

### ⚡ Notas Rápidas
- ASGI = especificación para aplicaciones web asincrónicas en Python.
- Es la evolución asincrónica de WSGI (Web Server Gateway Interface).
- Permite que el servidor maneje múltiples conexiones simultáneamente sin bloqueos.
- `uvicorn` es un servidor ASGI que ejecuta aplicaciones con el comando `uv`.

### 🔑 Conceptos Clave
- ASGI define cómo interactúan servidores web y aplicaciones Python.
- WSGI = sincrónico, ASGI = asincrónico.
- Un servidor ASGI puede procesar muchas peticiones concurrentemente.
- FastAPI y Starlette utilizan ASGI por defecto.

### ❓ Dudas
- ¿Qué diferencia hay entre ASGI y WSGI?
- ¿Necesito entender async/await para usar ASGI?
- ¿Por qué ASGI es mejor que WSGI para aplicaciones modernas?

### 💡 Insights
- ASGI no es un framework, es una especificación de interfaz entre servidor y aplicación.
- La asincronía en ASGI permite mejor utilización de recursos en aplicaciones web.

### ⚠️ Importante
- No todas las librerías Python son asincrónicas: algunas bloquean aún dentro de ASGI.
- ASGI requiere un entendimiento básico de `async` y `await`.

---

## 📝 Notas Detalladas

### ¿Qué es ASGI?
ASGI es una especificación que define cómo los servidores web Python se comunican con aplicaciones web asincrónicas. Actúa como un puente entre el protocolo HTTP y la lógica de la aplicación.

Antes de ASGI existía WSGI (sincrónico), que procesaba una solicitud a la vez. ASGI permite procesar múltiples solicitudes concurrentemente usando async/await.

### Diferencia entre WSGI y ASGI

| Característica | WSGI | ASGI |
|---|---|---|
| Modelo | Sincrónico | Asincrónico |
| Concurrencia | Múltiples procesos/threads | Async/await en un evento loop |
| Bloqueos | Bloquean la aplicación | No bloquean si se usa `async` |
| Frameworks | Django, Flask tradicional | FastAPI, Starlette, Quart |
| Escalabilidad | Limitada por procesos | Mejor uso de recursos |

### Ejemplos de servidores ASGI
- `uvicorn` (recomendado)
- `hypercorn`
- `daphne`

### ¿Cómo funciona ASGI con `uv`?
Cuando ejecutas:

```bash
uv app:app --reload
```

Estás indicando a `uvicorn` que:
1. Cargue la aplicación ASGI desde `app.py` (variable `app`).
2. Reinicie automáticamente ante cambios de código (`--reload`).
3. Procese solicitudes de forma asincrónica.

### Relación con async
ASGI y `async` están íntimamente ligados. Para aprovechar ASGI, las funciones manejadoras deben ser `async`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello"}
```

Sin `async`, la aplicación se comportaría como WSGI tradicional y perdería beneficios de ASGI.

---

## 🔄 Procesamiento Post-Clase

### 📋 Checklist de Procesamiento
- [ ] Confirmar la diferencia WSGI vs ASGI con ejemplos prácticos.
- [ ] Revisar cómo FastAPI usa ASGI.
- [ ] Entender async/await en profundidad.

### 🎯 Acciones Prioritarias
1. Leer la nota sobre [[async - Programación asincrónica]].
2. Probar una aplicación FastAPI con `uv`.
3. Comparar rendimiento de WSGI vs ASGI con múltiples conexiones.

### 🔗 Conexiones
- [[async - Programación asincrónica]]
- [[uv y npm en virtual environment]]
- [[FastAPI vs FastMCP]]

---

## 🎴 Flashcards Rápidas
- **¿Qué es ASGI?**
  - Especificación para servidores y aplicaciones web asincrónicas en Python.
- **¿Cuál es la principal ventaja de ASGI sobre WSGI?**
  - Manejo concurrente de solicitudes sin bloqueos gracias a async/await.
- **¿Qué es uvicorn?**
  - Un servidor ASGI rápido para ejecutar aplicaciones Python asincrónicas.
