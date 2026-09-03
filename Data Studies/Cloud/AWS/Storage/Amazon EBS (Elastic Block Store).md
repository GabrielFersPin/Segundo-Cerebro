---
created: 2026-08-14
modified: 2026-08-14
area: ""
tipo_nota: ""
status: 🌱
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
estado: "pendiente"
---

# EBS (Elastic Block Store)

> [!info] Contexto captura
> **Fecha**: 2026-08-14 09:57
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> Volúmenes de almacenamiento persistente que se conectan a instancias


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->

- Los datos persisten independientemente del ciclo de vida de la instancia
- Puedes crear snapshots (backups) y restaurarlos cuando necesites
- Permiten redimensionamiento dinámico sin downtime
- Diferentes tipos: gp3 (SSD general), io2 (alto IOPS), st1 (throughput optimizado)


---

## 🔑 Keywords / Conceptos clave

`keyword1`, `keyword2`, `keyword3`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

¿Qué es Amazon EBS?::Es un servicio de almacenamiento por bloques persistente que se conecta a instancias de Amazon EC2. #aws #ebs #storage

¿Qué ocurre con los datos de EBS cuando se detiene o termina una instancia?::Los datos persisten independientemente del ciclo de vida de la instancia, según la configuración del volumen. #aws #ebs

¿Qué es un snapshot de EBS?::Es una copia de respaldo de un volumen EBS que puede almacenarse y utilizarse para restaurar o crear nuevos volúmenes. #aws #ebs #backup

¿Qué ventaja ofrece el redimensionamiento de un volumen EBS?::Permite aumentar su capacidad o ajustar su rendimiento sin necesidad de detener la instancia, evitando downtime en muchos casos. #aws #ebs

¿Cuándo usarías un volumen gp3?::Cuando necesitas almacenamiento SSD de propósito general para cargas comunes, como el disco de una aplicación o una base de datos moderada. #aws #ebs

¿Cuándo usarías un volumen io2?::Cuando necesitas alto rendimiento y muchos IOPS, por ejemplo para una base de datos crítica con muchas operaciones de entrada y salida. #aws #ebs

¿Cuándo usarías un volumen st1?::Cuando la carga necesita alto throughput para procesar grandes volúmenes de datos secuenciales, como logs o procesamiento de big data. #aws #ebs

¿Qué diferencia principal hay entre EBS y un almacenamiento de objetos como S3?::EBS proporciona almacenamiento por bloques para una instancia, mientras S3 almacena objetos y se accede mediante APIs. #aws #ebs #s3

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
- [x] Crear flashcards si es necesario
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
| Capturado | 2026-08-14 09:57 |
| Área/Tema | `= this.area` |
| Prioridad | `= this.prioridad` |
| Estado | Captura rápida → Pendiente procesamiento |
| Revisión | `= this.proxima-revision` |

---

#pendiente-procesar #captura-rapida
