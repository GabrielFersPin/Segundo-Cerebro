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

# Cidr

> [!info] Contexto captura
> **Fecha**: 2026-08-17 11:46
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> _Classless Inter-Domain Routing_ (Enrutamiento Interdominios sin Clases)
> En la práctica, un **bloque CIDR** es simplemente la forma estándar de expresar **un rango o grupo de direcciones IP**.


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->

### 💡 La forma fácil de entenderlo

Una dirección IP tiene 4 bloques de números (ej: `10.0.1.50`). 

La barra diagonal al final (`/16`, `/24`, etc.) indica **cuántos números se quedan fijos** y cuántos pueden cambiar libremente para asignarse a tus servidores:

| Bloque CIDR | ¿Qué números se quedan fijos? | Rango de IPs disponibles | Nº de IPs totales | Uso típico en AWS |
| :--- | :--- | :--- | :--- | :--- |
| **`10.0.0.0/16`** | Los 2 primeros (`10.0.x.x`) | `10.0.0.1` hasta `10.0.255.254` | **65.536 IPs** | **VPC completa** |
| **`10.0.1.0/24`** | Los 3 primeros (`10.0.1.x`) | `10.0.1.1` hasta `10.0.1.254` | **256 IPs** | **Una Subred** |
| **`10.0.1.5/32`** | Los 4 números fijos (`10.0.1.5`) | Únicamente `10.0.1.5` | **1 IP exacta** | **Un Servidor o Tu IP de casa** |

---

### 🧠 Regla de oro para recordar

* **Número tras la barra MÁS PEQUEÑO (`/16`)** ➡️ Red **MÁS GRANDE** (muchas IPs).
* **Número tras la barra MÁS GRANDE (`/24`)** ➡️ Red **MÁS PEQUEÑA** (pocas IPs).

---


Al poner:
```yaml
Properties:
  CidrBlock: 10.0.0.0/16
```
Le estás diciendo a AWS: *"Créame una red virtual privada (VPC) que tenga espacio para hasta 65.536 direcciones IP privadas (desde la 10.0.0.1 hasta la 10.0.255.254)"*.



---

## 🔑 Keywords / Conceptos clave

`keyword1`, `keyword2`, `keyword3`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

_Flashcards pendientes de crear_

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

- [[Amazon VPC (Virtual Private Cloud)]]
-

---

## ✅ Checklist procesamiento

- [ ] Revisar y expandir contenido
- [ ] Crear flashcards si es necesario
- [ ] Hacer ejercicios relacionados
- [x] Conectar con otras notas ([[]]) ✅ 2026-08-17
- [ ] Actualizar nivel de comprensión
- [ ] Mover a vault definitivo / Cambiar status a 🌿

---

## 💭 Notas adicionales / Ideas rápidas

<!-- Zona libre para cualquier cosa que quieras capturar rápido -->

Define un rango de Ip's capaces de conectar con el puerto abierto


---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-08-17 11:46 |
| Área/Tema | `= this.area` |
| Prioridad | `= this.prioridad` |
| Estado | Captura rápida → Pendiente procesamiento |
| Revisión | `= this.proxima-revision` |

---

#pendiente-procesar #captura-rapida
