---
cards-deck: Data Science Studies
created: 2025-11-27
modified: 2025-11-27
status: 🌱
tipo_nota: tecnica
---

# Embeddings (Representaciones Vectoriales)

> [!abstract] Objetivo
> Entender cómo el texto se convierte en vectores numéricos y por qué esto es fundamental para RAG

---

## 📚 Definición

Un **embedding** es una representación numérica (vector) de un texto que captura su significado semántico en un espacio vectorial de alta dimensionalidad.

**En términos simples**: Convertir palabras/frases en listas de números de forma que textos con significados similares tengan números similares.

**Analogía**: Es como asignar coordenadas GPS a cada concepto. Conceptos relacionados están "cerca" en el espacio vectorial, conceptos diferentes están "lejos".

---

## ⚙️ Conceptos Clave

### 📌 Vector

**Tipo**: Estructura de datos

**Características**:
- Lista ordenada de números (floats)
- Dimensionalidad fija (ej: 384, 768, 1536)
- Cada dimensión captura un aspecto semántico
- Se puede hacer matemáticas con vectores

**Ejemplo**:
```python
embedding_quicksort = [0.23, -0.45, 0.67, 0.12, ..., 0.89]
# ↑ 384 números que representan "QuickSort"
```

**Relacionado**: [[Álgebra Lineal]] • [[Espacios Vectoriales]]

### 📌 Sentence Transformers

**Tipo**: Modelo de ML

**Características**:
- Basado en BERT/RoBERTa (Transformers)
- Optimizado para generar embeddings de frases completas
- Modelos pre-entrenados disponibles
- Funciona offline (local)
- Rápido: ~1000 frases/segundo

**Modelos populares**:
- `all-MiniLM-L6-v2`: Ligero, 384 dim (22MB) ⭐
- `all-mpnet-base-v2`: Mejor calidad, 768 dim (420MB)
- `paraphrase-multilingual`: Soporte multiidioma

**Relacionado**: [[BERT]] • [[Transformers]] • [[Transfer Learning]]

### 📌 Cosine Similarity (Similitud Coseno)

**Tipo**: Métrica

**Características**:
- Mide el ángulo entre dos vectores
- Rango: -1 (opuestos) a 1 (idénticos)
- Ignora la magnitud, solo dirección
- Muy usado en búsqueda semántica

**Fórmula**:
```
cos(θ) = (A · B) / (||A|| × ||B||)

donde:
- A · B = producto punto
- ||A|| = norma (longitud) del vector A
```

**Relacionado**: [[Similarity Metrics]] • [[Distance Functions]]

### 📌 Semantic Search (Búsqueda Semántica)

**Tipo**: Técnica

**Características**:
- Busca por significado, no por keywords exactos
- Usa embeddings + similarity
- Encuentra resultados conceptualmente relacionados
- Más inteligente que búsqueda tradicional

**Ejemplo**:
```
Query: "algoritmo rápido de ordenar"
Resultados:
  1. QuickSort (0.89)      ← No contiene las palabras exactas
  2. MergeSort (0.85)      ← Pero son semánticamente relevantes
  3. Heap Sort (0.78)
```

**Relacionado**: [[Information Retrieval]] • [[RAG]]

---

## 💻 Ejemplo Práctico
```python
from sentence_transformers import SentenceTransformer

# 1. Cargar modelo pre-entrenado
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Generar embeddings
textos = [
    "QuickSort es un algoritmo eficiente",
    "Algoritmo de ordenamiento rápido",
    "Me gusta practicar surf"
]

embeddings = model.encode(textos)

# 3. Resultado
print(embeddings[0].shape)  # (384,) - vector de 384 dimensiones
print(embeddings[0][:5])    # [0.234, -0.456, 0.678, ...]

# 4. Calcular similitud
from numpy import dot
from numpy.linalg import norm

def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))

sim_1_2 = cosine_similarity(embeddings[0], embeddings[1])
sim_1_3 = cosine_similarity(embeddings[0], embeddings[2])

print(f"QuickSort vs Ordenamiento rápido: {sim_1_2:.2f}")  # ~0.85
print(f"QuickSort vs Surf: {sim_1_3:.2f}")                 # ~0.05
```

**Explicación paso a paso**:

1. **`SentenceTransformer('all-MiniLM-L6-v2')`**: 
   - Carga modelo pre-entrenado (descarga ~22MB primera vez)
   - Este modelo fue entrenado en millones de pares de frases

2. **`model.encode(textos)`**:
   - Cada texto pasa por red neuronal
   - Sale vector de 384 números
   - Captura el "significado" del texto

3. **`cosine_similarity(a, b)`**:
   - Calcula ángulo entre vectores
   - 0.85 = muy similares
   - 0.05 = muy diferentes

---

## 💭 Reflexiones & Conexiones

**Por qué esto es crucial para RAG**:
En mi sistema RAG, cuando hago una pregunta como "¿Qué es QuickSort?", el sistema:
1. Convierte mi pregunta en embedding
2. Busca embeddings similares en mi vault
3. Encuentra mis notas sobre algoritmos (incluso si no dicen "QuickSort" exactamente)

**Conexión con búsqueda tradicional**:
- Google antiguo: busca palabras exactas (keyword matching)
- Google moderno: usa embeddings (semantic search)
- Mi RAG: también usa embeddings → búsqueda "inteligente"

**Matemáticas detrás**:
Los embeddings usan conceptos de:
- [[Álgebra Lineal]]: vectores, productos punto, normas
- [[Cálculo]]: gradientes, backpropagation (durante entrenamiento)
- [[Estadística]]: distribuciones, probabilidades

**Limitaciones importantes**:
1. **Idioma**: Modelos monolingües solo entienden un idioma
2. **Dominio**: Modelos generales pueden no captar jerga específica
3. **Longitud**: Límite de tokens (típicamente 512)
4. **Contexto**: No capturan contexto de documento completo

**Aplicaciones reales**:
- Búsqueda en Google
- Recomendaciones (Netflix, Spotify)
- Traducción automática
- Sistemas de preguntas y respuestas (mi RAG!)

---

## 🎴 Flashcards

¿Qué es un embedding?::Una representación numérica (vector) de texto que captura su significado semántico

¿Cuántas dimensiones tiene el modelo all-MiniLM-L6-v2?::384 dimensiones

¿Qué mide la similitud coseno?::El ángulo entre dos vectores, indicando qué tan similares son semánticamente (rango: -1 a 1)

Embedding de "QuickSort" vs "MergeSort" tendría similitud::==Alta== (ambos son algoritmos de ordenamiento)

Embedding de "QuickSort" vs "Surf" tendría similitud::==Baja== (conceptos no relacionados)

¿Por qué usamos embeddings en RAG?::Para buscar documentos por significado (semantic search) no solo por palabras exactas

Sentence Transformers vs Word2Vec:::Sentence Transformers procesa frases completas con contexto. Word2Vec solo palabras individuales sin contexto

La ventaja de all-MiniLM-L6-v2 es::Ligero (22MB), rápido, y suficientemente preciso para la mayoría de casos

---

## 📚 Referencias & Enlaces

**Enlaces internos**: 
- [[RAG]]
- [[Vector Databases]]
- [[Similarity Metrics]]
- [[Transformers Architecture]]

**Referencias externas**: 
- [Sentence Transformers Documentation](https://www.sbert.net/)
- [Understanding Embeddings](https://simonwillison.net/2023/Oct/23/embeddings/)
- [Cosine Similarity Explained](https://www.machinelearningplus.com/nlp/cosine-similarity/)

**Papers**:
- Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks (Reimers & Gurevych, 2019)

**Fuente**: Implementación en `src/embeddings.py`

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2025-01-XX
- **Próxima revisión**: 2025-01-XX (3 días)
- **Veces revisado**: 0
- **Nivel de comprensión**: 💡 Entiendo bien
- **Tiempo estimado de repaso**: 📖 15 minutos

---

> [!tip] 💡 Experimento para entender mejor
> Prueba generar embeddings de:
> 1. Tu nota de "QuickSort"
> 2. Tu nota de "MergeSort"  
> 3. Tu nota de "Albert Camus"
> 
> Luego calcula similitudes. ¿Los algoritmos están más cerca entre ellos que con filosofía? ¡Debería!