---
area: Infraestructura-Nube
cards-deck: Nube::Docker
created: 2025-11-20
modified: 2026-08-20
nivel-comprension: 💡
dias-para-revision: 25
status: 🌿 Creciendo
tiempo-repaso: 5min
tipo_nota: tecnica
ultima-revision: 2026-08-20
veces-revisado: 3
tiempo-estimado: 20min
proxima-revision: 2026-09-19
---
# 🐳 DOCKER

**Plataforma de Contenedores**

## ¿Qué es?
- Plataforma para desarrollar, enviar y ejecutar aplicaciones en contenedores
- Aísla aplicaciones del sistema host
- "Funciona en mi máquina" → "Funciona en todas las máquinas"
- Ligero comparado con VMs (comparte kernel del OS)
- ![[Pasted image 20260814100325.png]]

## Conceptos Core
- **Imagen**: Plantilla inmutable (como una clase)
- **Contenedor**: Instancia ejecutable de una imagen (como un objeto)
- **Dockerfile**: Receta para crear una imagen
- **Docker Hub**: Registro público de imágenes
- **Volume**: Almacenamiento persistente
- **Network**: Comunicación entre contenedores

## Filosofía
- Un proceso por contenedor
- Inmutabilidad (reconstruir, no parchear)
- Contenedores son efímeros
- Configuration as Code (Dockerfile)

## Diferencia con VMs
```
VM: Hardware → Hypervisor → [SO + App] + [SO + App]
Docker: Hardware → OS → Docker Engine → [App] + [App]
```

**Ventaja**: Más ligero, arranca en segundos



**Relacionado**: 
- [[Kubernetes vs Docker Compose]]
- [[Contenedores vs VMs]]
- [[Docker para Data Science]]

## 🎴 Flashcards

¿Qué es Docker?::Es una plataforma para desarrollar, enviar y ejecutar aplicaciones en contenedores, aislando la app del sistema host.

¿Qué es una imagen en Docker?::Es una plantilla inmutable que define cómo debe ejecutarse una aplicación.

¿Qué es un contenedor?::Es la instancia ejecutable de una imagen; es como un objeto creado a partir de una clase.

¿Qué es un Dockerfile?::Es la receta que define cómo crear una imagen Docker.

¿Qué es Docker Hub?::Es el registro público donde se almacenan y comparten imágenes de contenedores.

¿Qué es un volume en Docker?::Es un almacenamiento persistente para datos que deben sobrevivir a la vida del contenedor.

¿Qué es una red en Docker?::Es la capa que permite la comunicación entre contenedores y entre estos y el exterior.

¿Cuál es la diferencia principal entre un contenedor y una VM?::Los contenedores comparten el kernel del sistema operativo y son más ligeros; las VMs virtualizan hardware y requieren un SO completo.

¿Qué significa “un proceso por contenedor”?::Cada contenedor debe ejecutar normalmente un único proceso principal, manteniendo aislamiento y simplicidad.

¿Qué es la inmutabilidad en Docker?::Las imágenes no se modifican y, si cambias algo, se reconstruyen; no se parchean en producción.

¿Qué quiere decir “Configuration as Code” en Docker?::La configuración de la aplicación se define en un Dockerfile, lo que hace la ejecución reproducible.

¿Por qué Docker es más ligero que una VM?::Porque comparte el kernel del host y no necesita virtualizar hardware ni un SO completo para cada instancia.

¿Qué ventaja principal tiene Docker sobre un entorno tradicional?::Permite que la app “funcione igual en todas las máquinas” y arranca mucho más rápido.


---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Tarea para aclarar una duda de concepto. Usa #mejora-concepto
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia
