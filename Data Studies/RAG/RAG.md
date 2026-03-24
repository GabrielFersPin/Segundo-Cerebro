---
cards-deck: DataScience
created: 2025-01-XX
modified: 2025-01-XX
status: 🌱
tipo_nota: tecnica
---

# RAG (Retrieval-Augmented Generation)

> [!abstract] Objetivo
> Entender cómo funciona RAG y por qué lo uso en mi sistema de segundo cerebro

---

## 📚 Definición

RAG es una técnica que combina recuperación de información (Retrieval) con generación de texto (Generation) usando LLMs.

**Problema que resuelve**: Los LLMs tienen conocimiento general pero no saben sobre MIS datos específicos. RAG permite que el LLM responda basándose en mi información personal.

**Analogía**: Es como tener un asistente muy inteligente (Claude) pero con acceso a mis apuntes personales. Sin RAG, el asistente solo sabe lo que aprendió en internet. Con RAG, puede leer mis notas antes de responder.

---

## ⚙️ Conceptos Clave

### 📌 Retrieval (Recuperación)

**Tipo**: Técnica

**Características**:
- Busca documentos relevantes en una base de datos
- Usa similitud semántica (no solo keywords)
- Retorna top-K documentos más relevantes
- Es RÁPIDO (milisegundos)

**Relacionado**: [[Embeddings]] • [[Similarity Search]] • [[Vector Databases]]

### 📌 Augmentation (Aumento)

**Tipo**: Técnica

**Características**:
- Construye un prompt enriquecido con contexto
- Combina: pregunta del usuario + documentos recuperados
- Gestiona el context window del LLM
- Formatea la información de manera óptima

**Relacionado**: [[Prompt Engineering]] • [[Context Window]]

### 📌 Generation (Generación)

**Tipo**: Técnica

**Características**:
- El LLM genera respuesta basada en el contexto aumentado
- Puede citar fuentes específicas
- Reduce alucinaciones (porque tiene fuentes reales)
- Personalizado a mis datos

**Relacionado**: [[LLMs]] • [[Claude API]]

---

## 💻 Ejemplo Práctico
```python
# Ejemplo simplificado de RAG

# 1. RETRIEVAL: Buscar notas relevantes
query = "¿Qué es QuickSort?"
relevant_notes = vector_db.search(query, top_k=3)
# Resultado: [nota_algoritmos.md, nota_complejidad.md, nota_sorting.md]

# 2. AUGMENTATION: Construir contexto
context = f"""
Basándote en mis notas:

Nota 1: {relevant_notes[0].content}
Nota 2: {relevant_notes[1].content}
Nota 3: {relevant_notes[2].content}

Pregunta: {query}
"""

# 3. GENERATION: Claude responde
response = claude.generate(context)
# Respuesta personalizada basada en MIS notas
```

**Explicación del código**:
- `vector_db.search()`: Busca en mi base de datos vectorial
- `top_k=3`: Devuelve las 3 notas más similares
- El contexto incluye el contenido real de mis notas
- Claude lee TODO esto antes de responder

---

## 💭 Reflexiones & Conexiones

**Conexión con mi Zettelkasten**: 
RAG es como automatizar el proceso manual que hago cuando estudio. Normalmente busco en mis notas → leo varias → sintetizo. RAG hace esto automáticamente.

**Conexión con Ciencia de Datos**:
- Retrieval = Information Retrieval (búsqueda)
- Embeddings = Feature engineering en NLP
- Vector DB = Nearest Neighbor Search

**Aplicación en mi RPG app**:
Podría usar RAG para que mi app sugiera objetivos basándose en lo que YO he aprendido sobre alcanzar metas. Datos personalizados > datos genéricos.

**Diferencia clave vs. fine-tuning**:
- Fine-tuning: Reentrenar el modelo (caro, lento, necesita muchos datos)
- RAG: Agregar contexto en tiempo real (barato, rápido, flexible)

---

## 🎴 Flashcards

¿Qué significa RAG?::Retrieval-Augmented Generation (Generación Aumentada por Recuperación)

¿Cuáles son las 3 etapas de RAG?::1) Retrieval (buscar documentos), 2) Augmentation (agregar contexto), 3) Generation (generar respuesta)

¿Por qué RAG es mejor que LLM puro para mi caso de uso?::Porque el LLM solo tiene conocimiento general, pero RAG le permite acceder a MIS notas específicas y responder basándose en MI conocimiento

RAG vs Fine-tuning:::RAG agrega contexto dinámicamente (rápido, barato). Fine-tuning modifica el modelo (lento, caro, necesita muchos datos)

El componente que busca documentos relevantes en RAG se llama ==Retrieval==

La técnica que reduce alucinaciones al dar fuentes reales al LLM es ==RAG==

---

## 📚 Referencias & Enlaces

**Enlaces internos**: 
- [[Embeddings]]
- [[Vector Databases]]
- [[Claude API]]
- [[Prompt Engineering]]

**Referencias externas**: 
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [Anthropic RAG Guide](https://docs.anthropic.com/)

**Fuente**: Implementación propia en `obsidian-rag-system`

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2025-01-XX
- **Próxima revisión**: 2025-01-XX (3 días)
- **Veces revisado**: 0
- **Nivel de comprensión**: 💡 Entiendo bien
- **Tiempo estimado de repaso**: 📖 15 minutos

---

> [!tip] 💡 Próximos pasos
> 1. Crear nota sobre [[Embeddings]]
> 2. Crear nota sobre [[Vector Databases]]
> 3. Implementar versión simplificada de RAG