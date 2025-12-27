# Tema 7

# Tracción o compresión

- Tracción o compresión simple
    
    Cuando sobre sus secciones actúan únicamente esfuerzos axiles, es decir, fuerzas normales a las secciones y aplicadas en sus respectivo centros de gravedad
    
    Tracción>0
    
    Compresión<0
    
    Tensión Normal: $\sigma=N/A$
    
- Hipótesis de Bernoulli
    
    Durante la deformación de una pieza recta sometida a esfuerzo axil las secciones transversales permanecen planas y paralelas a sí mismas
    
- Alargamiento o acortamiento
    
    $\Delta l=\frac{N.l}{E.A}$
    

# Barras que no trabajan

1. Cuando se tienen dos barras no colineales, concurrentes en un nudo, y en éste no hay carga exterior, ni reacción de apoyo aplicada, entonces ninguna de las barras trabajan.

![](Studies/UPM/Tecnología%20de%20los%20Materiales%2072d3fd20e92345e1852afc64d86bb26d/Resistencia%20de%20los%20Materiales%20f934fbe6f2fc4050a942a7c207d35bc7/Tema%207%20c9873862fedf4f2b84c1e854ab49fa91/Untitled.png)

1. Cuando se tienen tres barras, dos de ellas colineales, concurrentes en un nudo no cargado (ni carga exterior ni reacción de apoyo). La barra que forma ángulo tendrá un esfuerzo axil nulo y las dos barras colineales, estarán sometidas al mismo esfuerzo.

![](Studies/UPM/Tecnología%20de%20los%20Materiales%2072d3fd20e92345e1852afc64d86bb26d/Resistencia%20de%20los%20Materiales%20f934fbe6f2fc4050a942a7c207d35bc7/Tema%207%20c9873862fedf4f2b84c1e854ab49fa91/Untitled%201.png)

# Resolución de estructuras articuladas planas por el método de los nudos

1. Dibujar el diagrama del sólido libre de la celosía completa$\rightarrow$equilibrio estático$\rightarrow$reacciones en los apoyos.
2. Escoger el nudo en el que sólo concurran dos barras de esfuerzo desconocido
3. Aislar el nudo en cuestión y plantear las ecuaciones de equilibrio en el nudo, suponiendo de tracción los esfuerzos desconocidos. Si el resultado es positivo significará que la barra trabaja a tracción; en caso contrario,(esfuerzo negativo), indica que la barra trabaja a compresión.
    
    ![](Studies/UPM/Tecnología%20de%20los%20Materiales%2072d3fd20e92345e1852afc64d86bb26d/Resistencia%20de%20los%20Materiales%20f934fbe6f2fc4050a942a7c207d35bc7/Tema%207%20c9873862fedf4f2b84c1e854ab49fa91/Untitled%202.png)
    
4. Calcular el valor de los axiles en el resto de barras. Para ello se procede del mismo modo: se aísla el nudo y se restablecen las ecuaciones de equilibrio.

# Variaciones Térmicas

- Variación de longitud
    
    $\Delta l=\alpha.l.\Delta T$
    
    $\Delta l=\frac{N.l}{E.A}+\alpha.l.\Delta T$
    
- Defectos de montaje
    
    Barra 1mm más corta $\Delta l=\frac{N.l}{E.A}(mm)-1$
    
    Barra 2mm más larga $\Delta l=\frac{N.l}{EA}(mm)+2$
    

# Tensiones de elementos de pequeño espesor

- Depósitos esféricos
    - Tensión superficial o tensión normal
        
        $\sigma_1=\sigma_2=\frac{p.r}{2.t}$
        
        $p-$presión
        
        $r-$radio
        
        $t-$espessor
        
    - Tensión tangencial máxima
        
        $\tau_{máx}=\frac{\sigma_1-\sigma_3}{2}=\frac{p.r}{4.t}$
        
    - Deformación máxima
        
        $\varepsilon_{máx}=\frac{\sigma}{E}(1-\upsilon)$
        
        $\upsilon-$coef. de Poisson
        
- Depósitos cilíndricos
    - Tensión circunferencial
        
        $\sigma_1=\frac{p.r}{t}$
        
    - Tensión superficial
        
        $\sigma_2=\frac{p.r}{2t}$
        
    - Tensión tangencial máxima
        
        $\tau_{max}=\frac{\sigma_1-\sigma_3}{2}=\frac{p.r}{2t}$
        
    - Deformación máxima
        
        $\varepsilon_{max}=\frac{1}{E}[\sigma_1-\upsilon\sigma_2]$