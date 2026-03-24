---
cards-deck: Nube::Monolítica-Microservicio
created: 2025-11-02
modified: 2026-01-22
status: 🌳 Maduro
tipo_nota: tecnica
asignatura: Infraestructura-Nube
nivel-comprension: ✅
proxima-revision: 2026-02-21
ultima-revision: 2026-01-22
tiempo-repaso: 5min
veces-revisado: 1
tiempo-estimado: 5m
---

# Arquitecturas Monolíticas

> [!abstract] Objetivo
> 

---

## 🎓 Contexto Académico

**Asignatura/Curso**: Infraestructura y Servicios en la Nube
**Relevancia para**: Examen
**Dificultad percibida**: ⭐⭐☆☆☆
---

## 📝 Definición

En este modelo, la interfaz del usuario, la lógica de negócio y la capa de datos están estrechamente acopladas, lo que significa que los cambios hechos en una parte influye en el resto.

---

## ⚙️ Conceptos Clave

### 📌 Unidad Coherente: Todo se ejecuta dentro de un solo proceso o contenedor

**Tipo**: Definición

**Características**:
- Unidad Coherente: Todos esta acoplado en un único proceso o contenedor que se ejecuta todo en un solo proceso
- Despliegue monoítico: Las mejoras se aplican de manera conjunta, cualquier actualización se ejecuta en el sistema por entero
- Comunicación directa: Todos los modulos se interactuán entre sí
- Escalabilidad Limitada: La medida que se aumenta la carga de trabajo es necesário aumentar toda la estructura, lo que es más costoso
- Complejidad y acoplamiento: A medida que la aplicación crece, la complejidad y el acoplamiento entre los diferentes modulos también aumenta
- Ejemplos: Wordpress, todo se procesa dentro de la misma aplicación

**Relacionado**: [[Nube]] • [[Arquitectura Monolítica]]

### 📌 Microservicios

**Tipo**: Definición

**Características**:
- Descomposició: Las aplicaciones se descomponen en servicios más pequeños y especializados
- Inependencia: Los equipos pueden trabajar de manera independiente en cada servicio
- Comunicación bajo API: Facilita la evolución de la aplicación a medida que se agregan o modifican servicios
- Escalabilidad Flexible: Los servicios individuales pueden escalarse de forma independiente según las necesidades de la aplicación

**Relacionado**: [[Nube]] • [[Microservicios]]

---

## 💻 Ejemplo Práctico

Facebook antiguamente
---

## 💭 Reflexiones & Conexiones

Mi aplicación de InnerLevel tiene una arquitectura híbrida entre monílitca y microservicios. Mi frontend y Backend están comunicados por una API, pero están comunicados como un bloque, ya la base de  datos está en un [[Modelos_Servicios#📌 Software como Servicio (SaaS)]] que es Supabase una aplicación que gestiona la base de datos que se comunica con API con las otras funciones de la aplicación

---

## 🎴 Flashcards

> 💡 **Formato**: Usa `Pregunta::Respuesta` para flashcards inline

¿Cuál es la diferencia fundamental entre un monolito y arquitecturas distribuidas en términos de acoplamiento?::En un monolito, todos los componentes (interfaz, lógica, datos) están acoplados en una sola unidad. Un cambio en una parte afecta potencialmente todo. En arquitecturas distribuidas, los componentes están desacoplados y se comunican a través de interfaces definidas. #Arquitectura #Monolítica, #Microservicios, #Nube #card
<!--SR:!2026-01-26,4,270-->

¿Por qué el despliegue es más simple pero más riesgoso en monolitos?::Es simple porque despliegas UNA sola unidad. Pero es riesgoso porque cualquier cambio pequeño requiere desplegar TODO. Si falla, cae toda la aplicación. No puedes actualizar "solo el módulo de cartas". #Arquitectura #monolítica, #microservicios, #nube #card
<!--SR:!2026-01-26,4,270-->

¿Por qué la escalabilidad horizontal es ineficiente en monolitos?::Para manejar más tráfico, debes replicar TODO el monolito (incluso las partes que no necesitan más recursos). Si solo "Cartas" tiene mucho tráfico, aún replicas toda la BD y lógica de Batallas. #card
<!--SR:!2026-01-26,4,270-->

¿En qué casos el monolito SÍ es la mejor opción?::Aplicaciones pequeñas/medianas (< 5 desarrolladores) Tiempo de market-to-launch crítico Equipo no tiene experiencia con sistemas distribuidos Tráfico predecible y manejable Cambios frecuentes en toda la aplicación #card
<!--SR:!2026-01-26,4,270-->

El monolito sacrifica == escalabilidad == para ganar == velocidad inicial == #card
<!--SR:!2026-01-26,4,270!2026-01-25,3,250--> 

---

**📊 Total de flashcards**: 5

> 🎯 **Para revisar**: Cmd/Ctrl+P → "Flashcards: Review flashcards"
---

## 📚 Referencias & Enlaces

**Enlaces internos**: 
**Referencias externas**: 
**Fuente**: 

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2025-11-02
- **Próxima revisión**: 2025-11-05
- **Veces revisado**: 0
- **Nivel de comprensión**: 💡
- **Tiempo estimado de repaso**: 5min
---

> [!tip] 💡 Próximos pasos
> _Cuando revises esta nota, actualiza el contador de revisiones y ajusta la próxima fecha según tu comprensión_
