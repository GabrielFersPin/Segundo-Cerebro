# Tema 1

# Movimiento vibratorio

## Vibraciones

- Tipos de vibraciones (2)
    - Libres
        
        No amortiguadas/Amortiguadas
        
    - Forzadas
        
        No amortiguadas/Amortiguadas
        

## Elementos de un sistema oscilatorio (3)

- Inercia (masas)
    
    $F=m\alpha=m\ddot{x}$
    
- Elásticos
    
    $F=kx$
    
- Amortiguamiento
    - Rozamiento viscoso
        
        $F_V=cv$
        
        $c$ - coeficiente de amortiguamiento
        
    - Rozamiento de fricción seca
        
        $F=\mu N$
        

## Ecuación general de un sistema masa-resorte

- Movimiento libre
    
    $m\ddot{x}+kx=0$
    
- Forzado no amortiguado
    
    $m\ddot{x}+kx=F$
    
- Forzado amortiguado
    
    $m\ddot{x} +c\dot{x}+kx=F$
    

## Movimiento armónico simple

- Fórmula
    
    $x(t)=Asen(\omega t+\varphi_0)$
    
    $x$ - elongación
    
    $A$  - Amplitud
    
    Fase: $\varphi=\omega t+\varphi_0$
    
    Fase inicial: $\varphi_0$
    
- Periodo T
    
    $T=\frac{2\pi}{\omega}$
    
- Frecuencia
    
    $f=\frac{1}{T}=\frac{\omega}{2\pi}$ (Hz)
    
- Frecuencia Angular
    
    $\omega=\frac{2\pi}{T}=2\pi f$
    
- Condiciones iniciales
    
    $x_0=Asen(\varphi_0)$
    
    $V_0=A\omega_ncos\varphi$
    
    $A=\sqrt{x^2_0+(\frac{V_0}{\omega_n})^2}$
    
    $\varphi_0=arctg(\frac{x_0\omega_n}{V_0})$
    
    $x(t)=x_0cons\omega_nt+\frac{v_o}{\omega_n}sen \omega_nt$
    
- Vibración propia natural
    
    $T_n=\frac{2\pi}{\omega_n} \longrightarrow \omega_n=2\pi f_n$ (Hz)
    

## Derivadas de la ecuación del desplazamiento

### Desplazamiento

$x(t)=Asen(\omega_nt+\varphi_0)$

### Velocidad

$v(t)=\dot{x}(t)=A\omega_ncos(\omega_n t+\varphi_0)=A\omega_nsen(\omega_n t+\varphi_0+\frac{\pi}{2})$

### Aceleración

$a(t)=\ddot{x}(t)=-A\omega_n^2sen(\omega_nt+\varphi_0)=A\omega_n^2sen(\omega_n t+\varphi_0+\pi)=-\omega_n^2x$

## Características

- El período de oscilación no depende de la amplitud
- En las posiciones extremas la velocidad es nula
- La velocidad es máxima en el punto medio de la oscilación
- La fuerza restauradora en cualquier punto del movimiento es proporcional a su distancia al punto central

## Energía del movimiento armónico simple

- Energía cinética
    
    $E_c=\frac{1}{2}mv^2=\frac{1}{2}mA^2\omega_n^2cos^2(\omega_n t+\varphi_0)=\frac{1}{2}m\omega_n^2(A^2-x^2)$
    
    $E_c$  - máxima en el centro
    
    $E_c=0$ - en los extremos
    
- Energía potencial de deformación
    
    $E_p=\frac{1}{2}kx^2=\frac{1}{2}kA^2sen^2(\omega_n t+\varphi_0)$
    
- Trabajo realizado por una fuerza para producir una deformación x:
    
    $W=\int\overrightarrow{F}d\overrightarrow{r}=\int_{0}^{x}kxdx=\frac{1}{2}kx^2=\frac{1}{2}kA^2sen^2(\omega_n t+\varphi_0)$
    
- Energía total
    
    $E_T=\frac{1}{2}kx^2+\frac{1}{2}mv^2=\frac{1}{2}kA^2=\frac{1}{2}m\omega_n^2A^2=cte$
    

# Oscilador armónico simple

$ms^2+cs+kx=0$

$S_{1,2}=\frac{-c+\sqrt{c^2-4Km}}{2m}=\frac{-c}{2m}\pm\sqrt{(\frac{c}{2m})^2-\frac{K}{m}}$

$(\frac{c}{2m})^2-\frac{K}{m}\leq0$

- $>0$
    - Reales negativas
- $=0$
    
    Doble
    
- $<0$
    
    Imaginarias conjugadas
    
- Amortiguamiento critico
    
    $(\frac{c}{2m})^2=\frac{K}{m}\rightarrow c=2m\omega_n=2\sqrt{Km}$
    

## Representación compleja del movimiento vibratorio

