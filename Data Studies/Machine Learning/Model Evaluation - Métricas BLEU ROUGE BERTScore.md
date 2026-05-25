---
tags:
  - evaluación
  - métricas
  - NLP
  - modelos
deck: Obsidian::Evaluación de Modelos
created: 2026-05-11 11:00
modified: 2026-05-11 11:00
status: 🟡
tipo_nota: clase
profesor: No especificado
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
cards-deck: ""
---

# 📝 Model Evaluation - Métricas BLEU, ROUGE y más

> [!info] Metadata de la clase
> **Fecha**: 2026-05-11
> **Hora**: 11:00
> **Profesor**: No especificado
> **Estado**: 🟡 Por procesar

---

## 🎯 Objetivo de la clase

Entender las principales métricas de evaluación para modelos de lenguaje (BLEU, ROUGE, METEOR, BERTScore) y cuándo usar cada una en diferentes contextos.

---

## 📊 Captura Rápida

### ⚡ Notas Rápidas
- Las métricas de evaluación cuantifican qué tan bien un modelo cumple una tarea.
- BLEU mide similitud con referencia por n-gramas (traducción automática).
- ROUGE mide coincidencias de n-gramas y secuencias (resúmenes).
- BERTScore usa embeddings semánticos para evaluación más profunda.
- Ninguna métrica es perfecta: combinar varias da mejor visión.

### 🔑 Conceptos Clave
- **Métrica de referencia**: compara output con respuesta "correcta" esperada.
- **Métrica sin referencia**: evalúa sin depender de una respuesta predefinida.
- **N-grama**: secuencia de N palabras (unigrama, bigrama, trigrama).
- **Precision y recall**: cobertura de lo correcto vs lo generado.
- **Score normalizado**: valores entre 0 y 1 para fácil interpretación.

### ❓ Dudas
- ¿Qué métrica debo usar para mi tarea específica?
- ¿Por qué BLEU y ROUGE a veces dan resultados contradictorios?
- ¿Cómo evalúo tareas sin respuesta única correcta (generación creativa)?

### 💡 Insights
- Una métrica con score alto no garantiza calidad percibida por humanos.
- Evaluar siempre con múltiples métricas y juicio humano.
- La métrica ideal debe correlacionar con evaluación humana.

### ⚠️ Importante
- No confiar en una sola métrica para decisiones críticas.
- Conocer las limitaciones de cada métrica es tan importante como usarlas.
- Métricas automatizadas son herramientas, no jueces definitivos.

---

## 📝 Notas Detalladas

### ¿Qué son las métricas de evaluación?

Las métricas de evaluación cuantifican qué tan bien un modelo genera texto comparándolo con referencias o criterios específicos. Son fundamentales para:
- Medir progreso durante el entrenamiento.
- Comparar diferentes modelos.
- Detectar regresiones o mejoras.
- Validar calidad de salidas.

---

## 🔍 Métricas principales

### 1. **BLEU (Bilingual Evaluation Understudy)**

**Uso**: Traducción automática, principalmente.

**Cómo funciona**:
- Compara n-gramas del texto generado con referencias.
- Calcula precisión: qué porcentaje de n-gramas generados están en las referencias.
- Aplica penalización si el texto es demasiado corto.

**Fórmula simplificada**:
$$\text{BLEU} = BP \times \exp\left(\sum_{n=1}^{N} w_n \log p_n\right)$$

Donde:
- $BP$ = penalty por brevedad
- $p_n$ = precisión de n-gramas
- $w_n$ = pesos (típicamente 0.25 para cada n)

**Rango**: 0-1 (0 = pésimo, 1 = perfecto)

**Ventajas**:
- Rápido de calcular.
- Métrica estándar en traducción.
- Reproducible.

**Limitaciones**:
- No considera significado semántico.
- Penaliza paráfrasis válidas.
- Requiere múltiples referencias para ser confiable.

**Ejemplo**:
```
Referencia: "El gato está en la mesa"
Generado: "El gato está sobre la mesa"
BLEU bajo porque "sobre" ≠ "en" (cambio de palabra)
```

---

### 2. **ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**

**Uso**: Resúmenes de texto, generación de abstractos.

**Variantes principales**:

#### ROUGE-N
Compara n-gramas entre resumen generado y referencias.

```
ROUGE-1: unigramas
ROUGE-2: bigramas
ROUGE-L: secuencias más largas (LCS)
```

**Fórmula**:
$$\text{ROUGE-N} = \frac{\sum_{\text{ref}} \sum_{\text{n-grama}} \min(\text{count}_{\text{gen}}(\text{n-grama}), \text{count}_{\text{ref}}(\text{n-grama}))}{\sum_{\text{ref}} \sum_{\text{n-grama}} \text{count}_{\text{ref}}(\text{n-grama})}$$

**Rango**: 0-1

**Ventajas**:
- Mejor para resúmenes que BLEU.
- Múltiples variantes capturan diferentes aspectos.
- Considera recall, no solo precisión.

