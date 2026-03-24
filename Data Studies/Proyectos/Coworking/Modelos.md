# En esta sección explico los modelos utilizados en el proyecto

## Modelo 1: Similitud de Coseno
#MachineLearning 

[[Similitud de Coseno]]

### Utilización
Este modelo ha sido utilizado en el proyecto con la intención de crear una recomendación sencilla de espacios similares

Entrenado con una matriz de características y precios poniendo cada característica como 1 si existe o 0 si no existe en el coworking para crear un vector que compara diferentes espacios escogiendo con los angulos similares.

## Modelo 2: K-Means

[[K-Means]]

### Utilización
Este modelo ha sido utilizado con la intención de mostrar los tipos de espacios disponible para cada publico haciendo una agrupacio según los precios y algunas características clave

## Modelo 3: RandonForest

[[RandonForest]]

### Utilización
Este modelo ha sido utilizado con la itención de crear un sistema de puntuación para cada espacio, comparandolo con los otros en ralción a precio y características. He creado un sistema artificial de puntos poniendo pesos para cada característica y al final he entrenado el modelo en base a este sistema artificial que ayuda el usuario a comparar el coworking en que ha elegido.