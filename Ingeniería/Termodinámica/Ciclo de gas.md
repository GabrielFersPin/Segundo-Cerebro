# Tema 10

# Ciclo de gas

Son máquinas térmicas que utilizan como combustible gas natural

![](Studies/UPM/Termodinámica%20855c50ea520449b2a8e44316f47e7c32/Tema%2010%205a2bdb7007634956ac162f0c5004fa26/Untitled.png)

- Ratio entre las presiones de entrada en el compresor y la de salida
    
    $r=\frac{p_2}{p_1}$ $p_2=p_3$, $p_1=p_4$ $r=\frac{p_3}{p_4}$
    
- Rendimiento del ciclo
    
    $\eta=\frac{w_N}{q_e}=\frac{w_t-w_c}{q_e}=1-\frac{h_4-h_1}{h_3-h_2}$
    
    Para resolver termodinámicamente un ciclo de gas se necesitarán hallar las entalpías específicas de cada uno de los estados.
    
    $h=u+pV=u+RT$
    
    Siempre que se conozca la temperatura del gas ideal se conocen sus coordenadas termodinámicas.
    
- Entropía
    
    $s_2(p_2,T_2)-s_1(P_1,T_1)=sº(T_2)-sº(T_1)-R\ln\frac{p_2}{p_1}\longrightarrow$ Transformación reversible adiabática
    
    $e^{\frac{sº(T_2)-sº(T_1)}{R}}=\frac{p_2}{p_1}\rightarrow \frac{e^{\frac{sº(T_2)}{R}}}{e^\frac{sº(T_1)}{R}}$
    
    $e^{\frac{sº(T)}{R}}=p_r\longrightarrow$presión reducida( depende únicamente de la temperatura)
    
    $\frac{p_2}{p_1}=\frac{p_{r_2}(T_2)}{p_{r_1}(T_1)}$
    
- Modelo aire estándar frío
    
    Es aquél que considera un ciclo de gas bajo las simplificaciones del análisis estándar  y además supone que el calor específico se mantiene constante para todo el rango de temperaturas.
    
    $s_2(P_2,T_2)-s_1(p_1,T_1)=c_p\ln\frac{T_2}{T_1}-R\ln\frac{p_2}{p_1}$
    
    $\eta=1-\frac{1}{T_2/T_1}=1-\frac{1}{\frac{p_2^{\frac{\gamma-1}{\gamma}}}{p_1}}$ Cuanto mayor el ratio de compresión mayor será el rendimiento 
    
- Irreversibilidad en turbina y compresor
    
    Los estados 2s y 4s son estados ideales.
    
    Para saber cuanto se aleja el ciclo real del ciclo ideal calculase el rendimiento
    
    $\eta_t=\frac{h_3-h_4}{h_3-h_{4s}}$ $\eta_c=\frac{h_1-h_{2s}}{h_1-h_2}$ Para resolver los ciclos tenemos que hallar los estados 2s y 4s.
    
    ![](Studies/UPM/Termodinámica%20855c50ea520449b2a8e44316f47e7c32/Tema%2010%205a2bdb7007634956ac162f0c5004fa26/Untitled%201.png)
    
- ciclo combinado
    
    Es un ciclo de gas y vapor
    
    El calor que cede el aire al pasar por dicho intercambiador debe ser igual al que esta el vapor.
    
    $\dot{m_g}(h_4-h_5)=\dot{m_v}(h_7-h_6)$
    
    ![](Studies/UPM/Termodinámica%20855c50ea520449b2a8e44316f47e7c32/Tema%2010%205a2bdb7007634956ac162f0c5004fa26/Untitled%202.png)
    
    - Rendimiento
        
        El rendimiento del ciclo lleva en cuenta el trabajo neto realizado por ambos ciclos divididos por el calor aportado al ciclo. Este calor es aportado por la combustión.
        
        $\eta=\frac{\dot{W_{N_V}}+\dot{W_{N_g}}}{\dot{Q_{e-gas}}}$
        
        $\dot{W_{N_V}}$- potencia neta desarrollada por el ciclo de vapor
        
        $\dot{W_{N_g}}$- potencia neta desarrollada por el ciclo de gas
        
        $\dot{Q_{e-gas}}$ - Potencia calorífica aportada por la cámara de combustión
        
        $\dot{W_{N_v}}=\dot{m_v}(w_t-w_b)=\dot{m_v}(h_7-h_8)-\dot{m_v}(h_6-h_9)$
        
        $\dot{W_{N_g}}=\dot{m_g}(w_t-w_c)=\dot{m_g}(h_3-h_4)-\dot{m_g}(h_2-h_1)$
        
        $\dot{Q_{e-gas}}=\dot{m_g}(h_3-h_2)$
        
        $\eta=\frac{W_{N_g}+\frac{\dot{m_v}}{\dot{m_g}}W_{N_V}}{h_3-h_2}$
        
        Ratio entre los caudales
        
        $\frac{\dot{m_v}}{\dot{m_g}}=\frac{h_4-h_5}{h_7-h_6}$