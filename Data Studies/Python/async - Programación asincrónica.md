---
tags: [clase, Python, async, await, concurrencia]
deck: Obsidian::Python
created: 2026-05-06 15:40
modified: 2026-05-06 15:40
status: 🟡
tipo_nota: clase
profesor: No especificado
---

# 📝 async - Programación asincrónica

> [!info] Metadata de la clase
> **Fecha**: 2026-05-06
> **Hora**: 15:40
> **Profesor**: No especificado
> **Estado**: 🟡 Por procesar

---

## 🎯 Objetivo de la clase

Entender qué es la programación asincrónica en Python, cómo funcionan `async` y `await`, y cuándo usarlas en el contexto de ASGI.

---

## 📊 Captura Rápida

### ⚡ Notas Rápidas
- `async` declara una función que puede pausarse y reanudarse.
- `await` pausa una función `async` hasta que una operación termine.
- La programación asincrónica permite ejecutar múltiples operaciones sin bloquear.
- Ideal para operaciones I/O (red, archivos, bases de datos).

### 🔑 Conceptos Clave
- **Sincrónico**: esperas a que termine una operación antes de continuar.
- **Asincrónico**: inicias una operación y continúas con otras tareas mientras se completa.
- **Event loop**: bucle que gestiona tareas asincrónicas.
- **await**: solo se puede usar dentro de funciones `async`.

### ❓ Dudas
- ¿async crea threads nuevos? No, todo se ejecuta en un solo thread con el event loop.
- ¿Puedo mezclar código sincrónico y asincrónico? Con cuidado, sí.
- ¿Es async más rápido para operaciones CPU? No, para I/O.

### 💡 Insights
- `async` no es paralelismo, es concurrencia: múltiples tareas intercaladas en un thread.
- La verdadera ventaja de async aparece cuando hay muchas operaciones I/O simultáneas.

### ⚠️ Importante
- `await` solo funciona dentro de funciones `async`.
- Si una función `async` hace operaciones CPU pesadas sin `await`, bloquea todo el event loop.
- Usar bibliotecas asincrónicas (`aiohttp`, `asyncpg`) para maximizar beneficios.

---

## 📝 Notas Detalladas

### ¿Qué es la programación asincrónica?
La programación asincrónica permite que un programa ejecute múltiples operaciones sin esperar a que cada una termine. En lugar de bloquear, el programa pausa una tarea y continúa con otra, volviendo a la primera cuando esté lista.

### Ejemplo sincrónico vs asincrónico

**Sincrónico (bloqueante):**
```python
def fetch_data(url):
    response = requests.get(url)  # Espera aquí
    return response.json()

# Toma 2 segundos si cada llamada tarda 1 segundo
fetch_data("http://api1.com")
fetch_data("http://api2.com")
```

**Asincrónico (no bloqueante):**
```python
async def fetch_data(url):
    response = await aiohttp.get(url)  # Pausa aquí, pero no bloquea
    return await response.json()

# Toma 1 segundo si ambas llamadas se ejecutan concurrentemente
await asyncio.gather(
    fetch_data("http://api1.com"),
    fetch_data("http://api2.com")
)
```

### Cómo funcionan `async` y `await`

1. `async def`: declara una función asincrónica que devuelve una "corrutina".
2. `await`: pausa la corrutina actual y deja que otros trabajen.
3. **Event loop**: gestor de las corrutinas, que las ejecuta intercaladamente.

```python
import asyncio

async def tarea_a():
    print("A inicio")
    await asyncio.sleep(1)  # Pausa, no bloquea
    print("A fin")

async def tarea_b():
    print("B inicio")
    await asyncio.sleep(1)
    print("B fin")

async def main():
    # Ejecuta ambas concurrentemente
    await asyncio.gather(tarea_a(), tarea_b())

asyncio.run(main())
# Output:
# A inicio
# B inicio
# A fin
# B fin
```

### Cuándo usar async
- ✅ Operaciones I/O: red, archivos, bases de datos.
- ✅ Servidores web (ASGI).
- ✅ Procesamiento de muchas conexiones simultáneas.
- ❌ Operaciones CPU pesadas.
- ❌ Código que necesita comportarse como sincrónico.

### Relación con ASGI
ASGI se construye sobre async porque permite que un servidor maneje muchas solicitudes HTTP sin crear múltiples threads. Cada solicitud es una corrutina que se pausa cuando espera (I/O) y se reanuda cuando está lista.

```python
# En FastAPI (que usa ASGI)
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    # Esta función es async para aprovechar ASGI
    return {"message": "Hello"}
```

---

## 🔄 Procesamiento Post-Clase

### 📋 Checklist de Procesamiento
- [ ] Probar ejemplos sincrónico vs asincrónico.
- [ ] Entender el event loop.
- [ ] Practicar con bibliotecas async (`aiohttp`, `asyncpg`).
- [ ] Conectar con ASGI y FastAPI.

### 🎯 Acciones Prioritarias
1. Leer [[ASGI - Asynchronous Server Gateway Interface]].
2. Escribir un script async con `asyncio.gather()`.
3. Comparar rendimiento con múltiples I/O.

### 🔗 Conexiones
- [[ASGI - Asynchronous Server Gateway Interface]]
- [[uv y npm en virtual environment]]
- [[FastAPI vs FastMCP]]

---

## 🎴 Flashcards Rápidas
- **¿Qué es async?**
  - Una forma de escribir código concurrente que pausa sin bloquear el programa.
- **¿Cuál es la diferencia entre async y threading?**
  - Async usa concurrencia en un thread; threading usa múltiples threads.
- **¿Cuándo debo usar async?**
  - Para operaciones I/O en servidores web y cuando necesites manejar muchas conexiones simultáneamente.
