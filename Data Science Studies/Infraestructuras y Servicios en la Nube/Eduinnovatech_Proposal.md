
# Memoria Técnica: Plataforma EduInnovatech

**Proyecto:** Sistema de Monitorización Educativa y Olimpiada Interescolar
**Arquitectura:** Cloud Native (PaaS & Serverless) en Microsoft Azure

---

## 1. Resumen Ejecutivo

El objetivo del proyecto es desplegar una plataforma SaaS educativa capaz de operar en dos modalidades distintas con la misma infraestructura:

1. **Modo Diario ("Jornada Escolar"):** Herramienta de monitorización de ejercicios en tiempo real para clases habituales (tráfico moderado y constante de 08:00 a 17:00).
2. **Modo Evento ("Olimpiada Interescolar"):** Capacidad para escalar instantáneamente y soportar la concurrencia masiva de múltiples colegios simultáneamente durante ventanas de 2 horas.

La solución se basa en una arquitectura **Serverless sobre Microsoft Azure**, priorizando la elasticidad de costes, la integración con el ecosistema escolar (Microsoft 365) y la privacidad del menor.

---

## 2. Arquitectura de la Solución

Para cumplir con el requisito de **"Monitorización en Tiempo Real"** sin saturar el servidor web, hemos desacoplado la gestión de conexiones mediante **Azure SignalR Service**. A continuación, se detalla la arquitectura lógica y de red.

### 2.1. Diagrama de Componentes (Mermaid)

```mermaid
graph TD
    %% --- Estilos ---
    classDef azure fill:#0078d4,stroke:#fff,stroke-width:2px,color:#fff;
    classDef external fill:#444,stroke:#fff,stroke-width:2px,color:#fff;
    classDef data fill:#5c2d91,stroke:#fff,stroke-width:2px,color:#fff;
    classDef realtime fill:#ffb900,stroke:#fff,stroke-width:2px,color:#333;

    %% --- Actores Externos ---
    Student(["👤 Alumno"]) :::external
    Teacher(["🎓 Profesor (Monitor)"]) :::external
    EntraID{"🔐 Microsoft Entra ID\n(Login Colegios)"} :::azure

    %% --- Azure Cloud Scope ---
    subgraph AzureRegion ["☁️ Microsoft Azure (West Europe)"]
        style AzureRegion fill:#f4f9fd,stroke:#0078d4,stroke-dasharray: 5 5

        %% Capa Web y API
        subgraph ComputeLayer ["⚡ Capa de Computación"]
            style ComputeLayer fill:#fff,stroke:#ddd
            AppService["📱 Azure App Service\n(Python Backend)"] :::azure
            SignalR(("📡 Azure SignalR\nWebSockets Gestionados")) :::realtime
        end

        %% Capa Privada de Datos (VNet)
        subgraph DataLayer ["🔒 VNet Privada (Datos)"]
            style DataLayer fill:#eefbfb,stroke:#008080,stroke-width:2px
            
            SQL[("🛢️ SQL Database\nServerless")] :::data
            Redis["🚀 Azure Redis Cache\n(Sesiones Rápidas)"] :::data
            OpenAI["🧠 Azure OpenAI\n(GPT-4o)"] :::data
            
            %% Private Endpoints
            PE_SQL((Private EP))
            PE_AI((Private EP))
        end
    end

    %% --- Flujos ---
    Student -- "1. Login SSO" --> EntraID
    EntraID -. "Token JWT" .-> AppService
    
    Student -- "2. HTTPS / Examen" --> AppService
    Student -- "3. WebSocket (Estado)" --> SignalR
    
    AppService -- "4. Push Updates" --> SignalR
    SignalR -- "5. Vista en Tiempo Real" --> Teacher
    
    AppService -- "6. Persistencia" --> PE_SQL --> SQL
    AppService -- "7. Cache Session" --> Redis
    AppService -- "8. Consultas IA" --> PE_AI --> OpenAI
```

### 2.2. Justificación de Componentes Nuevos

- **Azure SignalR Service:** Esencial para la funcionalidad de "Monitorización". Mantiene miles de conexiones persistentes (WebSockets) con los navegadores de los alumnos para detectar si están activos o escribiendo. Libera al servidor web (`App Service`) de gestionar estas conexiones, evitando cuellos de botella durante la Olimpiada.

- **Azure Redis Cache:** Almacena el estado volátil del examen (ej: "¿En qué pregunta está el alumno?"). Esto reduce la carga sobre la base de datos SQL en un 80%, permitiendo una experiencia de usuario ultra-rápida.

---

## 3. Justificación Estratégica: ¿Por qué Azure?

La elección de Azure no se basa únicamente en el precio, sino en su capacidad para adaptarse al **Ciclo de Vida Escolar**.

### 3.1. Adaptabilidad al Ritmo Escolar (FinOps)

A diferencia de una empresa que opera 24/7, los colegios tienen un horario marcado.

- **La Competencia (AWS/GCP):** Obligan a aprovisionar bases de datos para el "pico máximo" (la Olimpiada), pagando por esa capacidad incluso de noche o fines de semana.

- **La Solución Azure:** Gracias a **SQL Serverless**, la infraestructura "respira" con el colegio:
  - _Noches/Fines de Semana:_ La base de datos se pausa o reduce al mínimo (0.5 vCores). **Coste: ~0€**.
  - _Clases Diarias:_ Escala a capacidad media.
  - _Evento Interescolar:_ Escala automáticamente hasta 40 vCores.

**Impacto:** Convertimos un coste fijo ineficiente en un coste variable inteligente.

### 3.2. Integración Nativa (Reducción de Fricción)

Al tratarse de una **Olimpiada Interescolar**, el mayor reto no es técnico, sino logístico: gestionar las contraseñas de miles de alumnos de distintos centros.

- La mayoría de colegios utilizan **Microsoft 365 Education**.
- Utilizamos **Microsoft Entra ID** para permitir que los alumnos entren con su cuenta del colegio.
- **Beneficio:** Eliminamos el registro de usuarios. Seguridad "Zero Trust" desde el primer día.

---

## 4. Seguridad, Privacidad y Protección del Menor

El tratamiento de datos de menores exige un cumplimiento estricto del **RGPD**.

1. **Aislamiento de Red:** Como se observa en el diagrama, la Base de Datos y la IA no son accesibles desde internet. Utilizan **Private Endpoints**, lo que impide ataques externos directos.
2. **Privacidad en la IA:** Utilizamos **Azure OpenAI Service** bajo contrato empresarial, garantizando que los datos de los ejercicios y respuestas de los alumnos **NO se utilizan para entrenar** al modelo público de ChatGPT.
3. **Auditoría:** Todas las acciones de los profesores y administradores quedan registradas en _Azure Monitor_ para garantizar la trazabilidad.

---

## 5. Modelo de Costes (Estimación Mensual)

A pesar de añadir capacidades de tiempo real (SignalR) para el uso diario, Azure sigue siendo la opción más eficiente frente a la competencia aprovisionada.

| Componente | Configuración Azure | Coste Est. | Notas |
| :--- | :--- | :--- | :--- |
| **Base de Datos** | SQL Serverless (Auto-Pause) | **~45 €** | Se adapta al horario escolar (8h/día). |
| **Computación** | App Service (Linux B1) | **~12 €** | Servidor Web Backend. |
| **Tiempo Real** | **Azure SignalR (Free/Std)** | **~4 €** | 20 conexiones concurrentes gratis (dev) / escalado en evento. |
| **IA Generativa** | OpenAI (GPT-4o mini) | **~2 €** | Modelo eficiente para corrección automática. |
| **Almacenamiento** | Blob Storage & Redis | **~10 €** | Caché y copias de seguridad. |
| **TOTAL** | **Infraestructura Completa** | **~73 €** | **vs ~280€ en AWS/GCP** |

---

## 6. Conclusión

La plataforma **EduInnovatech** demuestra que es posible desplegar una arquitectura de nivel empresarial (Alta Disponibilidad, Tiempo Real e IA) con un presupuesto de centro educativo.

La combinación de **Azure SignalR** para la experiencia en tiempo real y **SQL Serverless** para la eficiencia de costes nos permite ofrecer un servicio premium durante la Olimpiada Interescolar sin hipotecar la viabilidad financiera del proyecto en el día a día.
