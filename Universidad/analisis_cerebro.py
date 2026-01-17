import frontmatter
import pandas as pd
import glob
import os

# CONFIGURACIÓN
# Cambia esto por la ruta a tu carpeta de Diario en Obsidian
# Si el script está en la misma carpeta, usa "."
RUTA_DIARIO = "./Diario/*.md" 

datos = []

print("🧠 Leyendo tu Segundo Cerebro...")

files = glob.glob(RUTA_DIARIO)
for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            post = frontmatter.load(f)
            # Solo procesamos si tiene fecha (es una nota diaria)
            if 'fecha' in post.metadata:
                fila = post.metadata
                # Añadimos métricas calculadas si faltan
                if 'horas-deep-work' not in fila: fila['horas-deep-work'] = 0
                datos.append(fila)
        except Exception as e:
            print(f"Error leyendo {file_path}: {e}")

# Crear DataFrame
df = pd.DataFrame(datos)

# Limpieza básica
df['fecha'] = pd.to_datetime(df['fecha'])
df = df.sort_values('fecha')

print("\n--- 📊 ESTADÍSTICAS DEL GABRIEL ---\n")

# 1. Total de Deep Work
total_horas = df['horas-deep-work'].sum()
print(f"🔥 Total horas Deep Work registradas: {total_horas}h")

# 2. Promedio de Concentración por calidad de sueño
if 'sueño-calidad' in df.columns and 'nivel-concentracion' in df.columns:
    print("\n💤 Relación Sueño -> Concentración (Promedio):")
    print(df.groupby('sueño-calidad')['nivel-concentracion'].mean())

# 3. ¿Qué días eres más productivo?
df['dia_nombre'] = df['fecha'].dt.day_name()
print("\n📅 Productividad media por día de la semana:")
print(df.groupby('dia_nombre')['horas-deep-work'].mean().sort_values(ascending=False))

# 4. Correlación (Si tienes suficientes datos numéricos)
print("\n🔗 Correlaciones:")
cols_num = ['horas-deep-work', 'nivel-concentracion']
print(df[cols_num].corr())

print("\n🚀 ¡Sigue alimentando los datos!")
