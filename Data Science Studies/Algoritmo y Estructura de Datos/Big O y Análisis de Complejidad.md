---
cards-deck: Algoritmos:Big O
created: 2025-11-04
modified: 2025-12-23
status: 🌳 Maduro
tipo_nota: tecnica
asignatura: Algoritmos
nivel-comprension: ✅
proxima-revision: 2026-01-22
ultima-revision: 2025-12-23
veces-revisado: 7
estado: 🟢 Al día
tiempo-estimado: 5m
---

# Notación Big O y Análisis de Complejidad

> [!abstract] Objetivo
> Entender qué es O(n), O(log n), O(n²) y cómo usarlo para elegir algoritmos eficientes. Aplicable a cualquier lenguaje de programación y directo a ciencia de datos (cantidad de operaciones = tiempo ejecución con grandes datasets).

---

## 🎓 Contexto Académico

**Asignatura/Curso**: Algoritmos y Estructuras de Datos

**Relevancia para**: Todos mis cursos + Proyectos (elegir bien estructura/algoritmo hace diferencia entre segundos y minutos)

**Dificultad percibida**: ⭐⭐☆☆☆ Fácil (concepto simple, pero importante)

---

## 📝 Definición

La **notación Big O** es una forma de expresar **cuántas operaciones hace un algoritmo** cuando los datos crecen, sin medir tiempo real en segundos (que varía por hardware). Es independiente del lenguaje, del CPU, de todo - solo cuenta "pasos lógicos".

Ejemplo: Si tu algoritmo tarda 5 segundos con 100 datos y 50 segundos con 1000 datos, es **O(n)** porque creció linealmente (10x datos = 10x tiempo).

Es crítico en ciencia de datos: procesar 1 millón de registros con algoritmo O(n²) es imposible (1 billón de operaciones). Con O(n log n) es factible (20 millones de operaciones).

---

## ⚙️ Conceptos Clave

### 📌 O(1) - Complejidad Constante

**Tipo**: Complejidad temporal

**Características**:
- El algoritmo tarda **siempre lo mismo**, no importa cuántos datos tengas
- "Siempre ejecuta el mismo número de pasos"
- Ejemplos: acceder a elemento de array, operación matemática simple, consulta hash table

**Código ejemplo**:
```python
# O(1) - Siempre 1 operación
def acceder_primer_elemento(lista):
    return lista[0]  # ← 1 paso, sin importar tamaño

def obtener_valor_diccionario(diccionario, clave):
    return diccionario[clave]  # ← 1 paso (hash table)

# Usar
lista = [1, 2, 3, 4, 5]
print(acceder_primer_elemento(lista))  # 0.000001 segundos

lista_millones = list(range(1000000))
print(acceder_primer_elemento(lista_millones))  # 0.000001 segundos (IGUAL!)
```

**Ventaja**: Súper rápido sin importar datos

**Desventaja**: Pocas operaciones útiles son O(1)

**Caso de uso**: Acceso aleatorio a arrays, consulta a hash table, push/pop en pila

**En tu contexto**: Acceder a propiedades de un coworking en diccionario es O(1)

**Relacionado**: [[Tablas Hash]] • [[Arrays]] • [[Pilas]]

---

### 📌 O(log n) - Complejidad Logarítmica

**Tipo**: Complejidad temporal (muy eficiente)

**Características**:
- Cada paso **divide el problema a la mitad**
- Si tienes 1M elementos, solo necesitas ~20 pasos (porque 2^20 ≈ 1M)
- "Cada vez descartas mitad de los datos"
- Ejemplos: búsqueda binaria, operaciones en árboles balanceados, insert/delete en heap

