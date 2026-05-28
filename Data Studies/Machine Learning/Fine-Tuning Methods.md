---
created: 2026-05-22 09:34
modified: 2026-05-22 09:34
area: Machine Learning
tipo_nota: captura_rapida
status: 🔴 Por procesar
nivel-comprension: "❓"
proxima-revision: 2026-05-29
ultima-revision: 2026-05-22
veces-revisado: 0
tiempo-repaso: ""
cards-deck: 
procesamiento: CAPTURA-RAPIDA
prioridad: EXAMEN-PROXIMO
tipo-captura: concepto
complejidad: ⭐
origen: Curso
urgente: false
tags: 
deck: Obsidian::Fine-Tuning
profesor: No especificado
---


# 📝 Fine-Tuning Methods

> [!info] Metadata de la clase
> **Fecha**: 2026-05-11
> **Hora**: 11:30
> **Profesor**: No especificado
> **Estado**: 🟡 Por procesar

---

## 🎯 Objetivo de la clase

Entender los métodos de fine-tuning para modelos de lenguaje y aprendizaje profundo: cuándo usar cada técnica y cuáles son sus ventajas y limitaciones.

---

## 📊 Captura Rápida

### ⚡ Notas Rápidas
- Fine-tuning es ajustar un modelo pre-entrenado a una tarea específica.
- Métodos comunes: full fine-tuning, freeze layers, LoRA, adapters, delta tuning.
- Cada técnica busca equilibrio entre calidad, costo computacional y memoria.
- En NLP, el fine-tuning a menudo mejora rendimiento en tareas específicas.

### 🔑 Conceptos Clave
- **Pre-trained model**: modelo entrenado en datos generales.
- **Fine-tuning**: ajuste posterior con datos de tarea concreta.
- **Parameter-efficient tuning**: ajustar menos parámetros para reducir costo.
- **Transfer learning**: reutilizar conocimiento previo en nuevas tareas.

### ❓ Dudas
- ¿Cuándo conviene usar LoRA en lugar de full fine-tuning?
- ¿Cómo elegir qué capas congelar?
- ¿Qué tamaño de dataset es suficiente para fine-tuning?

### 💡 Insights
- Los métodos de fine-tuning eficientes son clave para usar LLMs con recursos limitados.
- Algunas técnicas permiten actualizar modelos sin guardar pesos completos.
- El fine-tuning puede reducir alucinaciones al especializar el modelo.

### ⚠️ Importante
- Fine-tuning mal hecho puede sobreajustar a datos pequeños.
- No todos los modelos y datos se benefician del fine-tuning.
- Es importante evaluar comparando con un baseline sin ajuste.

---

## 📝 Notas Detalladas

### ¿Qué es el fine-tuning?
Fine-tuning consiste en tomar un modelo pre-entrenado y continuar su entrenamiento en un conjunto de datos específico para mejorar su rendimiento en una tarea concreta.

El modelo ya tiene representaciones generales del lenguaje; el fine-tuning ajusta esas representaciones para el dominio o la tarea deseada.

---

## 🔍 Métodos 

### PEFT (Parameter-efficient fine-tuning)

- Parameter-efficient fine-tunig: is a process and set of techniques that freeze or preserve the parameters and weights of the original LLM and fine-tune or train a small number of task.specific adaptor layers and parameters.
	**LoRa**: Popular PEFT technique that also preservers or freezes the original weights of the foundation model and creates new trainable low-rank matrices into each layer of a transformer architecture.
- PEFT and LoRa modify the weights of your model, but not the representations.

### ReFT (Representation fine-tuning)

-  Is a fine-tunig process that freezes the base model and learns task-specific interventions 

### RLHF (Reinforcement learning from human feedback)

- You can improve performance in specific domains. You can also fine-tune reinforcement learning from human feedback.


---

## ⚖️ Comparación de métodos

| Método | Parámetros entrenados | Costo | Flexibilidad | Uso recomendado |
|---|---|---|---|---|
| Full Fine-Tuning | Todos | Alto | Muy alta | Datos grandes, máxima adaptación |
| Freeze Layers | Parcial | Medio | Alta | Dataset moderado, recursos limitados |
| Adapters | Bajo | Bajo | Alta | Múltiples tareas, múltiples dominios |
| LoRA | Muy bajo | Muy bajo | Alta | LLM grande, recursos limitados |
| Prompt Tuning | Muy bajo | Muy bajo | Media | Adaptación rápida, tareas similares |

---

## ✅ Casos de uso

- **Clasificación de texto**: fine-tuning de un modelo de lenguaje general a un corpus específico.
- **Generación de respuestas**: adaptar un LLM a estilo de escritura o tipo de contenido.
- **NLP en dominio especializado**: medicina, legal, finanzas.
- **Sistemas multimodales**: ajustar modelos que combinan texto e imagen.

---

## 🔗 Conexiones
- [[Prompt Engineering - Técnicas y mejores prácticas]]
- [[Model Evaluation - Métricas BLEU ROUGE BERTScore]]
- [[FastMCP - Ejemplo de implementación]]
- [[A2A - Agent-to-Agent]]

---

## 🔄 Procesamiento Post-Clase

### 📋 Checklist de Procesamiento
- [ ] Probar fine-tuning en un modelo pequeño.
- [ ] Comparar LoRA vs full fine-tuning en el mismo dataset.
- [ ] Registrar costo en GPU/memoria.
- [ ] Evaluar con métricas BLEU/ROUGE/BERTScore si aplica.

### 🎯 Acciones Prioritarias
1. Seleccionar una tarea de NLP y dataset de prueba.
2. Implementar un ejemplo con LoRA.
3. Medir mejoras y riesgos de sobreajuste.

---

## 🎴 Flashcards Rápidas
¿Qué es fine-tuning?::Ajustar un modelo pre-entrenado a una tarea específica. #card
¿Qué es LoRA?::Low-Rank Adaptation, método eficiente para ajustar solo partes pequeñas del modelo. #card
¿Cuándo usar adapters?::Cuando se necesitan múltiples adaptaciones sin entrenar el modelo completo. #card
¿Cuál es el riesgo del full fine-tuning?::Sobreajuste y altos costos de memoria. #card
