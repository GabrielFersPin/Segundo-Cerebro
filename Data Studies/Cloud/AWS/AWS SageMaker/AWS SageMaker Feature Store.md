---
created: 2026-08-22
modified: 2026-08-22
area: ""
tipo_nota: captura_rapida
status: 🌱
nivel-comprension: ""
proxima-revision: 2026-08-25
ultima-revision: 2026-08-22
veces-revisado: 0
tiempo-repaso: 5min
---

# AWS Sagemaker Feature Store

> [!info] Contexto captura
> **Fecha**: 2026-08-22 18:42
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> Amazon SageMaker Feature Store es un servicio para almacenar, organizar y reutilizar _features_ —variables preparadas para modelos de machine learning— de forma centralizada.


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->

Por ejemplo, para un modelo de detección de fraude podrías guardar:

```
user_id = 12345
total_compras_24h = 8
importe_medio = 73.50
ultima_compra_minutos = 15

```

Tiene dos almacenes principales:

- Online Store: devuelve features rápidamente para predicciones en tiempo real.
- Offline Store: guarda datos históricos para entrenar modelos y analizar información.

Flujo típico:


```text

Datos originales
      ↓
Procesamiento y creación de features
      ↓
SageMaker Feature Store
      ├── Online Store → predicciones en tiempo real
      └── Offline Store → entrenamiento y análisis

```

Ventajas principales:

- Evita duplicar el código de preparación de datos.
- Permite reutilizar las mismas features entre distintos modelos.
- Mantiene consistencia entre entrenamiento y producción.
- Guarda versiones e historial de features.
- Facilita compartir features entre equipos.
- Puede controlar quién puede leer o modificar los datos.

Un ejemplo conceptual usando Python sería:

```python

import boto3
client = boto3.client("sagemaker-featurestore-runtime")
respuesta = client.get_record(    FeatureGroupName="usuarios-features",    RecordIdentifierValueAsString="12345")
print(respuesta["Record"])

```

Esto recupera las features del usuario `12345` desde el Online Store.

Es especialmente útil cuando tienes modelos en producción que necesitan consultar características actualizadas con poca latencia.


---

## 🔑 Keywords / Conceptos clave

`AWS`, `SageMaker`, `Feature Store`

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




---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-08-22 18:42 |
| Área/Tema | `= this.area` |
| Estado | `= this.status` |
| Prioridad | `= this.prioridad` |
| Revisión | `= this.proxima-revision` |
| Nivel de comprensión | `= this.nivel-comprension` |

---

#pendiente-procesar #captura-rapida
