# 1. ¿Qué es una Tabla Hash?

Es una estructura de datos diseñada para búsquedas ultra-rápidas.

**Objetivo:** Encontrar un dato en tiempo constante O(1) (instantáneo), sin importar cuántos datos tengas almacenados.
**Diferencia clave:** En una lista normal buscas "registro por registro" (lento). En una tabla hash, calculas la posición exacta donde está el dato.

# 2. Componentes Principales

## A. La Clave (Key)

Es el identificador único del dato (ej. ID del documento: '100', 'A1'). Sobre esto realizamos el cálculo.

## B. Función Hash

Es la "fórmula mágica" que convierte la Clave (texto) en un Índice (número).

**Misión:** Transformar cualquier dato complejo en una "dirección de memoria" válida.
**Estrategias comunes:**

- **Suma:** Sumar los valores ASCII de las letras. (Sencillo, pero genera colisiones fáciles, ej: "ABC" = "CBA").
- **Producto:** Multiplicar los valores ASCII. (Más disperso, reduce agrupamientos).
- **Operación Módulo (%):** Se usa siempre al final `resultado % tamaño_tabla` para asegurar que el número resultante caiga dentro de los límites de tu tabla (ej. entre 0 y 9).

## C. El Bucket (Cubo)

Es el espacio físico en la tabla donde se guarda el dato. La función hash te dice "Vete al bucket 5".

# 3. Manejo de Colisiones

**¿Qué es una colisión?** Cuando dos claves diferentes generan el mismo índice hash. (Ej. "Ana" y "Pepe" intentan entrar en la habitación 8). Esto es inevitable.

**Solución típica: Encadenamiento (Chaining)**

- Cada "habitación" (Bucket) no es un solo espacio, sino una Lista.
- Si llega un dato nuevo y la habitación está ocupada, se añade a la lista de esa habitación.

**Búsqueda con colisión:**

1. Calculas hash -> Vas al bucket.
2. Si hay varios datos en la lista del bucket, la recorres linealmente hasta encontrar el tuyo.
*Nota: Si las listas se hacen muy largas, la velocidad se pierde.*

# 4. Problema de Rendimiento (Factor de Carga)

Si metes 1000 datos en una tabla de tamaño 10, cada bucket tendrá listas de 100 elementos. Tu búsqueda rápida se volverá lenta.

**Solución (Re-hashing):** Cuando la tabla se llena (ej. al 70%), debes crear una tabla más grande (ej. duplicar tamaño) y volver a calcular la posición de todos los datos para redistribuirlos y "vaciar" los buckets.
