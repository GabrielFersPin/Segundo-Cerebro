---
created: 2026-09-07
modified: 2026-09-07
area: ""
tipo_nota: captura_rapida
status: 🌱
nivel-comprension: ""
proxima-revision: 2026-09-09
ultima-revision: 2026-09-07
veces-revisado: 0
tiempo-repaso: 5min
---

# Boto3

> [!info] Contexto captura
> **Fecha**: 2026-09-07 12:53
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> Boto3 es el SDK oficial de AWS para Python: permite llamar a las APIs de los servicios de AWS desde código, por ejemplo para crear un bucket de S3 o iniciar un trabajo de SageMaker.


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->

Boto3 no crea servicios por sí mismo ni sustituye a `pip`; proporciona clientes y recursos que envuelven las APIs de AWS. Las credenciales deben obtenerse preferentemente mediante la cadena de credenciales de AWS (perfil, variables de entorno o rol IAM), no escribirse directamente en el código.

Para instalar el SDK en un entorno Python:

```bash
pip install boto3
```

El siguiente ejemplo separa un cliente S3 local de LocalStack de los clientes que llamarían a AWS real:

```python

import boto3

region = 'us-east-1'

# 1. Cliente S3 contra LocalStack. Solo es un entorno local de pruebas.
s3 = boto3.client(
    's3',
    region_name=region,
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test'
)

# Crear bucket de pruebas antes de subir archivos
bucket_name = 'test-bucket'
s3.create_bucket(Bucket=bucket_name)
print(f'Bucket "{bucket_name}" creado exitosamente.')

# Listar buckets
response = s3.list_buckets()
print("Buckets disponibles:")
for bucket in response['Buckets']:
    print(f" - {bucket['Name']}")

# 2. Cliente de SageMaker. Usa las credenciales configuradas para AWS.
sagemaker = boto3.client('sagemaker', region_name=region)

# A. Crear Training Job
training_job_name = 'test-training-job'
sagemaker.create_training_job(
    TrainingJobName=training_job_name,
    HyperParameters={'epochs': '10', 'learning_rate': '0.01'},
    AlgorithmSpecification={
        'TrainingImage': '763104351884.dkr.ecr.us-east-1.amazonaws.com/sagemaker-scikit-learn:0.23-1-cpu-py3',
        'TrainingInputMode': 'File'
    },
    RoleArn='arn:aws:iam::123456789012:role/SageMakerRole',
    InputDataConfig=[{
        'ChannelName': 'training',
        'DataSource': {
            'S3DataSource': {
                'S3DataDistributionType': 'FullyReplicated',
                'S3DataType': 'S3Prefix',
                'S3Uri': f's3://{bucket_name}/test'
            }
        }
    }],
    OutputDataConfig={'S3OutputPath': f's3://{bucket_name}/output'},
    ResourceConfig={
        'InstanceCount': 1,
        'InstanceType': 'ml.m4.xlarge',
        'VolumeSizeInGB': 30
    },
    StoppingCondition={'MaxRuntimeInSeconds': 3600}
)
print(f'Training job "{training_job_name}" creado.')

# ---------------------------------------------------------
# DESPLIEGUE DEL MODELO
# ---------------------------------------------------------

# Paso 1: Registrar el Modelo en SageMaker
model_name = 'test-sagemaker-model'
sagemaker.create_model(
    ModelName=model_name,
    PrimaryContainer={
        'Image': '763104351884.dkr.ecr.us-east-1.amazonaws.com/sagemaker-scikit-learn:0.23-1-cpu-py3',
        'ModelDataUrl': f's3://{bucket_name}/output/{training_job_name}/output/model.tar.gz'
    },
    ExecutionRoleArn='arn:aws:iam::123456789012:role/SageMakerRole'
)
print(f'Modelo "{model_name}" registrado.')

# Paso 2: Crear la Configuración del Endpoint
endpoint_config_name = 'test-endpoint-config'
sagemaker.create_endpoint_config(
    EndpointConfigName=endpoint_config_name,
    ProductionVariants=[
        {
            'VariantName': 'AllTraffic',
            'ModelName': model_name,
            'InitialInstanceCount': 1,
            'InstanceType': 'ml.t2.medium',
            'InitialVariantWeight': 1.0
        }
    ]
)
print(f'Endpoint Config "{endpoint_config_name}" creada.')

# Paso 3: Desplegar el Endpoint de SageMaker
endpoint_name = 'test-endpoint'
sagemaker.create_endpoint(
    EndpointName=endpoint_name,
    EndpointConfigName=endpoint_config_name
)
print(f'Endpoint "{endpoint_name}" desplegado correctamente.')

# Ingesta de Kinesis
kinesis_client = boto3.client('kinesis', region_name=region)
kinesis_client.put_record(
    StreamName='my_stream',
    Data=b'evento de prueba',
    PartitionKey='key'
)

# Transformacion de datos con Glue
glue_client = boto3.client('glue', region_name=region)
glue_client.start_job_run(JobName='my_etl_job')

# Analisis con Athena
athena_client = boto3.client('athena', region_name=region)
athena_client.start_query_execution(QueryString='SELECT * FROM my_table')


# Manda un mensaje con SNS
sns = boto3.client('sns')
response = sns.publish(
    TopicArn='arn:aws:sns:us-east-1:123456789012:MyTopic',
    Message='Hello, AWS SNS!',
)

print(response)


``` 

El ejemplo requiere que LocalStack esté ejecutándose para S3 y que, en AWS, existan el rol IAM, la imagen de entrenamiento, los datos de entrada, el stream de Kinesis, el job de Glue y la tabla consultada.


---

## 🔑 Keywords / Conceptos clave

`Boto3`, `SDK`, `Python`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

¿Qué es Boto3?::Es el SDK oficial de AWS para Python; permite llamar a las APIs de los servicios de AWS desde código. #aws #boto3 #python

¿Es Boto3 un gestor de paquetes?::No. Boto3 es una librería/SDK; se instala como paquete Python, normalmente con `pip install boto3`, pero su función es acceder a APIs de AWS. #aws #boto3 #python

¿Qué es un cliente de Boto3?::Es un objeto que permite llamar directamente a las operaciones de un servicio de AWS, como `s3.list_buckets()` o `glue.start_job_run()`. #aws #boto3

¿Cómo debería gestionar las credenciales una aplicación que usa Boto3?::Debe usar la cadena de credenciales de AWS, como un perfil, variables de entorno o un rol IAM, evitando claves escritas en el código. #aws #boto3 #security

¿Para qué sirve `endpoint_url` en Boto3?::Para dirigir las llamadas a un endpoint alternativo, por ejemplo LocalStack durante pruebas locales, en lugar del endpoint real de AWS. #aws #boto3 #localstack

¿Qué tipo de dato necesita `Kinesis.put_record` en el parámetro `Data`?::Bytes o un valor que pueda convertirse al formato esperado; por ejemplo, `b'evento de prueba'`. #aws #boto3 #kinesis

¿Qué prerrequisitos necesita el ejemplo de SageMaker?::Un rol IAM válido, una imagen de entrenamiento accesible, datos de entrada en S3 y permisos para SageMaker y S3. #aws #sagemaker #boto3

¿Qué diferencia hay entre Boto3 y AWS CLI?::Ambos pueden llamar a APIs de AWS, pero Boto3 se integra en programas Python y AWS CLI se utiliza principalmente desde la terminal o scripts de shell. #aws #boto3

> 💡 **Formato recomendado**:
> - Inline: `¿Pregunta?::Respuesta #tags`
> - Reversa: `Término:::Definición #tags`
> - Cloze: `Texto con ==palabra== oculta`
---

## ❓ Preguntas / Dudas pendientes

- [ ]
- [ ]

---

## 🧩 Conexiones potenciales

<!-- ¿Con qué otros temas se relaciona? Escribe rápido, ya harás los links después -->

- [[Python]], [[SDK's]]
-

---

## ✅ Checklist procesamiento

- [x] Revisar y expandir contenido
- [x] Crear flashcards si es necesario
- [ ] Hacer ejercicios relacionados
- [x] Conectar con otras notas ([[]])
- [ ] Actualizar nivel de comprensión
- [ ] Mover a vault definitivo / Cambiar status a 🌿

---

## 💭 Notas adicionales / Ideas rápidas

<!-- Zona libre para cualquier cosa que quieras capturar rápido -->

Es un paquete que se descarga directamente con código para crear los servicios de AWS


---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-09-07 12:53 |
| Área/Tema | `= this.area` |
| Estado | `= this.status` |
| Prioridad | `= this.prioridad` |
| Revisión | `= this.proxima-revision` |
| Nivel de comprensión | `= this.nivel-comprension` |

---

#pendiente-procesar #captura-rapida
