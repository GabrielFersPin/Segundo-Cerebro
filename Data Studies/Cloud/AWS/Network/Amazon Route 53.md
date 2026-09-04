---
created: 2026-09-03
modified: 2026-09-03
area: ""
tipo_nota: captura_rapida
status: 🌱
nivel-comprension: ""
proxima-revision: 2026-09-06
ultima-revision: 2026-09-03
veces-revisado: 0
tiempo-repaso: 5min
---

# Routing Policies

> [!info] Contexto captura
> **Fecha**: 2026-09-03 19:43
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> Maneras de conectar el usuario a un servidor


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->

Tu resumen trata sobre las **políticas de enrutamiento de Amazon Route 53**. Estas serían las definiciones corregidas:

| Política | Definición mejorada | Uso típico |
|---|---|---|
| **Simple** | Dirige el tráfico hacia un único recurso. Puede devolver uno o varios valores, pero no realiza balanceo avanzado ni selección basada en salud. | Un dominio que apunta a un servidor web o recurso sencillo. |
| **Weighted** | Distribuye el tráfico entre varios recursos según porcentajes configurados, por ejemplo, 90 % a una versión y 10 % a otra. | Pruebas A/B, despliegues graduales o migraciones. |
| **Geolocation** | Dirige a los usuarios según su ubicación geográfica, como continente, país o estado/provincia. Permite configurar una ubicación predeterminada para los usuarios que no coincidan. | Mostrar contenido regional o cumplir requisitos legales. |
| **Geoproximity** | Dirige el tráfico basándose en la proximidad geográfica entre los usuarios y los recursos. Permite modificar esa distribución mediante un valor de *bias* y requiere Route 53 Traffic Flow. | Desviar más tráfico hacia una región o centro de datos concreto. |
| **Latency-based** | Envía al usuario al recurso ubicado en la región de AWS que ofrece la menor latencia estimada, no necesariamente al servidor geográficamente más cercano. | Aplicaciones globales con réplicas en varias regiones. |
| **Failover** | Define un recurso principal y otro secundario. Si el principal deja de estar saludable, Route 53 dirige el tráfico al secundario mediante comprobaciones de estado. | Alta disponibilidad y recuperación ante fallos. |
| **Multivalue answer** | Devuelve varios registros saludables para un mismo nombre DNS. El cliente puede elegir uno de ellos; no sustituye completamente a un balanceador de carga. | Mejorar la disponibilidad de varios servidores o endpoints. |
| **IP-based** | Dirige el tráfico según la dirección IP de origen del usuario mediante rangos de IP previamente configurados. No es una política de control de acceso o firewall. | Enviar redes corporativas, operadores o rangos concretos a endpoints específicos. |

Una versión muy breve para memorizar:

> **Simple**: un recurso.  
> **Weighted**: porcentajes.  
> **Geolocation**: ubicación del usuario.  
> **Geoproximity**: proximidad ajustable.  
> **Latency**: menor latencia hacia AWS.  
> **Failover**: principal y respaldo.  
> **Multivalue**: varias respuestas saludables.  
> **IP-based**: rangos de IP.


---

## 🔑 Keywords / Conceptos clave

`keyword1`, `keyword2`, `keyword3`

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
| Capturado | 2026-09-03 19:43 |
| Área/Tema | `= this.area` |
| Estado | `= this.status` |
| Prioridad | `= this.prioridad` |
| Revisión | `= this.proxima-revision` |
| Nivel de comprensión | `= this.nivel-comprension` |

---

#pendiente-procesar #captura-rapida
