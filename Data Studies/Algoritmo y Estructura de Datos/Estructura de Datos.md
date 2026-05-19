---
created: 2025-11-26
modified: 2025-12-10
status: 🌿 Creciendo
tipo_nota: tecnica
area: Algoritmos
cards-deck: Algoritmos::Estructura-de-Datos
nivel-comprension: 💡
proxima-revision: 2025-12-24
ultima-revision: 2025-12-10
veces-revisado: 4
estado: 🟢 Al día
tiempo-repaso: 15min
tiempo-estimado: 30m
---
## 🎯 Tabla Comparativa Rápida

| Estructura | Acceso | Búsqueda | Inserción | Eliminación | Espacio | Visual |
|-----------|--------|----------|-----------|-------------|---------|--------|
| **Array** | O(1) | O(n) | O(n) | O(n) | O(n) | `[1][2][3][4][5]` |
| **Lista Enlazada** | O(n) | O(n) | O(1)* | O(1)* | O(n) | `[1]→[2]→[3]→[4]→[5]→null` |
| **Pila (Stack)** | O(n) | O(n) | O(1) | O(1) | O(n) | `[5]↑[4]↑[3]↑[2]↑[1]` |
| **Cola (Queue)** | O(n) | O(n) | O(1) | O(1) | O(n) | `[1]→[2]→[3]→[4]→[5]→` |
| **Hash Table** | O(1)† | O(1)† | O(1)† | O(1)† | O(n) | `{"key": "value"}` |
| **Heap (Min)** | O(n) | O(n) | O(log n) | O(log n) | O(n) | `Árbol semi-ordenado` |
| **Árbol Binario (BST)** | O(log n)‡ | O(log n)‡ | O(log n)‡ | O(log n)‡ | O(n) | `Árbol ordenado` |
| **Grafo** | - | O(V+E) | O(1) | O(1) | O(V+E) | `Red de nodos conectados` |

*Con referencia al nodo | †Promedio, peor caso O(n) | ‡Si está balanceado

---

## 📦 1. LISTA ENLAZADA (Linked List)

### Estructura Visual:
```
HEAD → [dato|next] → [dato|next] → [dato|next] → [dato|next] → NULL
       ↑             ↑             ↑             ↑
       Nodo 1        Nodo 2        Nodo 3        Nodo 4
```

### Operaciones Visualizadas:

**Insertar al inicio:**
```
ANTES:  HEAD → [2] → [3] → [4] → NULL

DESPUÉS: HEAD → [1] → [2] → [3] → [4] → NULL
                ↑_____ nuevo nodo
```

**Eliminar del medio:**
```
ANTES:  HEAD → [1] → [2] → [3] → [4] → NULL

DESPUÉS: HEAD → [1] → [2] ----→ [4] → NULL
                       ↑           ↑
                       Se elimina [3]
```

### 🎨 Características Clave:
- ✅ Tamaño dinámico
- ✅ Inserción/eliminación eficiente (O(1) con referencia)
- ❌ Acceso secuencial lento (O(n))
- ❌ Más memoria (punteros extra)

---

## 📚 2. PILA (Stack) - LIFO

### Estructura Visual:
```
     ┌───┐
     │ 5 │ ← TOP (último en entrar, primero en salir)
     ├───┤
     │ 4 │
     ├───┤
     │ 3 │
     ├───┤
     │ 2 │
     ├───┤
     │ 1 │ ← BOTTOM
     └───┘
```

### Operaciones:
```
push(6)              pop()
     ┌───┐               ┌───┐
     │ 6 │ ← NEW TOP     │ X │ (eliminado)
     ├───┤               ├───┤
     │ 5 │               │ 5 │ ← NEW TOP
     ├───┤               ├───┤
     │ 4 │               │ 4 │
     └───┘               └───┘
```

### 🎨 Usos Comunes:
- 🔙 Botón "Atrás" del navegador
- ↩️ Undo/Redo en editores
- 🔄 Recursión (call stack)
- 🌳 DFS en grafos

---

## 🚶 3. COLA (Queue) - FIFO

### Estructura Visual:
```
FRONT                                    REAR
  ↓                                        ↓
┌───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │
└───┴───┴───┴───┴───┘
  ↑                   ↑
Dequeue()         Enqueue()
(sacar)           (añadir)
```

### Operaciones:
```
enqueue(6)          dequeue()
┌───┬───┬───┬───┬───┬───┐       ┌───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │  →    │ 2 │ 3 │ 4 │ 5 │ 6 │
└───┴───┴───┴───┴───┴───┘       └───┴───┴───┴───┴───┘
                    ↑            ↑
                  añadido      eliminado
```

### 🎨 Usos Comunes:
- 🖨️ Cola de impresión
- 📞 Sistema de atención al cliente
- 🌐 BFS en grafos
- ⚙️ Procesamiento de tareas (task queue)

---

## #️⃣ 4. TABLA HASH (Hash Table) [[Tablas Hash]]

### Estructura Visual:
```
hash("manzana") % 10 = 3

Array Interno:
índice  │ Contenido
────────┼─────────────────────
  0     │ → ["pera", 🍐]
  1     │ → NULL
  2     │ → ["uva", 🍇]
  3     │ → ["manzana", 🍎] → ["naranja", 🍊]  ← Colisión (chaining)
  4     │ → NULL
  5     │ → ["kiwi", 🥝]
  ...   │
  9     │ → NULL
```

### Funcionamiento:
```
1. Entrada: clave = "gato"

2. Hash: hash("gato") = 42834729 → 42834729 % 10 = 9

3. Almacenar: tabla[9] = "gato"

4. Buscar: O(1) - directo al índice 9
```

### 🎨 Características:
- ⚡ Búsqueda O(1) promedio
- 🔑 Clave única
- ⚠️ Colisiones posibles
- 💾 Usa más memoria

### Manejo de Colisiones:

**Chaining (encadenamiento):**
```
tabla[3] → [("manzana", 🍎)] → [("naranja", 🍊)] → NULL
```

**Open Addressing (direccionamiento abierto):**
```
Si tabla[3] ocupado → probar tabla[4], tabla[5], etc.
```

---

## 🏔️ 5. HEAP (Montículo)

### Min Heap Visual:
```
           1
         /   \
        3     2
       / \   / \
      7   8 4   6
     / \
    9  10

Array: [1, 3, 2, 7, 8, 4, 6, 9, 10]
       [0, 1, 2, 3, 4, 5, 6, 7, 8]
```

### Relaciones Padre-Hijo:
```
Para nodo en índice i:
- Padre:       (i-1) // 2
- Hijo izq:    2*i + 1
- Hijo der:    2*i + 2

Ejemplo con i=1 (valor 3):
- Padre: (1-1)//2 = 0 → valor 1 ✓
- Hijo izq: 2*1+1 = 3 → valor 7 ✓
- Hijo der: 2*1+2 = 4 → valor 8 ✓
```

### Inserción Visual (push):
```
1. Insertar 0 al final:
           1
         /   \
        3     2
       / \   / \
      7   8 4   6
     / \ /
    9 10 0

2. "Bubble up" (flotar hacia arriba):
           1                 0
         /   \             /   \
        3     2    →      3     1
       / \   / \         / \   / \
      7   8 0   6       7   8 2   6
     / \                / \
    9  10              9  10
```

### 🎨 Usos:
- 📊 Priority Queue (cola de prioridad)
- 🗺️ Algoritmo de Dijkstra
- 🔝 Top K elementos
- 📈 HeapSort

---

## 🌳 6. ÁRBOL BINARIO DE BÚSQUEDA (BST)

### Estructura Visual:
```
         8
       /   \
      3     10
     / \      \
    1   6      14
       / \    /
      4   7  13

Propiedad: izquierda < nodo < derecha
```

### Recorridos:

**Inorden (Izq-Raíz-Der):**
```
         8
       /   \
     [3]    10
     / \      \
    1   6      14

Resultado: 1 → 3 → 4 → 6 → 7 → 8 → 10 → 13 → 14
          (ordenado!)
```

**Preorden (Raíz-Izq-Der):**
```
Resultado: 8 → 3 → 1 → 6 → 4 → 7 → 10 → 14 → 13
```

**Postorden (Izq-Der-Raíz):**
```
Resultado: 1 → 4 → 7 → 6 → 3 → 13 → 14 → 10 → 8
```

### Búsqueda Visual:
```
Buscar 6:

         [8]  (6 < 8, ir izquierda)
       /   \
     [3]    10  (6 > 3, ir derecha)
     / \      \
    1  [6] ✓   14

Pasos: 3 (log n con árbol balanceado)
```

### ⚠️ Árbol Desbalanceado:
```
         8
          \
          10
            \
            14
              \
              20

Degrada a O(n) - ¡como lista enlazada!
```

---

## 🕸️ 7. GRAFO

### Representaciones:

**Grafo Visual:**
```
    A ------- B
    |       / |
    |     /   |
    |   /     |
    | /       |
    C ------- D
```

**Matriz de Adyacencia:**
```
    A  B  C  D
A [ 0  1  1  0 ]
B [ 1  0  1  1 ]
C [ 1  1  0  1 ]
D [ 0  1  1  0 ]

Espacio: O(V²)
```

**Lista de Adyacencia:**
```
A → [B, C]
B → [A, C, D]
C → [A, B, D]
D → [B, C]

Espacio: O(V + E)
```

### BFS vs DFS Visual:

**BFS (Breadth-First Search) - por niveles:**
```
       A          Nivel 0
      / \
     B   C        Nivel 1
    / \   \
   D   E   F      Nivel 2

Orden: A → B → C → D → E → F
Usa: Cola (Queue)
```

**DFS (Depth-First Search) - profundidad primero:**
```
       A
      / \
     B   C
    / \   \
   D   E   F

Orden: A → B → D → E → C → F
Usa: Pila (Stack) o Recursión
```

### Dijkstra Visual (camino más corto):
```
      (A)---2---(B)
       |         |
       1         3
       |         |
      (C)---1---(D)

Camino de A a D:
A → C → D = 1 + 1 = 2 ✓ (más corto)
A → B → D = 2 + 3 = 5
```

---

## 🎯 Cuándo Usar Cada Estructura

```
┌─────────────────────────────────────────────────────────┐
│ NECESITO...                  → USA...                   │
├─────────────────────────────────────────────────────────┤
│ Acceso rápido por índice     → Array                    │
│ Inserciones/eliminaciones     → Lista Enlazada          │
│ LIFO (último en salir)        → Pila (Stack)            │
│ FIFO (primero en salir)       → Cola (Queue)            │
│ Búsqueda O(1) por clave       → Hash Table              │
│ Máximo/mínimo rápido          → Heap                    │
│ Búsqueda ordenada O(log n)    → Árbol Binario (BST)     │
│ Relaciones entre elementos    → Grafo                   │
│ Procesamiento por prioridad   → Priority Queue (Heap)   │
└─────────────────────────────────────────────────────────┘
```

---

## 💾 Comparación de Memoria

```
Array vs Lista Enlazada (5 elementos):

Array [100 bytes]:
┌────┬────┬────┬────┬────┐
│ 1  │ 2  │ 3  │ 4  │ 5  │  = 5 × 4 bytes = 20 bytes
└────┴────┴────┴────┴────┘

Lista Enlazada [180 bytes]:
[1|ptr]→[2|ptr]→[3|ptr]→[4|ptr]→[5|ptr]→NULL
  ↑        ↑        ↑        ↑        ↑
8 bytes  8 bytes  8 bytes  8 bytes  8 bytes  = 40 bytes

Array: contiguo en memoria ✓ cache-friendly
Lista: disperso en memoria ✗ cache misses
```

---

## 🎮 Ejercicios Visuales de Práctica

### Ejercicio 1: Pila
```
Ejecuta estas operaciones:
push(1), push(2), push(3), pop(), push(4), pop(), pop()

Estado final: [  ?  ]
```

### Ejercicio 2: Cola
```
Ejecuta estas operaciones:
enqueue(A), enqueue(B), dequeue(), enqueue(C), dequeue()

Estado final: [  ?  ]
```

### Ejercicio 3: Heap
```
Inserta estos valores en un Min Heap:
5, 3, 8, 1, 9, 2

Dibuja el árbol resultante
```

### Ejercicio 4: BST
```
Inserta en orden: 8, 3, 10, 1, 6, 14, 4, 7, 13

¿Cuál es el recorrido inorden?
```

---

## 🧠 Mnemotécnicos

**Heap - Relaciones:**
```
"Padre Italiano Doble"
Padre:    (i-1)/2
Izq:      2i+1
Der:      2i+2
```

**Complejidades comunes:**
```
O(1)      → Hash lookup (instantáneo)
O(log n)  → Divide y vencerás (búsqueda binaria, heap)
O(n)      → Recorrer todo (búsqueda lineal)
O(n log n)→ Ordenar eficientemente (mergesort, heapsort)
O(n²)     → Bucles anidados (bubble sort)
```

**Grafos - BFS vs DFS:**
```
BFS = "Breadth" = Ancho = Cola = Niveles
DFS = "Depth" = Profundo = Pila = Ramas
```

---

## 📝 Resumen en 1 Página

