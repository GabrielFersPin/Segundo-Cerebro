# 🧠 Segundo Cerebro con Agentes — Plan de Implementación v2

**LangGraph + ChromaDB + NetworkX + Obsidian**  
*Actualizado: Marzo 2026*

> **Cambios respecto a v1**
> - ❌ Eliminado Neo4j — over-engineering para el volumen actual de notas
> - ✅ Añadido NetworkX como grafo ligero sin infraestructura extra
> - ✅ Arquitectura de dos repositorios separados con responsabilidades claras
> - ✅ El repo de agentes consume `obsidian-rag-system` como dependencia local

---

## Índice

1. [Visión general](#1-visión-general)
2. [Arquitectura de dos repositorios](#2-arquitectura-de-dos-repositorios)
3. [Stack tecnológico](#3-stack-tecnológico)
4. [Fase 0 — Preparación del entorno](#4-fase-0--preparación-del-entorno)
5. [Fase 1 — Pipeline LangGraph base](#5-fase-1--pipeline-langgraph-base)
6. [Fase 2 — Integración con RAG existente](#6-fase-2--integración-con-rag-existente)
7. [Fase 3 — Grafo de conocimiento con NetworkX](#7-fase-3--grafo-de-conocimiento-con-networkx)
8. [Fase 4 — Agentes especializados](#8-fase-4--agentes-especializados)
9. [Fase 5 — Automatización y triggers](#9-fase-5--automatización-y-triggers)
10. [Estructura de archivos del proyecto](#10-estructura-de-archivos-del-proyecto)
11. [Referencia rápida de comandos](#11-referencia-rápida-de-comandos)

---

## 1. Visión general

El objetivo es construir un sistema de agentes que gestione automáticamente el conocimiento entre:

- **Obsidian** — notas atómicas en formato Zettelkasten (vault en `/home/gabriel/Documents/Segundo_Cerebro`)
- **ChromaDB** — búsqueda semántica por vectores (ya operativo en `obsidian-rag-system`)
- **NetworkX** — grafo ligero que lee los `[[wikilinks]]` de Obsidian directamente
- **LangGraph** — orquestador del flujo entre agentes con estado compartido

El flujo completo cuando llega un input nuevo:

```
Input (texto / voz / PDF / URL)
        ↓
[capturar_nota] → genera nota atómica con frontmatter
        ↓
[evaluar_calidad] → ¿es atómica? si no → vuelve a capturar (máx. 3 intentos)
        ↓
    ┌───┴───┐
[conectar]  [flashcards]   ← corren en paralelo
    └───┬───┘
        ↓
[guardar_obsidian] → escribe .md + actualiza NetworkX en memoria
        ↓
      END
```

---

## 2. Arquitectura de dos repositorios

La razón de mantener dos repos separados es de responsabilidad: `obsidian-rag-system` es infraestructura estable que Claude Desktop usa activamente via MCP. El nuevo repo de agentes es experimental y en desarrollo. Mezclarlos rompería la estabilidad del primero.

```
obsidian-rag-system/          ← ya existe, no tocar
│   src/rag_chain.py          ← ObsidianRAGSystem (se importa desde agentes)
│   src/obsidian_loader.py
│   src/vectorstore.py
│   mcp_server.py             ← Claude Desktop lo usa via MCP
│   chroma_db/                ← base de datos vectorial compartida
│   data/vault → /home/gabriel/Documents/Segundo_Cerebro
│
segundo-cerebro-agentes/      ← nuevo repo (este plan)
│   requirements.txt          ← incluye obsidian-rag-system como dep local
│   src/
│       state.py
│       graph.py
│       nodes/
│       agentes/
```

El nuevo repo referencia al RAG como dependencia local — cualquier mejora que hagas en `obsidian-rag-system` se refleja automáticamente en los agentes sin duplicar código.

---

## 3. Stack tecnológico

| Componente | Herramienta | Versión | Estado |
|---|---|---|---|
| Orquestador de agentes | LangGraph | `>=0.2` | instalar |
| LLM | Claude Sonnet (Anthropic) | `claude-sonnet-4-20250514` | API key ya tienes |
| Vector store + RAG | obsidian-rag-system | local | **ya existe** |
| Grafo de conocimiento | NetworkX | `>=3.0` | instalar (ligero) |
| Notas | Obsidian | cualquier versión | **ya existe** |
| Automatización | watchdog | `>=4.0` | instalar |
| Lenguaje | Python | `>=3.11` | **ya tienes** |

> ✅ No se necesita Docker ni Neo4j. Todo corre en local sin infraestructura adicional.

---

## 4. Fase 0 — Preparación del entorno

### 4.1 Requisitos previos

Antes de empezar, verifica que tienes:

- [ ] `obsidian-rag-system` funcionando con notas indexadas
- [ ] API key de Anthropic (`ANTHROPIC_API_KEY`)
- [ ] Python 3.11+ con `pip`
- [ ] El vault en `/home/gabriel/Documents/Segundo_Cerebro`

### 4.2 Crear el repositorio nuevo

```bash
# Crear al mismo nivel que obsidian-rag-system
cd /home/gabriel/Documents
mkdir segundo-cerebro-agentes
cd segundo-cerebro-agentes

git init
python -m venv .venv
source .venv/bin/activate
```

### 4.3 Instalar dependencias

`requirements.txt`:

```txt
# Orquestación de agentes
langgraph>=0.2
langchain-anthropic>=0.1
langchain-community>=0.2

# Grafo de conocimiento (ligero, sin infraestructura)
networkx>=3.0

# Utilidades
python-dotenv>=1.0
watchdog>=4.0

# Tu RAG existente como dependencia local
# Esto permite importar ObsidianRAGSystem directamente
-e /home/gabriel/Documents/obsidian-rag-system
```

```bash
pip install -r requirements.txt
```

> 💡 La línea `-e /home/gabriel/Documents/obsidian-rag-system` instala tu repo RAG en modo editable. Si mejoras el RAG, los agentes recogen el cambio automáticamente sin reinstalar.

### 4.4 Variables de entorno

`.env`:

```env
ANTHROPIC_API_KEY=sk-ant-...
OBSIDIAN_VAULT_PATH=/home/gabriel/Documents/Segundo_Cerebro
RAG_SYSTEM_PATH=/home/gabriel/Documents/obsidian-rag-system
CHROMA_DB_PATH=/home/gabriel/Documents/obsidian-rag-system/chroma_db
```

> ⚠️ Añade `.env` al `.gitignore`. Nunca subas tus API keys a GitHub.

### 4.5 Verificar que la integración funciona

```bash
# Desde segundo-cerebro-agentes/ con el venv activado
python -c "
from src.rag_chain import ObsidianRAGSystem
import os
from dotenv import load_dotenv
load_dotenv()

rag = ObsidianRAGSystem(vault_path=os.getenv('OBSIDIAN_VAULT_PATH'))
info = rag.get_system_info()
print(f'✅ RAG conectado: {info[\"indexed_notes\"]} notas indexadas')
"
```

Si ves el número de notas, la integración funciona correctamente.

---

## 5. Fase 1 — Pipeline LangGraph base

### 5.1 Definir el estado compartido

Crea `src/state.py`:

```python
from typing import TypedDict, List, Optional, Annotated
import operator

class BrainState(TypedDict):
    # Input
    raw_input: str
    asignatura: str            # Algoritmos | Arquitectura | Infraestructura-Nube | Fundamentos-DS
    tipo_nota: str             # tecnica | filosofia | idea | proyecto

    # Procesamiento
    nota_md: Optional[str]     # contenido generado de la nota
    titulo: Optional[str]      # título extraído
    calidad_ok: bool
    intentos: int

    # Salidas
    wikilinks: List[str]       # [[enlaces]] a notas relacionadas
    flashcards: List[str]      # tarjetas generadas

    # Metadatos
    dificultad: Optional[str]  # ⭐ a ⭐⭐⭐⭐⭐
    proxima_revision: Optional[str]
    errores: Annotated[List[str], operator.add]  # acumula errores sin sobreescribir
```

### 5.2 Nodo 1 — Capturar nota

Crea `src/nodes/capturar.py`:

```python
from langchain_anthropic import ChatAnthropic
from src.state import BrainState
import re

llm = ChatAnthropic(model="claude-sonnet-4-20250514", max_tokens=2000)

PROMPT_CAPTURA = """Eres un experto en el método Zettelkasten aplicado a Data Science e IA.

Convierte el siguiente input en una nota atómica. Una nota atómica = UN solo concepto.

Input: {raw_input}
Asignatura: {asignatura}
Tipo: {tipo_nota}

Genera la nota en este formato exacto:

---
titulo: [título del concepto, max 6 palabras]
asignatura: {asignatura}
tipo_nota: {tipo_nota}
dificultad: [⭐☆☆☆☆ | ⭐⭐☆☆☆ | ⭐⭐⭐☆☆ | ⭐⭐⭐⭐☆ | ⭐⭐⭐⭐⭐]
status: 🌱
proxima_revision: [fecha en 3 días desde hoy, formato YYYY-MM-DD]
---

# [título]

## Definición
[2-3 párrafos explicando UN concepto]

## Conceptos clave
- **[término]**: [definición breve]

## Ejemplo práctico
[código o caso de uso concreto]

## Conexiones
[qué otros conceptos relacionados existen - solo nombres, sin [[links]] aún]
"""

def capturar_nota(state: BrainState) -> BrainState:
    try:
        prompt = PROMPT_CAPTURA.format(**state)
        respuesta = llm.invoke(prompt)
        contenido = respuesta.content

        titulo_match = re.search(r'titulo:\s*(.+)', contenido)
        titulo = titulo_match.group(1).strip() if titulo_match else "Sin título"

        return {
            **state,
            "nota_md": contenido,
            "titulo": titulo,
            "intentos": state.get("intentos", 0) + 1
        }
    except Exception as e:
        return {**state, "errores": [f"Error en capturar_nota: {str(e)}"]}
```

### 5.3 Nodo 2 — Evaluar calidad

Crea `src/nodes/evaluar.py`:

```python
from langchain_anthropic import ChatAnthropic
from src.state import BrainState

llm = ChatAnthropic(model="claude-sonnet-4-20250514", max_tokens=100)

def evaluar_calidad(state: BrainState) -> BrainState:
    if not state.get("nota_md"):
        return {**state, "calidad_ok": False}

    prompt = f"""Evalúa si esta nota Zettelkasten es suficientemente atómica.
Una nota atómica trata UN SOLO concepto central.

Nota:
{state['nota_md'][:500]}

Responde ÚNICAMENTE con una de estas dos palabras: OK o REVISAR"""

    respuesta = llm.invoke(prompt)
    es_ok = "OK" in respuesta.content.upper()
    return {**state, "calidad_ok": es_ok}


def debe_revisar(state: BrainState) -> str:
    """Edge condicional: decide si iterar o continuar."""
    if state.get("calidad_ok") or state.get("intentos", 0) >= 3:
        return "continuar"
    return "revisar"
```

### 5.4 Construir el grafo

Crea `src/graph.py`:

```python
from langgraph.graph import StateGraph, START, END
from src.state import BrainState
from src.nodes.capturar import capturar_nota
from src.nodes.evaluar import evaluar_calidad, debe_revisar
from src.nodes.conectar import conectar_semantico
from src.nodes.flashcards import generar_flashcards
from src.nodes.guardar import guardar_en_obsidian

def build_graph():
    workflow = StateGraph(BrainState)

    workflow.add_node("capturar_nota", capturar_nota)
    workflow.add_node("evaluar_calidad", evaluar_calidad)
    workflow.add_node("conectar_semantico", conectar_semantico)
    workflow.add_node("generar_flashcards", generar_flashcards)
    workflow.add_node("guardar_obsidian", guardar_en_obsidian)

    workflow.add_edge(START, "capturar_nota")
    workflow.add_edge("capturar_nota", "evaluar_calidad")

    # Ciclo de revisión — la ventaja clave de LangGraph sobre CrewAI
    workflow.add_conditional_edges(
        "evaluar_calidad",
        debe_revisar,
        {
            "revisar": "capturar_nota",
            "continuar": "conectar_semantico"
        }
    )

    # Paralelo: conectar Y flashcards al mismo tiempo
    workflow.add_edge("evaluar_calidad", "generar_flashcards")
    workflow.add_edge("conectar_semantico", "guardar_obsidian")
    workflow.add_edge("generar_flashcards", "guardar_obsidian")
    workflow.add_edge("guardar_obsidian", END)

    return workflow.compile()

app = build_graph()
```

---

## 6. Fase 2 — Integración con RAG existente

Aquí está la clave: en lugar de re-implementar ChromaDB, importas directamente `ObsidianRAGSystem` de tu repo existente.

### 6.1 Nodo conector semántico

Crea `src/nodes/conectar.py`:

```python
import os
from src.rag_chain import ObsidianRAGSystem   # importado del repo RAG via -e
from src.state import BrainState

# Instancia única reutilizable (no crear una nueva en cada llamada)
_rag_instance = None

def get_rag() -> ObsidianRAGSystem:
    global _rag_instance
    if _rag_instance is None:
        _rag_instance = ObsidianRAGSystem(
            vault_path=os.getenv("OBSIDIAN_VAULT_PATH"),
            persist_dir=os.getenv("CHROMA_DB_PATH", "./chroma_db")
        )
    return _rag_instance


def conectar_semantico(state: BrainState) -> BrainState:
    try:
        rag = get_rag()
        resultado = rag.query(
            question=state["nota_md"],
            n_results=5,
            deck_filter=state["asignatura"]  # filtra por asignatura
        )

        wikilinks = [
            f"[[{s['file_name']}]]"
            for s in resultado.get("sources", [])
            if s["file_name"] != state.get("titulo")  # no enlazar a sí misma
        ]

        return {**state, "wikilinks": wikilinks}

    except Exception as e:
        return {**state, "wikilinks": [], "errores": [f"ChromaDB error: {str(e)}"]}
```

### 6.2 Nodo generador de flashcards

Crea `src/nodes/flashcards.py`:

```python
from langchain_anthropic import ChatAnthropic
from src.state import BrainState

llm = ChatAnthropic(model="claude-sonnet-4-20250514", max_tokens=1000)

PROMPT_FLASHCARDS = """Genera exactamente 5 flashcards desde esta nota Zettelkasten.
Usa el formato de Obsidian:

- Básica:    ¿Pregunta?::Respuesta
- Reversa:   Término:::Definición
- Cloze:     Texto con ==palabra clave== oculta

Nota:
{nota_md}

Genera las 5 flashcards, una por línea, sin numeración ni texto extra."""

def generar_flashcards(state: BrainState) -> BrainState:
    try:
        prompt = PROMPT_FLASHCARDS.format(nota_md=state["nota_md"])
        respuesta = llm.invoke(prompt)

        cards = [
            line.strip()
            for line in respuesta.content.strip().split("\n")
            if line.strip() and ("::" in line or "==" in line)
        ]

        return {**state, "flashcards": cards}
    except Exception as e:
        return {**state, "flashcards": [], "errores": [f"Flashcards error: {str(e)}"]}
```

### 6.3 Nodo guardar en Obsidian

Crea `src/nodes/guardar.py`:

```python
import os
from pathlib import Path
from src.state import BrainState

VAULT_PATH = os.getenv("OBSIDIAN_VAULT_PATH")

def guardar_en_obsidian(state: BrainState) -> BrainState:
    """Escribe la nota .md en el vault con los wikilinks y flashcards añadidos."""
    try:
        titulo = state["titulo"]
        contenido = state["nota_md"]

        # Añadir wikilinks si los hay
        if state["wikilinks"]:
            enlaces = "\n".join(state["wikilinks"])
            contenido += f"\n\n## 🔗 Notas relacionadas\n{enlaces}"

        # Añadir flashcards si las hay
        if state["flashcards"]:
            cards = "\n\n".join(state["flashcards"])
            contenido += f"\n\n## 🃏 Flashcards\n\n{cards}"

        # Determinar carpeta por asignatura
        carpeta = Path(VAULT_PATH) / state["asignatura"]
        carpeta.mkdir(exist_ok=True)

        # Escribir archivo
        nombre_archivo = titulo.replace(" ", "_").replace("/", "-") + ".md"
        ruta = carpeta / nombre_archivo
        ruta.write_text(contenido, encoding="utf-8")

        print(f"✅ Nota guardada: {ruta}")
        return state

    except Exception as e:
        return {**state, "errores": [f"Error guardando nota: {str(e)}"]}
```

---

## 7. Fase 3 — Grafo de conocimiento con NetworkX

NetworkX lee los `[[wikilinks]]` directamente de tus notas de Obsidian. Sin Docker, sin base de datos externa, sin setup. El grafo vive en memoria y se reconstruye en segundos.

### 7.1 Construir el grafo desde el vault

Crea `src/grafo.py`:

```python
import networkx as nx
from pathlib import Path
import re
import os

VAULT_PATH = os.getenv("OBSIDIAN_VAULT_PATH")

def cargar_grafo_obsidian() -> nx.DiGraph:
    """
    Lee todos los [[wikilinks]] del vault y construye un grafo dirigido.
    Nodo = nota · Arista = enlace entre notas
    """
    G = nx.DiGraph()
    vault = Path(VAULT_PATH)

    for archivo in vault.rglob("*.md"):
        nota = archivo.stem
        contenido = archivo.read_text(encoding="utf-8")

        # Extraer asignatura del frontmatter
        asig_match = re.search(r'asignatura:\s*(.+)', contenido)
        asignatura = asig_match.group(1).strip() if asig_match else "general"

        # Añadir nodo con atributos
        G.add_node(nota, asignatura=asignatura, archivo=str(archivo))

        # Añadir aristas por cada [[wikilink]]
        links = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', contenido)
        for link in links:
            G.add_edge(nota, link.strip())

    return G


# Consultas útiles

def notas_relacionadas(G: nx.DiGraph, titulo: str, profundidad: int = 1) -> list:
    """Notas conectadas a una nota dada hasta N saltos."""
    if titulo not in G:
        return []
    vecinos = nx.ego_graph(G, titulo, radius=profundidad)
    return [n for n in vecinos.nodes if n != titulo]


def notas_huerfanas(G: nx.DiGraph) -> list:
    """Notas sin ningún enlace entrante ni saliente."""
    return [n for n in G.nodes if G.degree(n) == 0]


def prerequisitos(G: nx.DiGraph, titulo: str) -> list:
    """Notas que enlazan hacia una nota (predecesores)."""
    return list(G.predecessors(titulo))


def camino_entre(G: nx.DiGraph, origen: str, destino: str) -> list:
    """Camino más corto entre dos conceptos."""
    try:
        return nx.shortest_path(G, origen, destino)
    except nx.NetworkXNoPath:
        return []


def notas_por_asignatura(G: nx.DiGraph, asignatura: str) -> list:
    """Todas las notas de una asignatura con sus conexiones."""
    return [
        {
            "nota": n,
            "conexiones": list(G.successors(n)),
            "referencias": list(G.predecessors(n))
        }
        for n, data in G.nodes(data=True)
        if data.get("asignatura") == asignatura
    ]
```

### 7.2 Cuándo añadir Neo4j en el futuro

NetworkX es suficiente mientras el vault tenga menos de ~500 notas. Cuando necesites:
- Consultas Cypher complejas sobre el grafo
- Persistencia del grafo entre sesiones sin reconstruirlo
- Múltiples usuarios o acceso concurrente

…en ese momento migrar a Neo4j es directo: el mismo código de nodos y aristas funciona en ambos.

---

## 8. Fase 4 — Agentes especializados

### 8.1 Agente revisor diario

Crea `src/agentes/revisor.py`:

```python
"""
Corre cada mañana. Lee el frontmatter de las notas y genera
la cola de repaso del día ordenada por dificultad.
"""
import os
import re
from datetime import datetime, date
from pathlib import Path
from langchain_anthropic import ChatAnthropic

VAULT_PATH = os.getenv("OBSIDIAN_VAULT_PATH")
llm = ChatAnthropic(model="claude-sonnet-4-20250514", max_tokens=1500)

def obtener_notas_para_hoy() -> list[dict]:
    vault = Path(VAULT_PATH)
    notas_hoy = []
    hoy = date.today()

    for archivo in vault.rglob("*.md"):
        contenido = archivo.read_text(encoding="utf-8")
        fecha_match = re.search(r'proxima_revision:\s*(\d{4}-\d{2}-\d{2})', contenido)
        if not fecha_match:
            continue

        fecha = datetime.strptime(fecha_match.group(1), "%Y-%m-%d").date()
        if fecha <= hoy:
            titulo_match = re.search(r'titulo:\s*(.+)', contenido)
            asig_match = re.search(r'asignatura:\s*(.+)', contenido)
            dif_match = re.search(r'dificultad:\s*(.+)', contenido)
            notas_hoy.append({
                "titulo": titulo_match.group(1).strip() if titulo_match else archivo.stem,
                "asignatura": asig_match.group(1).strip() if asig_match else "Desconocida",
                "dificultad": dif_match.group(1).strip() if dif_match else "",
                "fecha_revision": str(fecha)
            })

    return sorted(notas_hoy, key=lambda x: x["dificultad"], reverse=True)


def generar_plan_diario() -> str:
    notas = obtener_notas_para_hoy()

    if not notas:
        return "✅ No hay notas pendientes de repaso hoy."

    lista = "\n".join([
        f"- [{n['asignatura']}] {n['titulo']} {n['dificultad']}"
        for n in notas[:15]
    ])

    prompt = f"""Eres un tutor de Data Science.
Tengo estas notas pendientes de repasar hoy ({len(notas)} en total):

{lista}

Genera un plan de estudio para hoy (máx. 2 horas) con:
1. Orden de repaso recomendado (más difícil primero, alternando asignaturas)
2. Tiempo estimado por nota
3. Técnica recomendada: active recall / flashcards / ejercicio práctico"""

    return llm.invoke(prompt).content
```

### 8.2 Agente síntesis semanal

Crea `src/agentes/sintesis.py`:

```python
"""
Corre cada domingo. Usa NetworkX para analizar el estado
del grafo y detectar gaps de conocimiento.
"""
from langchain_anthropic import ChatAnthropic
from src.grafo import cargar_grafo_obsidian, notas_huerfanas, notas_por_asignatura

llm = ChatAnthropic(model="claude-sonnet-4-20250514", max_tokens=3000)
ASIGNATURAS = ["Algoritmos", "Arquitectura", "Infraestructura-Nube", "Fundamentos-DS"]

def generar_sintesis_semanal() -> str:
    G = cargar_grafo_obsidian()

    resumen_lineas = []
    for asig in ASIGNATURAS:
        notas = notas_por_asignatura(G, asig)
        total_conexiones = sum(len(n["conexiones"]) for n in notas)
        resumen_lineas.append(
            f"- {asig}: {len(notas)} notas, {total_conexiones} conexiones"
        )

    huerfanas = notas_huerfanas(G)
    resumen_lineas.append(f"\nNotas sin conexiones (gaps): {len(huerfanas)}")
    if huerfanas[:5]:
        resumen_lineas.append(f"Ejemplos: {', '.join(huerfanas[:5])}")

    prompt = f"""Analiza este estado de mi segundo cerebro:

{"".join(resumen_lineas)}

Genera:
1. Progreso por asignatura (semáforo 🔴🟡🟢)
2. Top 3 notas mejor conectadas del grafo
3. Gaps detectados — notas sin conexiones que deberían tenerlas
4. Recomendación de qué crear esta semana
5. Una conexión interdisciplinar interesante que detectes"""

    return llm.invoke(prompt).content
```

---

## 9. Fase 5 — Automatización y triggers

### 9.1 CLI para uso manual

Crea `main.py`:

```python
import argparse
from dotenv import load_dotenv
from src.graph import app
from src.agentes.revisor import generar_plan_diario
from src.agentes.sintesis import generar_sintesis_semanal

load_dotenv()

def procesar_nota(raw_input: str, asignatura: str, tipo: str = "tecnica"):
    estado_inicial = {
        "raw_input": raw_input,
        "asignatura": asignatura,
        "tipo_nota": tipo,
        "nota_md": None,
        "titulo": None,
        "calidad_ok": False,
        "intentos": 0,
        "wikilinks": [],
        "flashcards": [],
        "dificultad": None,
        "proxima_revision": None,
        "errores": []
    }

    print(f"🚀 Procesando nota para {asignatura}...")
    resultado = app.invoke(estado_inicial)

    if resultado["errores"]:
        print(f"⚠️  Errores: {resultado['errores']}")
    else:
        print(f"✅ Nota creada: {resultado['titulo']}")
        print(f"🔗 Conexiones encontradas: {len(resultado['wikilinks'])}")
        print(f"🃏 Flashcards generadas: {len(resultado['flashcards'])}")

    return resultado


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Segundo Cerebro — Agentes")
    parser.add_argument("--modo", choices=["nota", "revisar", "sintesis"], required=True)
    parser.add_argument("--input", type=str, help="Texto de la nota a procesar")
    parser.add_argument("--asignatura", type=str, default="Algoritmos",
                        choices=["Algoritmos", "Arquitectura", "Infraestructura-Nube", "Fundamentos-DS"])
    parser.add_argument("--tipo", type=str, default="tecnica",
                        choices=["tecnica", "filosofia", "idea", "proyecto"])
    args = parser.parse_args()

    if args.modo == "nota":
        procesar_nota(args.input, args.asignatura, args.tipo)
    elif args.modo == "revisar":
        print(generar_plan_diario())
    elif args.modo == "sintesis":
        print(generar_sintesis_semanal())
```

### 9.2 Ejemplos de uso

```bash
# Procesar una nota nueva
python main.py --modo nota \
  --input "El algoritmo de Dijkstra encuentra el camino más corto en grafos ponderados usando una cola de prioridad" \
  --asignatura Algoritmos

# Ver plan de repaso del día
python main.py --modo revisar

# Síntesis semanal (corre los domingos)
python main.py --modo sintesis
```

### 9.3 Watcher automático (opcional)

Crea `src/watcher.py` — monitorea el vault y dispara el pipeline cuando detecta una nota con el tag `#procesar`:

```python
import time
import os
import re
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.graph import app
from dotenv import load_dotenv

load_dotenv()
VAULT_PATH = os.getenv("OBSIDIAN_VAULT_PATH")

class NuevaNota(FileSystemEventHandler):
    def on_created(self, event):
        if not event.src_path.endswith(".md"):
            return

        time.sleep(1)  # espera a que Obsidian termine de escribir
        ruta = Path(event.src_path)
        contenido = ruta.read_text(encoding="utf-8")

        if "#procesar" not in contenido:
            return

        print(f"🔍 Nueva nota detectada: {ruta.name}")

        # Extraer asignatura del frontmatter
        asig_match = re.search(r'asignatura:\s*(.+)', contenido)
        asignatura = asig_match.group(1).strip() if asig_match else "Algoritmos"

        # Lanzar el grafo
        estado = {
            "raw_input": contenido,
            "asignatura": asignatura,
            "tipo_nota": "tecnica",
            "nota_md": None, "titulo": None,
            "calidad_ok": False, "intentos": 0,
            "wikilinks": [], "flashcards": [],
            "dificultad": None, "proxima_revision": None,
            "errores": []
        }
        app.invoke(estado)

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(NuevaNota(), VAULT_PATH, recursive=True)
    observer.start()
    print(f"👁️  Monitoreando {VAULT_PATH}...")
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

---

## 10. Estructura de archivos del proyecto

```
segundo-cerebro-agentes/
│
├── .env                          # variables de entorno (no subir a git)
├── .gitignore
├── requirements.txt              # incluye obsidian-rag-system como dep local
├── main.py                       # CLI principal
│
├── src/
│   ├── state.py                  # BrainState — estado compartido del grafo
│   ├── graph.py                  # construcción del StateGraph LangGraph
│   ├── grafo.py                  # NetworkX — grafo de conocimiento del vault
│   │
│   ├── nodes/
│   │   ├── capturar.py           # Nodo 1: genera nota atómica con LLM
│   │   ├── evaluar.py            # Nodo 2: evalúa calidad + edge condicional
│   │   ├── conectar.py           # Nodo 3: búsqueda semántica via RAG existente
│   │   ├── flashcards.py         # Nodo 4: genera flashcards formato Obsidian
│   │   └── guardar.py            # Nodo 5: escribe .md en vault
│   │
│   └── agentes/
│       ├── revisor.py            # Plan de repaso diario
│       └── sintesis.py           # Síntesis semanal con análisis NetworkX
│
├── src/
│   └── watcher.py                # Monitor automático del vault
│
└── tests/
    └── test_pipeline.py          # Tests básicos del flujo
```

Y los dos repos en contexto:

```
/home/gabriel/Documents/
│
├── obsidian-rag-system/          ← estable, no tocar, Claude Desktop lo usa
│   └── src/rag_chain.py          ← ObsidianRAGSystem (importado por agentes)
│
└── segundo-cerebro-agentes/      ← este repo, experimental
    └── requirements.txt          ← -e ../obsidian-rag-system
```

---

## 11. Referencia rápida de comandos

```bash
# Setup inicial (una sola vez)
cd /home/gabriel/Documents
git clone ... segundo-cerebro-agentes   # o mkdir + git init
cd segundo-cerebro-agentes
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Verificar integración con RAG
python -c "from src.rag_chain import ObsidianRAGSystem; print('✅ OK')"

# Uso diario
source .venv/bin/activate

python main.py --modo nota \
  --input "..." \
  --asignatura Algoritmos

python main.py --modo revisar      # plan del día

python main.py --modo sintesis     # resumen semanal (domingos)

# Watcher en segundo plano
python src/watcher.py &

# Consultar el grafo de conocimiento
python -c "
from src.grafo import cargar_grafo_obsidian, notas_huerfanas
G = cargar_grafo_obsidian()
print(f'Nodos: {G.number_of_nodes()}')
print(f'Conexiones: {G.number_of_edges()}')
print(f'Notas sin conectar: {len(notas_huerfanas(G))}')
"
```

---

## Roadmap de implementación sugerido

| Semana | Objetivo | Criterio de éxito |
|---|---|---|
| 1 | Fase 0 — entorno y verificación integración RAG | `python -c "from src.rag_chain import ..."` funciona |
| 2 | Fase 1 — pipeline LangGraph con `capturar` + `evaluar` | Nota generada en consola |
| 3 | Fase 2 — `conectar` + `flashcards` + `guardar` | Nota completa guardada en vault |
| 4 | Fase 3 — NetworkX cargando el grafo del vault | Consultas de conexiones funcionando |
| 5 | Fase 4 — agente revisor diario | Plan de repaso generado cada mañana |
| 6 | Fase 4 — agente síntesis semanal | Reporte semanal con gaps detectados |
| 7+ | Fase 5 — watcher automático | Pipeline disparado al guardar en Obsidian |

> 💡 Cada fase es independiente. Puedes usar el pipeline desde la Fase 2 sin necesitar NetworkX ni los agentes. Añade capas a medida que terminas los cursos de LangGraph y Knowledge Graph.

---

*v1 — Marzo 2026 (con Neo4j)*  
*v2 — Marzo 2026 — eliminado Neo4j, añadido NetworkX, arquitectura dos repos*
