---
area: Algoritmos
cards-deck: Algoritmos
created: 2025-12-27
modified: 2025-12-27
nivel-comprension: 💡
origen: PDF Tema5 (Visual)
proxima-revision: '2026-05-04'
status: 🌱
tiempo-estimado: 15m
tipo_nota: tecnica
ultima-revision: '2026-04-27'
veces-revisado: 1
tiempo-repaso: ""
---

# Resolución de Problemas 🎨

> [!abstract] Objetivo Visual
> Entender *cómo se mueve* el algoritmo. No memorices código, visualiza el flujo.



## 1. Recursividad vs Iteración 🔄

### Visualizando el Stack (Pila de Llamadas)

Cuando usas recursividad, el ordenador apila tareas pendientes. Esto consume memoria.

```mermaid
graph TD
    subgraph Iterativo [Iterativo: bucle while/for]
        I[Inicio] --> C{¿Condición?}
        C -- Sí --> A[Acción]
        A --> C
        C -- No --> F[Fin]
    end

    subgraph Recursivo [Recursivo: Llamada a sí mismo]
        R1["Función(5)"] --> R2["Función(4)"]
        R2 --> R3["Función(3)"]
        R3 --> R4[...]
        R4 -.-> RET[Retorno Base]
        RET -.-> R3
        R3 -.-> R2
        R2 -.-> R1
    end
```



## 2. Grafos: Los 4 Fantásticos 🕸️

Visualiza para qué sirve cada uno en el mapa de una ciudad.

```mermaid
graph LR
    A((Casa)) -- 5 min --> B((Metro))
    B -- 10 min --> C((Trabajo))
    A -- 20 min --> C
    
    style A fill:#f9f,stroke:#333
    style C fill:#9f9,stroke:#333

    dijkstra[Dijkstra: Busca el camino MÁS CORTO considerando el tiempo]
    bfs[BFS: Busca el camino con MENOS PARADAS]
```

### Tabla Visual de Algoritmos

| Algoritmo | Mentalidad | Visualización |
| :--- | :--- | :--- |
| **Dijkstra** | ⚡ **El Prisa-Matas** | Expande ondas desde el origen. Elige siempre el nodo más cercano. |
| **Floyd-Warshall** | 🧠 **El Omnisciente** | Calcula una **Matriz Gigante**. Sabe la distancia de todos a todos. |
| **BFS** (Amplitud) | 🌊 **La Mancha de Aceite** | Se expande capa por capa (Vecinos -> Vecinos de vecinos). |
| **Kruskal** | 💰 **El Tacaño** | Ordena cables por precio (baratos primero). Conecta islas hasta tener todo unido. |



## 3. Backtracking (Vuelta Atrás) 🔙

Imagina un laberinto. Pruebas un camino, te chocas, y vuelves al último cruce.

```mermaid
graph TD
    A[Inicio] --> B{¿Opción 1?}
    B -- Camino A --> C[❌ Pared]
    C -.->|Backtrack| B
    B -- Camino B --> D[✅ Salida]
    
    style C fill:#faa
    style D fill:#afa
```



## 4. Programación Dinámica 💾

### El Árbol de Fibonacci (El Problema)

Sin Dynamic Programming, calculas `fib(2)` millones de veces.

```mermaid
graph TD
    F5[fib 5] --> F4a[fib 4]
    F5 --> F3a[fib 3]
    F4a --> F3b[fib 3]
    F4a --> F2a[fib 2]
    F3a --> F2b[fib 2]
    F3a --> F1[fib 1]
    
    style F3b fill:#ff9,stroke:#f00,stroke-width:2px
    style F3a fill:#ff9,stroke:#f00,stroke-width:2px
    note[¡Cálculo Repetido!]
```

### La Solución (Memorización)

Guardamos el resultado la primera vez. La segunda vez es instantáneo.



## 🎴 Flashcards Visuales

¿Qué forma tiene la expansión de un BFS?::Como ondas en el agua (círculos concéntricos).

¿Qué estructura visualiza mejor la Recursividad?::Una Pila (Stack) de platos apilados.

¿Qué hace Kruskal visualmente?::Une "islas" de nodos usando las aristas más baratas posibles.


