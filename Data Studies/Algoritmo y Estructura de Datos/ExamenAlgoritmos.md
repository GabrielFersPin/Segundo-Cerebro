
Parte 1: Tipo Test (15 preguntas)
1. ¿Qué mide principalmente la notación Big O? a) El tiempo exacto en segundos que tarda un algoritmo. b) El espacio en disco que ocupa el código fuente. c) La tasa de crecimiento de operaciones con respecto al tamaño de la entrada en el peor caso. d) La complejidad promedio en el mejor escenario posible.

d) La complejidad promedio en el mejor escenario posible.

2. Ordena las siguientes complejidades de MEJOR (más eficiente) a PEOR (menos eficiente): O(n), O(1), O(n²), O(log n) a) O(1) < O(n) < O(log n) < O(n²) b) O(1) < O(log n) < O(n) < O(n²) c) O(log n) < O(1) < O(n) < O(n²) d) O(1) < O(log n) < O(n²) < O(n)

a)

3. Para aplicar una Búsqueda Binaria O(log n), ¿qué condición es indispensable? a) La lista debe ser de números enteros. b) La lista debe estar ordenada previamente. c) La lista debe estar implementada como una LinkedList. d) No tiene requisitos previos.

b)

4. ¿Qué estructura de datos sigue el principio LIFO (Last In, First Out)? a) Cola (Queue) b) Árbol Binario c) Pila (Stack) d) Grafo

c)

5. En una Tabla Hash bien implementada, ¿cuál es la complejidad temporal promedio de búsqueda? a) O(1) b) O(log n) c) O(n) d) O(n log n)

a)

6. En un Árbol Binario de Búsqueda (BST), ¿qué propiedad se cumple para cualquier nodo X? a) Todos los nodos del subárbol izquierdo son mayores que X. b) Todos los nodos del subárbol derecho son menores que X. c) Todos los nodos del subárbol izquierdo son menores que X y los del derecho son mayores. d) No hay un orden específico, solo una estructura jerárquica.

d)

7. ¿Cuál es la principal ventaja de un Array sobre una Lista Enlazada en términos de acceso? a) Inserción más rápida al inicio O(1). b) Tamaño dinámico ilimitado. c) Acceso directo a cualquier elemento por índice en O(1). d) Mejor uso de memoria para listas dispersas.

a)

8. ¿Cuál es la complejidad temporal promedio del algoritmo QuickSort? a) O(n²) b) O(n log n) c) O(n) d) O(log n)

b)

9. ¿Qué significa que un algoritmo de ordenación sea "estable"? a) Que su complejidad siempre es O(n log n). b) Que no utiliza memoria extra (in-place). c) Que mantiene el orden relativo original de los elementos con valores iguales. d) Que nunca produce errores de desbordamiento de pila.

c)

10. ¿Cuál es el Mejor Caso O(n) para el algoritmo de Ordenación por Inserción? a) Cuando la lista está ordenada inversamente. b) Cuando la lista es aleatoria. c) Cuando la lista ya está ordenada o casi ordenada. d) La inserción siempre es O(n²).

c)

11. ¿Cuál es una limitación clave del algoritmo de Dijkstra? a) No funciona en grafos dirigidos. b) No funciona si hay aristas con pesos negativos. c) Es más lento que Bellman-Ford en todos los casos. d) Solo puede encontrar el camino más corto a un solo nodo destino, no a todos.

b)

12. ¿Qué estructura de datos auxiliar utiliza el algoritmo BFS (Búsqueda en Anchura)? a) Pila (Stack) b) Cola (Queue) c) Montículo (Heap) d) Tabla Hash

b)

13. ¿Qué define a un Árbol de Expansión Mínima (MST)? a) Conecta todos los vértices, tiene ciclos y el costo es máximo. b) Conecta un subconjunto de vértices con el costo mínimo. c) Conecta todos los vértices sin ciclos y con la suma de pesos mínima posible. d) Es un árbol binario balanceado construido a partir de un grafo.

d)

14. Si usas una Matriz de Adyacencia para representar un grafo con V vértices, ¿cuál es la complejidad espacial? a) O(V + E) b) O(V) c) O(V²) d) O(E)

b)

15. Para aplicar un Ordenamiento Topológico, ¿qué tipo de grafo necesitas? a) Cualquier grafo conexo. b) Un grafo no dirigido y ponderado. c) Un Grafo Dirigido Acíclico (DAG). d) Un árbol binario completo.

c) No lo sé

Parte 2: Preguntas de Desarrollo (5 preguntas)
16. Tablas Hash y Colisiones Explica brevemente qué es una "colisión" en una tabla hash. Describe dos métodos comunes para resolverla (Chaining/Encadenamiento y Open Addressing/Direccionamiento Abierto).

Una colisión es cuando una clave es la misma para dos elementos de la tabla, Entonces se crea un chaining para crear una lista enlazada para esta clave y se guarda con el mismo indice, pero con claves diferentes.

17. Comparación de Algoritmos de Ordenación Imagina que tienes una lista de 100,000 elementos totalmente desordenada. a) ¿Por qué evitarías usar Bubble Sort (Burbuja)? b) ¿Qué algoritmo elegirías entre Merge Sort o QuickSort y por qué? Menciona sus complejidades Big O en tu respuesta.

Un Bubble Sort tiene una complejidad muy alta para ordenar la lista O=(n²). La mejor opción sería un Merge Sort con O=(n log n) por ser un algoritmo que funciona mejor que QuickSort en listas desordenadas podiendo llegar a O=(n²)

18. Lógica del Algoritmo de Dijkstra Explica con tus propias palabras cómo decide Dijkstra qué nodo visitar a continuación. ¿Por qué se le considera un algoritmo "voraz" (greedy)? ¿Qué papel juega la Cola de Prioridad (Priority Queue) en este proceso?



19. Recorridos de Árboles Dados los siguientes nodos en un árbol binario simple (Raíz: A, Hizq: B, Hder: C), describe el orden de visita para: a) Pre-orden (Pre-order) b) In-orden (In-order) c) Post-orden (Post-order) Explica brevemente la regla de cada uno.

20. Análisis de Código Analiza el siguiente fragmento de código y determina su complejidad temporal Big O. Justifica tu respuesta paso a paso.

def procesar_lista(lista):
    n = len(lista)
    contador = 0
    # Bloque A
    for i in range(n):
        print(lista[i])
    
    # Bloque B
    for i in range(n):
        for j in range(n):
            contador += 1
            
    return contador
