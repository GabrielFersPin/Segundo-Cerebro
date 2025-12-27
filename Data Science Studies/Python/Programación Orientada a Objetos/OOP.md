
## Objetos

- Atributos(Datos):
    
    Características
    
- Métodos(Procedimientos):
    
    Comportamiento
    

## Clase

- Definición:
    
    Generalización de objetos con las mismas características (atributos) y el mismo comportamiento (métodos).
    
- Objetos:
    
    Instancia de una clase
    

```python
class NombreClase:
	atributo = valor
	def metodo(self):
		código
```

## Método Constructor

```python
class NombreClase:
	def __init__(self, argumento1, argumento2): #__init__ constructor
		self.atributo1 = argumento1
		self.atributo2 = argumento2
	def metodo(self):
		código
```

- ¿Cómo crear un objeto a partir de una clase?
    
    se utiliza el nombre seguido de paréntesis: 
    
    ```python
    objeto = Nombreclase(valor1, valor2)
    ```
    
- ¿Cómo dar valores a un objeto?
    
    ```python
    objeto.atributo1 = nuevo_valor1
    objeto.atributo2 = nuevo_valor2
    ```
    

## Definición de métodos sobre una clase

- Métodos
    
    Son funciones dentro de una clase que están diseñadas para realizar una tarea específica.
    
- Añadir un método dentro de otro
    
    ```python
    class Bag:
    	def __init__(self):
    	self.data = [] #lista
    	def add(self, x): #método que añade el valor x
    		self.data.append(x)
    	def addtwice(self, x):
    		self.add(x)
    		self.add(x)
    ```
    
- Incluir diccionario a una clase
    
    ```python
    My_dict = {'key1': 'value1', 'key2': 'value2'}
    ```