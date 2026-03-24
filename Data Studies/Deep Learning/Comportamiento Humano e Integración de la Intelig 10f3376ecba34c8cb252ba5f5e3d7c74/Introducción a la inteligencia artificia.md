# (Introducción a la inteligencia artificial)

- Procesamiento Simbólico 
    - Simbolo: Es algo que representa otra cosa(objeto físico o concepto)
    - Apredizage automático (Machine Learning): Generalización de comportamientos a partir de información no estructurada en formas de ejemplos(inducción del conocimiento)[[Machine Learning]]
    - Procesamiento de lenguaje natural
    - Marcos
        
        Descripción general de un objeto derivada de conceptos básicos y de la experiencia
        
    - Nodos
        
        Cada nodo corresponde a un objeto o a una clase que se convierte en un marco, que consta de una primera línea con el nombre del marco.
        
    - Slots
        
        Describen atributos particulares al frame
        
    - Frame
        
        Colección de atributos y la descripción de sus características. Son un modo natural de representar el conocimiento
        
- Procesamiento Subsimbólico
    - Basado en el modelo biológico de la neurona
    - Redes Neuronales
        
        Compuesto por neuronas conectadas a una red
        
    - Neurona
        
        ![Untitled](Unidad%201(Introduccio%CC%81n%20a%20la%20inteligencia%20artificia%20439cadea289947a284f732f172fde532/Untitled.png)
        
    - Arquitectura
        1. Capa: elemento estructural
        2. Red: capa de entrada/intermedia
        3. Tipos de conexiones: 
            1. Por la actividad: excitatorias o inhibitorias
            2. Por la topología: lateral, capa a capa o recurrentes
            3. Por la dirección: feedfoward y feedback
    - Procesamiento
        
        Pattern Matching: dado un patrón A, produce el patrón B asociado. Si no se encuentra el patrón de salida exacto(matching no perfecto) se produce el patrón de salida que mejor encaje con el estímulo.
        
    - Aprendizaje
        
        Es un proceso(algoritmo) por el que la red modifica sus pesos en función de sus salidas presentadas asociando patrones de entrada a patrones de salida. El resultado es la modificación de la estructura de la red(matriz de pesos). La red genera un modelo interno del mundo, un algoritmo para resolver el problema propuesto. La solución se almacena de forma distribuida entre la matriz de pesos y la arquitectura de la red.
        
        - Estratégias de aprendizaje:
            - No supervisadas:
                
                Memoria asociativa/aprendizaje competitivo
                
            - Supervisadas(pares input/output):
                
                La función de error es la regla delta que es un algoritmo iterativo que ajusta los pesos de la red intentando minimizar el error cuadrático medio entre las salidas esperadas y las producidas por la red.
                