#MachineLearning 
# Machine Learning Resume

1️⃣ Concepto Básico del Aprendizaje Automático
El aprendizaje automático es un proceso en el que un modelo aprende patrones a partir de datos sin necesidad de programación explícita. Se usa para hacer predicciones o encontrar patrones ocultos en los datos.

2️⃣ Fases Principales del Aprendizaje Automático

🔹 1. Recopilación y preparación de datos

- Se obtienen los datos y se preprocesan: limpieza, eliminación de valores nulos, normalización, etc.
- Se dividen los datos en conjunto de entrenamiento (80%) y conjunto de prueba (20%).

🔹 2. Elección del modelo

- Dependiendo del problema, se elige un modelo adecuado:
    - Clasificación: cuando la variable objetivo es categórica (ej. "spam" o "no spam").
    - Regresión: cuando la variable objetivo es numérica (ej. predecir precios de casas).
    - Clustering: para agrupar datos sin etiquetas (ej. segmentación de clientes).

🔹 3. Entrenamiento del modelo

- Se alimenta al modelo con los datos de entrenamiento.
- El modelo ajusta sus parámetros internos para minimizar el error.
- Se usa una función de costo (ej. error cuadrático medio en regresión) para medir qué tan bien se ajusta el modelo.

🔹 4. Ajuste de hiperparámetros

- Aquí es donde se optimiza el modelo para mejorar su rendimiento.
- Los hiperparámetros son configuraciones externas que afectan el aprendizaje del modelo, como:
    - Tasa de aprendizaje (learning rate): qué tan rápido aprende el modelo.
    - Número de árboles en Random Forest o cantidad de neuronas en redes neuronales.
    - Regularización: para evitar sobreajuste (overfitting).
- Se ajustan probando distintos valores y validando el rendimiento con un conjunto de validación.

🔹 5. Evaluación del modelo

- Se usa el conjunto de prueba para medir qué tan bien generaliza el modelo con datos nuevos.
- Algunas métricas comunes para evaluar modelos son:
    - Precisión, Recall y F1-score en clasificación.
    - Error cuadrático medio (MSE) o R² en regresión.

🔹 6. Interpretación de resultados y mejora

- Si el modelo no es bueno, hay varias estrategias para mejorarlo:
    - Recoger más datos o limpiarlos mejor.
    - Probar otro modelo más adecuado.
    - Ajustar hiperparámetros (usando técnicas como Grid Search o Random Search).
    - Manejo de desbalance de clases en clasificación.
    - Uso de técnicas como reducción de dimensionalidad.

3️⃣ Cómo Interpretar los Resultados

✅ Clasificación:

- Precisión (Accuracy): Porcentaje de predicciones correctas.
- Matriz de confusión: Muestra errores específicos (falsos positivos y falsos negativos).
- F1-score: Buen balance entre precisión y recall cuando hay datos desbalanceados.

✅ Regresión:

- MSE (Error Cuadrático Medio): Cuánto se desvía en promedio la predicción del valor real.
- R² (Coeficiente de Determinación): Qué tan bien el modelo explica la variabilidad de los datos (1 es perfecto, 0 significa que no explica nada).

💡 Resumen Final
El proceso de aprendizaje automático no termina solo con entrenar un modelo, sino que hay que evaluarlo, interpretarlo y ajustarlo para lograr una buena predicción. Los hiperparámetros se afinan para mejorar el rendimiento, y la evaluación con métricas te ayuda a entender qué tan bien funciona.