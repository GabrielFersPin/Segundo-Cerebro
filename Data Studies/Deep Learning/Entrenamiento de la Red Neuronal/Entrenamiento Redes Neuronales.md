
# Entrenamiento de Redes Neuronales

_Estas notas son una síntesis del proceso de entrenamiento de redes neuronales. Fueron creadas para ayudarme a entender cada paso, pero también están pensadas para compartir ese camino con quienes, como yo, están aprendiendo desde cero con profundidad y curiosidad._

**Objetivo:** Minimizar la función de costo ajustando los pesos y sesgos de la red.

## 1. Arquitectura de la Red
<details>
<summary>Haz clic para ver detalles sobre la Arquitectura de la Red</summary>

La arquitectura de una red neuronal define la forma y el número de capas de la red, y cómo están conectadas entre sí. Existen varios tipos de arquitecturas, como las redes neuronales [[Arquitecturas#Perceptrón (ANN o MLP) - Redes neuronales feed-forward networks]], [[Arquitecturas#Redes Neuronales Convolucionales (CNN)]] y más.

</details>

## 2. Inicialización de Pesos
<details>
<summary>Haz clic para ver detalles sobre la Inicialización de Pesos</summary>

La inicialización de los pesos es crucial para el entrenamiento de la red neuronal. Si los pesos se inicializan con valores muy grandes o pequeños, pueden dificultar el aprendizaje.

- **Inicialización Aleatoria**: Pesos con valores aleatorios pequeños.
- **Inicialización Xavier/Glorot**: Ajusta los pesos dependiendo de la cantidad de entradas (útil para redes profundas).
- **Inicialización He**: Similar a Xavier, optimizada para funciones de activación ReLU.

</details>

## 3. Propagación Hacia Adelante
<details>
<summary>Haz clic para ver detalles sobre la Propagación Hacia Adelante</summary>

Es el proceso mediante el cual la entrada se transforma en una predicción. Los datos pasan a través de las capas de la red, y cada neurona aplica una [[Funciones de Activación]] para decidir si pasa información al siguiente nivel.

</details>

## 4. Función de Pérdida
<details>
<summary>Haz clic para ver detalles sobre la Función de Pérdida</summary>

La función de pérdida mide cuán lejos están las predicciones de los valores reales. El entrenamiento busca minimizar esta función.

- **MSE (Error Cuadrático Medio)**: Para regresión.
- **Cross-Entropy Loss**: Para clasificación.

</details>

## 5. Cálculo del Gradiente
<details>
<summary>Haz clic para ver detalles sobre el Cálculo del Gradiente</summary>

El gradiente mide la tasa de cambio de la pérdida respecto a los parámetros de la red (pesos y sesgos), y se calcula con derivadas.

</details>

## 6. Retropropagación
<details>
<summary>Haz clic para ver detalles sobre la Retropropagación</summary>

La retropropagación es el algoritmo que permite actualizar los pesos a partir del error calculado. Usa la regla de la cadena para propagar el error desde la salida hasta las capas anteriores, y ajusta los pesos usando gradiente descendente.

</details>

## 7. Actualización de Pesos y Sesgos
<details>
<summary>Haz clic para ver detalles sobre la Actualización de Pesos y Sesgos</summary>

Después de calcular el gradiente, se actualizan pesos y sesgos para reducir la pérdida. Utiliza optimizadores como **SGD**.

- **Fórmula**: `Nuevo peso = Peso actual - tasa de aprendizaje × gradiente`

</details>

## 8. Iteración (Épocas)
<details>
<summary>Haz clic para ver detalles sobre las Épocas</summary>

El entrenamiento ocurre en múltiples épocas. Cada época pasa todo el set de entrenamiento por la red.

</details>

## 9. Optimización (Algoritmos Avanzados)
- [[Optimización del descenso del gradiente]]

## 10. Overfitting
> La red puede ajustarse demasiado al set de entrenamiento, perdiendo capacidad de generalización.

## 11. Regularización
> Métodos para prevenir el sobreajuste y mejorar la generalización.

### Early stopping
> Detener el entrenamiento cuando la pérdida de validación empeora.

### Dropout
> En cada paso de entrenamiento, cada neurona tiene una probabilidad _p_ de desactivarse temporalmente. Así se evita que se “coadapten”.

### L1 y L2
> Penalizan los pesos grandes. L1 favorece la dispersión; L2 la estabilidad.

### Max-Norm
> Limita la norma máxima de los pesos por neurona.  
$$\omega_2 \leq r$$

---

## 📌 Resumen Visual

- **Input → Forward Propagation → Loss → Backpropagation → Weight Update → Repeat**
- Técnicas clave: Inicialización correcta, función de pérdida adecuada, optimización eficiente y regularización constante.

