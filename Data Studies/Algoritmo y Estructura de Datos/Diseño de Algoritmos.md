---
cards-deck: Algoritmos
created: 2025-12-27
modified: 2026-01-14
status: 🌱 Semilla
tipo_nota: tecnica
asignatura: Algoritmos
nivel-comprension: 🤔
proxima-revision: 2026-01-17
tiempo-estimado: 15m
origen: PDF Tema6 (Visual)
ultima-revision: 2026-01-14
veces-revisado: 1
---

# Diseño de Algoritmos  🎨

> [!abstract] Objetivo Visual
> Asociar cada familia de algoritmos con una **forma** o **movimiento**.

---

## 1. Las 3 Estrategias Maestras 🧠

### A. Divide y Vencerás (Divide & Conquer) ⚔️

**Forma**: Un Árbol Invertido.
Rompes el problema hasta que es trivial, luego reconstruyes.

  

```mermaid

graph TD

Prob["Problema Grande [8,3,1,7]"] --> D1[División]

D1 --> Izq["[8,3]"]

D1 --> Der["[1,7]"]

Izq --> I1[8] & I2[3]

Der --> D2[1] & D3[7]

I1 & I2 --> Comb1["Ordenar: 3,8"]

D2 & D3 --> Comb2["Ordenar: 1,7"]

Comb1 & Comb2 --> Fin["Mezclar: 1,3,7,8"]

style Fin fill:#afa,stroke:#333

```

### B. Algoritmos Voraces (Greedy) 🍔

**Forma**: Una línea recta (sin mirar atrás).
Tomas la moneda más grande posible en cada paso.

```mermaid
graph LR
    Goal[Objetivo: 7€]
    A[Tengo Monedas: 5, 2, 1] --> B{¿Cabe 5?}
    B -- Sí --> C[Tomo 5]
    C --> D{¿Cabe 2?}
    D -- Sí --> E[Tomo 2]
    E --> Fin[Total: 7€ ✅]
    
    B -- No --> F[...]
```

### C. Programación Dinámica 💾

**Forma**: Una Tabla / Rejilla.
Vas rellenando huecos basándote en los huecos anteriores.

---

## 2. Mapa Visual de Casos de Uso (⚠️ Examen)

Asocia el icono con el algoritmo.

```mermaid
graph TD
    subgraph A[Mundo Real]
        Inv[📦 Inventario / Stocks] --- BS[Bubble Sort]
        Cat[📑 Catálogos] --- IS[Insertion Sort]
        Med[🏥 Historial Médico] --- MS[Merge Sort]
        Log[🚚 Logística / Amazon] --- QS[Quick Sort]
    end
    
    subgraph B[Grafos y Redes]
        GPS[📍 GPS / Uber] --- Dijk[Dijkstra]
        Sub[🚇 Plano Metro] --- FW[Floyd-Warshall]
        Emer[🚨 Evacuación] --- BFS[BFS]
        Tel[📡 Antenas 5G] --- Krusk[Kruskal]
        Moch[🎒 Trekking] --- Knap[Mochila]
    end
    
    style GPS fill:#f9f
    style Dijk fill:#f9f
    style Tel fill:#9ff
    style Krusk fill:#9ff
```

---

## 🎴 Flashcards Visuales

¿Qué forma tiene la estrategia "Divide y Vencerás"?::Un árbol que se ramifica y luego se une (como Merge Sort). #card 

¿Qué visualización representa mejor a los algoritmos Voraces?::Comerse la pieza más grande disponible en cada paso (Pacman). #card 

¿Si ves un mapa de Metro (todos conectados con todos), qué algoritmo es?::Floyd-Warshall. #card 

¿Si ves antenas que hay que conectar con el mínimo cable posible?::Kruskal. #card 

---

## 🔗 Referencias

- [[Resolución de Problemas]]
- [[Big O y Análisis de Complejidad]]


---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Tarea para aclarar una duda de concepto. Usa #mejora-concepto
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia
