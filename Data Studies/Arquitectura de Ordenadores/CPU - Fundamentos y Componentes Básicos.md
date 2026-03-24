---
nivel-comprension: 💡
proxima-revision: 2026-01-25
ultima-revision: 2026-01-15
modified: 2026-01-15
tiempo-estimado: 15m
veces-revisado: 3
status: 🌿 Creciendo
cards-deck: Arquitectura::CPU-Fundamentos
created: 2026-01-15
tipo_nota: tecnica
asignatura: Arquitectura
estado: 🟢 Al día
tiempo-repaso: 5min
---

# CPU - Fundamentos y Componentes Básicos

> [!abstract] Objetivo
> Comprender qué es la CPU, sus funciones principales y los componentes básicos que permiten su operación

---

## 🎓 Contexto Académico

**Asignatura/Curso**: Arquitectura de Computadores
**Relevancia para**: Examen UD2 - Estructura CPU
**Dificultad percibida**: ⭐⭐⭐☆☆
**Hub padre**: [[cpu-indice-general|🗂️ CPU - Índice General]]

---

## 📝 Definición

**¿Qué es la CPU?**

Es la Unidad Central de Procesamiento (Central Processing Unit). Es el componente hardware encargado de interpretar las instrucciones de los programas y procesar los datos. Coordina el funcionamiento de todo el sistema informático gobernando el resto de componentes.

**Analogía personal**: 
Es como el **Director de Orquesta**. No toca todos los instrumentos (no guarda datos como el disco, ni muestra imágenes como la pantalla), pero lleva la batuta: dice quién entra, cuándo, a qué ritmo y coordina que todos suenen en armonía para ejecutar la "sinfonía" (el programa).

---

## ⚙️ Las 5 Funciones Principales

### 🔍 1. Decodificación de Instrucciones

**¿Qué hace?**
La CPU recibe una secuencia de ceros y unos (lenguaje máquina) y necesita "traducirlos" a señales eléctricas específicas que activen los circuitos internos correctos. Transforma el "qué quiero hacer" (software) en "qué cables activar" (hardware).

**Componentes de una instrucción**:
- **Código de operación (opcode)**: Indica la acción a realizar (ej: SUMAR, MOVER, SALTAR).
- **Operandos**: Indica sobre qué datos se va a realizar esa acción (ej: el número 5, el contenido del Registro AX, o una dirección de memoria).

**Ejemplo mental**: 
Si la instrucción es "suma 5 + 3":
- Opcode = "suma" (La acción)
- Operandos = 5 y 3 (Los sujetos de la acción)

---

### ⚡ 2. Ejecución de Instrucciones

La CPU puede realizar 5 tipos de operaciones:

#### Operaciones Matemáticas
Suma, resta, multiplicación, división (realizadas por la ALU o FPU).

#### Operaciones Lógicas  
Comparaciones (mayor que, menor que), y operadores booleanos (AND, OR, NOT, XOR, NAND). Fundamentales para la toma de decisiones.

#### Operaciones de Memoria
Transferencia de datos: Cargar datos desde la RAM a la CPU (Load) y guardar resultados de la CPU a la RAM (Store).

#### Operaciones de Entrada/Salida
Comunicación con el mundo exterior: leer una pulsación de tecla, enviar un píxel a la pantalla, enviar datos a la red.

#### Control de Flujo
Saltos y bifurcaciones. Permiten romper la secuencia lineal de ejecución (bucles `for`, condicionales `if`). Sin esto, los programas serían solo una lista recta de órdenes sin inteligencia.

---

### 💾 3. Gestión de la Memoria

**Interacción con RAM**:
- La CPU continuamente busca instrucciones (Fetch) y datos en la RAM.
- **Lectura**: Traer datos para procesar. **Escritura**: Guardar resultados finales o temporales.

**Memoria Caché**:
- **Ventaja**: Es infinitamente más rápida que la RAM porque está construida con tecnología SRAM (estática) y físicamente dentro del chip.
- **Desventaja**: Es muy cara y ocupa mucho espacio físico en el silicio, por lo que su capacidad es pequeña (Megabytes vs Gigabytes de la RAM).
- **Ubicación**: Está integrada dentro del encapsulado del procesador (L1, L2, L3).

**Conexión**: Esto se relaciona con [[memoria-jerarquia|Jerarquía de Memoria]]

---

### 🎮 4. Control de Periféricos

**Dispositivos que coordina**:
Teclado, ratón, pantalla, discos duros, tarjetas de red, impresoras.

