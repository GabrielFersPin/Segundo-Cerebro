---
tags: [clase, 2026-01-29]
deck: Obsidian::Infraestructuras y Servicios en la Nube
created: 2026-01-29 19:25
modified: 2026-01-29 19:25
status: 🟢
tipo_nota: clase
profesor: "No especificado"
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
cards-deck: ""
---

# 📝 Infraestructuras y Servicios en la Nube - DevOps y Jenkins

> [!info] Metadata de la clase
> **Fecha**: 2026-01-29
> **Hora**: 19:25
> **Profesor**: No especificado
> **Estado**: 🟢 Procesada

---

## 🎯 Objetivo de la clase

Comprender la herramienta Jenkins para la automatización en entornos DevOps, su arquitectura cliente-servidor, el concepto de Pipelines, y el ciclo de vida de las aplicaciones (ALM).

---

## 📊 Captura Rápida

> 💡 **Modo captura rápida**: Contenido extraído de las diapositivas.

### ⚡ Notas Rápidas
<!-- Escribe aquí cualquier cosa que necesites capturar rápidamente -->
- Jenkins es una herramienta de automatización escrita en Java, multiplataforma.
- Arquitectura Cliente-Servidor: Controlador (Server) y Agentes (Nodos).
- Concepto de "Trabajos" (Jobs): Build, Test, Deploy, Notification.

### 🔑 Conceptos Clave
<!-- Marca con ** los conceptos importantes -->
- **Jenkins**: Servidor de automatización open source.
- **Pipeline**: Flujos de trabajo complejos orquestados lógicamente.
- **ALM (Application Lifecycle Management)**: Gestión del ciclo de vida de aplicaciones.
- **CI/CD**: Integración Continua / Despliegue Continuo.

### ❓ Dudas
<!-- Preguntas que surjan durante la clase -->
- [ ]

### 💡 Insights
<!-- Conexiones o ideas que se te ocurran -->
- Jenkins permite paralelizar trabajos para mayor eficiencia.

### ⚠️ Importante
<!-- Información crítica para exámenes o proyectos -->
- Las etapas del ALM: Concepción, Planificación, Diseño, Desarrollo, Pruebas, Despliegue, Operación/Mantenimiento, Retirada.

### 📚 Referencias Mencionadas
<!-- Papers, libros, recursos -->
- [Jenkins IO](https://www.jenkins.io/)
- [Sentrio Blog - Qué es Jenkins](https://sentrio.io/blog/que-es-jenkins/)
- [AWS Jenkins Automation](https://www.aws.ps/how-to-implement-jenkins-automation-on-aws/)

---

## 📝 Notas Detalladas

<!-- Desarrolla aquí los conceptos con más detalle cuando tengas tiempo -->

### 📐 Jenkins: Herramienta de automatización

**Arquitectura Cliente-Servidor:**
- **Servidor (Controlador):** Coordina y supervisa actividades. Aloja la UI.
- **Agentes (Nodos):** Máquinas remotas que ejecutan los trabajos. Permiten asignar trabajos según SO (ej: Linux para compilar, Windows para probar).
- **Trabajos (Jobs):** Unidades de tarea.
  - *Build jobs*: Compilan código.
  - *Test jobs*: Pruebas automatizadas (unitarias, integración).
  - *Deploy jobs*: Automatizan implementación.
  - *Notification jobs*: Notifican estado (email, SMS).

**Pipelines:**
Permiten definir flujos de trabajo complejos. Se pueden definir vía web o mediante `Jenkinsfile`.

**Registros:**
Jenkins ofrece registros detallados de acciones y errores para facilitar la corrección.

### 🔄 Cycle de Vida de Aplicaciones (ALM)

Etapas:

1. **Concepción**: Identificar necesidad y viabilidad.
2. **Planificación**: Cronograma, recursos, objetivos.
3. **Diseño**: Tecnología, interfaz, datos, escalabilidad.
4. **Desarrollo**: Codificación.
5. **Pruebas**: Unitarias, Integración, Regresión, Rendimiento, Seguridad. (Automatización aporta eficiencia y consistencia).
6. **Despliegue**: Implementación en producción.
7. **Operación y mantenimiento**: Monitoreo y actualizaciones.
8. **Retirada**: Obsolescencia.

### 📊 Beneficios, Desafíos y Mejores Prácticas en DevOps

**Beneficios:**
- Eficiencia y velocidad (CI/CD).
- Calidad mejorada (menos fallas).
- Colaboración interdisciplinar.
- Escalabilidad y satisfacción del cliente.

**Desafíos:**
- Cambio cultural.
- Complejidad técnica.
- Gestión del cambio.

**Mejores Prácticas:**
- Participación activa de partes interesadas.
- Pruebas automatizadas.
- Integración y Despliegue continuo.
- Soporte de producción.
- Monitorización de aplicaciones.

---

## 🔄 Procesamiento Post-Clase

### 📋 Checklist de Procesamiento

- [ ] Revisar y organizar notas rápidas
- [ ] Clarificar conceptos confusos
- [ ] Resolver dudas pendientes
- [ ] Crear notas atómicas de conceptos clave
- [ ] Generar flashcards de lo importante
- [ ] Conectar con conocimiento previo
- [ ] Identificar gaps de conocimiento
- [ ] Planificar repaso con Active Recall

### 🎯 Acciones Prioritarias
<!-- Identifica 3 acciones clave después de clase -->
1. Repasar los tipos de Jobs en Jenkins.
2. Investigar cómo crear un Pipeline básico en Jenkinsfile.
3. Memorizar las etapas del ALM.

### 🔗 Conexiones con otras notas
<!-- Enlaces a notas relacionadas -->
- Conceptos previos: Introducción a Cloud Computing
- Temas relacionados: Docker, Kubernetes
- Aplicaciones: Automatización de deploys

---

## 🎴 Flashcards Rápidas

_[Flashcards pendientes - Crear después del procesamiento]*

---

## 📊 Resumen y Takeaways

### 🎯 Los 3 puntos clave

1. Jenkins es fundamental para CI/CD con arquitectura Master-Slave.
2. Las Pipelines orquestan el flujo de desarrollo, pruebas y despliegue.
3. DevOps requiere un cambio cultural además de herramientas técnicas.

### 💭 Reflexión personal

_¿Qué es lo más importante/útil/interesante de esta clase?*
La automatización de pruebas y despliegue parece ser el cuello de botella que Jenkins resuelve eficazmente.

### 🔮 Aplicaciones futuras

_¿Dónde y cómo puedo aplicar este conocimiento?*
En cualquier proyecto de software moderno para asegurar entregas rápidas y fiables.

---

## 📈 Métricas de Estudio

- **Comprensión inicial**: 👍 Entendí bastante
- **Importancia para el curso**: ⭐⭐⭐⭐ Muy importante
- **Dificultad percibida**: 🟡 Medio
- **Tiempo estimado de estudio**: 2h
- **Próxima revisión**: 2026-01-31

---

## 🏷️ Tags Semánticos

# devops #jenkins #alm #cicd #automatizacion
