````markdown
# {{Similitud de Coseno}}

## 📌 Resumen

El **modelo de similitud de coseno** es una métrica utilizada para medir la similitud entre dos vectores no nulos en un espacio de producto interior. Se calcula como el coseno del ángulo entre los dos vectores. Un valor de 1 indica que los vectores apuntan exactamente en la misma dirección (máxima similitud), un valor de 0 indica que son ortogonales (no hay similitud lineal) y un valor de -1 indica que apuntan en direcciones opuestas (máxima disimilitud).

## 🔗 Conexiones
- [[Machine Learning]]
- [[]]
	
## 📝 Código Ejemplo
```python
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity
````