# Electromagnetismo

[Electro - Timetable](Electro%20-%20Timetable%205c8a6de8265142aeaf73c7b5ea3066a1.md)

[FLP Vol. II Table of Contents](https://www.feynmanlectures.caltech.edu/II_toc.html)

[Tema 1](Ingeniería/Electromagnetismo/Tema%201.md)

[Tema 2](Ingeniería/Electromagnetismo/Tema%202.md)

# Tema 3

[Cuestiones importantes tema 3](Cuestiones%20importantes%20tema%203%20e80488221f9d49faa306d6e000c648d9.md)

- Campo magnético
    
    Las corrientes eléctricas son una fuente de campo magnético
    
    La divergencia del campo magnético es nula
    
    Las líneas de campo magnético, o son cerradas, o nacen y mueren en el infinito, o se retuercen recubriendo densamente una superficie.
    
    - Propiedades de las fuerzas magnéticas
        1. Las fuerzas sobre una carga en reposo es nula 
        2. Si la velocidad de la partícula es paralela al campo magnético la fuerza ejercida es nula.
        3. La fuerza magnética no tiene componente tangencial, por lo que la aceleración provocada sobre la carga es exclusivamente normal.
        4. El trabajo realizado por el campo magnético sobre la carga en movimiento es nulo. 
    - Definición de campo magnético
        
        $B=\frac{mv}{qR}$ ($1T kgA^{-1}s^{-1})$
        
        $\omega=\frac{qB}{m}$
        
        $T=\frac{2\pi m}{qB}$
        
    - Ecuaciones del campo magnético estacionario
        - Ley de Gauss para $\overrightarrow{E}$
            
            $\nabla{\overrightarrow{E}}=\frac{\rho}{\varepsilon_0}$
            
        - Ley de Faraday
            
            $\nabla \times\overrightarrow{E}=-\frac{\partial{B}}{\partial t}$
            
        - Lay de Ampère-Maxwell
            
            $\nabla\times\overrightarrow{B}=\mu_0\overrightarrow{j}+\varepsilon_0 \mu_0\frac{\partial\overrightarrow{E}}{\partial{t}}$
            
        - Ley de Gauss para $\overrightarrow{B}$
            
            $\nabla\overrightarrow{B}=0$
            
        - Electrostática
            
            $\nabla\overrightarrow{E}=\frac{\rho}{\varepsilon_0}=0$
            
        - Magnetostática
            
            $\nabla\overrightarrow{B}=\mu_0\overrightarrow{j}=0$
            
    - La ley de Ampère
        
        La circulación del campo magnético $\overrightarrow{B}$  a lo largo de una curva cerrada $\Gamma$ solo depende de la intensidad neta que atraviesa la superficie abierta S delimitada por dicha curva ($\Gamma$).
        
        Solo puede ser aplicada cuando hay una cierta simetría.
        
        $B \int_\Gamma Bdlcos\alpha=Bcos\alpha\int_{\Gamma}dl=\mu_0I$
        
        $B=\frac{\mu_0 I}{cos\alpha L}$
        
        La superficie de integración es la superficie efectiva, la cual corresponde a la intersección entre la superficie elegida S(delimitada por $\Gamma$) y el volumen ocupado por la corriente ($V_j$).
        
        La divergencia de un campo vectorial se puede entender como flujo por unidad de volumen.
        
        - Planteamiento del problema
            1. Estudiar la simetría del problema. Si no existe simetría no utilizar la Ley de Ampère.
            2. Si hay simetrías, elegir una curva sencilla.
            3. Escoger una superficie fácil y suave. La superficie más cómoda es la superficie plana y es siempre abierta.
            4. Determinar el sentido de $d\overrightarrow{l}$( antihorario u horrario) y en función de dicha orientación, asignar la orientación correcta de $S$ (vector $n$ hacia fuera o hacia dentro, respectivamente regla del sacacorchos).
        - Resolución matemática
            1. Tomar un sistema de referencia coherente con las simetrías del sistema. Esto es fácil de saber, ya que la curva elegida para realizar la integral de línea posee esta misma simetría.
            2. Tener cuidado con la integral del segundo miembro. La integral doble se extiende, en principio, a la superficie $S$ elegida, sin embargo, la superficie real sobre la que se integra corresponde a la intersección entre $S$ y el volumen correspondiente a la densidad de corriente $V_j$.
    - Los potenciales magnéticos
        - El potencial vector
            
            $\nabla\overrightarrow{B}=0$   $\nabla(\nabla\times\overrightarrow{\omega})=0$
            
            Potencial vector $\overrightarrow{A}$ al campo vectorial que verifica la siguiente relación
            
            $\overrightarrow{B}=\nabla\times\overrightarrow{A}$
            
            Si sumamos a $\overrightarrow{A}$ cualquier gradiente, el nuevo potencial $\overrightarrow{A´}$ obtenido reproduce el mismo campo magnético $\overrightarrow{B}$.
            
            $\overrightarrow{A´}=\overrightarrow{A}+\nabla\varphi$
            
            $\overrightarrow{B}=\nabla\times\overrightarrow{A´}=\nabla\times\overrightarrow{A}+0=\overrightarrow{B}$ $\longrightarrow$ Transformación de Gauge
            
    - La ley de Biot y Savart
        
        $\overrightarrow{B}(\overrightarrow{r})=\frac{\mu_0}{4\pi}\int_{V´}\frac{\overrightarrow{j_v}(\overrightarrow{r})\times(\overrightarrow{r}-\overrightarrow{r´})}{|\overrightarrow{r}-\overrightarrow{r´}|^3}dV´$
        
    - Fuerza sobre una corriente
        - Fuerza sobre una corriente volumétrica
            
            La fuerza sobre un volumen $\Delta{V}$ que contiene $\Delta{N}$ cargas disponibles que se mueven con velocidad $\overrightarrow{v}$ en presencia de un campo magnético $\overrightarrow{B}$.
            
            $\Delta\overrightarrow{F}=q\Delta N(\overrightarrow{v}\times\overrightarrow{B})$
            
            $\overrightarrow{F}=\int_V(\overrightarrow{j}\times\overrightarrow{B})dV$
            
        - Fuerza sobre un elemento filiforme
            
            ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled.png)
            
            $\overrightarrow{F}=\int Id\overrightarrow{l}\times\overrightarrow{B}$
            
        - Fuerza dos circuitos filiformes
            
            Fuerza sobre el circuito $C_2$ en presencia de un campo magnético $\overrightarrow{B_{21}}$ ocasionado por la carriente $I_1$ del circuito $C_1$ es:
            
            $\overrightarrow{F_{21}}=\int_{C_2}I_2d\overrightarrow{l_2}\times\overrightarrow{B_{21}}$
            
            Campo creado por la corriente $I_1$ em un elemento del circuito $C_2$:
            
            $\overrightarrow{B_{21}}=\frac{\mu_0}{4\pi}\int_{C_2} I_1d\overrightarrow{l_1}\times\overrightarrow{B_{21}}$
            
            Fuerza sobre $C_2$:
            
            $\overrightarrow{F_{21}}=\frac{\mu_0}{4\pi}I_2I_2\int_{C_2}\int_{C_1}d\frac{\overrightarrow{l_2}\times[d\overrightarrow{l_1}\times(\overrightarrow{r_2}-\overrightarrow{r_1})]}{|\overrightarrow{r_2}-\overrightarrow{r_1}|^3}$
            
        - Equivalencia entre elementos de una corriente
            - Volumen
                
                $\overrightarrow{j}=\rho\overrightarrow{v}=nq\overrightarrow{v}$
                
            - Hilo
                
                $\overrightarrow{j}dV=\overrightarrow{j}(\overrightarrow{S}\ldotp d\overrightarrow{l})=(\overrightarrow{j}\ldotp\overrightarrow{s})d\overrightarrow{l}=Id\overrightarrow{l}$
                
    - Magnetismo en la materia
        - Descripción microscópica del magnetismo de la materia
            - Cada átomo se asemeja a una pequeña espira de radio, por la que circula una cantidad de corriente. Esta corriente se produce como consecuencia de que $q$ se desplaza alrededor del núcleo cada cierto intervalo de tiempo.
            - La cantidad de intensidad que circula: $I=\frac{qv}{2\pi \rho}$
        - Momento Magnético
            - Momento magnético orbital
            
            $$
            ⁍
            $$
            
            $$
            ⁍
            $$
            
            $\overrightarrow{L}$ - momento angular
            
        - Dipolo magnético
            - Potencial vector en P (campo lejano):
            
            ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%201.png)
            
            - Campo magnético en P (campo lejano):
            
            ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%202.png)
            
            - Aunque se ha tomado una pequeña espira circular como dipolo magnético, se obtiene las mismas expresiones para $\overrightarrow{A}$ y $\overrightarrow{B}$ en la zona lejana cuando la espira tiene otras formas pero tiene igual momento magnético m.
            - Todos los circuitos que tienen el mismo momento dipolar producen el mismo campo $\overrightarrow{B}$ en un punto lejano, independiente de la forma de dicho circuito.
            - Dipolo en un campo externo $B$
                - $\overrightarrow{N}=\overrightarrow{m}\times\overrightarrow{B}$
                - $E_p=-\overrightarrow{m}\cdot \overrightarrow{B}$
                - $\overrightarrow{F}=\nabla(\overrightarrow{m}.\overrightarrow{B})$
            - Vector magnetización M
                - Momento dipolar por unidad de volumen
                
                ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%203.png)
                
                - La materia es un conjunto de dipolos magnéticos descritos por $M$
    - Corrientes de magnetización
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%204.png)
        
        - Densidad de corriente volumétrica
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%205.png)
        
        - Densidad de corriente superficial
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%206.png)
        
        - Meteria $\rightarrow$ Dipolo $\rightarrow$Densidades ( $\overrightarrow{j_m}$ y $\overrightarrow{j_{ms}}$)
    - El campo magnético $H$
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%207.png)
        
        - Siendo $\overrightarrow{j_c}$ la densidades de corriente de cara libre y $\overrightarrow{j_m}$ la densidades de cagas ligadas.
        - Se denomina campo magnético $\overrightarrow{H}$ a la magnitud:
            
            ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%208.png)
            
        - En condiciones estacionarias, el campo $\overrightarrow{H}$ y las corrientes de conducción $\overrightarrow{j_c}$ están relacionadas por la Ley de Ampère.
    - Ley de Ampère para el campo $\overrightarrow{H}$
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%209.png)
        
    - Ley de Ampére-Maxwell modificada
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2010.png)
        
        $\overrightarrow{j_c}$ y $\frac{\partial\overrightarrow{D}}{\partial{t}}$ - Fuentes de $\overrightarrow{H}$
        
        $\overrightarrow{D}$ - vector desplazamiento
        
    - Tipos básicos de magnetismo. Susceptibilidad y permeabilidad magnéticas
        - Ecuaciones materiales
            
            ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2011.png)
            
            ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2012.png)
            
            $\chi_m-$susceptibilidad magnética
            
            ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2013.png)
            
            - Permeabilidad magnética:
            
            ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2014.png)
            
            - Permeabilidad magnética relativa
            
            ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2015.png)
            
        - Clases de sustancias
            - Sustancias diamagnéticas
                
                $\sum\overrightarrow{m_i}=\overrightarrow{0}$
                
                $\chi_m<0$
                
                $\mu_r<1$
                
                Es una característica general de cualquier materia.
                
            - Sustancias paramgnéticas
                
                $\sum\overrightarrow{m_i}=\chi_m$
                
                $\chi_m>0$
                
                $\mu_r>1$
                
                - El paramagnetismo y el diamagnetismo son fenómenos lineales
            - Sustancias ferromagnéticas
                
                $\chi_m=\chi_m(H)$
                
                $\overrightarrow{B}=\mu(H)\overrightarrow{H}$
                
                - El ferromagnetismo es un fenómeno no lineal
    - Ferromagnetismo
        - La iteración electromagnética de los dipolos es más fuerte que en los dos anteriores
        - Dispositivo para caracterizar un material ferromagnético
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2016.png)
        
        $H=\frac{NI}{l}$          $l=2\pi R_m$
        
        $\overrightarrow{B}=\mu_0(\overrightarrow{H}+\overrightarrow{M})$
        
        $M=\frac{B}{\mu_0}-H$
        
        - Ciclo de Histéresis $B(H)$:
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2017.png)
        
        - $OP_1$: Curva de primera imanación
        - $B_r$: Campo remanente
        - $H_c$: Campo coercitivo
        - Si el campo $H$ es lo suficientemente alto en $P_1$ se alcanza la saturación
        - Dominios magnéticos
            
            La observación microscópica demuestra que un material ferromagnético (como Fe, Co, Ni y aleaciones) está formado por pequeñas regiones, llamadas dominios.
            
            - Dominios magnéticos - contienen de $10^{15}$ a $10^{16}$ átomos, estan totalmente magnetizados, en el sentido de que dentro de un dominio, los dipolos magnéticos astán alineados. La dirección de alineación varía de un dominio a otro
            
            ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2018.png)
            
        - Circuitos magnéticos
            
            Cuando el flujo asociado al sistema de corrientes sigue el camino definido, el circuito asociado se considera un circuito magnético. 
            
            - Asociar el valor de los campos $\overrightarrow{H}, \overrightarrow{M}$ y $\overrightarrow{B}$
            1. Aplicar la Ley de Ampère eligiendo la curva que represente la trayectoria media sobre el sistema. no hay flujo disperso.
            2. Alplicar la igualdad de flujos magnéticos donde sea conveniente. La unidad de medida del flujo del campo $B$ es el Weber (Wb).
    - Resumen para los problemas
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2019.png)
        
