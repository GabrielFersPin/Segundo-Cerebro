---
created: 2026-09-07
modified: 2026-09-07
area: Machine Learning
tipo_nota: captura_rapida
status: 🌱
nivel-comprension: 🤔 Entiendo parcialmente
proxima-revision: 2026-09-09
ultima-revision: 2026-09-07
veces-revisado: 0
tiempo-repaso: 5min
---

# Amazon SageMaker Model Registry

> [!info] Contexto captura
> **Fecha**: 2026-09-07 11:34
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> Amazon SageMaker Model Registry es un repositorio para registrar, versionar y gestionar modelos de machine learning.


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->
Permite:

- Guardar distintas versiones de un modelo.
- Asociar metadatos, métricas, parámetros y artefactos.
- Gestionar estados como `Pending`, `Approved` o `Rejected`.
- Controlar qué modelos están autorizados para desplegarse.
- Mantener un historial de cambios.
- Integrarse con pipelines de entrenamiento, validación y despliegue.
- Facilitar procesos de CI/CD para machine learning.

Un flujo típico sería:

> Entrenar modelo → evaluar métricas → registrar versión → aprobar modelo → desplegar en SageMaker Endpoint

Importante:

- Training Jobs: entrenan el modelo.
- Model Registry: guarda y controla sus versiones.
- Endpoints: sirven el modelo para realizar predicciones.
- SageMaker Pipelines: automatizan el flujo completo.



---

## 🔑 Keywords / Conceptos clave

`AWS`, `SageMaker`, `Machine Learning`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

_Flashcards pendientes de crear_

> 💡 **Formato recomendado**:
> - Inline: `¿Pregunta?::Respuesta #tags`
> - Reversa: `Término:::Definición #tags`
> - Cloze: `Texto con ==palabra== oculta`
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

SageMaker Model Registry funciona como un control de versiones y catálogo de modelos de machine learning listos para ser evaluados o desplegados.


---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-09-07 11:34 |
| Área/Tema | `= this.area` |
| Estado | `= this.status` |
| Prioridad | `= this.prioridad` |
| Revisión | `= this.proxima-revision` |
| Nivel de comprensión | `= this.nivel-comprension` |

---

#pendiente-procesar #captura-rapida
