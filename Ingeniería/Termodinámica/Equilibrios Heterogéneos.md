# Tema 4

## Equilibrios Heterogéneos

- Convenio de signos
    
    $\Delta U = Q_e + W_e$
    
    $+Q_e$ - Calor entrante en el sistema 
    
    $+W_e$ - Trabajo entrante en el sistema
    
- Expresión del calor
    
    $\partial Q = dU + \partial W$
    
    $dU$ - diferencial total exacta
    
    $\partial Q, \partial W$ - diferncial total no exacta
    
- Capacidad Calorífica del sistema a volumen constante
    
    ![](Studies/UPM/Termodinámica%20855c50ea520449b2a8e44316f47e7c32/Tema%204%20973c10893877457e824a1874ba8a3844/Untitled.png)
    
- Capacidad calorífica del sistema a presión constante
    
    ![](Studies/UPM/Termodinámica%20855c50ea520449b2a8e44316f47e7c32/Tema%204%20973c10893877457e824a1874ba8a3844/Untitled%201.png)
    
- Calores molares
    
    ![](Studies/UPM/Termodinámica%20855c50ea520449b2a8e44316f47e7c32/Tema%204%20973c10893877457e824a1874ba8a3844/Untitled%202.png)
    
- Calores específicos
    
    ![](Studies/UPM/Termodinámica%20855c50ea520449b2a8e44316f47e7c32/Tema%204%20973c10893877457e824a1874ba8a3844/Untitled%203.png)
    
- Magnitudes energéticas
    - Entalpía
        
        $H=U+pV$
        
    - Entropía
        
        $dS=\partial S_e+\partial S_i$
        
    - Energía libre (Función de Helmholtz)
        
        F=U-TS
        
    - Entalpía libre (Función de Gibbs)
        
        G=H-TS
        
- Primer principio de la termodinámica
    
    $\partial Q = dU + \partial W$
    
    $\partial W = p dV$
    
- Segundo principio de la termodinámica
    
    $dS = \partial S_e + \partial S_i$
    
- Condiciones de equilibrio
    - Sistema que evoluciona espontáneamente
        
        $dU+pdV-TdS\leq0$
        
        $TdS_a=-\delta Q$
        
        $S_a$  - Entropía ambiente 
        
        - Entropía y volumen constante
            
             Solo son posibles transformaciones que no aumentan su energía interna.
            
            $dS=dV=0$
            
            $\delta Q=dU$
            
            $TdS_a=-dU$
            
        - Entropía y presión constante
            
            $dS=dp=0$
            
            $\delta Q=dH$
            
            $TdS_a=-dH$
            
            Solo son posible transformaciones en que no aumentan la entalpía.
            
        - Energía interna y volumen constante
            
            $dU=dV=0$
            
            $\delta Q = 0$
            
            $dS_a=0$
            
            Sólo son posibles transformaciones que no hagan disminuir su entropía.
            
        - Temperatura y volumen constante
            
            $dT=dV=0$
            
            $\delta Q = dU$
            
            $TdS_a=-dU$
            
            Posibles transformaciones que no aumenten su energía libre.
            
        - Temperatura y presión constante
            
            $dT=dV=0$
            
            $\delta Q = dH$
            
            $TdS_a = -dH$
            
            Posibles transformaciones que no aumenten su entalpía libre.
            
- Sistema heterogéneos
    - Número de componentes independientes
        
        $c=n-r$
        
        $c$ - componentes independientes
        
        $n$ - número de fases
        
        $r$ - reacciones
        
    - Magnitud extensiva
        
        $Y_i = (\frac{\partial{Y}}{\partial{n_i}})_{T,p,n_j}$ - Funciones de estados extensivas
        
        $Y_i=Y_i(T,p,x_1,x_2,...,x_i,...)$ - Funciones de estado extensivas
        
        $Y_m=y/n=\sum{y_ix_i}$ - Función molar media
        
    - Funciones extensivas convertidas en funciones molares parciales
        
        $(\frac{\partial G_i}{\partial T})_p = -S_i$ 
        
        $(\frac{\partial G_i}{\partial p})_T = V_i$
        
    - Ecuación
        
        $dU^\alpha =T^\alpha dS^\alpha-p^\alpha dV^\alpha + \sum_i{\mu_i}^\alpha {dn_i}^\alpha$
        
        $\alpha - fases$
        
- Sistema Homogéneo abierto
    
    $dU=(\frac{\partial U}{\partial s})_{S,V,n_j} dS + (\frac{\partial U}{\partial V})_{S,n_i} dV + \sum(\frac{\partial U}{\partial{n_i}})_{S,V,n_j} dn_i$
    
    - Ecuaciones termodinámicas
        
        $dH=TdS+Vdp+\sum{\mu_i}{dn_i}$
        
        $dF=-SdT-pdV+\sum{\mu_i}{dn_i}$ Fución de Helmholtz
        
        $dG=-SdT+Vdp+\sum\mu_idn_i$ Función de Gibbs
        
        $dU=TdS-pdV+\sum\mu_idn_i$
        
    - Potencial químico
        
        $\mu_i \equiv (\frac{\partial U}{\partial n_i})_{S,V,n_j}$
        
        $\mu_i=G_i$ - Potencial químico igual a la entalpía libre molar parcial
        
- Sistema homogéneo cerrado
    
    $dU=TdS-pdV$
    
- Condiciones de equilíbrio
    - Equilibrio mecánico
        
        Todas las fases están cerradas y sus energías internas permanecen constantes
        
        ${dn_i}^\alpha =0$ ${dU}^\alpha=0$
        
        En un sistema heterogéneo en equilibrio termodinámico, todas sus fases han de encontrarse a una misma presión.
        
        La presión es la propiedad intensiva que promueve las aceleraciones locales de materia.
        
    - Equilibrio Térmico
        
        No cambia el volumen de ninguna de las fases
        
        ${dV}^\alpha = 0$ y ${dU}^\alpha =0$
        
        Las fases de un sistema heterogéneo en equilibrio termodinámico han de encontrarse todas a una misma temperatura. 
        
        La temperatura es la propiedad intensiva que gobierna los flujos de calor entre las fases.
        
    - Equilibrio químico entre fases
        
        Pasa la cantidad de sustancia ${dn_i}^1$ del componente $i$ de la fase 2 a la 1, permaneciendo constante las demás.
        
        ${dn_i}^1 + {dn_i}^2 = 0$
        
        ${dn_i}^\alpha =0$
        
        ${dn_j}^\alpha =0$
        
    - Teorema de Gibbs
        
        En un sistema heterogéneo en equilibrio termodinámico, el potencial químico de cada uno de sus componentes ha de ser el mismo en todas las fases.
        
        El potencial químico es la propiedad intensiva que impulsa los flujos de materia entre fases.
        
- Ecuaciones termodinámicas en sistemas heterogéneos
    
    Las ecuaciones termodinámicas de un sistema heterogéneo abierto en equilibrio termodinámico tienen la misma forma que las de un sistema homogéneo abierto.
    
    Los sistemas cerrados en equilibrio, tanto homogéneo como heterogéneos verifican las mismas ecuaciones termodinámicas.
    
    El estado de un sistema heterogéneo cerrado en equilibrio queda determinado por sus variables.
    
- Regla de las fases
    
    $f+l=c+2$
    
    la regla de las fases determina el número $l$ de variables intensivas que pueden ser alteradas en un sistema abierto sin destruir el equilibrio.
    
    $l$ - grados de libertad, número de libertad, variancia.
    
    $l$ =0,1,2,3,....
    
    $l = 1$ - monovariante, $l=2$  - bivariante, $l>2$ - plurivariante
    
    $cf+2$ - incógnitas
    
    $c(f-1) + f$ - ecuaciones
    
    $f$ - cantidades de materia
    
    - Sistema plurivariante
        
        $l=c-f+2>2$
        
        Si el sistema está abierto, podemos fijar la $T$ y la $p$ y todavía quedará $l-2=c-f$ fracciones molares indeterminadas
        
        Si se cierra el sistema, quedan fijadas las $n_i$, lo que da origen a c ecuaciones y aparecen como f nuevas incógnitas las cantidades de materia totales $n^\alpha$ de las fases.
        
        $c$  incógnitas que se determinarán mediante las c ecuaciones.
        
    - Sistema bivariante
        
        $l=c-f+2=2$
        
        $f=c$, si fiajmos $T$ y $p$, quedan determinadas todas las fracciones molares.
        
        Al cerrar el sistema se originan $c$ ecuaciones para determinar $f=c$ incógnitas $n^\alpha$.