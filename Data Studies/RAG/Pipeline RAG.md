---
cards-deck: DataScience
created: 2025-11-18
modified: 2025-11-18
status: 🌱
tipo_nota: tecnica
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
---

# Pipeline RAG (Flujo completo)

> [!abstract] Objetivo
> Entender cómo se integran todos los componentes del RAG en un pipeline end-to-end

---

## 📚 Definición

Un **Pipeline RAG** es la orquestación completa de todos los componentes necesarios para:
1. Indexar documentos (una vez)
2. Procesar queries (muchas veces)
3. Generar respuestas contextualizadas

Es el "pegamento" que une: Loader → Embeddings → VectorDB → LLM

---

## ⚙️ Conceptos Clave

### 📌 Indexación (Index Time)

**Tipo**: Proceso batch (una vez o periódico)

**Pasos**:
1. Cargar documentos del vault
2. Generar embeddings
3. Almacenar en vector database
4. Crear índices

**Cuándo**: 
- Primera vez (setup)
- Cuando añades/modificas notas
- Periódicamente (cron job)

**Relacionado**: [[ETL]] • [[Batch Processing]]

### 📌 Query Time (Tiempo de consulta)

**Tipo**: Proceso online (cada búsqueda)

**Pasos**:
1. Convertir query a embedding
2. Buscar similares en vector DB
3. Recuperar contexto relevante
4. Construir prompt aumentado
5. LLM genera respuesta

**Latencia típica**: 500ms - 2s

**Relacionado**: [[RAG]] • [[Retrieval]]

### 📌 Incremental Updates

**Tipo**: Optimización

**Problema**: Reindexar TODO es lento

**Solución**: Solo procesar notas nuevas/modificadas

**Implementación**:
- Trackear última fecha de indexación
- Comparar `last_modified` de archivos
- Solo reindexar cambios

**Relacionado**: [[Caching]] • [[Optimization]]

---

## 💻 Ejemplo de Pipeline
```python
# Pipeline completo simplificado

class RAGPipeline:
    def __init__(self, vault_path):
        self.loader = ObsidianLoader(vault_path)
        self.embedder = EmbeddingGenerator()
        self.store = ObsidianVectorStore()
        self.claude = ClaudeClient()
    
    def index(self):
        # 1. Cargar notas
        notas = self.loader.load_notes()
        
        # 2. Generar embeddings
        contents = [n['content'] for n in notas]
        embeddings = self.embedder.embed_batch(contents)
        
        # 3. Guardar en DB
        self.store.create_collection("notas")
        self.store.add_notes("notas", notas, embeddings)
    
    def query(self, pregunta, n_results=5):
        # 1. Query → embedding
        query_emb = self.embedder.embed_text(pregunta)
        
        # 2. Buscar similares
        results = self.store.search("notas", query_emb, n_results)
        
        # 3. Construir contexto
        contexto = self._build_context(results)
        
        # 4. LLM genera respuesta
        respuesta = self.claude.generate(pregunta, contexto)
        
        return respuesta
```

---

## 💭 Reflexiones & Conexiones

**Trade-offs importantes**:

1. **Indexación completa vs Incremental**:
   - Completa: Simple, siempre actualizada, pero lenta
   - Incremental: Rápida, compleja, puede desincronizar

2. **Número de resultados (n_results)**:
   - Pocos (3-5): Rápido, pero puede perder contexto
   - Muchos (10-20): Más contexto, pero:
     - Más lento
     - Más tokens (más caro)
     - Puede confundir al LLM

3. **Frecuencia de reindexación**:
   - Cada cambio: Siempre fresh, pero costoso
   - Periódica: Balance, requiere scheduler
   - Manual: Control total, puede olvidarse

**Conexión con mi workflow**:
- Indexo una vez al día (cron)
- Queries son instantáneas
- Actualización manual cuando hago cambios grandes

**Optimizaciones posibles**:
- Cache de queries frecuentes
- Batch de queries similares
- Precompute embeddings de queries comunes

---

## 🎴 Flashcards

Las dos fases principales del RAG son::==Index time== (indexación) y ==Query time== (consulta)

Index time incluye estos pasos::Cargar documentos → Generar embeddings → Almacenar en vector DB

Query time incluye::Query → Embedding → Búsqueda → Contexto → LLM → Respuesta

¿Por qué usar incremental updates?::Para no reindexar todo el vault cada vez, solo procesar notas nuevas/modificadas

Trade-off de n_results:::Pocos (3-5) = rápido pero menos contexto. Muchos (10-20) = más contexto pero más lento y caro

---

## 📚 Referencias & Enlaces

**Enlaces internos**: 
- [[RAG]]
- [[Embeddings]]
- [[Vector Databases]]
- [[Claude API]]

**Fuente**: Implementación en `src/rag_chain.py`

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2025-01-XX
- **Próxima revisión**: 2025-01-XX (3 días)
- **Veces revisado**: 0
- **Nivel de comprensión**: 💡 Entiendo bien
- **Tiempo estimado de repaso**: 📖 15 minutos