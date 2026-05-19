---
tipo_nota: Trabajo
area: Arquitectura
nivel-comprension: 💡
proxima-revision: 2026-01-25
tiempo-repaso: 10 min
veces-revisado: 2
tags:
  - seguridad
  - cpu
  - hardware
  - performance
created: 2025-12-17
ultima-revision: 2026-01-15
modified: 2026-01-15
tiempo-estimado: 20min
status: 🌳 Maduro
cards-deck: ""
---

# La Carrera por la Velocidad: Ejecución Especulativa y Vulnerabilidades

## 1. Introducción y Contexto Histórico
La **[[Ejecución Fuera de Orden]] (OoOE)** es un paradigma de arquitectura de computadores diseñado para evitar que la CPU esté ociosa.
* **Origen**: Algoritmo de Tomasulo (IBM, años 60).
* **Estandarización**: Intel Pentium Pro (1995).
* **Objetivo**: Maximizar el uso de las unidades funcionales mientras se espera a la memoria.

## 2. ¿Qué es la Ejecución Especulativa?
Es una técnica de optimización donde la CPU realiza tareas *antes* de saber si son necesarias, basándose en la **[[Predicción de Saltos]]**.
* **Si acierta**: El rendimiento aumenta drásticamente.
* **Si falla**: Se descartan los cambios en los registros (estado arquitectónico).

> [!info] El problema invisible
> Aunque el estado de los registros se revierte tras una mala predicción, el estado de la **[[Memoria Caché]]** (micro-arquitectónico) *no* se limpiaba completamente.

## 3. Las Vulnerabilidades: Spectre y Meltdown
Descubiertas en 2018, explotan las huellas que deja la ejecución especulativa en la caché (Ataques de Canal Lateral).

### [[Meltdown]] (Rogue Data Cache Load)
* **Mecanismo**: Rompe el aislamiento entre usuario y Kernel. La CPU lee memoria privilegiada especulativamente antes de verificar permisos.
* **Impacto**: Permite leer toda la memoria física del sistema.
* **Hardware afectado**: Principalmente Intel.

### [[Spectre]] (Bounds Check Bypass)
* **Mecanismo**: Engaña al predictor de saltos para que un programa "inocente" acceda a datos de su propia memoria que no debería tocar.
* **Dificultad**: Muy difícil de parchear porque abusa del funcionamiento *correcto* de la predicción de saltos.
* **Hardware afectado**: Intel, AMD, ARM (casi universal).

## 4. Métodos de Mitigación

| Tipo | Solución | Impacto |
| :--- | :--- | :--- |
| **Software** | **KPTI** (Kernel Page Table Isolation) | Aísla la memoria del Kernel. Alto impacto en rendimiento (I/O). |
| **Software** | **Retpoline** (Google) | Compilación que evita la especulación en saltos indirectos. |
| **Hardware** | Cambios en Silicio | Nuevas CPUs (Zen 2, Intel 9ª Gen+) incluyen protecciones físicas. |

## 5. Impacto en el Rendimiento
* **Servidores/Bases de Datos**: Impacto inicial significativo (5-30%) debido al costo de las *syscalls* con KPTI.
* **Usuario/Gaming**: Impacto despreciable (1-3%).

## 6. Referencias Bibliográficas
1. **Kocher, P., et al.** (2019). *Spectre Attacks: Exploiting Speculative Execution*.
2. **Lipp, M., et al.** (2018). *Meltdown: Reading Kernel Memory from User Space*.
3. **Intel Corporation**. *Intel Analysis of Speculative Execution Side Channels*.