**DMA (Direct Memory Access)**:
Resuelve el problema de la eficiencia. Permite que los dispositivos (como el disco duro o la tarjeta gráfica) lean o escriban en la RAM directamente **sin molestar a la CPU** para cada byte. La CPU solo inicia y finaliza la transferencia, quedando libre para hacer otros cálculos mientras tanto.

---

### ⚠️ 5. Gestión de Interrupciones

**¿Qué es una interrupción?**
Es una señal eléctrica o de software que rompe el flujo normal de ejecución para indicar que ha ocurrido un evento que requiere atención inmediata.

**¿Cuándo ocurren?**
- **Hardware**: Un periférico necesita atención (ej: se pulsó una tecla, llegó un paquete de red).
- **Excepciones**: Error del programa (ej: división por cero, acceso a memoria prohibida).
- **Temporizador**: El reloj del sistema dice que se acabó el tiempo de uso de CPU para este programa (multitarea).

**Flujo**:
1. La CPU está ejecutando la tarea A.
2. Llega una interrupción.
3. La CPU pausa A y guarda su estado (Context Switch) en la pila.
4. Ejecuta la Rutina de Servicio de Interrupción (ISR) correspondiente.
5. Recupera el estado de A y continúa exactamente donde lo dejó.

**Ejemplo real**: Cuando presionas una tecla mientras el ordenador está calculando algo, el cálculo se pausa microsegundos para guardar la letra pulsada en un buffer.

---

## 🧩 Registros de la CPU

Los registros son **memoria ultra-rápida dentro de la CPU** para almacenar datos temporales. Son "las manos" del procesador.

### 📦 Registros Generales
**Uso**: Son el "papel en sucio" de la CPU. Se usan para guardar operandos intermedios de operaciones aritméticas y lógicas, o direcciones de memoria comunes.
**Acceso**: Son accesibles por el programador (en ensamblador) y por las instrucciones estándar.

### 📋 Registro de Instrucción (RI)
**Función**: Almacena la instrucción que se está ejecutando **AHORA MISMO**.
**¿Quién lo usa?**: La Unidad de Control lo lee y decodifica para saber qué señales enviar al resto del chip.

### 🧭 Contador de Programa (CP / PC)
**Función**: Contiene la dirección de memoria de la **SIGUIENTE** instrucción a ejecutar.
**Importancia**: Es vital para el ciclo de instrucción; sin él, la CPU no sabría por dónde seguir.
**¿Cuándo se actualiza?**: Automáticamente justo después de buscar una instrucción (Fetch), se incrementa para apuntar a la siguiente.

### 🚩 Registro de Estado (Status Register / Flags)
**Función**: Almacena "banderas" (bits individuales) que indican el resultado o estado de la última operación realizada.

**Banderas importantes**:
- **Zero Flag (ZF)**: Se pone a 1 si el resultado de la operación fue CERO. (Crucial para comparar si dos números son iguales).
- **Overflow Flag (OF)**: Se activa si el resultado es demasiado grande para caber en el registro (desbordamiento).
- **Negative Flag (NF)**: Se activa si el resultado es negativo (bit de signo).
- **Parity Flag (PF)**: Indica si el número de bits a 1 es par o impar (control de errores simple).

**Uso**: Estas banderas son consultadas por las instrucciones de salto condicional (como los `if` en alto nivel).

### 📚 Stack Pointer (SP)
**Función**: Apunta a la dirección de memoria que es la "cima" (top) de la Pila (Stack).
**Uso**: Es fundamental para llamar a funciones. Permite saber dónde guardar las variables locales y a qué dirección volver (return) cuando la función termina.

### 🎯 Base Pointer (BP)
**Función**: Se usa como ancla o referencia fija dentro de la pila.
**Uso**: Mientras el SP se mueve mucho, el BP se usa para acceder a los argumentos de la función y variables locales de forma relativa y estable.

---

## 💡 Concepto Clave: La Instrucción

Una **instrucción** es la unidad básica de trabajo de la CPU.

**Estructura completa de una instrucción**:

1. **Código de operación**: QUÉ hacer (Suma, Resta, Mover).
2. **Operandos**: Sobre QUÉ datos operar (Registros, Números directos).
3. **Dirección de memoria**: DÓNDE están los datos si no están en registros (opcional).
4. **Modo de direccionamiento**: CÓMO interpretar la dirección (¿es el dato real o un puntero al dato?).
5. **Resultado**: DÓNDE guardar el resultado final.

**Ejemplo concreto**:
```assembly
ADD R1, R2, R3
````

- Operación: ADD (suma)
    
- Operandos fuente: R2 y R3 (suma los valores que hay dentro)
    
- Resultado: El valor resultante se sobrescribe en R1
    

---

## 💭 Reflexiones & Conexiones

**Conexión con tu background**: En ingeniería de sistemas, esto es similar a un PLC. El PLC tiene un ciclo de scan (leer entradas, ejecutar programa, escribir salidas) muy parecido al ciclo Fetch-Decode-Execute de la CPU.

**Conexión con programación**: Cuando escribes `a = b + 5` en Python, el intérprete genera múltiples instrucciones de bajo nivel: 1. Cargar 'b' en un registro. 2. Cargar '5' en otro. 3. Ejecutar ADD. 4. Guardar resultado en la dirección de memoria de 'a'. ¡Todo esto pasa transparente para ti!

**Conexión con tu proyecto React**: Tu app corre sobre el motor V8 de Chrome (escrito en C++). V8 compila tu JavaScript a código máquina nativo (JIT - Just In Time) para tu arquitectura (ARM en tu móvil o Mac, x86 en servidor). Si haces un bucle infinito en JS, bloqueas el hilo principal y la CPU sube al 100% hasta que el SO interviene.

**Pregunta para reflexionar**: _¿Por qué crees que los registros son tan importantes?_ Porque la diferencia de velocidad entre la CPU y la RAM es abismal (la CPU es un Ferrari, la RAM es una tortuga). Si tuviéramos que ir a RAM para cada suma parcial, el ordenador sería miles de veces más lento. Los registros son la "mesa de trabajo" donde todo ocurre a velocidad luz.

---

---
cards-deck: Arquitectura::CPU-Fundamentos
tipo_nota: tecnica
asignatura: Arquitectura
estado: 🟢 Al día
nivel-comprension: 💡
---

## 🎴 Flashcards  

¿Cuál es la función principal de la CPU?::Es el cerebro que coordina todas las operaciones y actúa como director de orquesta del sistema. #card

¿Qué dos componentes tiene una instrucción básica?::Código de operación (opcode) y operandos. #card

¿Diferencia entre Registro de Instrucción (RI) y Contador de Programa (CP)?::El RI tiene la instrucción ACTUAL, el CP apunta a la SIGUIENTE. #card

¿Qué flags almacena el Registro de Estado?::Zero (ZF), Overflow (OF), Negative (NF) y Parity (PF). #card

Ventaja y desventaja de la memoria caché::Ventaja: velocidad extrema. Desventaja: poca capacidad y alto coste. #card

Cuando presionas una tecla ejecutando Python, ¿qué se activa en la CPU?::Gestión de Interrupciones. #card

¿Qué unidad de la CPU calcula decimales para vectores en ML?::La FPU (Unidad de Punto Flotante). #card

¿Por qué los registros son vitales para Machine Learning?::Evitan ir a RAM en cada operación matemática, acelerando el entrenamiento. #card

3 funciones de la CPU al ejecutar np.dot() (NumPy)::1. Gestión Memoria, 2. Ejecución (FPU), 3. Control Flujo. #card

En una app React, ¿qué operaciones dominan al renderizar?::Entrada/Salida (actualizar DOM y memoria de video). #card

Si un bucle infinito pone la CPU al 100%, ¿qué falla?::La gestión de interrupciones (Timer del SO). #card 

---

**📊 Total de flashcards**: 11

> 🎯 **Para repasar**: Cmd/Ctrl+P → "Flashcards: Review flashcards" → Mazo "Arquitectura"

---

## 📚 Referencias & Enlaces

**Enlaces internos**:

- [[cpu-indice-general|🗂️ Hub CPU]]
    
- [[cpu-unidades-internas|Siguiente: Unidades UC y UE]]
    

**Referencias externas**:

- PDF UD2 - Páginas 4-18
    
- Emulador de CPU (mencionado en pág. 19)
    

**Fuente**: TCSO - UD2.pdf (Joaquín Gaspar Medina)

---

## 📋 Metadata

- **Estado**: 🌿 Semilla Brotanado
    
- **Última revisión**: 2024-12-25
    
- **Próxima revisión**: 2024-12-28
    
- **Veces revisado**: 1
    
- **Nivel de comprensión**: 💡 Entendido
    
- **Tiempo estimado de repaso**: 15min
    

---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Hacer flashcards #mejora-concepto
    
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
    
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia