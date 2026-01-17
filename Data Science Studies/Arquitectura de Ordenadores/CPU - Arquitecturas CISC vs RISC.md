---
cards-deck: Arquitectura::CISC vs RISC
created: 2024-12-13
modified: 2025-12-25
status: 🌿 Creciendo
tipo_nota: tecnica
asignatura: Arquitectura
nivel-comprension: 💡
proxima-revision: 2026-01-24
ultima-revision: 2025-12-25
veces-revisado: 2
tiempo-repaso: 25min
tiempo-estimado: 10m
---

# CPU - Arquitecturas CISC vs RISC

> [!abstract] Objetivo
> Comprender las dos filosofías fundamentales de diseño de procesadores y sus trade-offs

---

## 🎓 Contexto Académico

**Asignatura/Curso**: Arquitectura de Computadores
**Relevancia para**: ⭐⭐⭐⭐⭐ MUY PREGUNTABLE EN EXAMEN
**Dificultad percibida**: ⭐⭐⭐⭐☆
**Hub padre**: [[cpu-indice-general|🗂️ CPU - Índice General]]

---

## 📝 Introducción

Existen dos filosofías principales para diseñar CPUs:

1. **CISC**: Complex Instruction Set Computing
2. **RISC**: Reduced Instruction Set Computing

**Pregunta clave**: ¿Es mejor tener muchas instrucciones complejas o pocas instrucciones simples?

---

## 🏗️ RISC (Reduced Instruction Set Computing)

### Filosofía

**Idea central**: Menos es más - instrucciones simples ejecutadas muy rápido

**Principios de diseño**:
1. Conjunto de instrucciones pequeño y simplificado
2. Instrucciones de longitud fija
3. Cada instrucción se ejecuta en un solo ciclo de reloj
4. El compilador hace más trabajo

---

### Características Técnicas

#### ⚡ Complejidad
Las instrucciones son SIMPLES - cada una hace UNA sola operación básica

**Ejemplo**:
```
LOAD R1, [0x1000]  # Solo carga
ADD R1, R2         # Solo suma
STORE R1, [0x2000] # Solo guarda
```

#### 📚 Set de Instrucciones
Conjunto REDUCIDO - típicamente 50-100 instrucciones

**Ventaja**: Decodificación más rápida y eficiente

#### ⏱️ Ejecución
La mayoría de instrucciones se ejecutan en 1 ciclo de reloj

**Implicación**: Rendimiento predecible y constante

#### 🔧 Compilador
El compilador debe optimizar más - traduce instrucciones complejas en secuencias de instrucciones simples

**Ejemplo**: 
Operación compleja → Compilador la divide en 5-10 instrucciones RISC simples

---

### ✅ Ventajas RISC

1. **Rendimiento predecible**: Cada instrucción tarda lo mismo
2. **Eficiencia energética**: Menos circuitos activos = menos consumo
3. **Hardware más simple**: Diseño limpio, fácil de optimizar
4. **Ideal para pipelining**: Todas las instrucciones tienen la misma estructura
5. **Escalabilidad**: Fácil añadir más núcleos

---

### 📱 Ejemplos RISC

**ARM** (Advanced RISC Machine):
- Usado en: smartphones, tablets, Raspberry Pi, Apple M1/M2/M3
- Ventaja clave: eficiencia energética

**MIPS**:
- Usado en: routers, consolas de videojuegos antiguas

**SPARC**:
- Usado en: servidores Sun/Oracle

**RISC-V** (nuevo):
- Arquitectura de código abierto
- Ganando popularidad en IoT

**Tu conexión**: Mi móvil utiliza ARM

---

## 🏢 CISC (Complex Instruction Set Computing)

### Filosofía

**Idea central**: Una instrucción compleja puede hacer el trabajo de muchas simples

**Principios de diseño**:
1. Conjunto de instrucciones amplio y variado
2. Instrucciones de longitud variable
3. Una instrucción puede tardar varios ciclos
4. El hardware hace más trabajo

---

### Características Técnicas

