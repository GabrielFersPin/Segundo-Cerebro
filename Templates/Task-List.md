<%*
// --- 1. CONFIGURACIÓN LÓGICA ---
let date = tp.date.now("YYYY-MM-DD");
let dayOfWeek = moment(date).format('dddd'); // e.g., "Monday"
let isWeekend = (dayOfWeek === "Saturday" || dayOfWeek === "Sunday");

// --- 2. LOGICA A/B PARA LA TARDE ---
let bloqueTarde = "";
let focoTarde = "";

if (isWeekend) {
    bloqueTarde = "🌊 Surf / 🧗 Escalar / 💻 Proyecto App (Coworking)";
    focoTarde = "Disfrute y Construcción Creativa";
} else if (dayOfWeek === "Monday" || dayOfWeek === "Wednesday" || dayOfWeek === "Friday") {
    bloqueTarde = "🐍 Fundamentos DS (Proyecto Streamlit)";
    focoTarde = "Flow State: Código profundo e iteración";
} else {
    bloqueTarde = "☁️ Infraestructura Nube (AWS/Azure + Docker)";
    focoTarde = "Sistemas: Mapas conceptuales y comparativas";
}

// --- 3. INPUTS INICIALES ---
let sleepQuality = await tp.system.suggester(["🟢 Descansado", "🟡 Normal", "🔴 Cansado"], ["🟢 Descansado", "🟡 Normal", "🔴 Cansado"], false, "Cómo has dormido?");
let energyLevel = await tp.system.suggester(["⚡ Alta", "🔋 Media", "🪫 Baja"], ["⚡ Alta", "🔋 Media", "🪫 Baja"], false, "Nivel de energía cognitiva?");
let mainFocus = await tp.system.prompt("🎯 ¿Foco principal de hoy?", "Arquitectura y Algoritmos");
_%>
---
fecha: <% date %>
dia-semana: <% dayOfWeek %>
semana: <% moment(date).format("WW") %>
# Métricas Biológicas (Morning Check)
sueño-calidad: "<% sleepQuality %>"
energia-inicial: "<% energyLevel %>"

# Métricas de Rendimiento (Llenar al final del día)
horas-deep-work: 0
nivel-concentracion: 0 
estado-animo: "😐" 

# Hábitos
habito-lectura: false
habito-deporte: false
habito-codigo: false
habito-linkedin: false

# Contexto
foco-principal: "<% mainFocus %>"
tags: [diario, tracking]
---

# 📅 Diario: <% tp.date.now("dddd DD MMMM YYYY") %>

> "La verdadera generosidad hacia el futuro consiste en entregarlo todo al presente." — Albert Camus

---

## 🧠 Estado del Sistema (Neuro-Check)
- **Sueño:** <% sleepQuality %>
- **Energía Cognitiva:** <% energyLevel %>
- **Objetivo Principal de Hoy:** <%* if(isWeekend){tR += "Avanzar App y Desconectar"}else{tR += "Entender 2 conceptos de Arquitectura"} %>

---

<%* if (!isWeekend) { %>
## 🌞 Bloque Mañana: Carga Cognitiva Alta

### 08:00 - 09:00 | ☕ Activación & Camus
- [ ] Lectura Estoica/Existencialista (15 min)
- [ ] Desayuno + Hidratación

### 09:00 - 11:00 | 🐸 Arquitectura de Computadores (Focus)
*Meta: Crear notas atómicas, no solo leer.*
- **Concepto clave a atacar hoy:** - [ ] Crear/Refinar una nota en [[Arquitectura_Computadores_MOC]]
- [ ] Revisar temas marcados con ❓ en el Dashboard.

### 11:30 - 13:30 | 🧮 Algoritmos (Lógica)
*Meta: Resolver problemas + Teoría aplicada.*
- [ ] 1h Teoría / Repaso
- [ ] 1h Práctica de Código
- Enlace: [[Algoritmos_MOC]]

---

## 🥪 Bloque Mediodía: Bio-Regulación

### 13:30 - 15:30 | 🏋️‍♀️ Cuerpo & Nutrición
- [ ] Comida nutritiva
- [ ] **Actividad:** (Gimnasio / Escalar / Descanso activo)

---

## 🌇 Bloque Tarde: <% focoTarde %>

### 15:30 - 18:30 | <% bloqueTarde %>
<%* if (dayOfWeek === "Monday" || dayOfWeek === "Wednesday" || dayOfWeek === "Friday") { %>
> **Foco Proyecto DS:**
> - [ ] Revisar feedback del profesor
> - [ ] Implementar cambios en Streamlit
> - [ ] Commit en Git
<%* } else { %>
> **Foco Nube:**
> - [ ] Conceptos AWS/GCP
> - [ ] Revisar notas de Docker/Microservicios
> - [ ] Crear tabla comparativa en [[Infraestructura_Nube_MOC]]
<%* } %>

### 18:30 - 19:30 | 🚗 Transición
- [ ] Preparar mochila
- [ ] Ir a zona de reparto (Podcast/Música, cero código)

---

## 🌙 Bloque Noche: Trabajo & Cierre

### 19:30 - 23:30 | 🛵 Trabajo (Modo Automático)
*Objetivo: Cumplir con el trabajo ahorrando energía mental.*

### 00:00 | Cierre
- [ ] ¿Qué aprendí hoy? (Breve)
- [ ] Preparar el día de mañana
<%* } else { %>
## 🌊 Fin de Semana: Surf & Code

### Mañana
- [ ] 🏄‍♂️ **Surf / Escalar** (Aprovechar luz y olas)
- [ ] Batch Cooking (Solo Domingo)

### Tarde (Deep Work sin presión)
- [ ] **Proyecto App / Coworking**
    - [ ] Revisar Roadmap en [[Data Journey]]
    - [ ] Implementar una mejora pequeña (1-2 horas)
    - [ ] Escribir post para LinkedIn (si hay avance)
<%* } %>

---

## 📉 Cierre del Día: Input de Datos
*Rellena esto antes de dormir para alimentar el algoritmo de tu vida.*

- **⏱️ Horas de Deep Work Real:** [horas-deep-work:: ] 
- **🧠 Nivel de Concentración (1-10):** [nivel-concentracion:: ] 
- **mood::** (Selecciona: 🙂 / 😐 / 😫 / 🤬 / 🤩)

### ✅ Checklist de Hábitos
- [ ] 📚 Leí a Camus [habito-lectura:: true]
- [ ] 🏋️‍♀️ Hice Deporte [habito-deporte:: true]
- [ ] 💻 Piqué código [habito-codigo:: true]
- [ ] 📢 Publiqué/Interactué en LinkedIn [habito-linkedin:: true]

### 📝 Notas para el Gabriel del Futuro
- ¿Qué obstáculo tuve hoy?
- ¿Qué aprendí sobre mi forma de estudiar?

## 🔗 Zettelkasten: Conexiones de Hoy
*¿Qué nota nueva he creado hoy que se conecta con algo que ya sabía?*
- [[Nota Nueva]] se relaciona con [[Nota Antigua]] porque...