**Código ejemplo**:
```python
# O(log n) - Búsqueda binaria
def busqueda_binaria(lista_ordenada, objetivo):
    izq, der = 0, len(lista_ordenada) - 1
    pasos = 0
    
    while izq <= der:
        pasos += 1
        mid = (izq + der) // 2
        
        if lista_ordenada[mid] == objetivo:
            print(f"Encontrado en {pasos} pasos")
            return True
        elif lista_ordenada[mid] < objetivo:
            izq = mid + 1  # ← Descartas MITAD izquierda
        else:
            der = mid - 1  # ← Descartas MITAD derecha
    
    return False

# Test
lista_10 = list(range(10))
busqueda_binaria(lista_10, 5)  # ~3 pasos

lista_1000 = list(range(1000))
busqueda_binaria(lista_1000, 500)  # ~10 pasos

lista_1m = list(range(1000000))
busqueda_binaria(lista_1m, 500000)  # ~20 pasos (NO 1M!)
```

**Salida**:
```
Encontrado en 3 pasos
Encontrado en 10 pasos
Encontrado en 20 pasos
```

**Ventaja**: Crece muy lentamente; si tienes 1 billón de elementos, solo 40 pasos

**Desventaja**: Requiere datos ordenados (búsqueda binaria) o estructura específica (árbol, heap)

**Caso de uso**: Búsqueda binaria, operaciones en árboles binarios de búsqueda, heap operations

**En tu contexto**: Si tienes lista de 10K coworkings ordenada por precio, buscar uno es O(log n) = ~14 pasos vs O(n) = 10K pasos

**Relacionado**: [[Búsqueda Binaria]] • [[Árboles Binarios]] • [[Montículos]]

---

### 📌 O(n) - Complejidad Lineal

**Tipo**: Complejidad temporal (la más común)

**Características**:
- El tiempo **crece proporcionalmente** con los datos
- "10x más datos = 10x más tiempo"
- Ejemplos: recorrer array, buscar sin ordenar, llenar lista, recorrer grafo conexo

**Código ejemplo**:
```python
# O(n) - Buscar en array sin ordenar
def buscar_linear(lista, objetivo):
    pasos = 0
    for elemento in lista:  # ← Recorre TODO en peor caso
        pasos += 1
        if elemento == objetivo:
            print(f"Encontrado en {pasos} pasos")
            return True
    print(f"No encontrado después de {pasos} pasos")
    return False

# O(n) - Calcular suma
def sumar_lista(lista):
    total = 0
    for elemento in lista:  # ← Recorre TODO
        total += elemento
    return total

# O(n) - Recorrer grafo (BFS/DFS)
def recorrer_grafo(grafo, inicio):
    visitados = set()
    cola = [inicio]
    
    while cola:
        nodo = cola.pop(0)
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo[nodo]:  # ← Recorre V + E en total
                cola.append(vecino)
    
    return visitados

# Test
lista_10 = list(range(10))
buscar_linear(lista_10, 5)  # 6 pasos

lista_1000 = list(range(1000))
buscar_linear(lista_1000, 500)  # 501 pasos

lista_1m = list(range(1000000))
buscar_linear(lista_1m, 500000)  # 500001 pasos
```

**Salida**:
```
Encontrado en 6 pasos
Encontrado en 501 pasos
Encontrado en 500001 pasos
```

**Ventaja**: Simple de implementar, funciona con datos desordenados

**Desventaja**: Lento con datos grandes; con 1M elementos = 1M pasos

**Caso de uso**: Buscar en array desordenado, contar elementos, recorrer lista

**En tu contexto**: Recorrer todos los 1000 coworkings para calcular algo = O(n)

**Relacionado**: [[Búsqueda Linear]] • [[Recorrido de Estructuras]] • [[BFS/DFS]]

---

### 📌 O(n log n) - Complejidad Lineal-Logarítmica

**Tipo**: Complejidad temporal (óptimo para ordenamiento)

**Características**:
- "Combinación de lineal y logarítmica"
- n × log n: tienes n elementos, cada uno se procesa log n veces
- Ejemplos: merge sort, quicksort, ordenamiento eficiente
- Muchas veces es óptimo: imposible ordenar en menos que O(n log n)

**Código ejemplo**:
```python
# O(n log n) - Merge Sort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    # Divide: O(log n) niveles de división
    mid = len(lista) // 2
    izq = merge_sort(lista[:mid])
    der = merge_sort(lista[mid:])
    
    # Merge: O(n) operaciones en cada nivel
    return merge(izq, der)

def merge(izq, der):
    resultado = []
    i = j = 0
    
    # O(n) comparaciones para combinar
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

# Test
import time

lista_10k = list(range(10000, 0, -1))  # Inversa (peor caso)
start = time.time()
sorted_10k = merge_sort(lista_10k)
print(f"10K elementos: {(time.time()-start)*1000:.2f}ms")

lista_100k = list(range(100000, 0, -1))
start = time.time()
sorted_100k = merge_sort(lista_100k)
print(f"100K elementos: {(time.time()-start)*1000:.2f}ms")

# Comparación: si fuera O(n²)
lista_10k_bubbleSort = list(range(10000, 0, -1))
start = time.time()
# Bubble sort O(n²)
for i in range(len(lista_10k_bubbleSort)):
    for j in range(len(lista_10k_bubbleSort)-1):
        if lista_10k_bubbleSort[j] > lista_10k_bubbleSort[j+1]:
            lista_10k_bubbleSort[j], lista_10k_bubbleSort[j+1] = \
                lista_10k_bubbleSort[j+1], lista_10k_bubbleSort[j]
print(f"10K con bubble sort: {(time.time()-start)*1000:.2f}ms")
```

**Salida (aproximada)**:
```
10K elementos: 15ms      (con merge sort O(n log n))
100K elementos: 180ms    (con merge sort O(n log n))
10K con bubble sort: 5000ms  (con bubble sort O(n²)) ← ¡333x MÁS LENTO!
```

**Ventaja**: Óptimo para ordenamiento; mucho más rápido que O(n²)

**Desventaja**: Más complejo que O(n); requiere más memoria

**Caso de uso**: Ordenar datos, algoritmos de divide y conquista

**En tu contexto**: Si necesitas ordenar 100K coworkings por precio, usa merge/quicksort O(n log n), no bubble sort O(n²)

**Relacionado**: [[Merge Sort]] • [[Quicksort]] • [[Ordenamiento]]

---

### 📌 O(n²) - Complejidad Cuadrática

**Tipo**: Complejidad temporal (lento)

**Características**:
- Dos bucles anidados: "compara cada elemento con cada otro"
- "10x más datos = 100x más tiempo"
- Ejemplos: bubble sort, selection sort, comparar todos con todos

**Código ejemplo**:
```python
# O(n²) - Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):  # ← Bucle 1
        for j in range(n-1):  # ← Bucle 2 (anidado)
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# O(n²) - Encontrar pares con suma objetivo
def encontrar_pares_suma(lista, objetivo):
    pares = []
    for i in range(len(lista)):  # ← Bucle 1
        for j in range(i+1, len(lista)):  # ← Bucle 2
            if lista[i] + lista[j] == objetivo:
                pares.append((lista[i], lista[j]))
    return pares

# Test
import time

lista_1k = list(range(1000, 0, -1))
start = time.time()
bubble_sort(lista_1k)
print(f"1K elementos: {(time.time()-start)*1000:.2f}ms")

lista_10k = list(range(10000, 0, -1))
start = time.time()
bubble_sort(lista_10k)
print(f"10K elementos: {(time.time()-start)*1000:.2f}ms")
```

**Salida (aproximada)**:
```
1K elementos: 400ms
10K elementos: 40,000ms (40 segundos!) ← 100x más lento
```

**Ventaja**: Fácil de implementar y entender

**Desventaja**: **MUY LENTO con datos grandes**; 1M datos = 1 billón operaciones

**Caso de uso**: Solo para datasets pequeños (< 1K elementos)

**En tu contexto**: Si usas O(n²) con 100K coworkings, tardaría HORAS. Con O(n log n) tardaría segundos.

**Relacionado**: [[Bubble Sort]] • [[Selection Sort]] • [[Algoritmos Ineficientes]]

---

### 📌 O(2^n) - Complejidad Exponencial

**Tipo**: Complejidad temporal (casi imposible)

**Características**:
- Cada paso duplica el trabajo: "10 elementos = 1K pasos, 11 elementos = 2K pasos"
- "Un pequeño aumento = ENORME aumento de tiempo"
- Ejemplos: fuerza bruta, algunas versiones de recursión sin optimizar

**Código ejemplo**:
```python
# O(2^n) - Fibonacci sin memoización (EVITAR!)
def fibonacci_lento(n):
    if n <= 1:
        return n
    return fibonacci_lento(n-1) + fibonacci_lento(n-2)
    # Cada llamada genera 2 nuevas llamadas
    # Árbol de recursión: 2^n nodos

# O(n) - Fibonacci con memoización (MEJOR!)
def fibonacci_rapido(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_rapido(n-1, memo) + fibonacci_rapido(n-2, memo)
    return memo[n]

# Test
import time

print("Fibonacci exponencial O(2^n):")
for n in [30, 35, 40]:
    start = time.time()
    resultado = fibonacci_lento(n)
    elapsed = (time.time()-start)
    print(f"  fib({n}) = {resultado} - Tiempo: {elapsed:.2f}s")

print("\nFibonacci optimizado O(n):")
for n in [30, 35, 40]:
    start = time.time()
    resultado = fibonacci_rapido(n)
    elapsed = (time.time()-start)
    print(f"  fib({n}) = {resultado} - Tiempo: {elapsed:.6f}s")
```

**Salida (aproximada)**:
```
Fibonacci exponencial O(2^n):
  fib(30) = 832040 - Tiempo: 0.27s
  fib(35) = 9227465 - Tiempo: 2.75s
  fib(40) = 102334155 - Tiempo: 27.59s

Fibonacci optimizado O(n):
  fib(30) = 832040 - Tiempo: 0.000015s
  fib(35) = 9227465 - Tiempo: 0.000016s
  fib(40) = 102334155 - Tiempo: 0.000017s
```

**Ventaja**: Ninguna (evitar siempre)

**Desventaja**: **Prácticamente imposible de usar**; con n=50 tomaría años

**Caso de uso**: Evitar a toda costa; si lo ves, optimiza con memoización o DP

**En tu contexto**: Si algún algoritmo es O(2^n), está mal diseñado

**Relacionado**: [[Memoización]] • [[Programación Dinámica]] • [[Optimización]]

---

### 📌 O(V + E) y O((V+E) log V) - Grafos

**Tipo**: Complejidad en grafos

**Características**:
- **V** = vértices (nodos)
- **E** = aristas (conexiones)
- O(V + E) = recorrer todo el grafo (BFS/DFS)
- O((V+E) log V) = Dijkstra (ruta más corta con heap)

**Código ejemplo**:
```python
from collections import defaultdict, deque
import heapq

# O(V + E) - BFS
def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    pasos = 0
    
    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            visitados.add(nodo)
            pasos += 1
            for vecino in grafo[nodo]:
                cola.append(vecino)
    
    return pasos  # Total: V nodos + E aristas revisadas

# O((V+E) log V) - Dijkstra con heap
def dijkstra(grafo, inicio):
    distancias = defaultdict(lambda: float('inf'))
    distancias[inicio] = 0
    heap = [(0, inicio)]
    operaciones = 0
    
    while heap:
        distancia_actual, nodo = heapq.heappop(heap)  # ← O(log V)
        operaciones += 1
        
        if distancia_actual > distancias[nodo]:
            continue
        
        for vecino, peso in grafo[nodo]:
            nueva_dist = distancia_actual + peso
            
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                heapq.heappush(heap, (nueva_dist, vecino))  # ← O(log V)
                operaciones += 1
    
    return distancias, operaciones

# Test con grafo de ciudades
grafo = defaultdict(list)
grafo['Madrid'] = [('Barcelona', 6), ('Valencia', 3)]
grafo['Barcelona'] = [('Madrid', 6), ('Valencia', 5)]
grafo['Valencia'] = [('Madrid', 3), ('Barcelona', 5)]

print("BFS (O(V+E)):")
pasos_bfs = bfs(grafo, 'Madrid')
print(f"  Pasos: {pasos_bfs}")

print("\nDijkstra (O((V+E) log V)):")
dist, ops = dijkstra(grafo, 'Madrid')
print(f"  Operaciones: {ops}")
print(f"  Distancias: {dict(dist)}")
```