**Limitaciones**:
- Igual que BLEU: superficial, no semántica.
- Sensible a paráfrasis.

**Ejemplo**:
```
Referencia: "El cambio climático es una amenaza global"
Generado: "El cambio climático representa una amenaza mundial"
ROUGE-1 alto (palabras coinciden)
ROUGE-L también consideraría la secuencia
```

---

### 3. **METEOR (Metric for Evaluation of Translation with Explicit Ordering)**

**Uso**: Traducción automática, mejor que BLEU.

**Cómo funciona**:
- Alinea palabras entre referencia y generado.
- Considera sinónimos y formas morfológicas.
- Penaliza fragmentación y desorden.

**Ventajas**:
- Mejor correlación con juicio humano que BLEU.
- Maneja paráfrasis y sinónimos.
- Considera orden de palabras.

**Limitaciones**:
- Más lento que BLEU.
- Requiere recursos lingüísticos (diccionarios de sinónimos).

---

### 4. **BERTScore**

**Uso**: Evaluación general de generación de texto, semánticamente más profunda.

**Cómo funciona**:
- Usa embeddings de BERT para obtener representaciones semánticas.
- Compara similaridad coseno entre palabras.
- Calcula precisión, recall y F1 a nivel semántico.

**Ventajas**:
- Captura significado semántico, no solo palabras exactas.
- Correlación más alta con evaluación humana.
- No requiere referencias múltiples (aunque las usa si existen).

**Limitaciones**:
- Costoso computacionalmente.
- Dependiente del modelo BERT subyacente.
- Puede ser demasiado permisivo con paráfrasis.

**Ejemplo**:
```
Referencia: "El gato duerme en la cama"
Generado: "El felino descansa sobre el lecho"
BERTScore: alto (similitud semántica)
BLEU: bajo (palabras diferentes)
```

---

### 5. **METEOR vs ROUGE vs BLEU**

| Métrica | Mejor para | Velocidad | Semántica |
|---------|-----------|-----------|-----------|
| BLEU | Traducción | ⚡⚡⚡ | ❌ |
| ROUGE | Resúmenes | ⚡⚡ | ❌ |
| METEOR | Traducción+ | ⚡ | Parcial |
| BERTScore | General | 🐌 | ✅ |

---

### 6. **Otras métricas relevantes**

- **CHRF**: Character n-gram F-score (idiomas aglutinadores).
- **TER** (Translation Edit Rate): ediciones necesarias.
- **CIDEr**: Para generación de captions de imágenes.
- **SPICE**: Semantic Propositional Content.
- **Evaluación humana**: ALWAYS gold standard.

---

## 🔗 Cuándo usar cada métrica

| Tarea | Métrica recomendada |
|-------|-------------------|
| Traducción automática | BLEU, METEOR, BERTScore |
| Resumen de texto | ROUGE, BERTScore |
| Generación de diálogo | BERTScore, evaluación humana |
| Generación creativa | Evaluación humana + BERTScore |
| QA (pregunta-respuesta) | ROUGE, BERTScore |
| Reconocimiento entidades | Precision/Recall, F1 |

---

## ⚠️ Limitaciones comunes

1. **Paradoja del score alto**: alta métrica ≠ buena calidad
2. **Sesgo de referencia**: lo "correcto" puede tener múltiples formas
3. **Contexto ignorado**: métricas no entienden intención
4. **Sobreajuste**: optimizar para métrica puede degradar calidad real

---

## 🔄 Procesamiento Post-Clase

### 📋 Checklist de Procesamiento
- [ ] Implementar cálculo de BLEU, ROUGE, BERTScore en código.
- [ ] Comparar resultados en un dataset de prueba.
- [ ] Entender correlación con evaluación humana.
- [ ] Documentar en qué contexto usar cada métrica.
- [ ] Conectar con prompt engineering y evaluación de agentes.

### 🎯 Acciones Prioritarias
1. Instalar librerías (`rouge-score`, `bert-score`, `nltk`).
2. Practicar cálculo manual de BLEU en pequeños ejemplos.
3. Comparar múltiples métricas en tu tarea específica.

### 🔗 Conexiones
- [[Prompt Engineering - Técnicas y mejores prácticas]]
- [[A2A - Agent-to-Agent]]
- [[CrewAI]]
- [[FastMCP - Ejemplo de implementación]]

---

## 🎴 Flashcards Rápidas
¿Para qué sirven las métricas de evaluación?::Cuantificar qué tan bien un modelo cumple una tarea y comparar modelos. #card
¿Cuál es la diferencia entre BLEU y ROUGE?::BLEU para traducción, ROUGE para resúmenes. Ambas usan n-gramas. #card
¿Por qué BERTScore es mejor que BLEU?::Captura significado semántico además de coincidencias exactas de palabras. #card
¿Qué es el trade-off entre precisión y recall?::Precisión = exactitud; Recall = cobertura. F1 es el balance. #card
