#!/usr/bin/env python3
import datetime
import os

def main():
    print("🌟 Creación de Nueva Nota 🌟")
    print("-" * 30)
    
    titulo = input("📌 Título de la nota: ").strip()
    if not titulo:
        print("El título no puede estar vacío.")
        return

    area = input("📚 Área o Tema principal (ej: Algoritmos, Cloud, etc): ").strip()
    
    print("\nElige el tipo de nota:")
    print("1) Técnica")
    print("2) Filosofía / Lectura")
    print("3) Idea / Personal")
    print("4) Proyecto")
    print("5) Captura Rápida")
    opcion_tipo = input("Opción (1-5) [1]: ").strip()
    
    tipos = {"1": "tecnica", "2": "filosofia", "3": "idea", "4": "proyecto", "5": "captura_rapida"}
    tipo_nota = tipos.get(opcion_tipo, "tecnica")
    
    mazo = input("\n🎴 Mazo para Flashcards (opcional): ").strip()

    now = datetime.datetime.now()
    created = now.strftime("%Y-%m-%d %H:%M")
    date_only = now.strftime("%Y-%m-%d")
    proxima_revision = (now + datetime.timedelta(days=7)).strftime("%Y-%m-%d")

    filename = f"{titulo.replace(' ', '_')}.md"
    
    # Base del frontmatter unificado
    content = f"""---
created: {created}
modified: {created}
area: "{area}"
tipo_nota: {tipo_nota}
status: 🌱
nivel-comprension: ""
proxima-revision: {proxima_revision}
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
cards-deck: "{mazo}"
tags: [{tipo_nota}, {date_only}]
---

# {titulo}

> [!info] Metadata
> **Fecha**: {date_only}
> **Área**: {area}

---

## 📝 Desarrollo de la Nota

Empieza a escribir aquí...

"""

    filepath = os.path.join(os.getcwd(), filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print("-" * 30)
    print(f"✅ Nota creada exitosamente: {filepath}")

if __name__ == "__main__":
    main()
