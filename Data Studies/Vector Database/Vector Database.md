---
cards-deck: DataScience
created: 2025-27-11
modified: 2025-27-11
status: 🌱
tipo_nota: tecnica
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
---

# Vector Databases (Bases de Datos Vectoriales)

> [!abstract] Objetivo
> Entender qué son las vector databases, por qué son necesarias, y cómo ChromaDB permite búsquedas eficientes en espacios de alta dimensionalidad

---

## 📚 Definición

Una **vector database** es un tipo especializado de base de datos optimizada para almacenar, indexar y buscar vectores de alta dimensionalidad (embeddings) de manera eficiente.

A diferencia de bases de datos tradicionales que buscan coincidencias exactas, las vector databases buscan por **similitud semántica** usando distancias vectoriales.

**Problema que resuelve**: Con miles de embeddings, comparar cada vector contra todos los demás es computacionalmente prohibitivo (O(n)). Las vector databases usan índices especiales para reducir esto a O(log n) o mejor.

---

## ⚙️ Conceptos Clave

### 📌 Approximate Nearest Neighbor (ANN)

**Tipo**: Algoritmo

**Características**:
- Encuentra vecinos "aproximadamente" cercanos
- No garantiza encontrar EL más cercano, pero está muy cerca
- Trade-off: Precisión vs. Velocidad
- Mucho más rápido que búsqueda exhaustiva
- Suficientemente preciso para la mayoría de casos

**Algoritmos populares**:
- HNSW (Hierarchical Navigable Small World)
- IVF (Inverted File Index)
- LSH (Locality-Sensitive Hashing)

**Relacionado**: [[Algoritmos de búsqueda]] • [[Grafos]] • [[Complejidad]]

### 📌 HNSW (Hierarchical Navigable Small World)

**Tipo**: Algoritmo de indexación

**Características**:
- Usado por ChromaDB por defecto
- Construye grafo multi-capa de vectores
- Navegación jerárquica: empieza en capa abstracta → refina
- Muy rápido: O(log n) búsquedas
- Requiere más memoria que otros métodos

**Cómo funciona**:
1. Organiza vectores en capas jerárquicas
2. Capas superiores: pocos nodos, saltos grandes
3. Capas inferiores: muchos nodos, refinamiento
4. Búsqueda navega de capa en capa

**Relacionado**: [[Grafos]] • [[Skip Lists]] • [[Navegación jerárquica]]

### 📌 ChromaDB

**Tipo**: Vector Database

**Características**:
- Open-source, gratuito
- Funciona localmente (no requiere servidor)
- Persistencia con SQLite
- API simple en Python
- Soporte para metadata filtering
- Embeddings automáticos opcionales

**Ventajas**:
- Setup en 2 líneas de código
- Perfecto para desarrollo
- Integración fácil con Python

**Limitaciones**:
- No optimizado para >1M vectores
- No distribuido (single-node)
- Menos features que soluciones enterprise

**Relacionado**: [[RAG]] • [[Embeddings]]

### 📌 Collection (Colección)

**Tipo**: Estructura de datos

**Características**:
- Contenedor lógico de documentos vectoriales
- Similar a tabla en SQL
- Cada collection tiene:
  - Nombre único
  - Función de distancia (cosine, euclidean, etc.)
  - Configuración de índice

**Ejemplo de uso**:
```python
# Diferentes collections para diferentes tipos de datos
notes_collection = client.get_or_create_collection("obsidian_notes")
flashcards_collection = client.get_or_create_collection("flashcards")
```

**Relacionado**: [[Bases de datos]] • [[Organización de datos]]

### 📌 Metadata Filtering

**Tipo**: Técnica

**Características**:
- Permite filtrar antes de calcular similitud
- Reduce espacio de búsqueda
- Más rápido que post-filtering
- Combina búsqueda vectorial con búsqueda tradicional

**Ejemplo**:
```python
# Solo buscar en notas de Algoritmos
results = collection.query(
    query_embeddings=[query_vector],
    n_results=5,
    where={"deck": "Algoritmos"}  # ← Metadata filter
)
```

**Relacionado**: [[Índices de base de datos]] • [[Query optimization]]

---

## 💻 Ejemplo Práctico
```python
import chromadb
from chromadb.config import Settings

# 1. SETUP: Crear cliente
client = chromadb.Client(Settings(
    persist_directory="./chroma_db",
    anonymized_telemetry=False
))

# 2. CREAR COLLECTION
collection = client.get_or_create_collection(
    name="mis_notas",
    metadata={"description": "Notas de Obsidian"}
)

# 3. AÑADIR DOCUMENTOS
collection.add(
    ids=["nota_1", "nota_2", "nota_3"],
    embeddings=[
        [0.1, 0.2, 0.3, ...],  # 384 dimensiones
        [0.2, 0.3, 0.4, ...],
        [0.5, 0.1, 0.2, ...]
    ],
    metadatas=[
        {"deck": "Algoritmos", "file": "quicksort.md"},
        {"deck": "Algoritmos", "file": "mergesort.md"},
        {"deck": "Nube", "file": "docker.md"}
    ],
    documents=[
        "QuickSort es un algoritmo eficiente...",
        "MergeSort usa divide y conquista...",
        "Docker permite containerización..."
    ]
)

# 4. BUSCAR por similitud
results = collection.query(
    query_embeddings=[[0.15, 0.25, 0.35, ...]],  # Query vector
    n_results=2,  # Top-2
    where={"deck": "Algoritmos"}  # Solo algoritmos
)

print(results['documents'])
# ["QuickSort es un algoritmo...", "MergeSort usa divide..."]

# 5. ACTUALIZAR documento
collection.update(
    ids=["nota_1"],
    metadatas=[{"deck": "Algoritmos", "reviewed": True}]
)

# 6. ELIMINAR documento
collection.delete(ids=["nota_3"])

# 7. ESTADÍSTICAS
print(f"Total documentos: {collection.count()}")
```

