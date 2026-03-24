---
cards-deck: Nube
created: 2025-11-20
modified: 2026-01-22
status: 🌿 Creciendo
tipo_nota: tecnica
asignatura: Infraestructura-Nube
nivel-comprension: 💡
proxima-revision: 2026-01-29
ultima-revision: 2026-01-22
veces-revisado: 1
tiempo-repaso: 30min
tiempo-estimado: 10m
---

# Amazon EC2 (Elastic Compute Cloud)

> [!abstract] Objetivo
> Comprender el funcionamiento de EC2 como servicio principal de cómputo en AWS, sus componentes clave, modelos de pricing y casos de uso prácticos para proyectos de Data Science y desarrollo web.

---

## 🎓 Contexto Académico

**Asignatura/Curso**: Infraestructura-Nube
**Relevancia para**: Examen final y proyectos prácticos de despliegue
**Dificultad percibida**: ⭐⭐⭐☆☆

---

## 📝 Definición

Amazon EC2 (Elastic Compute Cloud) es el servicio de máquinas virtuales de AWS que proporciona capacidad de computación escalable en la nube. Funciona como un ordenador virtual completo donde puedes ejecutar aplicaciones, procesar datos, entrenar modelos de ML o desplegar servicios web, eliminando la necesidad de invertir en hardware físico.

EC2 te permite lanzar instancias (servidores virtuales) con diferentes configuraciones de CPU, memoria, almacenamiento y red según tus necesidades específicas. Estas instancias se pueden arrancar, detener, redimensionar o eliminar en minutos, pagando solo por el tiempo que las uses. Es la base sobre la cual se construyen muchos otros servicios de AWS.

El concepto de "elasticidad" es fundamental: puedes escalar verticalmente (cambiando a instancias más potentes) u horizontalmente (agregando más instancias) según la demanda de tu aplicación. Esto es especialmente útil en Data Science donde puedes necesitar mucha potencia de cómputo solo durante el entrenamiento de modelos, y luego reducir recursos para inferencia.

---

## ⚙️ Conceptos Clave

### 📌 Instancias EC2

**Tipo**: Definición

**Características**:
- Son máquinas virtuales que ejecutan en la infraestructura de AWS
- Se lanzan desde AMIs (Amazon Machine Images) que contienen el sistema operativo base
- Tienen configuraciones específicas de vCPUs, RAM, almacenamiento y red
- Se pueden arrancar, detener, reiniciar o terminar según necesidad
- Mantienen su configuración y datos mientras estén en estado "stopped" (detenidas)

**Relacionado**: [[AMI]] 

### 📌 Tipos de Instancia

**Tipo**: Técnica

**Características**:
- **t3/t4**: Propósito general con CPU burst, ideales para desarrollo y apps ligeras
- **c5/c6**: Optimizadas para cómputo intensivo (procesamiento de datos, HPC)
- **r5/r6**: Optimizadas para memoria, perfectas para bases de datos en RAM
- **p3/p4**: Equipadas con GPUs NVIDIA para ML/AI y deep learning
- **m5**: Balanceadas entre CPU y memoria, versátiles para cargas mixtas

**Relacionado**: [[GPU Computing]]

### 📌 AMI (Amazon Machine Image)

**Tipo**: Definición

**Características**:
- Plantilla que contiene sistema operativo, aplicaciones y configuraciones
- Puedes usar AMIs públicas (Ubuntu, Amazon Linux, Windows) o crear personalizadas
- Incluyen permisos de usuario, volumes de almacenamiento y launch settings
- Permiten replicar ambientes completos en segundos
- Se pueden compartir entre cuentas o hacer públicas

**Relacionado**: [[EC2 Snapshots]] • [[Instance Launch]]

### 📌 Security Groups

**Tipo**: Técnica

**Características**:
- Actúan como firewalls virtuales a nivel de instancia
- Controlan tráfico de entrada (inbound) y salida (outbound)
- Son stateful: si permites entrada, la respuesta se permite automáticamente
- Puedes especificar protocolos, puertos y rangos de IP
- Se pueden modificar en caliente sin reiniciar la instancia

**Relacionado**: [[Network Security]] • [[VPC]]

### 📌 EBS (Elastic Block Store)

**Tipo**: Técnica

**Características**:
- Volúmenes de almacenamiento persistente que se conectan a instancias
- Los datos persisten independientemente del ciclo de vida de la instancia
- Puedes crear snapshots (backups) y restaurarlos cuando necesites
- Permiten redimensionamiento dinámico sin downtime
- Diferentes tipos: gp3 (SSD general), io2 (alto IOPS), st1 (throughput optimizado)

**Relacionado**: [[Storage]] • [[Snapshots]] • [[Backup Strategies]]

### 📌 Modelos de Pricing

**Tipo**: Técnica

**Características**:
- **On-Demand**: Pago por hora/segundo sin compromiso, máxima flexibilidad
- **Reserved Instances**: Compromiso 1-3 años, ahorro hasta 70%
- **Spot Instances**: Hasta 90% descuento usando capacidad no utilizada, interruptible
- **Savings Plans**: Compromiso de gasto por hora, más flexible que Reserved
- Factores de precio: tipo de instancia, región, sistema operativo

**Relacionado**: [[Cloud Cost Optimization]] • [[AWS Pricing]]

---

## 💻 Ejemplo Práctico

```bash
# Lanzar instancia EC2 con AWS CLI
aws ec2 run-instances \
    --image-id ami-0c55b159cbfafe1f0 \
    --instance-type t3.micro \
    --key-name mi-keypair \
    --security-group-ids sg-0123456789abcdef \
    --subnet-id subnet-12345678 \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=DataScience-Dev}]'

# Conectarse por SSH
ssh -i ~/.ssh/mi-keypair.pem ec2-user@ec2-XX-XX-XX-XX.compute-1.amazonaws.com

# Instalar entorno de Data Science en la instancia
sudo yum update -y
sudo yum install python3 python3-pip -y
pip3 install jupyter pandas numpy scikit-learn matplotlib

# Lanzar Jupyter Notebook accesible remotamente
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser
```

**Explicación**: Este ejemplo muestra cómo lanzar una instancia EC2 desde la CLI, conectarse por SSH y configurar un entorno de Jupyter para trabajo de Data Science. La instancia t3.micro está en la capa gratuita si es tu primer año en AWS. Es importante abrir el puerto 8888 en el Security Group para acceder a Jupyter desde tu navegador.

---

## 💭 Reflexiones & Conexiones

EC2 es el corazón de la infraestructura cloud y entenderlo bien es fundamental para cualquier proyecto de Data Science en producción. Me doy cuenta de que la flexibilidad de poder lanzar instancias potentes solo cuando las necesito puede cambiar completamente mi workflow: podría entrenar modelos pesados en p3 con GPU durante la noche usando Spot Instances (ahorrando 90%) y luego usar una t3.small para servir el modelo entrenado.

La conexión con Docker es interesante: puedo crear una imagen Docker con todo mi stack de Data Science (pandas, scikit-learn, TensorFlow) y ejecutarla en cualquier instancia EC2, garantizando reproducibilidad. Esto se conecta perfectamente con mi proyecto del sistema de recomendación de coworkings: podría tener una instancia ejecutando el backend de la API y otra procesando las actualizaciones del modelo en batch.

Veo una analogía con el existencialismo de Camus: EC2 te da libertad total pero también responsabilidad total. Tú decides qué instalar, cómo configurar, cuándo escalar. No hay un "camino predefinido" como en PaaS. Es como el concepto del "hombre absurdo" que debe crear su propio significado: tú construyes tu infraestructura desde cero, con todas las posibilidades y todos los riesgos.

Para mi app de RPG con React, la arquitectura ideal sería: una t3.small para el frontend con Nginx, otra t3.small para el backend Node.js, y usar Lambda + una instancia Spot ocasional para la generación de cartas con IA. Total control, pago solo lo que uso.

---

## 🎴 Flashcards

> 💡 **Formato**: Usa `Pregunta::Respuesta` para flashcards inline

¿Qué es Amazon EC2?::Servicio de máquinas virtuales de AWS que proporciona capacidad de computación escalable en la nube #aws #card
<!--SR:!2026-01-26,4,270-->

¿Qué es una AMI en EC2?::Amazon Machine Image, plantilla que contiene SO, aplicaciones y configuraciones para lanzar instancias #ami #card
<!--SR:!2026-01-26,4,270-->

¿Cuál es la diferencia entre Security Groups y NACLs?::Security Groups son stateful y operan a nivel de instancia, NACLs son stateless y operan a nivel de subnet #networking #seguridad #card
<!--SR:!2026-01-23,1,230-->

Tipos de instancia EC2
?
t3/t4 (propósito general), c5/c6 (computación), r5/r6 (memoria), p3/p4 (GPU), m5 (balanceado) #instancias #card
<!--SR:!2026-01-26,4,270--> 

Amazon EC2 ofrece ==On-Demand== para pago por uso sin compromiso, ==Reserved Instances== con ahorro hasta 70% con compromiso 1-3 años, y ==Spot Instances== con hasta 90% descuento usando capacidad no utilizada #pricing #card
<!--SR:!2026-01-25,3,250!2026-01-26,4,270!2026-01-26,4,270--> 

EBS:::Elastic Block Store, almacenamiento en bloque persistente que se conecta a instancias EC2 y permite snapshots #storage #ebs #card
<!--SR:!2026-01-25,3,250!2026-01-25,3,250-->

¿Qué instancias usarías para entrenar modelos de deep learning?::Instancias p3 o p4 que tienen GPUs NVIDIA optimizadas para ML/AI #ml #gpu #card
<!--SR:!2026-01-26,4,270-->

¿Los datos en una instancia EC2 persisten cuando la detienes (stop)?::Los datos en EBS sí persisten, pero los datos en instance store (almacenamiento efímero) se pierden #storage #persistencia #card
<!--SR:!2026-01-26,4,270-->

Security Group:::Firewall virtual a nivel de instancia que controla tráfico inbound/outbound de forma stateful #security #networking #card
<!--SR:!2026-01-26,4,270!2026-01-23,1,230-->

¿Cuándo usarías Spot Instances?::Para cargas de trabajo interrumpibles como procesamiento batch, entrenamiento de modelos, análisis de datos donde puedes tolerar interrupciones #spot #pricing #card
<!--SR:!2026-01-26,4,270-->

---

**📊 Total de flashcards**: 10

> 🎯 **Para revisar**: Cmd/Ctrl+P → "Flashcards: Review flashcards"

---

## 📚 Referencias & Enlaces

**Enlaces internos**: [[AWS VPC]] • [[Cloud Computing Fundamentals]] • [[Load Balancing]] • [[Auto Scaling]] • [[IAM Roles]]

**Referencias externas**: 
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)
- [EC2 Pricing Calculator](https://calculator.aws/)

**Fuente**: Clase de Infraestructura y Servicios en la Nube - UAX, AWS Documentation, experiencia práctica

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2025-11-20
- **Próxima revisión**: 2025-11-23
- **Veces revisado**: 0
- **Nivel de comprensión**: 💡 Entiendo bien
- **Tiempo estimado de repaso**: 30min

---

> [!tip] 💡 Próximos pasos
> - Practicar lanzando una instancia real con la capa gratuita
> - Configurar un entorno de Jupyter en EC2 para procesamiento de datos
> - Experimentar con Spot Instances para entrenar un modelo pequeño
> - Crear una AMI personalizada con tu stack de Data Science
> - Cuando revises esta nota, actualiza el contador de revisiones y ajusta la próxima fecha según tu comprensión


---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Tarea para aclarar una duda de concepto. Usa #mejora-concepto
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia
