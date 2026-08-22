---
created: 2026-06-01
modified: 2026-08-20
area: ""
tipo_nota: ""
status: 🌿 Creciendo
nivel-comprension: 💡
proxima-revision: 2026-09-19
ultima-revision: 2026-08-20
veces-revisado: 1
tiempo-repaso: ""
cards-deck: Nube
tiempo-estimado: 20min
---

# Amazon S3

> [!abstract] Objetivo
> Definiciones y saber la diferencia entre los diferentes tipos

---

## 🎓 Contexto de Estudio

**Área/Tema**: Nube
**Relevancia para**: Certificación
**Dificultad percibida**: ⭐⭐☆☆☆
---

## 📝 Definición

Amazon S3 es un servicio de alamacenamiento que se puede acceder los datos frecuentemente

---

## ⚙️ Conceptos Clave

### 📌 Amazon S3

**Tipo**: Definición

**Características**:
- Servicio de almacenamiento con facil acceso a los datos

**Relacionado**: [[AWS]]

### 📌 S3 Standart-IA

**Tipo**: Definición

**Características**:
- Servicio para almacenar datos de manera menos frecuente, pero más rápido cuando necesario.
- Son clases que tienen un menor costo de almacenamiento

**Relacionado**: [[AWS]]

### 📌 S3 Intelligent-Tiering

**Tipo**: Definición

**Características**:
- Datos con un patrón de acceso desconocido o cambiable.
- automáticamente mueve los datos de menos acceso a zonas de acceso de bajo coste.

**Relacionado**: [[AWS]]

### 📌 S3 Glacier 

**Tipo**: Definición

**Características**:
-  Está hecho para los datos que son accedidos muy raramente

### 📌 S3 Glacier Deep Archive

- La opción más barata para datos que son accedidos muy raramente.

### 📌 S3 One Zone-IA

- Opción de menor coste para datos accedidos muy raramente en solo una AZ

---


## 💭 Reflexiones & Conexiones

 

---

## 🎴 Flashcards

¿Qué es Amazon S3?::Es un servicio de almacenamiento en la nube orientado a objetos, con acceso fácil y escalable a los datos. #aws #s3 #cloud

¿Qué caracteriza a S3 Standard-IA?::Es ideal para datos accedidos con menor frecuencia, pero que requieren acceso rápido cuando se necesitan. #aws #s3

¿Qué es S3 Intelligent-Tiering?::Es una clase que mueve automáticamente los datos entre niveles según su patrón de acceso para optimizar costes. #aws #s3

¿Cuándo conviene usar S3 Intelligent-Tiering?::Cuando el patrón de acceso de los datos es desconocido o cambia con el tiempo. #aws #s3

¿Qué es S3 Glacier?::Es una clase para datos archivados o accedidos muy raramente, con un coste menor y una recuperación más lenta. #aws #s3

¿Qué es S3 Glacier Deep Archive?::Es la opción más barata para datos que casi no se consultan y pueden tardar horas en recuperarse. #aws #s3

¿Qué es S3 One Zone-IA?::Es una opción más económica para datos poco accedidos, guardados en una sola zona de disponibilidad. #aws #s3

¿Cuál es la diferencia principal entre Standard-IA y Intelligent-Tiering?::Standard-IA requiere elegir la clase manualmente; Intelligent-Tiering la ajusta automáticamente según el acceso. #aws #s3

¿Qué tipo de almacenamiento es mejor para datos casi nunca accesados?::S3 Glacier Deep Archive. #aws #s3

¿Qué clase de S3 es la mejor opción para datos con acceso poco frecuente pero todavía requerido?::S3 Standard-IA. #aws #s3

¿Cuál es la ventaja principal del almacenamiento S3?::Facilita el acceso, la escalabilidad y la gestión de datos en la nube sin depender de infraestructura local. #aws #s3

> 💡 **Formato recomendado**:
> - Inline: `¿Pregunta?::Respuesta #tags`
> - Reversa: `Término:::Definición #tags`
> - Cloze: `Texto con ==palabra== oculta`
---

## 📚 Referencias & Enlaces

**Enlaces internos**: 
**Referencias externas**: 
**Fuente**: 

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2026-06-01
- **Próxima revisión**: 2026-06-04
- **Veces revisado**: 0
- **Nivel de comprensión**: 💡
- **Tiempo estimado de repaso**: 5min
---

> [!tip] 💡 Próximos pasos
> _Cuando revises esta nota, actualiza el contador de revisiones y ajusta la próxima fecha según tu comprensión_

---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Tarea para aclarar una duda de concepto. Usa #mejora-concepto
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia
