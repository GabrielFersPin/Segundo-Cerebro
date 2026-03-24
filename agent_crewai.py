#!/usr/bin/env python3
"""CrewAI workflow for Segundo_Cerebro note vault processing.

Flow:
  1) Agent 1: Analista -> extraer conceptos de las notas
  2) Agent 2: Creador de Etiquetas -> generar etiquetas clave por nota
  3) Agent 3: Verificador -> validar relaciones entre etiquetas/conceptos

Uso:
  $ cd /home/gabriel/Documents/Segundo_Cerebro
  $ . .venv/bin/activate
  $ python3 agent_crewai.py --vault ./  # o path a vault

Requisitos:
  - crewai (>=1.11.1)
  - langchain, openai
  - OPENAI_API_KEY set en el entorno

Nota: Si no quiere usar OpenAI, configure CREWAI_LLMS con un llm local (o el que prefiera)

"""

import argparse
import glob
import json
import os
from pathlib import Path
from typing import Dict, List

from crewai import Agent, Crew, Task
from crewai.process import Process


def gather_markdown_files(vault_path: str) -> List[Path]:
    pattern = os.path.join(vault_path, "**", "*.md")
    return [Path(p) for p in glob.glob(pattern, recursive=True) if Path(p).is_file()]


def load_note_text(file_path: Path) -> str:
    try:
        return file_path.read_text(encoding='utf-8')
    except Exception:
        return file_path.read_text(encoding='latin-1')


def make_input_payload(vault_path: str) -> Dict[str, str]:
    files = gather_markdown_files(vault_path)
    text_by_file = {}
    for idx, file_path in enumerate(files, start=1):
        # Opcional: saltar notas de metadata o index por nombre
        text_by_file[str(file_path)] = load_note_text(file_path)
        if idx >= 1000:
            # límite guardado para evitar entrada gigante por error
            break

    return {
        "vault_path": str(vault_path),
        "note_count": len(text_by_file),
        "notes": text_by_file,
    }


def build_crew() -> Crew:
    # 1. Agent 1: Analista
    analista = Agent(
        role="Analista",
        goal="Analizar las notas del vault y extraer conceptos de alto nivel.",
        backstory="Eres un analista de conocimiento que organiza información en categorías y conceptos.",
        verbose=False,
        allow_delegation=True,
    )

    # 2. Agent 2: Creador de Etiquetas
    creador_etiquetas = Agent(
        role="Creador de Etiquetas",
        goal="Generar etiquetas exactas para cada nota basándose en conceptos extraídos.",
        backstory="Eres experto en taxonomía de información y sistemas de etiquetas semánticas.",
        verbose=False,
        allow_delegation=False,
    )

    # 3. Agent 3: Verificador de notas
    verificador = Agent(
        role="Verificador de Notas",
        goal="Verificar relaciones entre etiquetas y elaborar un grafo de conexiones.",
        backstory="Eres un auditor que valida consistencia semántica y conexiones entre ideas.",
        verbose=False,
        allow_delegation=False,
    )

    # Tareas con descripciones claras (esta forma es muy importante para CrewAI)
    task1 = Task(
        agent=analista,
        description="Extrae los conceptos clave de las notas y estructura un resumen agrupado por área temática.",
        expected_output="JSON con map concept -> lista notas (o frases) y un breve resumen.",
    )

    task2 = Task(
        agent=creador_etiquetas,
        description="Genera etiquetas para cada nota según los conceptos del agente analista.",
        expected_output="JSON con cada nota, sus etiquetas y justificación breve.",
    )

    task3 = Task(
        agent=verificador,
        description="Verifica si las etiquetas tienen conexiones lógicas y produce un mapa de relaciones clave entre etiquetas/conceptos.",
        expected_output="JSON con grafos/relaciones de etiquetas y recomendación de vínculos pendientes.",
    )

    crew = Crew(
        name="VaultNotesCrew",
        agents=[analista, creador_etiquetas, verificador],
        tasks=[task1, task2, task3],
        process=Process.sequential,
        verbose=True,
        memory=True,
        cache=True,
    )

    return crew


def run(vault_path: str):
    payload = make_input_payload(vault_path)
    print(f"[INFO] Vault path: {vault_path}, notes found: {payload['note_count']}")

    crew = build_crew()

    # El input se puede inyectar a través de `inputs` y los agentes pueden referirse a él
    risultato = crew.kickoff(inputs={
        "vault_path": payload["vault_path"],
        "note_count": payload["note_count"],
        "notes": payload["notes"],
    })

    # Guardar outputs a archivo JSON con trazas de ejecución
    output_file = Path(vault_path) / "crew_output.json"
    try:
        output_data = risultato.model_dump() if hasattr(risultato, 'model_dump') else risultato
        output_file.write_text(json.dumps(output_data, ensure_ascii=False, indent=2), encoding='utf-8')
    except Exception as e:
        print(f"ERROR al serializar resultado CrewOutput: {e}")
        output_file.write_text(str(risultato), encoding='utf-8')

    print(f"[OK] Crew completado, output guardado en: {output_file}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ejecutar flujo de agente CrewAI sobre un vault de notas.')
    parser.add_argument('--vault', type=str, default='.', help='Ruta del vault de notas (md).')
    args = parser.parse_args()

    if 'OPENAI_API_KEY' not in os.environ:
        print('WARN: No se encontró OPENAI_API_KEY. Asegúrate de configurarlo, o configura otro proveedor compatible.')

    run(args.vault)
