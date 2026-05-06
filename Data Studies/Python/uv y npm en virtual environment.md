---
tags: [clase, Python, uv, npm, virtualenv]
deck: Obsidian::Python
created: 2026-05-06 15:25
modified: 2026-05-06 15:25
status: 🟡
tipo_nota: clase
profesor: No especificado
---

# 📝 `uv`, `npm` y Virtual Environment

> [!info] Metadata de la clase
> **Fecha**: 2026-05-06
> **Hora**: 15:25
> **Profesor**: No especificado
> **Estado**: 🟡 Por procesar

---

## 🎯 Objetivo de la clase

Entender qué es `uv` en el contexto de Python, cómo se relaciona conceptualmente con `npm` en el ecosistema JavaScript y por qué el uso de entornos virtuales es clave en Python.

---

## 📊 Captura Rápida

### ⚡ Notas Rápidas
- `uv` suele referirse a un ejecutable ligero asociado a servidores ASGI como `uvicorn`.
- `npm` es el gestor de paquetes y scripts de JavaScript/Node.js.
- Un virtual environment en Python aísla dependencias por proyecto.
- Para usar `uv` correctamente, es recomendable instalarlo dentro de una venv.

### 🔑 Conceptos Clave
- `uv` = comando para iniciar un servidor ASGI en Python.
- `npm` = instala paquetes y ejecuta scripts definidos en `package.json`.
- `venv` = entorno virtual que evita conflictos de versiones entre proyectos.

### ❓ Dudas
- ¿El comando `uv` ya viene con Python? No, se instala en el entorno del proyecto.
- ¿Cómo se relaciona `uv` con `uvicorn`?
- ¿Qué pasa si corro `uv` sin activar la venv?

### 💡 Insights
- El paralelismo entre `uv` y `npm` está en el concepto de herramientas de ejecución ligadas a dependencias del proyecto.
- `uv` no es un gestor de paquetes; es un ejecutable que depende de paquetes instalados en el entorno.

### ⚠️ Importante
- Nunca usar paquetes globales para desarrollo Python en producción: siempre preferir una venv.
- `npm` puede instalar paquetes globales, pero también tiene la opción más segura de instalarlos por proyecto.

---

## 📝 Notas Detalladas

### ¿Qué es `uv` en Python?
En Python, `uv` está asociado a la familia de servidores ASGI como `uvicorn`. Se utiliza como comando para arrancar aplicaciones web asíncronas. Por ejemplo:

```bash
uv app:app --reload
```

Esto ejecuta la aplicación ASGI definida en el archivo `app.py`.

### ¿Por qué usar `uv` dentro de un virtual environment?
Un virtual environment (`venv`) aísla las librerías y ejecutables de un proyecto. Si instalas `uv` dentro de la venv, el comando se resuelve con la versión correcta y no hay riesgo de conflictos con otras aplicaciones.

Ejemplo de flujo:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install uvicorn
uv app:app --reload
```

### Relación con `npm`
`npm` es el gestor de paquetes y scripts para Node.js. En muchos proyectos JavaScript se usan comandos como:

```bash
npm install
npm run dev
```

La relación con Python es conceptual:
- `npm install` instala dependencias para el proyecto.
- `npm run dev` ejecuta un script definido en el proyecto.
- `venv` en Python cumple una función similar a `node_modules` y `package-lock.json`: mantener dependencias aisladas por proyecto.
- `uv` en Python es equivalente a ejecutar un servidor con un script específico, similar a `npm run dev`.

### Comparación directa
- `npm` gestiona paquetes y scripts en JavaScript.
- `uv` ejecuta un servidor Python ASGI.
- `venv` aísla dependencias de Python, tal como `node_modules` y `package-lock.json` aíslan dependencias en Node.js.

---

## 🔄 Procesamiento Post-Clase

### 📋 Checklist de Procesamiento
- [ ] Confirmar si `uv` se refiere a `uvicorn` en el proyecto actual.
- [ ] Verificar el comando `uv` disponible en la venv.
- [ ] Comparar con `npm run` en un ejemplo real.

### 🎯 Acciones Prioritarias
1. Probar la instalación de `uvicorn` en una venv.
2. Documentar el flujo `venv` + `uv` versus `npm install` + `npm run`.
3. Actualizar notas si hay un significado específico de `uv` en el proyecto.

### 🔗 Conexiones
- [[ASGI - Asynchronous Server Gateway Interface]]
- [[async - Programación asincrónica]]
- [[FastMCP - Ejemplo de implementación]]
- [[FastMCP vs FastAPI]]
- [[Python - Entornos Virtuales]]

---

## 🎴 Flashcards Rápidas
- **¿Qué es `uv` en Python?**
  - Un comando para arrancar servidores ASGI, típicamente `uvicorn`.
- **¿Por qué usar `venv` con `uv`?**
  - Para aislar dependencias y evitar conflictos entre proyectos.
- **¿Qué equivalente tiene `npm` en Python?**
  - `pip` y `venv` juntos, donde `pip` instala dependencias y `venv` las aísla.
