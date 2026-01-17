---
cards-deck: Arquitectura::CPU_Unidades
created: 2024-12-13
modified: 2026-01-16
status: 🌱 Semilla
tipo_nota: tecnica
asignatura: Arquitectura
nivel-comprension: 🤔
proxima-revision: 2026-01-17
ultima-revision: 2026-01-14
veces-revisado: 1
tiempo-repaso: 20min
tiempo-estimado: 30m
---

# CPU - Unidades Internas (UC y UE)

> [!abstract] Objetivo
> Entender cómo la Unidad de Control y la Unidad de Ejecución trabajan juntas para procesar instrucciones

---

## 🎓 Contexto Académico

**Asignatura/Curso**: Arquitectura de Computadores
**Relevancia para**: Examen UD2 - Componentes internos
**Dificultad percibida**: ⭐⭐⭐⭐☆
**Hub padre**: [[cpu-indice-general|🗂️ CPU - Índice General]]

---

## 📝 Visión General

La CPU tiene dos "cerebros" complementarios:

1. **Unidad de Control (UC)**: El "jefe" que coordina todo
2. **Unidad de Ejecución (UE)**: El "trabajador" que hace los cálculos

**Analogía**: 
UC = director de obra, UE = albañiles/maquinaria que construye

---

## 🎛️ UNIDAD DE CONTROL (UC)

> [!info] Rol fundamental
> La UC es el "director de orquesta" que coordina TODAS las operaciones internas

### 1️⃣ Decodificación de Instrucciones

**¿Qué hace?**
Lee el Registro de Instrucción (RI) y determina qué operación realizar

**Proceso**:
1. Lee la instrucción del RI
2. Identifica el **opcode** (código de operación)
3. Identifica los **operandos**
4. Determina el **modo de direccionamiento**

**Pregunta**: ¿Por qué es necesario decodificar? Porque las instrucciones están en lenguaje máquina (binario)

---

### 2️⃣ Generación de Señales de Control

**¿Qué son?**
Señales eléctricas que activan/desactivan componentes de la CPU

**Ejemplos de señales**:
- "ALU, realiza una suma"
- "Memoria, lee de la dirección 0x1234"
- "Registro R1, guarda este valor"

**Analogía**: Como un semáforo que controla el tráfico de datos

---

### 3️⃣ Secuenciación de Ejecución

**Responsabilidad**: Garantizar que las instrucciones se ejecuten en orden correcto

**Herramienta clave**: **Contador de Programa (CP/PC)**
- Mantiene la dirección de la próxima instrucción
- Se actualiza automáticamente después de cada instrucción
- Permite ejecución **secuencial**

**Excepción**: Cuando hay saltos (if, bucles), el CP cambia

---

### 4️⃣ Control de Acceso a Memoria

**Buses que controla**:
- **Bus de direcciones**: especifica QUÉ dirección de memoria
- **Bus de datos**: transfiere la información entre CPU y RAM
- **Bus de control**: indica si es lectura o escritura

**Conexión**: Relacionado con [[buses-sistema|Buses del Sistema]]

---

### 5️⃣ Manejo de Excepciones e Interrupciones

**¿Qué hace cuando hay una interrupción?**
1. [Detecta la señal de interrupción]
2. [Pausa la ejecución actual]
3. [Guarda el estado (registros, CP)]
4. [Salta a la rutina de manejo de interrupción]
5. [Restaura el estado y continúa]

**Ejemplo real**: [División por cero → genera excepción → UC maneja el error]

---

### 6️⃣ Control de Banderas (Flags)

**Responsabilidad**: [Supervisar y actualizar el Registro de Estado]

**Banderas que controla**:
- Zero Flag (ZF)
- Overflow Flag (OF)
- Negative Flag (NF)
- Carry Flag (CF)

**Uso**: [Las instrucciones condicionales (if) leen estas banderas para decidir]

---

## ⚡ UNIDAD DE EJECUCIÓN (UE)

> [!info] Rol fundamental
> La UE es quien REALMENTE hace los cálculos y operaciones

### 1️⃣ ALU (Unidad Aritmético-Lógica)

**Función**: [Realiza operaciones matemáticas y lógicas]

**Operaciones aritméticas**:
[Suma, resta, multiplicación, división, módulo]

**Operaciones lógicas**:
[AND, OR, NOT, XOR, comparaciones]

**Input**: [Dos operandos + un opcode]
**Output**: [Un resultado + actualización de flags]

**Ejemplo**:
```
ALU recibe: 5 + 3 (operandos) y "ADD" (opcode)
ALU devuelve: 8 (resultado) y ZF=0 (no es cero)
```

---

### 2️⃣ FPU (Unidad de Punto Flotante)

**Función**: [Operaciones con números decimales]

**¿Por qué existe?**
[Los números decimales (3.14, 0.001) requieren cálculos especiales]

**Usos típicos**:
- Gráficos 3D
- Simulaciones científicas
- Machine Learning
- Cálculos de ingeniería

**Conexión personal**: [En tus proyectos de DS, ¿usas NumPy? NumPy usa la FPU intensivamente]

---

### 3️⃣ Unidad de Almacenamiento

**Función**: [Transferir datos entre CPU y RAM]

**Operaciones**:
- **Load**: [RAM → Registros de CPU]
- **Store**: [Registros de CPU → RAM]

**Importancia**: [Sin esta unidad, la CPU no podría acceder a datos grandes]

---

### 4️⃣ Unidad de Salto (Branch Unit)

**Función**: [Ejecutar instrucciones de salto (if, while, for)]

**Tipos de saltos**:
- **Condicional**: [solo salta si se cumple una condición]
- **Incondicional**: [siempre salta]

**Cómo decide**: [Lee las banderas del Registro de Estado]

