#  (Técnicas de búsqueda)

- Introducción al razonamiento artificial
    - Aproximación simbólica
        - Niveles de representación del mundo real
            1. Nivel de conocimiento(nivel conceptual): se modela la realidad mediante un modelo formal.
            2. Nivel simbólico(nivel lógico): El conocimiento se representa en un sistema de símbolos físico
            3. Nivel de implementación(nivel físico): El sistema de símbolos físicos se implementa en un lenguaje de programación.
    - Técnicas simbólicas
        - Técnicas de computación básica(enfoque algorítmico):
            
            Se tiene todo el conocimiento necesario para obtener la solución óptima del sistema
            
        - Técnicas específicas de la I.A.
            
            Las decisiones están basadas en la información parcial que no segura encontrar el óptimo. Estos métodos se denominan heurísticas que son estratégias de resolución de problemas que los seres humanos empleamos y donde se aloja parte de la inteligencia.
            
    - Áreas
        - Búsqueda en espacio de datos
            
            Utiliza un algoritmo para buscar la solución en el espacio de los posibles estados(grafo) en que se puede hallar un problema
            
            - Elementos para resolver un problema
                - Representación de un problema
                - Búsqueda de la solución
                    - Tipos de búsqueda
                        - Búsqueda no informada o ciega
                        - Búsqueda informada o heurística
        - Representación o Ingeniería del conocimiento
            - Definición:
                
                Permite generar nuevo conocimiento(inferencia) a partir del conocimiento explícito almacenado en las bases de conocimiento.
                
- Espacio de estados
    - Definición:
        
        Es un modelo matemático de una unidad física que consiste en un grafo en el que se muestran todos y cada uno de los posibles estados en los que se puede hallar el sistema y que tienen que ser representable mediante un árbol.
        
    - Grafo
        
        El grafo es una representación matemática de un espacio de estados en el que se muestran todos y cada uno de los posibles estados en los que se puede hallar un sistema. Este modelo se utiliza en la búsqueda en espacio de datos para buscar una solución óptima a un problema.
        
    - La búsqueda
        
        análisis simulado del grafo del espacio de estados a través de la generación de sucesores de los estados ya explorados. Crea un árbol de soluciones a partir del estado inicial del espacio de estados 
        
    - Nodo
        
        Estructura de datos que forma parte de un árbol de búsqueda 
        
    - Frontera
        
        Conjunto de nodos pendientes de expandir
        
    - Camino
        
        
-