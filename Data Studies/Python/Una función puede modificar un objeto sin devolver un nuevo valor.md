## Idea principal

En Python, una función puede realizar acciones (modificar un objeto, imprimir información, escribir un archivo, etc.) y devolver un valor mediante `return`. Estas son dos operaciones independientes.

Una función no devuelve automáticamente el resultado de las acciones que realiza. Solo devuelve el valor indicado por `return`. Si no existe un `return`, Python devuelve `None`.

## Ejemplo

```python
def mensaje():
    print("Hola")

resultado = mensaje()

print(resultado)
```

Salida:

```
Hola
None
```

La función imprime `"Hola"`, pero como no tiene `return`, el valor de `resultado` es `None`.

## Modificar un objeto

Algunas funciones o métodos modifican directamente el objeto sobre el que trabajan y no devuelven un nuevo objeto.

```python
numbers = [3, 1, 2]

numbers.sort()

print(numbers)
```

Salida:

```
[1, 2, 3]
```

`sort()` modifica la lista existente y devuelve `None`.

Por ello:

```python
resultado = numbers.sort()

print(resultado)
```

produce:

```
None
```

## Crear un nuevo objeto

Otras funciones no modifican el objeto original, sino que crean uno nuevo.

```python
numbers = [3, 1, 2]

sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)
```

Salida:

```
[3, 1, 2]
[1, 2, 3]
```

## Regla práctica

Preguntarse siempre:

> ¿Esta función modifica un objeto existente o devuelve uno nuevo?

- Modifica el objeto → normalmente devuelve `None`.
- Devuelve un objeto nuevo → normalmente puede asignarse a una variable.

## Ejemplos comunes

| Modifica el objeto | Devuelve un nuevo valor |
|--------------------|-------------------------|
| `list.sort()` | `sorted()` |
| `list.append()` | `sum()` |
| `list.extend()` | `len()` |
| `list.reverse()` | `max()` |
| `dict.update()` | `min()` |

## Idea clave

No confundir el efecto secundario de una función con su valor de retorno.

Una función puede modificar datos, imprimir información y devolver un valor distinto, o no devolver ninguno (`None`).