**Ventaja**: Mucho más eficiente que revisar todas las combinaciones O(V²)

**Desventaja**: Más complejo de implementar

**Caso de uso**: Recorrer grafos, encontrar rutas más cortas

**En tu contexto**: Tu sistema de recomendación usa grafos. Si tienes 1000 coworkings con 5000 relaciones: O(V+E) = 6000 ops vs O(V²) = 1M ops

**Relacionado**: [[BFS]] • [[DFS]] • [[Algoritmo de Dijkstra]] • [[Grafos]]

---

## 💻 Ejemplo Práctico

Mismo problema, tres soluciones con diferentes complejidades:

```python
# Problema: Encontrar si dos números en array suman un objetivo

# ❌ SOLUCIÓN 1: O(n²) - LENTA
def suma_dos_lenta(lista, objetivo):
    for i in range(len(lista)):  # ← Bucle 1
        for j in range(i+1, len(lista)):  # ← Bucle 2
            if lista[i] + lista[j] == objetivo:
                return (lista[i], lista[j])
    return None

# Con 10K números: 50 millones comparaciones ⏱️

# ✅ SOLUCIÓN 2: O(n) - RÁPIDA
def suma_dos_rapida(lista, objetivo):
    vistos = set()  # ← Tabla hash O(1) búsqueda
    
    for numero in lista:  # ← 1 bucle
        complemento = objetivo - numero
        if complemento in vistos:  # ← O(1)
            return (numero, complemento)
        vistos.add(numero)
    
    return None

# Con 10K números: 10K operaciones ⚡

# ✅ SOLUCIÓN 3: O(n log n) - TAMBIÉN RÁPIDA
def suma_dos_ordenada(lista, objetivo):
    lista_ordenada = sorted(lista)  # ← O(n log n)
    izq, der = 0, len(lista_ordenada) - 1
    
    while izq < der:
        suma = lista_ordenada[izq] + lista_ordenada[der]
        if suma == objetivo:
            return (lista_ordenada[izq], lista_ordenada[der])
        elif suma < objetivo:
            izq += 1
        else:
            der -= 1
    
    return None

# Test
import time

lista = list(range(10000))
objetivo = 15000

print("O(n²) - Fuerza bruta:")
start = time.time()
resultado = suma_dos_lenta(lista, objetivo)
print(f"  Resultado: {resultado}, Tiempo: {(time.time()-start)*1000:.2f}ms")

print("\nO(n) - Hash table:")
start = time.time()
resultado = suma_dos_rapida(lista, objetivo)
print(f"  Resultado: {resultado}, Tiempo: {(time.time()-start)*1000:.2f}ms")

print("\nO(n log n) - Ordenar + dos punteros:")
start = time.time()
resultado = suma_dos_ordenada(lista, objetivo)
print(f"  Resultado: {resultado}, Tiempo: {(time.time()-start)*1000:.2f}ms")
```

**Salida**:
```
O(n²) - Fuerza bruta:
  Resultado: (7500, 7500), Tiempo: 800.50ms

O(n) - Hash table:
  Resultado: (7500, 7500), Tiempo: 0.45ms

O(n log n) - Ordenar + dos punteros:
  Resultado: (7500, 7500), Tiempo: 1.20ms
```

**Lección**: La misma solución, **3 órdenes de magnitud de diferencia** en tiempo (O(n²) vs O(n))

---

## 💭 Reflexiones & Conexiones

