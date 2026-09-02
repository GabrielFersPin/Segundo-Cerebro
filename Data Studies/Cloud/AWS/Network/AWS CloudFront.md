---
created: 2026-08-14
modified: 2026-09-01
area: ""
tipo_nota: ""
status: 🌿 Creciendo
nivel-comprension: 💡
proxima-revision: 2026-10-01
ultima-revision: 2026-09-01
veces-revisado: 1
tiempo-repaso: ""
estado: pendiente
tiempo-estimado: 10min
---

# AWS Cloudfront

> [!info] Contexto captura
> **Fecha**: 2026-08-14 13:15
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> CloudFront is a CDN (Content Delivery Network) like an “in-between” layer that sits between your website/origin server and visitors. It has edge locations around the world, so when someone requests content, CloudFront can serve it from the nearest edge site (or fetch it from your origin only if it’s not cached yet). That makes delivery faster and reduces the load on your origin server


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->




---

## 🔑 Keywords / Conceptos clave

`AWS`, `CDN`, `CloudFront`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

¿Qué es Amazon CloudFront?::Es una CDN de AWS que entrega contenido desde edge locations cercanas al usuario para reducir latencia y mejorar rendimiento. #aws #cloudfront #cdn

¿Por qué CloudFront mejora la velocidad de una web?::Porque cachea contenido en edge locations cercanas al usuario y evita servir todo desde la origin cada vez. #aws #cloudfront

¿Qué significa que CloudFront use edge locations?::Que hay servidores distribuidos geográficamente para atender peticiones desde la zona más cercana al usuario. #aws #cloudfront

¿Cuándo conviene usar CloudFront?::Cuando tienes contenido estático o dinámico que se entrega a muchos usuarios globalmente, como sitios web, videos o APIs públicas. #aws #cloudfront

¿Qué ventaja tiene respecto a servir contenido directamente desde el origen?::Reduce la carga del backend y mejora la experiencia del usuario al disminuir la latencia. #aws #cloudfront

¿Qué tipo de contenido suele entregarse con CloudFront?::HTML, CSS, JS, imágenes, archivos estáticos, video y contenido protegido o caché. #aws #cloudfront

¿Cuál es el papel del caché en CloudFront?::Guardar copias del contenido para responder peticiones futuras más rápido sin volver al origen. #aws #cloudfront

¿Para qué serviría CloudFront en un escenario real?::Un sitio de e-commerce con clientes en Europa, América y Asia puede servir imágenes y páginas desde el edge más cercano. #aws #cloudfront

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

- [[Cloud Computing]]
-

---

## ✅ Checklist procesamiento

- [ ] Revisar y expandir contenido
- [x] Crear flashcards si es necesario ✅ 2026-09-01
- [ ] Hacer ejercicios relacionados
- [x] Conectar con otras notas ([[]]) ✅ 2026-08-14
- [ ] Actualizar nivel de comprensión
- [ ] Mover a vault definitivo / Cambiar status a 🌿

---

## 💭 Notas adicionales / Ideas rápidas

<!-- Zona libre para cualquier cosa que quieras capturar rápido -->

Es un intermedio entre la backend y el frontend en que puede enviar información mucho más rápido por tener servidores en muchas partes del mundo y conectar directamente con la región del usuario.


---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-08-14 13:15 |
| Área/Tema | `= this.area` |
| Prioridad | `= this.prioridad` |
| Estado | Captura rápida → Pendiente procesamiento |
| Revisión | `= this.proxima-revision` |

---

#pendiente-procesar #captura-rapida


---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Tarea para aclarar una duda de concepto. Usa #mejora-concepto
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia
