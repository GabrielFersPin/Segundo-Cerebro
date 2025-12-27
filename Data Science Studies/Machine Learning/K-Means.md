#MachineLearning 
# K-Means 

````markdown
# {{K-means}}

## 📌 Resumen

El modelo K-Means es un algoritmo de **aprendizaje no supervisado** ampliamente utilizado para la **agrupación (clustering) de datos**. Su objetivo principal es dividir un conjunto de n observaciones en k grupos o "clusters", donde cada observación pertenece al cluster con la media (o centroide) más cercana.

el **Método del Codo (Elbow Method)** es una de las formas más populares y utilizadas para intentar elegir el valor óptimo de k en K-Means.

**Graficar WCSS vs. k**: Traza un gráfico donde el eje X sea el número de clústeres (k) y el eje Y sea el WCSS.

El punto en el que la curva se "dobla" bruscamente (el "codo") es considerado el valor óptimo de k
## 🔗 Conexiones
- [[Machine Learning]]
- [[]]
	
## 📝 Código Ejemplo
```python
from sklearn.cluster import KMeans
````