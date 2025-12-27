#DeepLearnig
# Stochastic Gradient Descent (SGD)

>[!Definición]
>-  ¿Qué es SGD?:: Es una aproximación estocastica de la optimización descenso del gradiente



>[!Ventaja]
>- Reduce la carga computacional 

## Momentum Optimization
>[!Definición]
>- Recuerda el incremento aplicado a las variables en cada iteración
>- Determina la siguiente iteración como una combinación lineal entre el gradiente y el incremento anterior
>- Aplica a los incrementos cierta 'inercia'.#
# Nesterov Accelerated Gradient
>[!Definiición]
>- Es como la [[Optimización del descenso del gradiente#Momentum Optimization]], pero intenta que los incrementos disminuyan cuando el algoritmo se acerca al mínimo buscado

[[Nesterov]]
# AdaGrad
>[!Definición]
>- Utiliza diferentes tasas de aprendizaje para las variables teniendo en cuenta el gradiente acumulado en cada una de ellas

>[!Ventajas]
>- Mejora el rendimiento de la convergencia con respecto al descenso de gradiiente estocástico
>- Mejores en entornos con menos datos y parámetros

# RMSProp (Root Per Mean Square Propagation)
>[!Definición]
>- La tasa de aprendizaje se adpata a cada uno de los parámetros 
>- Variación de AdaGrad 
>- Considera solo los gradientes más recientes 
>- La idea es dividir la tasa de aprendizaje para un peso por media corrida de las magnitudes de los gradientes recientes para ese peso.

# Adam Optimization (Adaptative Moment Optimization)
>[!Definición]
>- Combina [[#RMSProp (Root Per Mean Square Propagation)]] con [[#Momentum Optimization]]
>- Se utilizan los promedios de los gradientes y los segundos momentos de los gradientes.

# Mini-Batches Training
>[!Defiinición]
>- Calcula el gradiente a partir de pequeños grupos de entrenamiento
>- Se entrena más facilmente que el [[Optimización del descenso del gradiente#Stochastic Gradient Descent (SGD)]], pero con el riesgo de caer más facilmente al mínimo local.