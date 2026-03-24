---
cards-deck: Nube::Modelos-Servicios
tipo_nota: tecnica
asignatura: Infraestructura-Nube
nivel-comprension: ✅
proxima-revision: 2026-02-21
ultima-revision: 2026-01-22
tiempo-repaso: 5min
status: 🌳 Maduro
veces-revisado: 1
created: 2025-11-20
modified: 2026-01-22
tiempo-estimado: 10min
---

# Modelos de Servicios en la Nube

> [!abstract] Objetivo
> Comprender los tres modelos principales de servicios en la nube y sus diferencias

---

## 🎓 Contexto Académico

**Asignatura/Curso**: Infraestructura y Servicios en la Nube
**Relevancia para**: Examen
**Dificultad percibida**: ⭐⭐☆☆☆

---

## 📝 Definición

Existen diferentes tipos de servicios en la nube, vamos a ver los tres principales.

---

## ⚙️ Conceptos Clave

### 📌 Software como Servicio (SaaS)

**Tipo**: Servicio

**Características**:
- Son accesibles desde cualquier dispositivo móvil
- Los datos y la lógica de la aplicación residen en los servidores del proveedor de la nube
- Algunos ejemplos son Google Workspace, Salesforce y Microsoft Teams
- Proporciona una experiencia de usuario conveniente
- Para los proveedores de software es una manera sencilla y rentable de actualizar aplicaciones a una gran cantidad de usuarios

**Relacionado**: [[Nube]] • [[SaaS]]

### 📌 Plataforma como Servicio (PaaS)

**Tipo**: Servicio

**Características**:
- Las plataformas PaaS ofrecen herramientas y servicios que permiten a los desarrolladores crear, probar y desplegar aplicaciones de manera eficiente
- Ejemplos de plataformas: Microsoft Azure App Service, Google App Engine y Heroku
- Los desarrolladores utilizan plataformas PaaS para crear aplicaciones personalizadas sin preocuparse por la infraestructura subyacente
- Las plataformas PaaS permiten colaboración entre miembros del equipo de desarrollo
- El modelo PaaS es muy bueno para organizaciones que buscan una forma rápida y eficiente de desarrollar y desplegar aplicaciones

**Relacionado**: [[PaaS]] • [[Nube]]

### 📌 Infraestructura como Servicio (IaaS)

**Tipo**: Servicio

**Características**:
- IaaS permite a los usuarios acceder a recursos informáticos bajo demanda
- Los usuarios tienen control total sobre la configuración y el uso de los recursos
- Los proveedores de IaaS ofrecen una variedad de opciones de máquinas virtuales, almacenamiento y redes para adaptarse a diferentes cargas de trabajo
- Las organizaciones utilizan IaaS para alojar aplicaciones, sitios web y bases de datos
- IaaS es especialmente útil para situaciones en las que se requiere una escalabilidad rápida y eficiente

**Relacionado**: [[IaaS]] • [[Nube]]

---

## 💻 Ejemplo Práctico

### Comparación con Analogía de Pizza

**IaaS (Horno e ingredientes)**: Tienes control total pero debes hacer todo
- Ejemplo: Alquilar un servidor EC2 en AWS y configurar todo manualmente

**PaaS (Masa preparada y horno listo)**: Solo te preocupas de la aplicación
- Ejemplo: Desplegar tu app en Heroku con `git push heroku main`

**SaaS (Pizza a domicilio)**: Solo usas el servicio final
- Ejemplo: Usar Gmail, Notion, Netflix sin preocuparte de nada técnico

---

## 💭 Reflexiones & Conexiones

Son servicios en la nube donde cada uno tiene sus ventajas y desventajas. De los más complejos como IaaS (totalmente configurable), pasando por PaaS (con menos complejidad) hasta SaaS (los más fáciles de usar).

En mi proyecto de coworkings y la app de gamificación, uso diferentes modelos:
- **SaaS**: Notion para documentación, GitHub para código
- **PaaS**: Podría usar Railway o Vercel para desplegar la app React
- **IaaS**: Si necesito entrenar modelos ML grandes, usaría EC2 con GPUs

---

## 🎴 Flashcards

¿Cuáles son los tres modelos de servicio en la nube?::IaaS (Infrastructure as a Service), PaaS (Platform as a Service) y SaaS (Software as a Service) #cloud #modelos #card
<!--SR:!2026-01-26,4,270-->

IaaS (Infrastructure as a Service):::Alquilas infraestructura virtualizada (servidores, almacenamiento, redes). Tú gestionas el SO y aplicaciones. Ejemplo: Amazon EC2, Google Compute Engine #cloud #iaas #card
<!--SR:!2026-01-26,4,270!2026-01-26,4,270-->

PaaS (Platform as a Service):::Entorno completo para desarrollar y desplegar aplicaciones sin gestionar servidores. Solo subes tu código. Ejemplo: Heroku, Google App Engine #cloud #paas #card
<!--SR:!2026-01-25,3,250!2026-01-26,4,270-->

SaaS (Software as a Service):::Aplicaciones completas listas para usar vía web. No gestionas nada de infraestructura. Ejemplo: Gmail, Notion, Spotify #cloud #saas
<!--SR:!2026-01-26,4,270!2026-01-26,4,270-->
#card 
Analogía de la pizza para servicios en la nube::IaaS = tienes horno e ingredientes, PaaS = masa preparada y horno listo, SaaS = pizza a domicilio #cloud #analogia #card
<!--SR:!2026-01-26,4,270-->

¿Qué modelo de servicio en la nube ofrece más control pero requiere más gestión técnica?::IaaS - tienes control total pero debes gestionar SO, seguridad, actualizaciones, etc. #cloud #iaas #card
<!--SR:!2026-01-26,4,270-->

¿Qué modelo de servicio usarías para desplegar una app web sin preocuparte de configurar servidores?::PaaS (ejemplo: Heroku) - subes el código con git push y automáticamente se despliega #cloud #paas #card
<!--SR:!2026-01-26,4,270-->

Responsabilidades en cloud::En IaaS gestionas desde el SO hacia arriba. En PaaS solo gestionas aplicación y datos. En SaaS no gestionas nada #cloud #responsabilidades #card
<!--SR:!2026-01-25,3,250-->

¿Cómo clasificas estos servicios? - Amazon EC2, Gmail, Heroku, Netflix, Google Compute Engine, Railway::IaaS: EC2, Google Compute Engine | PaaS: Heroku, Railway | SaaS: Gmail, Netflix #cloud #clasificacion #card
<!--SR:!2026-01-26,4,270-->

¿Para Data Science, cuándo usarías IaaS vs SaaS?::IaaS (EC2 con GPU) para entrenar modelos personalizados con control total. SaaS (Google Colab) para análisis rápidos sin configuración #cloud #datascience #card
<!--SR:!2026-01-26,4,270-->

---

**📊 Total de flashcards**: 10

> 🎯 **Para revisar**: Cmd/Ctrl+P → "Flashcards: Review flashcards"

---

## 📚 Referencias & Enlaces

**Enlaces internos**: [[Nube]], [[Computación en la Nube]], [[AWS]], [[Azure]]
**Referencias externas**: [AWS Service Models](https://aws.amazon.com/types-of-cloud-computing/)
**Fuente**: Apuntes de clase - Infraestructura y Servicios en la Nube

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2025-11-01
- **Próxima revisión**: 2025-11-04
- **Veces revisado**: 0
- **Nivel de comprensión**: 💡 Entiendo bien
- **Tiempo estimado de repaso**: 15min
