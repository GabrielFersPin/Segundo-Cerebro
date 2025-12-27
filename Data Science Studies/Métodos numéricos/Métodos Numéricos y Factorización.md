
## Funciones en Matlab

- Función
    
    ```matlab
    function [salida1, salida2] = nombre(entrada1, entrada2, entrada3)
    	%ordenes 
    end
    ```
    
- Llamar la función
    
    ```matlab
    [x, y] = nombre(1, 2, 3)
    ```
    
- Función symfun
    
    ```matlab
    syms x y
    
    f = symfun([x+y x-y x*y],[x y])
    ```
    
    $f(x, y)=[x+y \ x-y \ x y]$
    
- Bucles
    
    ```matlab
    for i = 1:2:10 %inicio: paso: final
    		disp(i)
    end
    ```
    

## Interpolación lineal de funciones

- Interpolación matlab
    
    ```matlab
    sysm x
    f=symfun(x^2, x);
    a=0;
    b=3;
    h=0.01;
    plot(a:h:b, f(a:h:b))
    ```
    
- Splines
    - Tenemos $(x_0, y_0), ..., (x_n, y_n)$ puntos para interpolar definida por $S(x) = S_i(x)$ siendo $S_i$  un polinomio cuadrático
    - Hay la condición que que pasen por los puntos dados. $S_i(x) = y_i$
    - Condición de suavidad: la derivada en los puntos de unión sean iguales: $S_i'(x_i)=S'_{i+1}(x_i)$
    - Condición inicial que depende de la función a interpolar: $S_0'(a)=f'(a)$
    - Spline Natural si $S''_0(x_0)=S''_n(x_n)=0$
    - Spline fijo si igualamos las derivadas a la función a interpolar $S'_0(a)=f'(a)$ $S'_n(b)= f'(b)$
- Polinomio de Taylor
    
    $T_n(x)=\sum_{k=0}^{n}\frac{f^{k)}(a)}{k!}(x-a)^k$
    

## Ecuaciones no Lineales

<aside>
👉 Este documento discute varios métodos numéricos para aproximar las soluciones de ecuaciones, incluyendo el método de la bisección, el método de la secante, el método de Newton-Raphson y el método del punto fijo.

</aside>

- Método de la bisección
    
    El método de la bisección es un algoritmo que se utiliza para encontrar la raíz de una función. Este método es muy sencillo de implementar y siempre converge a una solución. El método de la bisección consiste en dividir el intervalo en dos partes iguales y evaluar la función en el punto medio. Dependiendo del signo de la función en el punto medio, se selecciona la mitad del intervalo donde se encuentra la solución. Este proceso se repite hasta que se alcanza la precisión deseada.
    
    Considerando el intervalo $I_0 = [a, b]$ y lo dividimos a la mitad se queda:
    
    $r_0=\frac{a+b}{2}$
    
    Si consideramos la iteración $n + 1$ y conocemos $I_n=[a_n, b_n]$ entonces se queda:
    
    $r_n=\frac{a_n+b_n}{2}$ 
    
    Entonces se puede observar que el intervalo $I_n$  es igual a $I_n = |b_n -a_n|=\frac{b-a}{2^n}$
    
    Tomando $r$  como solución de la ecuación $f(x)=0$, entonces el error sería:
    
     $E_n=|r-r_n|$  
    
    El error se queda acotado en:
    
    $E_n\leq\frac{l_n}{2}=\frac{b-a}{2^{n+1}}$
    
    Y para lograr un error inferior a $E$ se necesita que el número de iteraciones $n$  sea:
    
    $n>\frac{\log(b-a)-\log(E)}{\log(2)}-1$
    
- Método de la secante
    
    <aside>
    👉 El método de la secante es otro método numérico utilizado para encontrar las raíces de una función. A diferencia del método de la bisección, el método de la secante no requiere que la función sea continua en el intervalo de búsqueda. En su lugar, el método de la secante utiliza una aproximación de la pendiente de la función para estimar la ubicación de la raíz.
    
    </aside>
    
    - Método de la secante
        
        El método de la secante se puede utilizar para aproximar la raíz de una función en un intervalo $$[a, b]$$. Para utilizar este método, se necesitan dos valores iniciales, $$x_0$$ y $$x_1$$, que se encuentran en el intervalo de búsqueda. A continuación, se calcula la siguiente aproximación de la raíz, $$x_2$$, utilizando la siguiente fórmula:
        
        $x_2=x_1-\frac{f(x_1)(x_1-x_0)}{f(x_1)-f(x_0)}$
        
        Este proceso se repite hasta que se alcanza la precisión deseada. El método de la secante es más rápido que el método de la bisección, pero no siempre converge a una solución.
        
- Método de Newton-Raphson
    
    <aside>
    👉 El método de Newton-Raphson es otro método numérico utilizado para encontrar las raíces de una función. Este método es más rápido que el método de la bisección y el método de la secante, pero puede ser más difícil de implementar y no siempre converge a una solución.
    
    </aside>
    
- Método del punto fijo
    
    El método del punto fijo es un método numérico utilizado para aproximar la solución de una ecuación a través de una iteración. Para utilizar este método, se necesita reescribir la ecuación en la forma $x = g(x)$. A continuación, se elige un valor inicial $x_0$ y se aplica la siguiente fórmula iterativa:
    
    $x_{n+1} = g(x_n)$
    
    Este proceso se repite hasta que se alcanza la precisión deseada. El método del punto fijo converge a una solución si se cumplen ciertas condiciones de convergencia, como la existencia de una raíz única y una función$g(x)$ que es continua y tiene una derivada acotada en el intervalo de solución.