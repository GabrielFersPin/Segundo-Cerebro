---
cards-deck: Algoritmos
created: 2024-11-27
modified: 2025-12-10
status: 🌿 Creciendo
tipo_nota: tecnica
asignatura: Algoritmos
procesamiento: COMPLETO
prioridad: EXAMEN-LEJANO
fecha-examen: 2025-02-15
proxima-revision: 2025-12-24
complejidad: ⭐⭐⭐⭐
tiempo-estimado: 2h
fuente: UD3 - Algoritmos y Estructuras de Datos UAX
nivel-comprension: 💡
ultima-revision: 2025-12-10
veces-revisado: 2
---

# Algoritmos y Estructuras de Búsqueda

> [!abstract] Objetivo
> Dominar algoritmos de búsqueda (lineal, binaria) y estructuras de datos especializadas (BST, árboles balanceados, grafos). Entender cuándo usar cada una.

---

## 📊 Comparativa Rápida

| Método | Complejidad | Requisito | Mejor Para |
|--------|-------------|-----------|------------|
| Búsqueda Lineal | O(n) | Ninguno | Listas pequeñas/desordenadas |
| Búsqueda Binaria | O(log n) | Lista ordenada | Listas grandes ordenadas |
| BST | O(log n) avg, O(n) worst | Árbol balanceado | Inserciones/búsquedas dinámicas |
| AVL/Rojo-Negro | O(log n) garantizado | Autobalanceo | Garantía de rendimiento |
| Hash Table | O(1) avg | Función hash | Búsquedas exactas rápidas |
| DFS/BFS | O(V + E) | Grafo | Exploración de relaciones |

---

## 1️⃣ Búsqueda Lineal (Secuencial)

### 🔍 Concepto

Examina cada elemento de la lista secuencialmente hasta encontrar el objetivo o llegar al final.

**Analogía**: Buscar un libro en una pila desordenada mirando uno por uno.

### ⚙️ Funcionamiento

1. Comienza desde el primer elemento
2. Compara con el valor buscado
3. Si coincide → devuelve índice
4. Si no coincide → pasa al siguiente
5. Si llega al final sin encontrar → devuelve -1

### 💻 Implementación Python
```python
def busqueda_lineal(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1
```

### ✅ Ventajas

- Muy simple de implementar
- Funciona con **listas desordenadas**
- No requiere preprocesamiento
- Funciona con cualquier tipo de dato comparable

### ❌ Desventajas

- **Muy ineficiente** para listas grandes: O(n)
- Examina en promedio n/2 elementos

### 🎯 Casos de Uso

- Listas pequeñas (<100 elementos)
- Listas desordenadas donde ordenar sería más costoso
- Búsquedas infrecuentes
- Cuando la simplicidad es prioritaria

---

## 2️⃣ Búsqueda Binaria

### 🔍 Concepto

Divide repetidamente la lista ordenada por la mitad, descartando la mitad donde el objetivo no puede estar.

**Analogía**: Buscar palabra en diccionario abriendo por la mitad.

### ⚙️ Funcionamiento

1. Compara objetivo con elemento central
2. Si es igual → encontrado
3. Si objetivo < central → busca en mitad izquierda
4. Si objetivo > central → busca en mitad derecha
5. Repite hasta encontrar o agotar espacio de búsqueda

### 💻 Implementación Python
```python
def busqueda_binaria(lista, objetivo, izquierda=0, derecha=None):
    if derecha is None:
        derecha = len(lista) - 1
    
    if izquierda > derecha:
        return -1
    
    medio = (izquierda + derecha) // 2
    
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, objetivo, medio+1, derecha)
    else:
        return busqueda_binaria(lista, objetivo, izquierda, medio-1)
```

**Versión iterativa** (más eficiente en memoria):
```python
def busqueda_binaria_iterativa(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1
```

### ✅ Ventajas