#### 🔀 Complejidad
Las instrucciones son COMPLEJAS - una instrucción puede hacer múltiples operaciones

**Ejemplo**:
```
ADDM R1, [0x1000]  # Carga desde memoria, suma y guarda - todo en UNA instrucción
```

#### 📚 Set de Instrucciones
Conjunto AMPLIO - típicamente 200-300+ instrucciones

**Ventaja**: Menos instrucciones totales para hacer la misma tarea
**Desventaja**: Decodificación más lenta y compleja

#### ⏱️ Ejecución
Las instrucciones tardan ciclos variables - algunas 1 ciclo, otras 10+ ciclos

**Implicación**: Rendimiento menos predecible

#### 🔧 Compilador
El compilador tiene menos trabajo - puede usar instrucciones complejas directamente

**Ejemplo**: 
Operación compleja → 1 instrucción CISC que lo hace todo

---

### 🎯 Modos de Direccionamiento

CISC soporta **modos complejos** de acceder a datos:
- **Directo**: dirección explícita
- **Indirecto**: la dirección está en un registro
- **Indexado**: base + offset
- **Relativo a PC**: offset desde la instrucción actual

**Ventaja**: Flexibilidad en manipulación de datos

---

### ✅ Ventajas CISC

1. **Código más compacto**: Menos instrucciones = menos espacio en memoria
2. **Programación más directa**: Una instrucción compleja = una línea de código de alto nivel
3. **Compatibilidad hacia atrás**: x86 mantiene compatibilidad desde los 80s
4. **Potencia en tareas específicas**: Instrucciones especializadas para ciertas operaciones

---

### 💻 Ejemplos CISC

**x86** (Intel, AMD):
- Usado en: PCs, laptops, servidores
- Familia: 8086 → 80286 → 80386 → Pentium → Core i3/i5/i7/i9

**x86-64** (extensión de 64 bits):
- Usado en: sistemas modernos
- Compatibilidad: ejecuta software x86 de 32 bits

**Tu conexión**: Mi PC utiliza esta tencología

---

## ⚔️ COMPARACIÓN DIRECTA

### 📊 Tabla Comparativa

| Aspecto | RISC | CISC |
|---------|------|------|
| **Filosofía** | [Simplicidad] | [Complejidad] |
| **Nº instrucciones** | [50-100] | [200-300+] |
| **Longitud instrucción** | [Fija] | [Variable] |
| **Ciclos por instrucción** | [1 típicamente] | [Variable 1-10+] |
| **Trabajo del compilador** | [Alto] | [Bajo] |
| **Consumo energético** | [Bajo] | [Alto] |
| **Complejidad hardware** | [Simple] | [Complejo] |
| **Pipelining** | [Fácil] | [Difícil] |
| **Ejemplos** | [ARM, MIPS] | [x86, x86-64] |

---

### 🔥 Debate Histórico

**Años 80-90**: RISC vs CISC era una guerra filosófica

**Resultado actual**: Híbridos - los procesadores modernos combinan ambas ideas

**Ejemplo**: 
- Intel Core i7 es oficialmente CISC (x86)
- PERO internamente traduce instrucciones CISC a micro-ops RISC
- Usa pipelining y técnicas RISC para ejecutar

**Moraleja**: La distinción pura ya no existe - todos son híbridos

---

## 🎯 ¿Cuál es Mejor?

**Depende del caso de uso**:

### RISC es mejor para:
- ✅ Dispositivos móviles (batería limitada)
- ✅ Sistemas embebidos
- ✅ IoT (Internet of Things)
- ✅ Rendimiento predecible

### CISC es mejor para:
- ✅ Compatibilidad con software antiguo
- ✅ Aplicaciones de escritorio/servidores
- ✅ Cuando el consumo energético no es crítico

---

## 🌐 Arquitecturas Modernas Adicionales

### Superescalar
Múltiples instrucciones en paralelo - combina ideas RISC
**Ejemplos**: Intel Pentium, AMD Ryzen, ARM Cortex

### VLIW (Very Long Instruction Word)
El compilador agrupa instrucciones en "paquetes" paralelos
**Ejemplo**: Intel Itanium (fracasó)

### EPIC (Explicitly Parallel Instruction Computing)
Similar a VLIW pero más sofisticado
**Ejemplo**: Intel Itanium IA-64

**Nota**: Estas arquitecturas no tuvieron mucho éxito comercial

---

## 💭 Reflexiones & Conexiones

**Conexión con ML**:
Los chips de IA modernos (TPUs, NPUs) son híbridos diseñados para operaciones específicas

**Pregunta para reflexionar**:
¿Por qué ARM dominó los móviles y x86 los PCs? 

**¿Porqué no se cambian todos las arquitecturas a ARM?**
Lo que pasa es que si cambiamos todos a ARM que son mucho más eficientes, los programas antiguos no funcionarían

---

## 🎴 Flashcards

¿Cuál es la diferencia fundamental en la **filosofía de diseño** entre RISC y CISC respecto a dónde reside la complejidad? #card

- **RISC:** Traslada la complejidad al **Software** (Compilador). Instrucciones simples, el compilador debe combinar muchas para hacer una tarea compleja.
    
- **CISC:** Traslada la complejidad al **Hardware** (CPU). Instrucciones complejas, el circuito interno debe ser capaz de decodificarlas.
    

¿Por qué se dice que los procesadores modernos x86 (Intel/AMD) son **"Híbridos"**? #card Porque aunque aceptan instrucciones **CISC** (complejas) del software para mantener compatibilidad, internamente las traducen y ejecutan como micro-operaciones **RISC** (simples) para ganar eficiencia.

### 🛠️ Mecánica y Lenguajes

¿Por qué un programa compilado para x86 (CISC) no funciona nativamente en un procesador ARM (RISC)? #card Porque tienen diferentes **ISAs (Arquitecturas de Conjunto de Instrucciones)**. Hablan "idiomas" diferentes (códigos binarios distintos) y la CPU no reconoce las instrucciones de la otra arquitectura sin un traductor/emulador.

En el contexto de lenguajes de programación, ¿qué distingue a un **Lenguaje de Bajo Nivel** (como Ensamblador) de uno de Alto Nivel? #card El bajo nivel da instrucciones **directas y puras** al hardware (control manual de registros y memoria, ej: `LOAD`, `STORE`), mientras que el alto nivel utiliza **abstracciones** (el compilador/intérprete gestiona la memoria y recursos por ti).

### ⚡ Casos de Uso

Si RISC (ARM) es más eficiente energéticamente, ¿por qué los servidores y PCs han seguido usando CISC (x86) durante décadas? #card Principalmente por la **compatibilidad de software (Legacy)**. Existe una cantidad masiva de programas antiguos (Windows, aplicaciones empresariales) compilados para x86 que no funcionarían en ARM sin ser reescritos o emulados lentamente.

¿Quién interactúa directamente con el hardware (gestión de CPU/RAM): El creador de un lenguaje (ej. Guido van Rossum) o el creador del Kernel (ej. Linus Torvalds)? #card **El Kernel (Linus Torvalds)**. El kernel gestiona los recursos físicos y "habla" con el metal. Los lenguajes de programación corren _sobre_ el kernel y le piden recursos a él, no al hardware directamente.

---

## 📚 Referencias & Enlaces

**Enlaces internos**: 
- [[cpu-unidades-internas|← Anterior: UC y UE]]
- [[cpu-arquitecturas-reales|→ Siguiente: Arquitecturas Reales x86/ARM]]
- [[cpu-indice-general|🗂️ Hub CPU]]

**Referencias externas**: 
- PDF UD2 - Páginas 27-40

**Fuente**: TCSO - UD2.pdf

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2024-12-13
- **Próxima revisión**: 2024-12-16
- **Veces revisado**: 0
- **Nivel de comprensión**: 🤔 Entiendo parcialmente
- **Tiempo estimado de repaso**: 25min

---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Tarea para aclarar una duda de concepto. Usa #mejora-concepto
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia
