---
cards-deck: Algoritmos:Big O
created: 2025-11-26
modified: 2025-12-23
status: 🌿 Creciendo
tipo_nota: tecnica
area: Algoritmos
nivel-comprension: 💡
proxima-revision: 2026-01-22
ultima-revision: 2025-12-23
veces-revisado: 2
estado: 🟢 Al día
tiempo-repaso: 15min
tiempo-estimado: 5min
---

# Notaciones Asintóticas: Big O, Omega y Theta

> [!abstract] Objetivo
> Entender las tres notaciones asintóticas principales (O, Ω, Θ) para describir el comportamiento de algoritmos: límites superiores, inferiores y exactos. Saber cuándo usar cada una y cómo se relacionan entre sí.

---

## 🎓 Contexto Académico

**Asignatura/Curso**: Algoritmos y Estructuras de Datos

**Relevancia para**: Examen + Análisis riguroso de algoritmos + Papers académicos

**Dificultad percibida**: ⭐⭐⭐☆☆ Medio (conceptualmente simple, pero fácil de confundir)

---

## 📝 Definición

Las **notaciones asintóticas** son herramientas matemáticas para describir el **comportamiento de un algoritmo** cuando el tamaño de entrada (n) crece hacia el infinito. Mientras que **Big O** (la más conocida) describe el **peor caso**, existen otras dos notaciones importantes:

- **Big O (O)**: **Límite superior** - "El algoritmo nunca será peor que esto"
- **Big Omega (Ω)**: **Límite inferior** - "El algoritmo nunca será mejor que esto"
- **Big Theta (Θ)**: **Límite ajustado** - "El algoritmo es exactamente esto"

**¿Por qué importan las tres?**
- En papers académicos se usan las tres para describir algoritmos con precisión
- Big O solo te dice el peor caso, pero no el mejor
- Big Theta te da la descripción más completa y precisa
- En la práctica cotidiana, Big O suele ser suficiente, pero conocer las tres te hace mejor analista

---

## ⚙️ Conceptos Clave

### 📌 Big O (O) - Límite Superior

**Tipo**: Cota superior asintótica

**Características**:
- Describe el **peor caso** o **límite máximo** de crecimiento
- "f(n) es O(g(n))" significa que f(n) **crece a lo mucho tan rápido** como g(n)
- Es la notación **más usada** en la práctica
- Puede ser **imprecisa**: un algoritmo O(n) también es O(n²) técnicamente (pero no es útil decirlo así)
- Útil para **garantizar que un algoritmo no será peor** que cierto límite

**Definición matemática**:
```
f(n) = O(g(n)) si existen constantes c > 0 y n₀ > 0 tales que:
f(n) ≤ c · g(n)  para todo n ≥ n₀
```

**Visualización**:
```
f(n) ≤ c·g(n)

       │                    c·g(n)
       │                   ╱
       │                 ╱
       │               ╱
f(n)   │    ╱╲      ╱
       │  ╱    ╲  ╱
       │╱        ╲╱
       └─────────────────────→ n
            n₀
```

**Relacionado**: [[Big O y Análisis de Complejidad]] • Peor Caso • Análisis de Algoritmos

---

### 📌 Big Omega (Ω) - Límite Inferior

**Tipo**: Cota inferior asintótica

**Características**:
- Describe el **mejor caso** o **límite mínimo** de crecimiento
- "f(n) es Ω(g(n))" significa que f(n) **crece al menos tan rápido** como g(n)
- Menos usado que Big O, pero importante para demostrar **límites de imposibilidad**
- Útil para decir "ningún algoritmo puede hacer esto más rápido que Ω(n log n)"
- Ejemplo: ordenar por comparaciones es Ω(n log n) - nadie puede hacerlo más rápido

**Definición matemática**:
```
f(n) = Ω(g(n)) si existen constantes c > 0 y n₀ > 0 tales que:
f(n) ≥ c · g(n)  para todo n ≥ n₀
```

**Visualización**:
```
f(n) ≥ c·g(n)

       │    f(n)
       │   ╱  ╲
       │ ╱      ╲
       │╱         ╲
       │            ╲
       │  c·g(n)     ╲
       │╱              ╲
       └─────────────────────→ n
            n₀
```

**Relacionado**: Mejor Caso • Límites Inferiores • Teoría de Complejidad

---

### 📌 Big Theta (Θ) - Límite Ajustado

**Tipo**: Cota ajustada asintótica

**Características**:
- Describe el **crecimiento exacto** del algoritmo
- "f(n) es Θ(g(n))" significa que f(n) **crece exactamente tan rápido** como g(n)
- Es la notación **más precisa** y **más informativa**
- Solo se puede usar cuando el algoritmo **tiene el mismo comportamiento en mejor y peor caso**
- Si f(n) = Θ(g(n)), entonces f(n) = O(g(n)) Y f(n) = Ω(g(n))

**Definición matemática**:
```
f(n) = Θ(g(n)) si existen constantes c₁, c₂ > 0 y n₀ > 0 tales que:
c₁ · g(n) ≤ f(n) ≤ c₂ · g(n)  para todo n ≥ n₀
```

**Visualización**:
```
c₁·g(n) ≤ f(n) ≤ c₂·g(n)

       │          c₂·g(n)
       │         ╱
       │       ╱
f(n)   │    ╱╲╱
       │  ╱ ╱ ╲
       │╱  ╱    ╲
       │  ╱ c₁·g(n)
       └─────────────────────→ n
            n₀
```

**Relacionado**: Análisis Exacto • Complejidad Promedio

---

## 💻 Ejemplos Prácticos

### Ejemplo 1: Búsqueda Lineal

```python
def busqueda_lineal(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

**Análisis**:
- **Mejor caso**: O(1) - elemento en primera posición → Ω(1)
- **Peor caso**: O(n) - elemento no existe o está al final
- **No tiene Θ exacto** porque mejor y peor difieren

**Notaciones correctas**:
- O(n) ✓ - nunca peor que lineal
- Ω(1) ✓ - en el mejor caso es constante
- NO se puede decir Θ(n) ✗ - no es exacto en todos los casos

---

### Ejemplo 2: Suma de Array

```python
def suma_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
```

**Análisis**:
- **Siempre recorre todo el array**: n operaciones
- **Mejor caso**: Θ(n)
- **Peor caso**: Θ(n)
- **Caso promedio**: Θ(n)

**Notaciones correctas**:
- O(n) ✓ - límite superior
- Ω(n) ✓ - límite inferior
- **Θ(n) ✓** - descripción exacta (lo más preciso)

---

### Ejemplo 3: Algoritmo con condicional

```python
def procesar(n):
    if n % 2 == 0:
        # Rama 1: O(n²)
        for i in range(n):
            for j in range(n):
                print(i, j)
    else:
        # Rama 2: O(n)
        for i in range(n):
            print(i)
```

**Análisis**:
- **Peor caso** (n par): O(n²)
- **Mejor caso** (n impar): Ω(n)
- **NO tiene Θ** porque depende de la entrada

**Notaciones correctas**:
- O(n²) ✓ - en el peor de los casos
- Ω(n) ✓ - en el mejor de los casos
- NO Θ - porque varía según entrada

---

## 📊 Tabla Comparativa Visual

| Algoritmo | Mejor Caso | Peor Caso | Promedio | Notación Más Precisa |
|-----------|------------|-----------|----------|---------------------|
| **Búsqueda Lineal** | Ω(1) | O(n) | O(n) | No tiene Θ único |
| **Búsqueda Binaria** | Ω(1) | O(log n) | Θ(log n) | Θ(log n) |
| **Bubble Sort** | Ω(n) | O(n²) | Θ(n²) | Θ(n²) en promedio |
| **Merge Sort** | Θ(n log n) | Θ(n log n) | Θ(n log n) | **Θ(n log n)** ✓ |
| **QuickSort** | Ω(n log n) | O(n²) | Θ(n log n) | No tiene Θ único |
| **Suma Array** | Θ(n) | Θ(n) | Θ(n) | **Θ(n)** ✓ |

---

## 🎯 Relación entre las Tres Notaciones

### Diagrama de Venn:

```
         ┌─────────────────────┐
         │      O(n²)          │
         │  ┌──────────────┐   │
         │  │   Θ(n log n) │   │
         │  └──────────────┘   │
         │                     │
         └─────────────────────┘
              ┌──────────────┐
              │   Ω(n)       │
              └──────────────┘

Algoritmo: Merge Sort
- O(n²) ✓ pero impreciso
- Θ(n log n) ✓ exacto
- Ω(n) ✓ pero impreciso
```

### Reglas:
1. **Si f(n) = Θ(g(n))** → entonces f(n) = O(g(n)) Y f(n) = Ω(g(n))
2. **Si f(n) = O(g(n))** → NO necesariamente f(n) = Θ(g(n))
3. **Si f(n) = Ω(g(n))** → NO necesariamente f(n) = Θ(g(n))
4. **Θ es la intersección de O y Ω**

---

## 💭 Reflexiones & Conexiones

**En la práctica diaria**, cuando programadores dicen "este algoritmo es O(n)", muchas veces quieren decir Θ(n) pero usan O por costumbre. Es técnicamente correcto (O es límite superior), pero menos preciso.

**En papers académicos**, la distinción es crucial:
- "Este problema es O(n log n)" → "Encontré un algoritmo que lo resuelve en n log n"
- "Este problema es Ω(n log n)" → "Demostré que NINGÚN algoritmo puede hacerlo más rápido"
- "Este problema es Θ(n log n)" → "Es exactamente n log n, ya encontramos el óptimo"

**Ejemplo histórico**: Ordenar por comparaciones es **Θ(n log n)**. Esto significa:
- Ω(n log n): nadie puede ordenar más rápido (límite inferior demostrado)
- O(n log n): existen algoritmos que lo logran (merge sort, heap sort)
- Por tanto, Θ(n log n): es el límite exacto, ya no se puede mejorar

Conecta con [[Big O y Análisis de Complejidad]] - esta nota expande el análisis más allá de solo Big O.

---

## 🎴 Flashcards

> 💡 **Formato**: Usa `Pregunta::Respuesta` para flashcards inline

¿Qué describe Big O (O)?::Límite superior (peor caso) - el algoritmo nunca será peor que esto #notacion-asintotica #bigO

¿Qué describe Big Omega (Ω)?::Límite inferior (mejor caso) - el algoritmo nunca será mejor que esto #notacion-asintotica #omega

¿Qué describe Big Theta (Θ)?::Límite ajustado (exacto) - el algoritmo es exactamente esto en todos los casos #notacion-asintotica #theta

Big O (O)
?
Límite superior. f(n) ≤ c·g(n). Describe el peor caso. Es la notación más usada.
#bigO #limite-superior

Big Omega (Ω)
?
Límite inferior. f(n) ≥ c·g(n). Describe el mejor caso. Útil para demostrar imposibilidades.
#omega #limite-inferior

Big Theta (Θ)
?
Límite ajustado. c₁·g(n) ≤ f(n) ≤ c₂·g(n). Describe el comportamiento exacto. La más precisa.
#theta #limite-exacto

¿Cuándo usar Θ en lugar de O?::Cuando el algoritmo tiene el mismo comportamiento en mejor y peor caso (ej: suma de array siempre es n pasos) #theta #cuando-usar

Si f(n) = Θ(g(n)), ¿qué más es cierto?::f(n) = O(g(n)) Y f(n) = Ω(g(n)) - Theta implica ambos límites #relacion #theta

¿Merge Sort es O, Ω o Θ?::Θ(n log n) - siempre toma n log n operaciones sin importar la entrada #mergesort #theta

¿Búsqueda lineal es O, Ω o Θ?::O(n) en peor caso, Ω(1) en mejor caso. NO tiene Θ único porque varía #busqueda-lineal

¿Por qué ordenar por comparaciones es Ω(n log n)?::Es un límite inferior demostrado matemáticamente - ningún algoritmo basado en comparaciones puede hacerlo más rápido #limite-inferior #ordenamiento

Un algoritmo O(n²) también es técnicamente O(n³). ¿Por qué no lo decimos así?::Porque O describe el límite superior MÁS AJUSTADO posible. O(n³) es correcto pero impreciso e inútil #precision #big-o

¿Qué notación usarías para decir "este es el algoritmo óptimo para este problema"?::Θ (theta) - porque demuestra que es exactamente el límite teórico #optimo #theta

Si un algoritmo tiene mejor caso O(1) y peor caso O(n), ¿cuál es su Θ?::No tiene un Θ único - Theta requiere que mejor y peor caso coincidan #theta #cuando-no-usar

En la práctica, ¿cuál notación se usa más?::Big O - aunque a veces se usa para referirse a Θ por convención #practica #big-o

---

**📊 Total de flashcards**: 13

> 🎯 **Para revisar**: Cmd/Ctrl+P → "Flashcards: Review flashcards"

---

## 📚 Referencias & Enlaces

**Enlaces internos**:
- [[Big O y Análisis de Complejidad]]
- [[Estructuras_Dinámicas_de_Datos]]

**Referencias externas**:
- "Introduction to Algorithms" - CLRS (Capítulo 3: Growth of Functions)
- Notación asintótica en Wikipedia
- Asymptotic Notation - Khan Academy

**Fuente**: UD1_EstructurasDatos.pdf + Apuntes de clase + CLRS Capítulo 3

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2025-11-26
- **Próxima revisión**: 2025-11-29 (en 3 días)
- **Veces revisado**: 0
- **Nivel de comprensión**: 💡 Entiendo bien (pero necesito practicar distinguir cuándo usar cada una)
- **Tiempo estimado de repaso**: 15min

---

> [!tip] 💡 Próximos pasos
> Cuando revises esta nota:
> 1. Practica identificar qué notación usar en algoritmos reales
> 2. Revisa las flashcards de definiciones matemáticas
> 3. Intenta demostrar formalmente un límite Θ para un algoritmo simple
> 4. Actualiza el contador de revisiones y ajusta la próxima fecha según comprensión


---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [x] Tengo que hacer algún ejercicio🏁 #mejora-concepto ✅ 2025-12-23