- Inducción electromagnética
    - Fuerza electromotriz inducida
        - Campo eléctrico efectivo:
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2020.png)
        
        - Fuerza electromotriz (f.e.m.): Fuerza total por unidad de carga a lo largo de una línea cerrada, no necesariamente formada por conductores.
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2021.png)
        
        - Campo eléctrico efectivo, antes definido, se descompone como suma de términos:
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2022.png)
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2023.png)
        
        $\overrightarrow{E_{ns}}\longrightarrow$Campos no estacionarios/movimientos en presencia de B
        
        - Solo los campos no electrostáticos contribuyen para la aparición de la f.e.m.
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2024.png)
        
        $-\oint_\Gamma \nabla \overrightarrow{V}d\overrightarrow{l}=\oint_\Gamma dV=0$
        
    - Inducción electromagnética debida al movimiento (Ley de Neumann
        - Expresa la f.e.m. debida al movimiento por medio de la regla del flujo.
        
        ![Untitled](Studies/UPM/Electromagnetismo%20223979c3ef284749b9b8b5b30e243e26/Untitled%2025.png)
        
        - Hay diferencia en el signo dependiendo del sentido de la intensidad
        - Se puede ver como una energía a lo largo de una curva cerrada
    - Ley de Lenz
        
        
    - Ley de inducción de Faraday
    - Caso general
    - Coeficiente de autoinducción L