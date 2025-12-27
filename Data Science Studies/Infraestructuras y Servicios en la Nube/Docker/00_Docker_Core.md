---
tipo_nota: tecnica
asignatura: Infraestructura-Nube
nivel-comprension: 🤔
proxima-revision: 2025-11-27
ultima-revision: 2025-11-20
tiempo-repaso: 5min
status: 🌿 Creciendo
veces-revisado: 0
created: 2025-11-20
modified: 2025-11-20
---
# 🐳 DOCKER

**Plataforma de Contenedores**

## ¿Qué es?
- Plataforma para desarrollar, enviar y ejecutar aplicaciones en contenedores
- Aísla aplicaciones del sistema host
- "Funciona en mi máquina" → "Funciona en todas las máquinas"
- Ligero comparado con VMs (comparte kernel del OS)

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

---

**Relacionado**: 
- [[Kubernetes vs Docker Compose]]
- [[Contenedores vs VMs]]
- [[Docker para Data Science]]
