# Tema 5

## Equilibrio de fases en sistemas monocomponentes

- Cuerpos puros
    
    Sistemas formados por un solo componente 
    
    No es posible más de tres fases en equilibrio
    
    - Una sola fase
        
        $f=1, l=2$ Sistema bivariante
        
    - Dos fases
        
        $f=2, l=1$ sistema monovariante
        
    - Tres fases
        
        $f=3, l=0$  Sistema invariante
        
- Diagrama de equilibrio
    
    ![](Studies/UPM/Termodinámica%20855c50ea520449b2a8e44316f47e7c32/Tema%205%201d915585c4ff4bada738415ade161530/Untitled.png)
    
    Corresponde a una sustancia que puede representarse en forma de tres fases $\alpha, \beta$ y $\gamma$.
    
    - Región en que es estable la fase $\alpha$
        
        ${G_m}^\alpha<{G_m}^\beta$
        
        ${G_m}^\alpha<{G_m}^\gamma$
        
    - En la línea que es estable la mezcla de las fases $\alpha$  y $\beta$
        
        ${G_m}^\alpha={G_m}^\beta$
        
    - En el punto triple **A**
        
        ${G_m}^\alpha={G_m}^\beta={G_m}^\gamma$
        
    - Fase estable por encima de la línea de equilibrio
        
        Es la fase de menor volumen ${V_m}^\alpha<{V_m}^\beta$
        
    - Fase a la derecha de la línea de equilibrio
        
        Fase que más absorbe calor al formarse
        
- Ecuación de Clapeyron
    
    $\frac{dp}{dT}=\frac{\lambda}{T\Delta V_m}$
    
    $\lambda$ - calor de transformación molar
    
- Ecuación de Clausiu-Clapeyron
    
    $\ln p=\frac{-\lambda}{RT} + A$
    
    $p=Be^{\frac{-\lambda}{RT}}$
    
    $B=e^A$
    
- Estado crítico
    
    La densidad del vapor, que es mucho más compresible que el líquido, irá aproximándose cada vez más a la de éste, hasta llegar a igualarse con ella a una cierta temperatura, característica de la sustancia de que se trate y denominase temperatura crítica $T_c$ de dicha sustancia. La presión $p_c$ se llama presión crítica y el volumen molar, que será el único por ser iguales las densidades, volumen molar crítico $V_{mc}$. 
    
- Gases Reales
    
    ![](Studies/UPM/Termodinámica%20855c50ea520449b2a8e44316f47e7c32/Tema%205%201d915585c4ff4bada738415ade161530/Untitled%201.png)
    
    **BC** - intervalo de saturación
    
    Curva de **B** a **C** - línea de saturación
    
    **KB** - línea del vapor saturado
    
    **KC** - línea del líquido saturado
    
    Dominio bajo la cuva - región de saturación en la que coexisten vapor y líquido
    
    Conforme aumenta la temperatura de la isoterma, los puntos **B** y **C** se van apoximando, hasta llegar al límite en el que el tramo horizontal **BC** se reduce a un punto de inflexión con tangente horizontal. Esto ocurre a una temperatura $T_c$, a la que se desvanece la diferencia entre líquido y vapor. En el diagrama se evidencia que a $T_c$ los volumenes molares del líquido y el vapor se hacen iguales, como ha de ocurrir con todas las demás propiedades intensivas de ambas fases.
    
- Ecuación de Van der Waals
    
    $pV_m=RT$ - ecuación para un gas ideal
    
    Para Tener en cuenta el primer efecto se suma $\frac{a}{V_m^2}$
    
    Para tener en cuenta el segundo efecto se resta $b$
    
    $(p + \frac{a}{V_m^2})(V_m-b)=RT$ - Para un mol
    
    $(p+\frac{n^2a}{V^2}(V-nb)=nRT$ - Para n moles
    
    b - volumen excluído
    
    ![](Studies/UPM/Termodinámica%20855c50ea520449b2a8e44316f47e7c32/Tema%205%201d915585c4ff4bada738415ade161530/Untitled%202.png)
    
    El volumen excluido por un par de moléculas es $2r$, ya que las moléculas no pueden aproximarse más. El volumen excluido será $\frac{4}{3}\pi(2r)^3$ por par de moléculas y $\frac{2}{3}\pi(2r)^3$  por par de moléculas y $\mathbb{N}\frac{4}{3}\pi r^3$ para un mol, siendo $\mathbb{N}$ el número de avogadro. El volumen de las moléculas ocupados por $\mathbb{N}$ moléculas se llama *covolumen*.
    
    a - constante de Van der Waals
    
    $T_c=\frac{8a}{27Rb}$; $p_c=\frac{a}{27b^2}$; $V_{mc}=3b$
    
    $a=3p_cV_{mc}^2$; $b=\frac{V_{mc}}{3}$; $R=\frac{8p_cV_{mc}}{3T_c}$
    
- Funciones de estado reducidas
    
    $T_r=\frac{T}{T_r};$ $p_r=\frac{p}{p_c}$; $V_{mr}=\frac{V_m}{V_{mc}}$
    
    $T=\frac{8aT_r}{27Rb}$; $p=\frac{ap_r}{27b^2};$ $V_m=3bV_{mr}$
    
    Ecuación de van der Waals reducida, que es universal y no contiene parámetro característico alguna del gas a que se aplique.
    
    Ley de los estados correspondientes, que dice: Si varias sustancias tienen iguales dos de sus funciones de estado reducidas, han de tener igual la tercera.