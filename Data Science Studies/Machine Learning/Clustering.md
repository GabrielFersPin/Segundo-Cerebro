#Python 

# ## **🔹 ¿Qué es Clustering?**
    
    El clustering es un método de **aprendizaje no supervisado** que agrupa datos según su similitud, sin necesidad de etiquetas. Se usa en segmentación de clientes, detección de anomalías, agrupación de imágenes, entre otros.
    
    ## **🔹 Principales Algoritmos de Clustering**
    
    ### **1️⃣ K-Means** (Clustering Particional)
    
    - Usa *k* centroides para dividir los datos en *k* clusters.
    - Pasos:
        1. Se eligen *k* centroides iniciales.
        2. Cada punto se asigna al centroide más cercano.
        3. Se recalculan los centroides como la media de los puntos asignados.
        4. Se repite hasta que los centroides se estabilicen.
    - **Ventajas**: Rápido y eficiente en grandes datasets.
    - **Desventajas**: No maneja bien outliers ni clusters no esféricos.
    
    ### **2️⃣ Clustering Jerárquico (Aglomerativo vs. Divisivo)**
    
    - **Aglomerativo**: Cada punto es un cluster y se fusionan hasta formar uno solo.
    - **Divisivo**: Comienza con un solo cluster y se divide hasta obtener los clusters finales.
    - Se representa con un **dendrograma**.
    - **Ventaja**: No requiere predefinir *k*.
    - **Desventaja**: Computacionalmente costoso.
    
    ### **3️⃣ DBSCAN (Clustering Basado en Densidad)**
    
    - Encuentra clusters de **formas irregulares** y **detecta outliers**.
    - Define clusters según la **densidad** de puntos cercanos.
    - **Ventaja**: No necesita definir *k*.
    - **Desventaja**: Sensible a los parámetros de densidad (*epsilon* y *min_samples*).

## **🔹 Cómo Elegir el Número de Clusters (k)**
    
    ### **1️⃣ Técnica del Codo (Elbow Method)**
    
    - Se grafica *k* vs. la **inercia (WCSS)**.
    - El punto donde la inercia deja de disminuir significativamente es el "codo" y representa el *k* óptimo.
    
    ### **2️⃣ Silhouette Score**
    
    - Mide qué tan bien separado está un punto de otros clusters.
    - Valores cercanos a **1** indican clusters bien formados.
    - Valores **negativos** indican que el punto está en el cluster equivocado.

## **🔹 Evaluación de la Calidad del Clustering**
    
    ✅ **Silhouette Score**: Evalúa cohesión y separación.
    
    ✅ **Índice de Dunn**: Relación entre la distancia mínima entre clusters y la máxima dentro de un cluster.
    
    ✅ **Índice de Davies-Bouldin**: Cuantifica la compactación y separación de los clusters.

    ## **🔹 Visualización de Clustering**
    
    - **Gráficas 3D** → Útiles si los datos tienen 3 dimensiones.
    - **PCA (Análisis de Componentes Principales)** → Reduce dimensiones para visualización 2D/3D.
    - **t-SNE y UMAP** → Técnicas avanzadas para visualizar relaciones en datos de alta dimensión.
### **🌟 Resumen Final**
    
    📌 El clustering agrupa datos sin etiquetas según similitudes.
    
    📌 **K-Means** es el más común pero **DBSCAN** maneja mejor ruido y formas irregulares.
    
    📌 La **Técnica del Codo y el Silhouette Score** ayudan a elegir el mejor *k*.
    
    📌 Se puede evaluar la calidad de los clusters con varias métricas.

## Evaluate the method

### Silhouette Score
The **Silhouette Score** is one of the most popular metrics for evaluating the quality of clusters. It measures how similar each point is to its own cluster compared to other clusters. The silhouette score ranges from -1 to 1:
- A score close to 1 means that the points are well-clustered.
- A score close to 0 means that the point lies between two clusters.
- A score close to -1 means that the point might have been assigned to the wrong cluster.
```python
from sklearn.metrics import silhouette_score

# For DBSCAN, use the predicted labels for clustering (dbscan_labels)
# For KMeans, use the cluster labels (kmeans_labels)
score = silhouette_score(X_combined, kmeans_labels)  # Or use dbscan_labels
print(f"Silhouette Score: {score}")

```
