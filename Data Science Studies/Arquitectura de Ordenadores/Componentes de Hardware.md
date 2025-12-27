---
cards-deck: Arquitectura::Hardware
created: 2025-11-04
modified: 2025-12-12
status: 🌳 Maduro
tipo_nota: tecnica
asignatura: Arquitectura
nivel-comprension: ✅
proxima-revision: 2026-01-11
ultima-revision: 2025-12-12
veces-revisado: 1
estado: 🟡 Atrasado
tiempo-estimado: 2min
---

# Componentes del Hardware

> [!abstract] Objetivo
> Saber los principales componentes y sus funciones

---

## 📝 Definición

Los componentes del hardware están divididos en cuatro categorías principales: entrada, salida, procesamiento y almacenamiento. Cada categoría cumple una función específica en el funcionamiento del ordenador.

---

## ⚙️ Conceptos Clave

### 📌 Entrada

**Tipo**: Componentes de Entrada

**Características**:
- Son componentes que llevan la información del usuario al ordenador
- El ordenador procesa esta información en un formato que puede entender
- Ejemplos: ratón, teclado, escáner, micrófono, cámara web

**Relacionado**: [[Hardware]] • [[Periféricos]]

---

### 📌 Salida

**Tipo**: Componentes de Salida

**Características**:
- Son los componentes mediante los cuales el ordenador envía señales al usuario
- Transforman la información procesada en formato comprensible para humanos
- Ejemplos: monitor, altavoz, impresora, proyector

**Relacionado**: [[Hardware]] • [[Periféricos]]

---

### 📌 Procesamiento

**Tipo**: Componentes de Procesamiento (CPU)

**Características**:
- **UC (Unidad de Control)**: Detecta señales de estado, interpreta instrucciones de memoria, genera órdenes para el sistema
- **ALU (Unidad Aritmético-Lógica)**: Realiza operaciones aritméticas y lógicas, devuelve resultados a la UC
- **Memoria Principal**: Memoria rápida que ejecuta programas. Incluye ROM (Read Only Memory) y RAM (Random Access Memory)

**Relacionado**: [[CPU]] • [[Arquitectura de von Neumann]]

---

### 📌 Almacenamiento

**Tipo**: Componentes de Almacenamiento

**Características**:
- **Memorias de almacenamiento**: HDD, SSD, unidades USB, unidades ópticas, tarjetas de memoria
- **Memoria no volátil**: Persistente, mantiene datos sin energía
- **Complemento a memoria principal**: Mayor capacidad pero menor velocidad que RAM

**Relacionado**: [[Memoria]] • [[Sistemas de Archivos]]

---

## 💻 Ejemplo Práctico

### Flujo de Información en un Ordenador

**Entrada → Procesamiento → Salida**

1. **Usuario escribe en el teclado** (Entrada)
2. **CPU procesa las pulsaciones** (Procesamiento)
   - UC coordina las operaciones
   - ALU realiza cálculos si es necesario
   - RAM almacena temporalmente
3. **Monitor muestra los caracteres** (Salida)
4. **SSD guarda el archivo** (Almacenamiento)

---

## 💭 Reflexiones & Conexiones

Son componentes que hacen funcionar el ordenador con más detalle de su funcionamiento. La arquitectura de von Neumann establece esta división clara entre componentes, lo que permite entender el flujo de datos en el sistema.

Conexión con mi proyecto: Al entrenar modelos de ML, la GPU actúa como procesador especializado, la RAM mantiene los datos en memoria activa, y el SSD almacena el modelo entrenado.

---

## 🎴 Flashcards

¿Cuál es la diferencia entre memoria ROM y RAM?::RAM es volátil (se borra al apagar) y se usa para procesar información activa. ROM es permanente y contiene instrucciones básicas del sistema #memoria #hardware

¿Qué hace la UC (Unidad de Control)?::Detecta señales de estado, interpreta instrucciones de memoria y genera órdenes para coordinar el sistema #cpu #procesamiento

¿Cuál es la diferencia entre memoria volátil y persistente?::Volátil se borra al apagar (RAM). Persistente permanece sin energía (ROM, SSD, HDD) #memoria #almacenamiento

¿Cuáles son las 4 categorías de componentes de hardware?::Entrada (teclado, ratón), Salida (monitor, altavoz), Procesamiento (CPU), Almacenamiento (HDD, SSD) #hardware #componentes

UC (Unidad de Control):::Componente de la CPU que coordina y controla las operaciones del sistema, interpreta instrucciones y gestiona señales #cpu #arquitectura

ALU (Unidad Aritmético-Lógica):::Componente de la CPU que realiza operaciones aritméticas y lógicas #cpu #arquitectura

¿Por qué necesitamos almacenamiento además de RAM?::RAM es rápida pero volátil y tiene poca capacidad. El almacenamiento (SSD/HDD) es persistente y tiene mayor capacidad #memoria #almacenamiento

¿Ejemplos de dispositivos de entrada?::Teclado, ratón, escáner, micrófono, cámara web, touchpad #hardware #entrada

¿Ejemplos de dispositivos de salida?::Monitor, altavoz, impresora, proyector, auriculares #hardware #salida

La CPU contiene ==UC== (Unidad de Control), ==ALU== (Unidad Aritmético-Lógica) y ==memoria principal== #cpu #componentes

---

**📊 Total de flashcards**: 10

> 🎯 **Para revisar**: Cmd/Ctrl+P → "Flashcards: Review flashcards"

---

## 📚 Referencias & Enlaces

**Enlaces internos**: [[Hardware]], [[CPU]], [[Memoria]], [[Arquitectura de von Neumann]]
**Referencias externas**: [Computer Architecture](https://en.wikipedia.org/wiki/Computer_architecture)
**Fuente**: Apuntes de clase - Arquitectura de Computadores

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2025-11-02
- **Próxima revisión**: 2025-11-05
- **Veces revisado**: 0
- **Nivel de comprensión**: 💡 Entiendo bien
- **Tiempo estimado de repaso**: 10min
