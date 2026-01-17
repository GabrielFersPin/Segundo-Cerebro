# -*- coding: utf-8 -*-
import datetime
import sys

# --- 1. CONFIGURACIÓN ---
hoy = datetime.date.today()
nombre_archivo = hoy.strftime("%Y-%m-%d.md")
dia_semana = hoy.strftime("%A") 

# Traducción
dias = {
    "Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles", 
    "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado", "Sunday": "Domingo"
}
dia_es = dias.get(dia_semana, dia_semana)

# --- 2. INPUTS ---
print(f"\n📝 Generando: {dia_es} {hoy.day}")
print("-" * 30)

try:
    sueno = input("💤 Sueño (1=Mal / 2=Bien) [Enter=2]: ") or "2"
    energia = input("⚡ Energía (1=Baja / 2=Alta) [Enter=2]: ") or "2"
    foco = input("🎯 Foco hoy: ") or "Avanzar Arquitectura"
except KeyboardInterrupt:
    sys.exit()

# --- 3. PREPARAR DATOS ---
tipo_callout = "fail" if sueno == "1" else "success"
texto_bateria = "🔴 Batería Baja" if sueno == "1" else "🟢 Batería Alta"

es_finde = dia_semana in ["Saturday", "Sunday"]
es_lunes_miercoles_viernes = dia_semana in ["Monday", "Wednesday", "Friday"]

# --- 4. CONSTRUCCIÓN LÍNEA A LÍNEA (A prueba de balas) ---
lines = []

# Cabecera YAML
lines.append("---")
lines.append(f"fecha: {hoy}")
lines.append(f"dia: {dia_es}")
lines.append("tags: [diario, tracking]")
lines.append("---\n")

# Título y Cita
titulo_extra = "🌊 Modo Flow" if es_finde else ("🐍 Día Data Science" if es_lunes_miercoles_viernes else "☁️ Día Cloud")
lines.append(f"# 📅 {dia_es} {hoy.day}: {titulo_extra}\n")
lines.append("> [!quote] Cita")
lines.append("> \"La generosidad hacia el futuro es darlo todo al presente.\" — Camus\n")

# Estado del Sistema (Callout)
lines.append("## 🧠 Estado del Sistema")
lines.append(f"> [!{tipo_callout}] {texto_bateria}")
lines.append(f"> **Sueño:** {sueno}/2 | **Energía:** {energia}/2")
lines.append(f"> **Objetivo:** `{foco}`\n")

# Gráfico Gantt (Mermaid)
lines.append("```mermaid")
lines.append("gantt")
lines.append("    title Tu Horario de Hoy")
lines.append("    dateFormat HH:mm")
lines.append("    axisFormat %H:%M")
lines.append("    section Mañana")
lines.append("    Lectura Camus        :done, 08:00, 1h")
lines.append("    ARQUITECTURA (Duro)  :active, 09:00, 2h")
lines.append("    ALGORITMOS           :11:30, 2h")

if es_finde:
    lines.append("    section Vida")
    lines.append("    Surf y Escalar       :active, 09:00, 4h")
    lines.append("    Comida               :14:00, 2h")
    lines.append("    Proyecto App         :crit, 16:00, 3h")
elif es_lunes_miercoles_viernes:
    lines.append("    section Tarde")
    lines.append("    Comida y Deporte     :13:30, 2h")
    lines.append("    PROYECTO DS (Code)   :crit, 15:30, 3h")
    lines.append("    Transición           :18:30, 1h")
    lines.append("    section Noche")
    lines.append("    TRABAJO              :done, 19:30, 4h")
else:
    lines.append("    section Tarde")
    lines.append("    Comida y Deporte     :13:30, 2h")
    lines.append("    INFRA NUBE (AWS)     :crit, 15:30, 3h")
    lines.append("    Transición           :18:30, 1h")
    lines.append("    section Noche")
    lines.append("    TRABAJO              :done, 19:30, 4h")

lines.append("```\n")
lines.append("---\n")

# Bloque Mañana
lines.append("## 🌞 Mañana: Roca Dura (09:00 - 13:30)\n")
lines.append("### 🐸 Arquitectura de Computadores")
lines.append("*Meta: Crear notas atómicas en [[Arquitectura_Computadores_MOC]]*")
lines.append("- [ ] Revisar temas marcados con ❓")
lines.append("- [ ] Concepto clave de hoy: \n")
lines.append("### 🧮 Algoritmos")
lines.append("- [ ] 1h Teoría + 1h Práctica ([[Algoritmos_MOC]])\n")
lines.append("---\n")

# Bloque Tarde
if es_finde:
    lines.append("## 🚀 Proyecto Personal")
    lines.append("- [ ] Revisar Roadmap")
    lines.append("- [ ] Implementar mejora App\n")
elif es_lunes_miercoles_viernes:
    lines.append("## 🐍 Proyecto Data Science")
    lines.append("> Enfócate en código.")
    lines.append("- [ ] Feedback profesor")
    lines.append("- [ ] Commit Git\n")
else:
    lines.append("## ☁️ Infraestructura Nube")
    lines.append("> Mapas conceptuales.")
    lines.append("- [ ] AWS/Azure")
    lines.append("- [ ] Docker\n")

lines.append("---\n")

# Cierre y Tracking
lines.append("## 📉 Cierre del Día (Dataview)")
lines.append("*Rellenar al finalizar el día*\n")
lines.append("| Métrica | Input |")
lines.append("| :--- | :--- |")
lines.append("| **Horas Deep Work** | [horas-deep-work:: 0] |")
lines.append("| **Concentración** | [nivel-concentracion:: 0] / 10 |\n")
lines.append("**Hábitos:**")
lines.append("- [ ] 📚 Camus [habito-lectura:: true]")
lines.append("- [ ] 🏋️‍♀️ Deporte [habito-deporte:: true]")
lines.append("- [ ] 💻 Código [habito-codigo:: true]")

# --- 5. ESCRIBIR ARCHIVO ---
contenido_final = "\n".join(lines)

with open(nombre_archivo, "w", encoding="utf-8") as f:
    f.write(contenido_final)

print(f"✅ Archivo creado: {nombre_archivo}")