$\overrightarrow{X}=A[cos(\omega_n t+\varphi_0)+isen(\omega_n t+\varphi_0)]$

$\overrightarrow{X}=Ae^{i(\omega_n t+\varphi_0)}$

- Ratio de amortiguamiento
    
    $\zeta=\frac{c}{c_{cr}}=\frac{c}{2\sqrt{km}}=\frac{c}{2m\omega_n}$
    
- Sistemas sobreamortiguados
    
    $c>c_{cr}\longrightarrow \zeta>1$
    
    Raíces reales y negativas
    
    Movimiento resultante no oscilatorio
    
- Sistemas con amortiguamiento crítico
    
    $c=c_{cr}\longrightarrow\zeta=1$
    
    Movimiento resultante no oscilatorio
    
- Sistemas Subamortiguados
    
    $c<c_{cr}\longrightarrow\zeta<1$
    
    $\omega_d=\omega_n\sqrt{1-\zeta^2}$
    
    Oscilatorio
    
    $\omega_d$ - frecuencia angular de vibración amortiguada
    
- Desplazamiento del sistema
    
    $x(t)=Ae^{-\zeta\omega_n t}sen(\omega_d t+\varphi_0)$
    
    $-\zeta\omega_n t$ - efecto disipativo
    
- Decremento logaritmico
    
    $\delta=ln\frac{x_1}{x_2}=ln\frac{e^{-\zeta\omega_n t_1}}{e^{-\zeta\omega_n(t_1+T_d)}}=\zeta\omega_n T_d=\frac{2\pi\zeta}{\sqrt{1-\zeta^2}}$
    
    Para $\delta=2\pi\zeta$ si $\zeta<<1$
    

## Vibraciones forzadas

$F(t)=F_0sen(\Omega t)$

Ecuación diferencial: $m\ddot{x}+c\dot{x}+Kx=F_0sen(\Omega t)$

Solución: $x(t)=x_h(t)+x_p(t)$

Homogénea: $x_h(t)=Ae^{-\zeta\omega_n t}sen(\omega_d t+\varphi_0)-$ Respuesta transitoria

Particular: $x_p(t)=X_0sen(\Omega t+\phi) -$Respuesta permanente

- Amplitud $X_o$
    
    $X_0=\frac{F_0/m}{\sqrt{(\omega_n^2-\Omega^2)+4\gamma^2\Omega^2}}=\frac{\delta_{st}}{\sqrt{(1-r^2)+(2\zeta r)^2}}$
    
- $r$ ratio de frecuencia
    
    Relación de la fuerza excitadora y la frecuencia natural del sistema libre:  $r=\frac{\Omega}{\omega_n}$
    
- $\delta_{st}$ deformación estática
    
    $\delta_{st}=\frac{F_0}{K}$
    
- Desfase $\phi$
    
    Retraso de la respuesta respecto de la fuerza aplicada
    
    $tan\phi=\frac{-c\Omega}{K-m\Omega^2}=\frac{-2\gamma\Omega}{\omega_n^2\Omega^2}=\frac{-2\zeta r}{1-r^2}$
    
- Factor dinámico de amplificación $H$
    
    Numero de veces que la amplitud de oscilación dinámica sobrepasa la estática
    
    $|H|=|\frac{X_0}{\delta_{st}}|=\frac{1}{\sqrt{(1-(\Omega/\omega_n)^2)^2+(2\zeta\Omega/\omega_n)^2}}=\frac{1}{\sqrt{(1-r^2)+(2\zeta r)^2}}$
    
- Resonancia en amplitud
    
    Para frecuencias de excitación muy próximas a la propia del sistema la amplitud se incrementa bruscamente 
    
    Para frecuencias de excitación cercanas a la propia del sistema, pero no muy próximas obtenemos una pulsación
    
    $|X_0|_{max}=\frac{F_0/m}{2\gamma}\sqrt{\omega_n^2-\gamma^2}=\frac{F_0/K}{2\zeta\sqrt{1-\zeta^2}}$
    
    $|H|_{max}=\frac{1}{2\zeta\sqrt{1-\zeta^2}}$
    
- Frecuencia de resonancia
    
    $\Omega_r=\sqrt{\omega_n^2-2\gamma^2}=\omega_n\sqrt{1-2\zeta^2}$
    
- Resonancia en energía
    
    Velocidad y energía cinética máxima
    
    $v=\dot{x}=X_0cos(\Omega t+\phi)$
    
    $|V_0|_{max}=\frac{F_0/m}{2\gamma}$
    
    Frecuencia de resonancia: $\Omega_{rel}=\omega_n$
    
- Representación del factor de amplificación en función de $r$ y $|H|$
    
    ![](Studies/UPM/Física%20II%20983324900afe4743a8932d79c2f36903/Tema%201%20d5df400329174f4ea5f981a8b14067ba/Untitled.png)