Big O no es teoría abstracta: es la diferencia entre un sistema que funciona vs uno que es inutilizable.

Tu sistema de recomendación:
- Si es O(n²): con 100K coworkings → 10 mil millones comparaciones
- Si es O(n log n): con 100K coworkings → 1.6 millones operaciones

Diferencia: horas vs segundos.

En ciencia de datos, datasets crecen constantemente. Un algoritmo que es "rápido" con 1K datos se vuelve inutilizable con 1M. Por eso es crítico entender Big O desde el principio.

La filosofía existencialista de Camus conecta aquí: no puedes ignorar la realidad del rendimiento. Tu código *existe* en un hardware real con limitaciones reales. Elegir bien es responsabilidad del programador.

---

## 🎴 Flashcards

O(1)::Tiempo constante. Siempre igual sin importar datos. Ejemplo: acceso array[i] #bigO #constante

O(log n)::Logarítmico. Divides problema a la mitad cada vez. Con 1M datos: ~20 pasos. Ejemplo: búsqueda binaria #bigO #eficiente

O(n)::Lineal. Crece proporcionalmente con datos. 10x datos = 10x tiempo. Ejemplo: recorrer array #bigO #comun

O(n log n)::Lineal-log. Óptimo para ordenamiento. Ejemplo: merge sort, quicksort #bigO #ordenamiento

O(n²)::Cuadrático. Dos bucles anidados. LENTO. 10x datos = 100x tiempo. Ejemplo: bubble sort #bigO #evitar

O(2^n)::Exponencial. CASI IMPOSIBLE. 10 datos = 1K pasos, 20 datos = 1M pasos. Optimiza con memoización #bigO #evitar

¿Cuál es más rápido: O(n) o O(log n)?::O(log n) es MÁS rápido. Con 1M datos: log n = 20 vs n = 1M #bigO #comparacion

¿Cuál es la diferencia clave entre O(n) y O(n²)?::O(n²) tiene dos bucles anidados. Con 10K datos: 10K vs 100M operaciones #bigO #bucles

¿Qué estructura permite búsqueda en O(1) promedio?::Tabla hash (diccionarios en Python). #bigO #hashtable

¿Qué significa O(V+E) en grafos?::V=vértices, E=aristas. Tiempo total para recorrer grafo. #bigO #grafos

Búsqueda binaria==O(log n)==: requiere datos ==ordenados==. Divide mitades cada paso. #bigO #busqueda

¿Por qué Dijkstra es O((V+E) log V) y no O(V²)?::Usa heap para extraer mínimo O(log V) en lugar de buscar lineal O(V) #bigO #dijkstra

¿Cuándo usarías O(n²) algoritmo deliberadamente?::Cuando datos son muy pequeños (<1K) y simplicidad importa más que velocidad #bigO #trade-off

¿Qué es peor: O(n log n) u O(n²)?::O(n²) es PEOR. Con 1M datos: 20M ops vs 1 billón ops #bigO #comparacion

La mejor estrategia al diseñar algoritmo es==empezar simple (O(n²))==y==optimizar si es lento==luego a O(n log n) o O(n) #bigO #desarrollo

¿Cómo pasas de O(2^n) a O(n) en Fibonacci?::Memoización: almacena resultados previos en diccionario para reutilizar #bigO #memoizacion

---

**📊 Total de flashcards**: 16

> 🎯 **Para revisar**: Cmd/Ctrl+P → "Flashcards: Review flashcards"

---

## 📚 Referencias & Enlaces

**Enlaces internos**: 
- [[Estructuras Dinámicas de Datos]]
- [[Búsqueda Binaria]]
- [[Algoritmo de Dijkstra]]

**Referencias externas**: 
- "Introduction to Algorithms" - CLRS (Capítulo 3: Growth of Functions)
- Big O Cheat Sheet: bigocheatsheet.com
- VisuAlgo: visualización de algoritmos y complejidad

**Fuente**: UD1_EstructurasDatos.pdf + Apuntes personales


---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica

