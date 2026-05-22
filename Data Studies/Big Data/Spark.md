---
cards-deck: null
created: 2026-04-07 09:06
modified: 2026-04-07 09:06
status: 🌱
tipo_nota: tecnica
area: null
procesamiento: CAPTURA-RAPIDA
prioridad: null
tipo-captura: concepto
fecha-examen: ""
proxima-revision: 2026-04-14
complejidad: ⭐
tiempo-estimado: ""
origen: Clase
urgente: false
nivel-comprension: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
---

# Spark

> [!info] Contexto captura
> **Fecha**: 2026-04-07 09:07
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura` <!--SR:!2000-01-01,1,250!2000-01-01,1,250!2026-04-15,4,270-->

---

#pendiente-procesar #captura-rapida


## 📝 Definición

Spark es un motor de procesamiento de datos en clúster, diseñado para ser rápido y de propósito general, capaz de manejar grandes volúmenes de datos a través de computación distribuida. Su arquitectura se basa en el uso de Resilient Distributed Datasets (RDDs) que permiten realizar operaciones en memoria para obtener un rendimiento superior al de los sistemas tradicionales basados en disco.

## ⚙️ Conceptos Clave

- **Lazy Evaluation**: Spark no ejecuta las operaciones inmediatamente, sino que las acumula y optimiza su ejecución cuando se realiza una acción que requiere un resultado.
- **Action**: Son operaciones que devuelven un valor al driver después de ejecutar el flujo de trabajo definido por las transformaciones.
- **Narrow vs Wild Transformations**: 
  - Narrow: Transformaciones que no requieren el movimiento de datos entre las particiones, como `filter` y `select`.
  - Wild: Transformaciones que producen una reorganización de datos, como `join` y `group by`, que pueden causar un `shuffle`.
- **Repartition vs Coalesce**:
  - Repartition: Aumenta el número de particiones distribuyendo uniformemente los datos.
  - Coalesce: Disminuye el número de particiones sin causar un `shuffle` innecesario.
- **DAG (Direct Acyclic Graph)**: Representación gráfica de las operaciones donde no se vuelve al nodo anterior, asegurando un flujo de trabajo unidireccional.

## 💻 Ejemplo Práctico

Supongamos que tenemos un conjunto de datos de ventas y queremos calcular la venta media por producto después de aplicar un filtro. Utilizaríamos:

```scala
val ventas = spark.read.csv("ventas.csv")
val ventasFiltradas = ventas.filter("cantidad > 10")
val mediaVentas = ventasFiltradas.groupBy("producto").agg(avg("venta"))

mediaVentas.show()
```

Este ejemplo demuestra el uso de transformaciones `filter` y `group by`, y una acción `show` para visualizar el resultado.

## 💭 Reflexiones & Conexiones

- **Conexiones con otros sistemas**: Spark se integra fácilmente con Hadoop y otras herramientas del ecosistema Big Data, lo que lo hace versátil para diferentes aplicaciones de procesamiento de datos.
- **Optimización de Recursos**: Considerar el uso de `Repartition` y `Coalesce` para optimizar el uso de recursos en clústeres grandes. <!--SR:!2026-04-15,4,270!2000-01-01,1,250-->

## ❓ Preguntas / Dudas pendientes

- ¿Cómo afecta el número de particiones al rendimiento en un clúster de Spark?
- ¿Cuáles son las mejores prácticas para manejar `shuffles` en operaciones complejas?

## 🔑 Keywords / Conceptos clave

- Lazy Evaluation
- Acción
- Narrow Transformation
- Wild Transformation
- Repartition
- Coalesce
- DAG

## 🧩 Conexiones potenciales

- Relación entre Spark y otros frameworks de procesamiento de datos como Hadoop MapReduce.
- Comparación del rendimiento de Spark en diferentes tipos de clústeres y configuraciones.
- [[Data Processing]]

## 🎓 Flashcards Educativas

1. **¿Qué es Lazy Evaluation en Spark?**
   - Es el retraso de la ejecución de las operaciones hasta que se requiere un resultado, optimizando así el flujo de trabajo. #card

2. **¿Cuál es la diferencia entre una Narrow y una Wild Transformation en Spark?**
   - Narrow Transformation opera dentro de una sola partición sin mover datos, mientras que Wild Transformation requiere mover datos entre particiones, causando un `shuffle`. #card <!--SR:!2026-04-15,4,270--> 

3. **¿Qué función tiene el DAG en Spark?**
   - El DAG representa el flujo de operaciones en Spark, asegurando que las tareas se ejecuten de manera eficiente y ordenada sin ciclos. #card 

4. **¿Cuándo usarías `repartition` en lugar de `coalesce`?**
   - `Repartition` se usa para aumentar el número de particiones, ideal para distribuir datos uniformemente, mientras que `coalesce` reduce particiones sin causar un `shuffle` adicional. #card 