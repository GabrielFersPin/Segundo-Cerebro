---
created: 2026-08-17
modified: 2026-08-17
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

# Amazon VPC (Virtual Private Cloud) 

> [!info] Contexto captura
> **Fecha**: 2026-08-17 13:28
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
>  Es una red virtual privada y aislada lógicamente dentro de tu cuenta de AWS en una región específica, que te da control total sobre tu entorno de red (direcciones IP, subredes, tablas de ruteo y pasarelas de internet).


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->

1. **Alcance Geográfico:** Una VPC pertenece a una **única Región**, pero se extiende automáticamente por **todas las Zonas de Disponibilidad (AZ)** de esa región.
2. **Direccionamiento (CIDR):** Define el rango de direcciones IP privadas internas de tu red (ej: `10.0.0.0/16`, que proporciona 65.536 IPs).
3. **Componentes Clave que contiene:**
   * **Subredes:** Divisiones de la VPC (públicas o privadas) asignadas a una AZ específica.
   * **Route Tables (Tablas de Ruteo):** Reglas que determinan a dónde se dirige el tráfico de red.
   * **Internet Gateway (IGW):** Permite la comunicación entre los recursos de la VPC e Internet.
   * **Security Groups & NACLs:** Capas de seguridad y cortafuegos.
4. **Modelo de Coste (Muy importante para la certificación):**
   * Crear VPCs, Subredes e Internet Gateways es **100% GRATIS**.
   * Solo pagas por componentes adicionales de tráfico como *NAT Gateways*, *VPC Endpoints* o *VPNs*.


---

## 🔑 Keywords / Conceptos clave

`AWS`, `VPC`, `keyword3`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

¿Qué es una Amazon VPC? :: Una red virtual aislada lógicamente dentro de una cuenta de AWS en una región específica. #card

¿Cuál es el alcance geográfico de una VPC dentro de AWS? :: Opera a nivel de Región (se extiende por todas las Zonas de Disponibilidad de esa región). #card

¿Tiene algún coste la creación de una VPC básica, subredes e Internet Gateway? :: No, la VPC, las subredes y los IGWs son totalmente gratuitos. Solo se pagan componentes de tráfico como NAT Gateways o VPC Endpoints. #card

¿Qué función cumple el bloque CIDR en una VPC? :: Define el rango de direcciones IP privadas que estarán disponibles dentro de esa red virtual. #card

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

- [[Cidr]] 
- [[AWS]]
-

---

## ✅ Checklist procesamiento

- [ ] Revisar y expandir contenido
- [ ] Crear flashcards si es necesario
- [ ] Hacer ejercicios relacionados
- [ ] Conectar con otras notas ([[]])
- [ ] Actualizar nivel de comprensión
- [ ] Mover a vault definitivo / Cambiar status a 🌿

---

## 💭 Notas adicionales / Ideas rápidas

<!-- Zona libre para cualquier cosa que quieras capturar rápido -->

Es una red de comunicación privada para configurar quien entra en tu red AWS.


---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-08-17 13:28 |
| Área/Tema | `= this.area` |
| Prioridad | `= this.prioridad` |
| Estado | Captura rápida → Pendiente procesamiento |
| Revisión | `= this.proxima-revision` |

---

#pendiente-procesar #captura-rapida
