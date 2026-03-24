# Entrenamiento de Redes Neuronales

**Objetivo:** Minimizar la función de costo ajustando los pesos y sesgos de la red.

## 1. Arquitectura de la Red
<details>
<summary>Haz clic para ver detalles sobre la Arquitectura de la Red</summary>

La arquitectura de una red neuronal define la forma y el número de capas de la red, y cómo están conectadas entre sí. Existen varios tipos de arquitecturas, como las redes neuronales [[Arquitecturas#Perceptrón (ANN o MLP) - Redes neuronales feed-foward networks]]
[[Arquitecturas#Redes Neuronales Convolucionales (CNN)]] y etc.

</details>

## 2. Inicialización de Pesos
<details>
<summary>Haz clic para ver detalles sobre la Inicialización de Pesos</summary>

La inicialización de los pesos es crucial para el entrenamiento de la red neuronal. Si los pesos se inicializan con valores muy grandes o pequeños, pueden dificultar el aprendizaje.

- **Inicialización Aleatoria**: Los pesos se inician con valores aleatorios pequeños.
- **Inicialización Xavier/Glorot**: Especialmente útil para redes profundas, ajusta los pesos dependiendo de la cantidad de entradas.
- **Inicialización He**: Similar a Xavier, pero diseñada para redes con funciones de activación ReLU.

</details>

## 3. Propagación Hacia Adelante
<details>
<summary>Haz clic para ver detalles sobre la Propagación Hacia Adelante</summary>

La propagación hacia adelante es el proceso mediante el cual la entrada se transforma en una predicción. Los datos pasan a través de las capas de la red neuronal, y cada neurona aplica una [[Funciones de Activación]] función de activación para decidir si pasar la información al siguiente nivel.

- Se calcula en función de los **pesos** y **sesgos** de cada neurona.

</details>

## 4. Función de Pérdida
<details>
<summary>Haz clic para ver detalles sobre la Función de Pérdida</summary>

La **función de pérdida** mide cuán lejos están las predicciones de la red neuronal de los valores reales. El objetivo del entrenamiento es minimizar esta función.

- **MSE (Mean Squared Error)**: Usada principalmente en problemas de regresión.
- **Cross-Entropy Loss**: Usada en problemas de clasificación.

</details>

## 5. Cálculo del Gradiente
<details>
<summary>Haz clic para ver detalles sobre el Cálculo del Gradiente</summary>

El gradiente mide la tasa de cambio de la función de pérdida con respecto a los parámetros de la red (pesos y sesgos). Es utilizado para determinar en qué dirección ajustar los pesos para minimizar el error.

- Se calcula utilizando la **derivada** de la función de pérdida con respecto a los pesos.


</details>

## 6. Retropropagación

## 7. Actualización de Pesos y Sesgos
<details>
<summary>Haz clic para ver detalles sobre la Actualización de Pesos y Sesgos</summary>

Después de calcular el gradiente, los pesos y sesgos de la red se actualizan para reducir la función de pérdida. La actualización se realiza utilizando un algoritmo de optimización como el **Descenso de Gradiente Estocástico (SGD)**.

- **Fórmula de actualización**: \( \text{Nuevo peso} = \text{Peso actual} - \text{Tasa de aprendizaje} \times \text{Gradiente} \)

</details>

## 8. Iteración (Épocas)
<details>
<summary>Haz clic para ver detalles sobre las Épocas</summary>

El entrenamiento de una red neuronal ocurre a través de múltiples **épocas**. Cada época implica pasar todo el conjunto de entrenamiento a través de la red.

- Después de cada época, se ajustan los pesos para mejorar la precisión de la red.
- Un número adecuado de épocas es importante para evitar el sobreajuste (overfitting).

</details>

## 9. Optimización (Algoritmos Avanzados)
- [[Optimización del descenso del gradiente]]
## 10. Overfitting
>[!Overfitting ]
>- La red tiene una **libertad increíble y puede adaptarse a una enorme variedad de conjuntos de datos complejos** y por eso es propensa a sobreajustar el conjunto de entrenamiento.

## 11. Regularización
>[!Definición]
>- Restringir la optimización para descartar problemas complejos.
>- Permite que el algoritmo generalice bien para nuevos datos.

### Early stopping
>[!Definición]
>- Interrupir el entrenamiento cuando su rendimiento en el conjunto de validación comienza a caer.
>- Evaluar el modelo en intervalos regulares para detección de la caída dela validación

### Dropout
>[!Definición]
>- Se basa en utilizar el hiperparámetro "p"
>	- El parámetro "p" es una probabilidad 
>	- Cada paso de entrenamiento, cada neurona tiene una probalidad "p" de ser descartada temporalmente
>	- Cada paso de entrenamiento la neurona puede ser descartada o no
>	- Al final del entrenamiento las neuronas ya no se pueden coadaptarse con las neuronas vecinas 
### L1 y L2 Regularization
>[!Definición]
>- Se puede utilizar la regularización L1 y L2 para restringir los pesos de conxión de una red neuronal

## Max-Norm Regularization
>[!Definición]
>- Regularización de la norma máxima para cada neurona
>- Cada neurona restringe los pesos de las conexiones entrantes
$$
> {\omega}_2<=r
$$