- **Muy eficiente**: O(log n)
- Reduce dramáticamente el espacio de búsqueda
- Para n=1,000,000 solo necesita ~20 comparaciones

### ❌ Desventajas

- **Requiere lista ordenada**
- Si la lista cambia frecuentemente, mantenerla ordenada es costoso
- Más complejo que búsqueda lineal

### 🎯 Casos de Uso

- Listas grandes ordenadas
- Bases de datos con índices
- Búsquedas frecuentes en datos estáticos
- Diccionarios, guías telefónicas

---

## 3️⃣ Árbol Binario de Búsqueda (BST)

### 🔍 Concepto

Estructura de árbol donde cada nodo tiene máximo 2 hijos, con la propiedad:
- **Subárbol izquierdo**: valores < nodo
- **Subárbol derecho**: valores > nodo

### 📐 Estructura
```
        50
       /  \
      30   70
     / \   / \
    20 40 60 80
```

### ⚙️ Propiedades

1. Cada nodo tiene 0, 1 o 2 hijos
2. Todos los nodos del subárbol izquierdo < nodo
3. Todos los nodos del subárbol derecho > nodo
4. Ambos subárboles también son BST (propiedad recursiva)

### 💻 Implementación Python
```python
class Nodo:
    def __init__(self, clave):
        self.izquierdo = None
        self.derecho = None
        self.clave = clave

def busqueda_bst(nodo, valor):
    if nodo is None:
        return False  # No encontrado
    
    if nodo.clave == valor:
        return True  # Encontrado
    elif nodo.clave < valor:
        # Buscar en subárbol derecho
        return busqueda_bst(nodo.derecho, valor)
    else:
        # Buscar en subárbol izquierdo
        return busqueda_bst(nodo.izquierdo, valor)
```

### ✅ Ventajas

- Búsqueda, inserción, eliminación en O(log n) promedio
- Mantiene datos ordenados dinámicamente
- Recorridos in-order dan elementos ordenados
- Flexible para inserciones/eliminaciones frecuentes

### ❌ Desventajas

- Puede **degenerarse en lista** (O(n)) si no está balanceado
- Ejemplo: insertar [1,2,3,4,5] crea una cadena lineal
- Requiere más memoria que array (punteros)

### 🎯 Casos de Uso

- Implementar diccionarios/mapas
- Cuando hay inserciones/eliminaciones frecuentes
- Mantener datos ordenados dinámicamente
- Bases de datos (con variantes balanceadas)

---

## 4️⃣ Árboles Balanceados (AVL y Rojo-Negro)

### 🔍 Concepto

BST que **se auto-balancea** mediante rotaciones para garantizar O(log n).

### 🌲 Tipos Principales

#### AVL (Adelson-Velsky y Landis)

**Propiedad**: Diferencia de alturas entre subárboles ≤ 1

**Rotaciones**:
- Simple derecha
- Simple izquierda
- Doble izquierda-derecha
- Doble derecha-izquierda
```
Desbalanceado:        Rotación Derecha:
      30                    20
     /                     /  \
    20          →        10    30
   /
  10
```

#### Rojo-Negro

**Propiedades**:
1. Cada nodo es rojo o negro
2. Raíz es negra
3. Hojas (null) son negras
4. Nodo rojo → hijos negros
5. Todos los caminos raíz→hoja tienen mismo número de nodos negros

### ⚙️ Comparación AVL vs Rojo-Negro

| Característica | AVL | Rojo-Negro |
|----------------|-----|------------|
| Balanceo | Más estricto | Más relajado |
| Búsquedas | Más rápidas | Ligeramente más lentas |
| Inserciones | Más rotaciones | Menos rotaciones |
| Uso típico | Lectura intensiva | Escritura intensiva |

