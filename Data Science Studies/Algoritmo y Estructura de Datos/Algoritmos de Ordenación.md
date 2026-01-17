---
cards-deck: "Algoritmos: Ordenación"
created: 2024-11-27
modified: 2026-01-14
status: 🌿 Creciendo
tipo_nota: tecnica
asignatura: Algoritmos
procesamiento: COMPLETO
prioridad: EXAMEN-LEJANO
fecha-examen: 2025-02-15
proxima-revision: 2026-01-28
complejidad: ⭐⭐⭐
tiempo-estimado: 1h
fuente: UD3 - Algoritmos y Estructuras de Datos UAX
nivel-comprension: 💡
ultima-revision: 2026-01-14
veces-revisado: 5
---

# Algoritmos de Ordenación

> [!abstract] Objetivo
> Dominar los 4 algoritmos fundamentales de ordenación: selección, inserción, burbuja y quicksort. Entender sus complejidades, ventajas/desventajas y casos de uso.

---

## 📊 Comparativa Rápida

| Algoritmo | Complejidad Promedio | Complejidad Peor Caso | In-place | Estable |
|-----------|---------------------|----------------------|----------|---------|
| Selección | O(n²) | O(n²) | ✅ | ❌ |
| Inserción | O(n²) | O(n²) | ✅ | ✅ |
| Burbuja | O(n²) | O(n²) | ✅ | ✅ |
| QuickSort | O(n log n) | O(n²) | ✅ | ❌ |

---

## 1️⃣ Ordenación por Selección

### 🔍 Concepto

Busca repetidamente el elemento más pequeño de la parte no ordenada y lo coloca en su posición correcta.

**Analogía**: Ordenar cartas buscando siempre la más pequeña primero.

### ⚙️ Funcionamiento

1. Encuentra el mínimo en la lista
2. Intercámbialo con el primer elemento
3. Repite con la sublista restante (excluyendo el primer elemento)
4. Continúa hasta ordenar toda la lista

### 💻 Implementación Python
```python
def ordenacion_por_seleccion(lista):
    for i in range(len(lista)):
        indice_minimo = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista
```

### ✅ Ventajas

- Simple de entender e implementar
- Comportamiento predecible (siempre hace el mismo número de comparaciones)
- Número mínimo de intercambios (útil si escribir en memoria es costoso)

### ❌ Desventajas

- Ineficiente para listas grandes: O(n²)
- No aprovecha listas parcialmente ordenadas
- No es estable (puede cambiar el orden relativo de elementos iguales)

### 🎯 Casos de Uso

- Listas muy pequeñas (<20 elementos)
- Cuando la escritura en memoria es muy costosa
- Propósitos educativos

---

## 2️⃣ Ordenación por Inserción

### 🔍 Concepto

Similar a cómo ordenas cartas en tu mano: tomas cada carta y la insertas en su posición correcta entre las ya ordenadas.

**Analogía**: Ordenar mano de póker carta por carta.

### ⚙️ Funcionamiento

1. Considera el primer elemento como "ordenado"
2. Toma el siguiente elemento (clave)
3. Compáralo con elementos anteriores
4. Desplaza elementos mayores una posición a la derecha
5. Inserta la clave en su posición correcta
6. Repite para todos los elementos

### 💻 Implementación Python
```python
def ordenacion_por_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista
```

### ✅ Ventajas

- Muy eficiente para listas pequeñas
- **Excelente para listas casi ordenadas**: O(n) en mejor caso
- Ordenamiento estable (mantiene orden relativo)
- In-place (no necesita memoria extra)
- Algoritmo online (puede ordenar mientras recibe datos)

### ❌ Desventajas

- Ineficiente para listas grandes: O(n²) en peor caso
- Más lento que QuickSort/MergeSort en datos aleatorios

### 🎯 Casos de Uso

- Listas pequeñas (< 50 elementos)
- **Listas casi ordenadas** (muy eficiente)
- Parte de algoritmos híbridos (Timsort usa inserción)
- Datos que llegan en streaming

---

## 3️⃣ Ordenación por Burbuja

### 🔍 Concepto

Los elementos "burbujean" hacia su posición correcta mediante intercambios repetidos de elementos adyacentes.

**Analogía**: Burbujas en un refresco suben a la superficie.

### ⚙️ Funcionamiento

1. Compara pares de elementos adyacentes
2. Si están en orden incorrecto, intercámbialos
3. Repite el proceso para toda la lista
4. Después de cada pasada, el elemento más grande está en su posición final
5. Repite n-1 veces (o hasta que no haya intercambios)

### 💻 Implementación Python
```python
def ordenacion_por_burbuja(lista):
    n = len(lista)
    for i in range(n):
        intercambiado = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
    return lista
```

### ✅ Ventajas

- Extremadamente simple de implementar
- Puede detectar si la lista ya está ordenada (optimización)
- Ordenamiento estable

### ❌ Desventajas

- **Muy ineficiente**: O(n²) incluso en casos promedio
- El peor algoritmo de ordenación en la práctica
- Solo útil para propósitos didácticos

### 🎯 Casos de Uso

- **Educación** (enseñar conceptos de ordenación)
- Listas muy pequeñas donde la simplicidad importa más que eficiencia
- Detección de si una lista está ordenada

---

## 4️⃣ QuickSort (Ordenación Rápida)

### 🔍 Concepto

Algoritmo **divide y conquista**. Selecciona un pivote, particiona la lista en menores y mayores que el pivote, y ordena recursivamente.

**Analogía**: Dividir grupo de personas por altura usando una persona como referencia.

### ⚙️ Funcionamiento

1. **Elegir pivote**: Selecciona un elemento (último, aleatorio, mediana de tres)
2. **Particionar**: 
   - Elementos < pivote → sublista izquierda
   - Elementos > pivote → sublista derecha
3. **Recursión**: Aplica QuickSort a ambas sublistas
4. **Caso base**: Sublista de 0-1 elementos ya está ordenada

### 💻 Implementación Python
```python
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    
    return quicksort(izquierda) + medio + quicksort(derecha)
```

### ✅ Ventajas

- **Muy rápido en promedio**: O(n log n)
- In-place (versión optimizada)
- Buena localidad de caché
- Funciona bien en la práctica (usado en bibliotecas estándar)

### ❌ Desventajas

- Peor caso O(n²) si pivote mal elegido (ej: lista ya ordenada)
- No es estable
- Recursión puede consumir memoria de pila

### 🎓 Técnicas de Optimización

**Pivote Mediano de Tres**: Selecciona mediana entre primer, medio y último elemento
```python
def mediana_de_tres(lista, inicio, fin):
    medio = (inicio + fin) // 2
    if lista[inicio] > lista[medio]:
        lista[inicio], lista[medio] = lista[medio], lista[inicio]
    if lista[inicio] > lista[fin]:
        lista[inicio], lista[fin] = lista[fin], lista[inicio]
    if lista[medio] > lista[fin]:
        lista[medio], lista[fin] = lista[fin], lista[medio]
    return lista[medio]
```

### 🎯 Casos de Uso

- **Uso general** para listas grandes
- Sistemas de ordenación en producción
- Cuando la velocidad promedio es crucial
- Bibliotecas estándar (muchas usan variantes híbridas)

---

## 🎴 Flashcards

¿Cuál es la complejidad promedio de QuickSort?::O(n log n) #algoritmos #ordenacion

¿Qué algoritmo de ordenación es mejor para listas casi ordenadas?::Ordenación por inserción (O(n) en mejor caso) #algoritmos #ordenacion

Ordenación por Selección - Complejidad::O(n²) en todos los casos #algoritmos

¿Qué significa que un algoritmo de ordenación sea "estable"?::Mantiene el orden relativo de elementos con el mismo valor #algoritmos

¿Cuál es el peor caso de QuickSort y cómo se evita?::O(n²) cuando el pivote es el peor elemento. Se evita con "pivote mediano de tres" #algoritmos #ordenacion

Ordenación por Burbuja - Principal desventaja::Es el más ineficiente (O(n²)) incluso en caso promedio, solo útil para educación #algoritmos

¿Qué algoritmos de ordenación son in-place?::Selección, Inserción, Burbuja y QuickSort (versión optimizada) #algoritmos

Inserción vs Selección para listas pequeñas::Inserción es mejor porque puede terminar antes si detecta orden #algoritmos

---

## 💭 Reflexiones

### Elección del Algoritmo
```
Lista pequeña (<20) → Inserción
Lista casi ordenada → Inserción
Lista grande aleatoria → QuickSort
Necesitas estabilidad → Inserción o MergeSort
Aprendiendo conceptos → Burbuja/Selección
Producción (uso real) → QuickSort o Timsort
```

### Complejidad vs Práctica

Los algoritmos O(n²) no siempre son malos:
- Para n=10, la diferencia con O(n log n) es mínima
- La simplicidad del código puede valer la pena
- Constantes ocultas importan (inserción puede ganar a quicksort en n<50)

---

## 🔗 Relacionado

[[Big O y Análisis de Complejidad]]

---

## 📚 Referencias

- UD3: Algoritmos de Búsqueda y Ordenación - UAX
- Cormen et al. (2009) - Introduction to Algorithms
- Sedgewick & Wayne (2011) - Algorithms 4th ed.

---

#algoritmos #ordenacion #quicksort #complejidad #programacion

---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Hacer cuestionario #mejora-concepto 