```
┌─────────────┬──────────┬──────────┬──────────┬──────────┐
│ Estructura  │ Buscar   │ Insertar │ Eliminar │ Uso      │
├─────────────┼──────────┼──────────┼──────────┼──────────┤
│ Array       │ O(n)     │ O(n)     │ O(n)     │ Índice   │
│ Lista       │ O(n)     │ O(1)*    │ O(1)*    │ Dinámico │
│ Pila        │ O(n)     │ O(1)     │ O(1)     │ LIFO     │
│ Cola        │ O(n)     │ O(1)     │ O(1)     │ FIFO     │
│ Hash        │ O(1)     │ O(1)     │ O(1)     │ Clave    │
│ Heap        │ O(n)     │ O(log n) │ O(log n) │ Min/Max  │
│ BST         │ O(log n) │ O(log n) │ O(log n) │ Ordenado │
│ Grafo       │ O(V+E)   │ O(1)     │ O(1)     │ Redes    │
└─────────────┴──────────┴──────────┴──────────┴──────────┘
```

---

## 🔗 Conexiones con tus Proyectos

**Sistema de Recomendación de Coworkings:**
```
Grafo → Coworkings = vértices, similaridad = aristas
Hash → Cache de resultados previos
Heap → Top-K recomendaciones
Set → Verificar coworkings únicos
```

**App RPG de Objetivos:**
```
Pila → Undo/redo de acciones
Priority Queue → Procesar objetivos por urgencia
Árbol → Dependencias entre objetivos
```
---

---
cards-deck: Algoritmos::Estructura-de-Datos
#card 
---

## 🎴 Flashcards

¿Cuál es la diferencia en complejidad de acceso entre un Array y una Lista Enlazada?::Array es O(1) (acceso directo por índice), Lista es O(n) (acceso secuencial). #card

¿Qué regla define el orden de salida en una Pila (Stack) y en una Cola (Queue)?::Pila es LIFO (Último en entrar, Primero en salir), Cola es FIFO (Primero en entrar, Primero en salir). #card

En una Tabla Hash, ¿qué complejidad temporal tiene la búsqueda en el caso promedio?::O(1) (Tiempo constante). #card 

¿Qué es una colisión en una Tabla Hash y cómo se soluciona con "chaining"?::Ocurre cuando dos claves dan el mismo hash. Con chaining, se crea una lista enlazada en esa posición para guardar ambos valores. #card

¿Qué propiedad fundamental cumple un Árbol Binario de Búsqueda (BST)?::Para cualquier nodo, los valores a su IZQUIERDA son menores y los valores a su DERECHA son mayores. #card 

Visualmente, ¿cuál es la diferencia entre BFS y DFS al recorrer un grafo?::BFS explora por niveles/ancho (usa una Cola), DFS explora por profundidad/ramas (usa una Pila o recursión). #card

Si estás programando la función "Deshacer" (Undo) de un editor, ¿qué estructura de datos es la ideal?::Una Pila (Stack). #card

Para encontrar la ruta más corta en un mapa sin pesos (laberinto), ¿qué algoritmo utilizas?::BFS (Búsqueda en Anchura). #card

¿Por qué los Arrays son más eficientes para la caché de la CPU que las Listas Enlazadas?::Porque ocupan memoria contigua, permitiendo cargar bloques enteros en caché. Las listas están dispersas. #card

¿Cuál es la complejidad temporal de insertar un elemento al inicio de un Array?::O(n), porque hay que desplazar todos los elementos restantes. #card 

---

## ✅ Checklist de Memorización

- [x] Puedo dibujar cada estructura de memoria ✅ 2025-12-10
- [x] Conozco la complejidad de cada operación ✅ 2025-12-10
- [x] Sé cuándo usar cada estructura ✅ 2025-12-10
- [x] Puedo implementar las básicas (lista, pila, cola) ✅ 2025-12-10
- [x] Entiendo las relaciones padre-hijo en heap ✅ 2025-12-27
- [x] Puedo hacer recorridos de árbol sin ver la respuesta ✅ 2025-12-27
- [x] Distingo BFS de DFS visualmente ✅ 2025-12-10

---

**Última actualización:** 2025-11-26
**Tiempo de repaso estimado:** 20-30 minutos
**Próxima revisión:** En 3 días


---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Hacer flashcards🏁 ➕ 2025-12-01  #mejora-concepto
- [x] Hacer otro cuestionario #mejora-practica ➕ 2025-12-01 ✅ 2025-12-10