### 💻 Ejemplo Conceptual (AVL)
```python
class NodoAVL:
    def __init__(self, clave):
        self.clave = clave
        self.izquierdo = None
        self.derecho = None
        self.altura = 1

def obtener_altura(nodo):
    if not nodo:
        return 0
    return nodo.altura

def obtener_balance(nodo):
    if not nodo:
        return 0
    return obtener_altura(nodo.izquierdo) - obtener_altura(nodo.derecho)

def rotacion_derecha(y):
    x = y.izquierdo
    T2 = x.derecho
    
    # Rotación
    x.derecho = y
    y.izquierdo = T2
    
    # Actualizar alturas
    y.altura = max(obtener_altura(y.izquierdo), obtener_altura(y.derecho)) + 1
    x.altura = max(obtener_altura(x.izquierdo), obtener_altura(x.derecho)) + 1
    
    return x
```

### ✅ Ventajas

- **Garantizan O(log n)** en todos los casos
- Evitan degeneración del BST
- Ideales para aplicaciones críticas

### ❌ Desventajas

- Más complejos de implementar
- Overhead de memoria (altura/color)
- Más lentos que BST simple en mejor caso

### 🎯 Casos de Uso

- **Bases de datos** (índices B-trees son variantes)
- Sistemas operativos (gestión de memoria)
- Librerías estándar (map/set en C++/Java)
- Cuando necesitas garantías de rendimiento

---

## 5️⃣ Tablas Hash (Hashing)

### 🔍 Concepto

Mapea claves a índices de un array mediante una función hash, permitiendo búsqueda O(1).

### ⚙️ Funcionamiento

1. **Función hash**: convierte clave en índice
   - Ejemplo: `hash("Carlos") = 42`
2. **Almacenamiento**: guarda valor en `array[42]`
3. **Búsqueda**: aplica hash a clave y accede directamente

### 💻 Implementación Simple
```python
class TablaHash:
    def __init__(self, tamaño=100):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]
    
    def _hash(self, clave):
        return hash(clave) % self.tamaño
    
    def insertar(self, clave, valor):
        indice = self._hash(clave)
        # Manejo de colisiones con encadenamiento
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                self.tabla[indice][i] = (clave, valor)
                return
        self.tabla[indice].append((clave, valor))
    
    def buscar(self, clave):
        indice = self._hash(clave)
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
        return None
```

### ✅ Ventajas

- **Búsqueda O(1) promedio** (la más rápida)
- Inserción y eliminación también O(1)
- Ideal para búsquedas exactas

### ❌ Desventajas

- No mantiene orden
- Colisiones pueden degradar a O(n)
- Consume más memoria
- Ineficiente para búsquedas por rango

### 🎯 Casos de Uso

- Diccionarios/mapas (Python dict, Java HashMap)
- Cachés
- Bases de datos (índices hash)
- Deduplicación de datos

---

## 6️⃣ Búsqueda en Grafos (DFS y BFS)

### 🔍 Concepto

Algoritmos para explorar grafos (nodos conectados por aristas).

### 🌐 DFS (Depth-First Search - Profundidad)

**Estrategia**: Explora tan profundo como sea posible antes de retroceder.
```python
def dfs(grafo, nodo_inicial):
    visitados = set()
    recorrido = []
    
    def dfs_recursivo(nodo):
        if nodo not in visitados:
            visitados.add(nodo)
            recorrido.append(nodo)
            for vecino in grafo.get(nodo, []):
                dfs_recursivo(vecino)
    
    dfs_recursivo(nodo_inicial)
    return recorrido
```

**Características**:
- Usa **pila** (recursión o explícita)
- Encuentra caminos, componentes conectados
- Útil para detección de ciclos

### 🌐 BFS (Breadth-First Search - Anchura)

**Estrategia**: Explora todos los vecinos inmediatos antes de profundizar.
```python
from collections import deque

def bfs(grafo, nodo_inicial):
    visitados = set()
    cola = deque([nodo_inicial])
    recorrido = []
    visitados.add(nodo_inicial)
    
    while cola:
        nodo_actual = cola.popleft()
        recorrido.append(nodo_actual)
        
        for vecino in grafo.get(nodo_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    
    return recorrido
```

