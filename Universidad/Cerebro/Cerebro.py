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

try:
    sueno = input("💤 Sueño (1=Mal / 2=Bien) [Enter=2]: ") or "2"
    energia = input("⚡ Energía (1=Baja / 2=Alta) [Enter=2]: ") or "2"
    foco = input("🎯 Foco hoy: ") or "Avanzar Arquitectura"
except KeyboardInterrupt:
    sys.exit()

# --- 3. PREPARAR DATOS ---
tipo_callout = "fail" if sueno == "1" else "success"
texto_bateria = "🔴 Batería Baja" if sueno == "1" else "🟢 Batería Alta"

# --- 4. CONSTRUCCIÓN LÍNEA A LÍNEA ---
lines = []

# Cabecera YAML
lines.append("---")
lines.append(f"fecha: {hoy}")
lines.append(f"dia: {dia_es}")
lines.append("tags: [diario, tracking]")
lines.append("---\n")

# Título y Cita
lines.append(f"# 📅 {dia_es} {hoy.day}\n")
lines.append("> [!quote] Cita")
lines.append("> \"La generosidad hacia el futuro es darlo todo al presente.\" — Camus\n")

# Estado del Sistema (Callout)
lines.append("## 🧠 Estado del Sistema")
lines.append(f"> [!{tipo_callout}] {texto_bateria}")
lines.append(f"> **Sueño:** {sueno}/2 | **Energía:** {energia}/2")
# --- 4.7. TAREAS ESPECÍFICAS ---
print("\n📚 Tareas de Asignatura:")
asignatura = input("Nombre de la asignatura: ") or "Arquitectura"
tareas_asig = input(f"Tareas para {asignatura} (separadas por ';'): ") or "Repasar apuntes;Hacer ejercicios"

lines.append(f"## 📚 {asignatura}")
for t in tareas_asig.split(";"):
    lines.append(f"- [ ] {t.strip()}")
lines.append("")

# --- 5. ESCRIBIR ARCHIVO ---
contenido_final = "\n".join(lines)

with open(nombre_archivo, "w", encoding="utf-8") as f:
    f.write(contenido_final)

print(f"✅ Archivo creado: {nombre_archivo}")