**Ejemplo en Python**:
```python
if x > 5:  # Branch Unit verifica la condición
    print("Mayor")  # Salta aquí si es True
else:
    print("Menor")  # O salta aquí si es False
```

---

### 5️⃣ Unidad de Manejo de Interrupciones

**Función**: [Gestiona interrupciones durante la ejecución]

**Proceso**:
1. Detecta interrupción
2. Detiene ejecución normal
3. Pasa control a rutina de manejo
4. Restaura ejecución

**Diferencia con UC**: [La UC coordina, la UE ejecuta el manejo]

---

### 6️⃣ Camino de Datos (Data Path)

**¿Qué es?**
[Red de cables y registros que conecta todos los componentes de la UE]

**Función**: [Permite transferir datos entre ALU, FPU, registros, etc.]

**Analogía**: [Como las carreteras que conectan ciudades]

---

### 7️⃣ Registro de Resultado

**Función**: [Almacena temporalmente resultados antes de escribirlos en su destino final]

**Flujo típico**:
ALU calcula → Resultado va al Registro de Resultado → Se escribe en memoria o registro destino

---

## 🔄 Interacción UC ↔ UE

**Ejemplo de flujo completo**:

```
Instrucción: ADD R1, R2, R3  (R1 = R2 + R3)

1. UC decodifica la instrucción
2. UC genera señales: "ALU, haz una suma"
3. UE (ALU) lee R2 y R3
4. UE (ALU) calcula R2 + R3
5. UE guarda resultado en Registro de Resultado
6. UC coordina: "escribe el resultado en R1"
7. UC actualiza CP para la siguiente instrucción
```

**Pregunta**: ¿Quién manda a quién? [UC manda, UE ejecuta]

---

## 💭 Reflexiones & Conexiones

**Conexión con software**:
[Cada línea de Python que escribes se traduce a cientos de operaciones UC/UE]

**Conexión con tu proyecto React**:
[Cuando React renderiza un componente, la UC está coordinando miles de instrucciones de la UE]

**Pregunta profunda**:
¿Por qué separar UC y UE en lugar de tener una sola unidad? [Especialización: cada una hace lo que mejor sabe hacer]

**Analogía con tu vida**:
[UC = tu mente planificando el día, UE = tu cuerpo ejecutando las tareas]

---

---
cards-deck: Arquitectura::CPU_Unidades
asignatura: Arquitectura
nivel-comprension: 💡
---

## 🎴 Flashcards

¿Cuál es la diferencia principal entre la Unidad de Control (UC) y la Unidad de Ejecución (UE)?::La UC es el "director" que coordina y decodifica (decide QUÉ hacer); la UE es el "trabajador" que realiza los cálculos y operaciones (ejecuta la acción). #cpu #uc-ue #card

¿Qué función realiza la Unidad de Control durante la etapa de decodificación?::Lee el opcode del Registro de Instrucción (RI) para interpretar qué operación debe realizarse y con qué operandos. #cpu #uc #card

¿Qué componente utiliza la UC para asegurar que las instrucciones se ejecuten en orden?::El Contador de Programa (CP/PC), que apunta siempre a la dirección de la siguiente instrucción. #cpu #uc #registros #card

¿Qué son las "señales de control" generadas por la UC?::Son señales eléctricas que activan o desactivan componentes específicos de la CPU (ej: decirle a la ALU "haz una suma" o a la Memoria "lee este dato"). #cpu #uc #card

¿Qué unidad de la UE es responsable de los cálculos matemáticos básicos y lógicos?::La ALU (Unidad Aritmético-Lógica). #cpu #ue #alu #card

¿Por qué es necesaria la FPU (Unidad de Punto Flotante) si ya tenemos una ALU?::Porque la ALU trabaja con enteros; la FPU está especializada en cálculos decimales complejos (coma flotante) necesarios para gráficos, física y Machine Learning. #cpu #ue #fpu #card

¿Qué función cumple la Unidad de Salto (Branch Unit) en la ejecución de código?::Gestiona el control de flujo (if, while, for) decidiendo si cambiar el Contador de Programa basándose en las banderas de estado (flags). #cpu #ue #control-flujo #card

¿Qué es el "Camino de Datos" (Data Path) en la CPU?::Es la red interna de buses y conexiones que permite mover datos entre los componentes de la Unidad de Ejecución (ALU, registros, FPU). #cpu #arquitectura #card

En la interacción UC-UE, ¿quién se encarga de manejar una interrupción (ej: error div/0)?::La UC detecta y coordina el cambio de contexto, mientras que la Unidad de Manejo de Interrupciones (en la UE) ejecuta la lógica de parada y restauración. #cpu #interrupciones #card

Si escribes `if x > 0` en Python, ¿qué componente de la CPU evalúa esa condición?::La Unidad de Salto (Branch Unit), leyendo las banderas (Zero/Negative Flag) actualizadas previamente por una comparación de la ALU. #cpu #practica #card 

---

## 📚 Referencias & Enlaces

**Enlaces internos**: 
- [[cpu-fundamentos|← Anterior: Fundamentos]]
- [[cpu-arquitecturas-cisc-risc|→ Siguiente: CISC vs RISC]]
- [[cpu-indice-general|🗂️ Hub CPU]]

**Referencias externas**: 
- PDF UD2 - Páginas 20-26

**Fuente**: TCSO - UD2.pdf

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2024-12-13
- **Próxima revisión**: 2024-12-16
- **Veces revisado**: 0
- **Nivel de comprensión**: 🤔 Entiendo parcialmente
- **Tiempo estimado de repaso**: 20min

---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Hacer infografia #mejora-concepto
- [ ] Hacer flashcards #mejora-practica
- [ ] Crear analogías #mejora-analogia
