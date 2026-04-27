---
titulo: Vector Databases para Búsqueda Semántica
contexto: Infraestructura-Nube
tipo_nota: tecnica
dificultad: ⭐⭐⭐☆☆
status: 🌱
proxima_revision: 2026-04-12
---

# Vector Databases para Búsqueda Semántica

## Definición

Una **Vector Database** es una base de datos especializada optimizada para almacenar y buscar vectores de alta dimensionalidad (embeddings) de manera eficiente.

A diferencia de bases de datos tradicionales que buscan coincidencias exactas, las vector databases buscan por **similitud semántica** usando distancias vectoriales como similitud del coseno.

## Conceptos Clave

### Approximate Nearest Neighbor (ANN)
- Encuentra vecinos "aproximadamente" cercanos sin garantizar el más cercano
- Trade-off: Precisión vs. Velocidad
- Algoritmos: HNSW, IVF, LSH

### HNSW (Hierarchical Navigable Small World)
- Algoritmo de indexación jerárquico
- Muy rápido para búsquedas
- Ampliamente usado en ChromaDB

## Ejemplo Práctico

```python
import chromadb

# Crear cliente
client = chromadb.Client()

# Crear colección
collection = client.create_collection(name="embeddings")

# Agregar embeddings
collection.add(
    ids=["id1", "id2"],
    embeddings=[[1.0, 2.0], [3.0, 4.0]],
    documents=["doc1", "doc2"]
)

# Buscar similar
results = collection.query(
    query_embeddings=[[1.1, 2.1]],
    n_results=1
)
```

## Conexiones

[[Embeddings]] • [[Búsqueda Semántica]] • [[Algoritmos de Indexación]] • [[ChromaDB]]

## 🃏 Flashcards

¿Qué es un Vector Database?::Una base de datos optimizada para almacenar y buscar embeddings en espacios de alta dimensionalidad
¿Cuál es el principal algoritmo usado en ChromaDB?::HNSW (Hierarchical Navigable Small World)
¿Qué busca un Vector Database?::Similitud semántica entre vectores usando distancias vectoriales
¿Cuál es el trade-off en ANN?::Precisión vs Velocidad (no garantiza el resultado exacto más cercano)
¿Qué es un embedding?::Una representación vectorial de alta dimensionalidad de un concepto o documento


## 🔗 Notas relacionadas
[[Embeddings]]
[[ChromaDB]]
[[Búsqueda Semántica]]

## 🃏 Flashcards

¿Qué es un Vector Database?::Una base de datos optimizada para almacenar y buscar embeddings

¿Cuál es el principal algoritmo?::HNSW

¿Qué busca?::Similitud semántica entre vectores

¿Trade-off en ANN?::Precisión vs Velocidad

¿Qué es embedding?::Representación vectorial de alta dimensionalidad