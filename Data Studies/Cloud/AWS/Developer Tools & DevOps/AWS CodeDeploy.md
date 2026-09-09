---
created: 2026-09-07
modified: 2026-09-07
area: Cloud
tipo_nota: captura_rapida
status: 🌱
nivel-comprension: ""
proxima-revision: 2026-09-09
ultima-revision: 2026-09-07
veces-revisado: 0
tiempo-repaso: 5min
cards-deck: Nube::DevOps
---

# AWS CodeDeploy

> [!info] Contexto captura
> **Fecha**: 2026-09-07
> **Origen**: AWS / Developer Tools & DevOps
> **Tipo**: Servicio de despliegue automatizado

---

## 📝 Captura principal

> [!tip] Lo más importante
> AWS CodeDeploy automatiza el despliegue de aplicaciones en servicios de cómputo como EC2, Lambda y ECS, reduciendo el trabajo manual y el riesgo de errores.

### 🎯 Detalles / Contenido

CodeDeploy puede automatizar:

- despliegues de aplicaciones en instancias EC2;
- actualizaciones de funciones Lambda;
- despliegues en servicios ECS;
- estrategias como in-place, blue/green y canary, según el destino;
- integración con CodePipeline para completar un flujo CI/CD.

Un flujo habitual es:

> CodeCommit/GitHub → CodeBuild → CodeDeploy → EC2, Lambda o ECS

En despliegues sobre EC2, la aplicación y sus instrucciones de instalación se describen normalmente mediante `appspec.yml`.

---

## 🔑 Keywords / Conceptos clave

`AWS`, `CodeDeploy`, `CI/CD`, `despliegue`, `blue-green`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

¿Qué es AWS CodeDeploy?::Es un servicio administrado que automatiza el despliegue de aplicaciones en EC2, Lambda y ECS. #aws #codedeploy #devops

¿Qué problema resuelve CodeDeploy?::Reduce los pasos manuales y los errores al publicar nuevas versiones de una aplicación. #aws #codedeploy #cicd

¿Qué relación hay entre CodeBuild y CodeDeploy?::CodeBuild compila y prueba el código; CodeDeploy utiliza el artefacto resultante para desplegarlo en el entorno destino. #aws #codebuild #codedeploy

¿Qué es un despliegue blue/green?::Es una estrategia que mantiene un entorno activo y prepara otro con la nueva versión para cambiar el tráfico de forma controlada. #aws #codedeploy #deployment

¿Para qué sirve `appspec.yml` en CodeDeploy?::Para describir instrucciones y hooks del despliegue, especialmente cuando se despliega una aplicación en instancias EC2. #aws #codedeploy

---

## ❓ Preguntas / Dudas pendientes

- [ ] ¿Cuándo conviene blue/green frente a un despliegue in-place?

---

## 🧩 Conexiones potenciales

- [[AWS CodeCommit]]
- [[AWS CodePipeline]]
- [[AWS CodeBuild]]
- [[Amazon EC2 (Elastic Compute Cloud)]]
- [[AWS Lambda]]

---

## ✅ Checklist procesamiento

- [x] Revisar y expandir contenido
- [x] Crear flashcards si es necesario
- [ ] Hacer ejercicios relacionados
- [x] Conectar con otras notas ([[]])
- [ ] Actualizar nivel de comprensión
- [ ] Mover a vault definitivo / Cambiar status a 🌿

---

## 💭 Notas adicionales / Ideas rápidas

CodeDeploy representa la fase de publicación de una versión ya construida y validada.

---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-09-07 |
| Área/Tema | Cloud |
| Estado | 🌱 |
| Revisión | 2026-09-09 |
| Nivel de comprensión |  |

---

#pendiente-procesar #captura-rapida