**Explicación paso a paso**:

1. **Client**: Punto de entrada a ChromaDB
   - `persist_directory`: Dónde guardar datos
   - Persiste automáticamente

2. **Collection**: Como una tabla SQL
   - `get_or_create`: Crea si no existe, obtiene si existe
   - Cada collection aislada de las demás

3. **Add**: Insertar documentos
   - `ids`: Únicos por collection
   - `embeddings`: Vectores (ya calculados)
   - `metadatas`: Info adicional (filtrable)
   - `documents`: Texto original (opcional)

4. **Query**: Buscar similares
   - `query_embeddings`: Vector de búsqueda
   - `n_results`: Cuántos retornar
   - `where`: Filtro de metadata (como SQL WHERE)
   - Retorna: IDs, distancias, documentos, metadata

5-7. **CRUD operations**: Update, Delete, Count

---

## 💭 Reflexiones & Conexiones

**Por qué esto es crucial para RAG**:
Sin vector database, mi sistema RAG tendría que:
1. Cargar TODOS los embeddings en memoria
2. Comparar query con TODOS los vectores
3. Ordenar TODOS los resultados

Con ChromaDB:
1. Solo carga índice en memoria (mucho más pequeño)
2. Usa HNSW para saltar a vecinos probables
3. Solo calcula similitud con ~1000 candidatos vs. 10,000+

**Escalabilidad**:
- 100 notas: Lista simple funciona (10ms)
- 1,000 notas: Lista simple aún OK (50ms)
- 10,000 notas: Vector DB necesaria (10ms vs. 500ms)
- 100,000+ notas: Vector DB obligatoria

**Conexión con estructuras de datos**:
- HNSW es como un [[Skip List]] pero en espacio vectorial
- Metadata filtering usa [[Índices B-tree]]
- Similitud vectorial usa [[KNN]] pero aproximado

**Trade-offs importantes**:
1. **Precisión vs. Velocidad**: ANN sacrifica un poco de precisión por mucha velocidad
2. **Memoria vs. Disco**: Índices en memoria son rápidos pero usan RAM
3. **Insert vs. Query**: ChromaDB optimiza queries, inserts son más lentos

**Comparación con otras opciones**:
- **Pinecone**: Mejor para producción, pero cuesta $$$
- **Weaviate**: Más features, pero setup complejo
- **Qdrant**: Mejor performance, pero overkill para mi caso
- **FAISS**: Más rápido, pero solo in-memory (no persistencia)

**Aplicación en mi proyecto**:
ChromaDB es perfecto porque:
- Tengo ~200-500 notas (escala adecuada)
- Desarrollo local (no necesito cloud)
- Quiero aprender los fundamentos
- Gratis y open-source

---

## 🎴 Flashcards

¿Qué problema resuelven las vector databases?::Búsqueda eficiente en espacios de alta dimensionalidad, evitando comparar con todos los vectores (O(n) → O(log n))

¿Qué significa ANN?::Approximate Nearest Neighbor - encuentra vecinos cercanos aproximadamente, no exactamente, pero mucho más rápido

HNSW significa::Hierarchical Navigable Small World - algoritmo de indexación usado por ChromaDB

ChromaDB usa ==HNSW== para indexar vectores eficientemente

La estructura que contiene documentos vectoriales en ChromaDB se llama::Collection

En ChromaDB, cada documento tiene cuatro componentes principales::==ID único==, ==embedding (vector)==, ==metadata (dict)==, ==document (texto)==

Ventaja de ChromaDB sobre Pinecone:::ChromaDB es gratuito y local. Pinecone es paid y cloud

¿Qué es metadata filtering?::Filtrar documentos por propiedades antes de calcular similitud vectorial (ej: solo deck="Algoritmos")

La complejidad de búsqueda en lista naive es::O(n) - compara con todos

La complejidad de búsqueda con HNSW es::O(log n) - navegación jerárquica

---

## 📚 Referencias & Enlaces

**Enlaces internos**: 
- [[RAG]]
- [[Embeddings]]
- [[Algoritmos de búsqueda]]
- [[Grafos]]

**Referencias externas**: 
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [HNSW Paper](https://arxiv.org/abs/1603.09320)
- [Vector Databases Explained](https://www.pinecone.io/learn/vector-database/)

**Comparaciones**:
- [ChromaDB vs Pinecone vs Weaviate](https://benchmark.vectorview.ai/)

**Fuente**: Implementación en `src/vectorstore.py`

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2025-01-XX
- **Próxima revisión**: 2025-01-XX (3 días)
- **Veces revisado**: 0
- **Nivel de comprensión**: 💡 Entiendo bien
- **Tiempo estimado de repaso**: 📖 15 minutos

---

> [!tip] 💡 Experimento mental
> Si tuvieras 10,000 notas y cada búsqueda comparara con todas:
> - 10,000 comparaciones × 0.01ms = 100ms
> - Con HNSW: ~1,000 comparaciones × 0.01ms = 10ms
> - **10x más rápido**, y la diferencia crece con más datos