**Características**:
- Usa **cola**
- Encuentra **camino más corto** (en grafos no ponderados)
- Recorrido por niveles

### 📊 DFS vs BFS

| Aspecto | DFS | BFS |
|---------|-----|-----|
| Estructura | Pila | Cola |
| Memoria | O(h) altura | O(w) anchura |
| Camino más corto | ❌ | ✅ |
| Uso típico | Detección ciclos, topological sort | Camino mínimo, nivel por nivel |

### 🎯 Casos de Uso

**DFS**:
- Resolver laberintos
- Detección de ciclos
- Ordenamiento topológico
- Análisis de dependencias

**BFS**:
- Camino más corto (no ponderado)
- Redes sociales (grados de separación)
- Rastreadores web
- Sistemas de recomendación

---

## 🎴 Flashcards

¿Cuál es la complejidad de búsqueda binaria?::O(log n) #algoritmos #busqueda

¿Qué requisito tiene la búsqueda binaria?::La lista debe estar ordenada #algoritmos #busqueda

BST - Propiedad fundamental::Subárbol izquierdo < nodo < subárbol derecho #algoritmos #estructuras

¿Cuál es el peor caso de un BST desbalanceado?::O(n) cuando se degenera en lista enlazada #algoritmos

AVL vs Rojo-Negro - diferencia principal::AVL más balanceado (mejor búsqueda), Rojo-Negro menos rotaciones (mejor inserción) #algoritmos #arboles

Hash Table - Complejidad promedio::O(1) para búsqueda, inserción y eliminación #algoritmos #hashing

DFS vs BFS - estructura de datos::DFS usa pila (o recursión), BFS usa cola #algoritmos #grafos

¿Qué algoritmo encuentra camino más corto en grafo no ponderado?::BFS (Breadth-First Search) #algoritmos #grafos

Búsqueda lineal - complejidad::O(n) #algoritmos #busqueda

¿Cuándo usar búsqueda lineal sobre binaria?::Cuando la lista es pequeña o desordenada y ordenarla sería más costoso #algoritmos

Árboles balanceados - garantía::O(log n) garantizado en todos los casos mediante autobalanceo #algoritmos #arboles

Hash - principal desventaja::No mantiene orden, colisiones pueden degradar rendimiento #algoritmos #hashing

---

## 💭 Guía de Decisión

### ¿Qué algoritmo/estructura usar?
```
¿Lista ordenada?
  ✅ SÍ → Búsqueda Binaria
  ❌ NO → ¿Vale la pena ordenar?
          ✅ SÍ → Ordena + Búsqueda Binaria
          ❌ NO → Búsqueda Lineal

¿Inserciones/eliminaciones frecuentes?
  ✅ SÍ → BST o Árbol Balanceado
  ❌ NO → Array ordenado + Búsqueda Binaria

¿Necesitas garantía de rendimiento?
  ✅ SÍ → Árbol Balanceado (AVL/Rojo-Negro)
  ❌ NO → BST simple

¿Búsquedas exactas y velocidad crítica?
  ✅ SÍ → Hash Table
  ❌ NO → Árbol

¿Explorar relaciones/caminos?
  → Grafo con DFS/BFS
```

---

## 🔗 Relacionado

[[Algoritmos de Ordenación]]
[[Big O y Análisis de Complejidad]]

---

## 📚 Referencias

- UD3: Algoritmos de Búsqueda y Ordenación - UAX
- Cormen et al. (2009) - Introduction to Algorithms (Cap. 12-13)
- Sedgewick & Wayne (2011) - Algorithms 4th ed.

---

#algoritmos #busqueda #bst #arboles #grafos #hashing #estructuras-datos

---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Tarea para aclarar una duda de concepto. Usa #mejora-concepto
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia
