---
created: 2026-08-17
modified: 2026-08-17
area: ""
tipo_nota: ""
status: 🌱
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
estado: "pendiente"
---

# CloudFormation

> [!info] Contexto captura
> **Fecha**: 2026-08-17 13:42
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> CloudFormation es un servicio de AWS para crear y gestionar infraestructura como código


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->

```yaml
  NombreLogicoDelRecurso:  # 1. Nombre inventado por ti (Ej:MiServidorWeb)
    Type: TIPO::DE::RECURSO::AWS # Tipo oficial de AWS (Ej: AWS::EC2::Instance)
    
    Properties:         # Las características del recurso
      Propiedad1: ValorTexto    # Valor directo
      Propiedad2: !Ref OtroRecurso    # Enlace a otro recurso o parámetro
      Propiedad3: true    # Booleano (true/false)
      Tags:         # Etiquetas de nombre y iorganización
        - Key: Name
          Value: Mi-Nombre-Visible
```

#### ### 1. `NombreLogicoDelRecurso` (Tu identificador interno)

- Eliges un nombre en _CamelCase_ sin espacios que identifique el recurso dentro de tu código.
- _Ejemplos:_ `MiVpc`, `SubredPrivada1`, `BaseDatosPostgres`, `SecurityGroupWeb`.


En CloudFormation, los símbolos con `!` son **funciones especiales** de AWS:

### 🔹 `!Ref` (Referencia)
* **¿Qué hace?:** Obtiene el valor de un **Parámetro** o el ID físico de un **Recurso**.
* **Ejemplo en tu código:** `VpcId: !Ref MiVpc`
* **Traducción:** *"No sé qué ID numérico le dará AWS a esta VPC, así que usa `!Ref MiVpc` para que tome el ID automáticamente una vez creada"*.

### 🔹 `!Sub` (Sustitución de Cadenas)
* **¿Qué hace?:** Reemplaza variables `${NombreVariable}` dentro de un texto.
* **Ejemplo en tu código:** `Value: !Sub '${EnvironmentName}-vpc'`
* **Traducción:** Si `EnvironmentName` es `dev`, el texto se convierte en `'dev-vpc'`. Si cambias a `prod`, se convierte en `'prod-vpc'`.

---

### ⚙️ 2. Propiedades Específicas de cada Recurso


### 🌐 `AWS::EC2::VPC`

```yaml
Properties:
  CidrBlock: !Ref VpcCidr       # El rango de IPs (10.0.0.0/16)
  EnableDnsSupport: true        # 💡 Habilita la resolución DNS interna de AWS
  EnableDnsHostnames: true      # 💡 Asigna nombres de dominio públicos (ej: ec2-54-xx.compute.amazonaws.com) a tus instancias
```
> **¿Por qué poner `EnableDnsHostnames: true`?** Si no pones esto en `true`, tus servidores solo tendrán dirección IP pero no podrán tener nombres de dominio DNS legibles.

---

### 🛣️ `AWS::EC2::Subnet`

```yaml
Properties:
  VpcId: !Ref MiVpc               # Vincula la subred a tu VPC
  CidrBlock: 10.0.1.0/24          # El rango reducido de IPs para esta subred (256 IPs)
  MapPublicIpOnLaunch: true       # 💡 HABILITADOR PÚBLICO
```
> **¿Qué hace `MapPublicIpOnLaunch: true`?:** Es la diferencia entre una subred pública y una privada. Cuando creas una instancia EC2 dentro de esta subred, AWS le asigna automáticamente una **IP pública de Internet** además de su IP privada.

---

### 🏷️ `Tags` (Etiquetas de Organización)

```yaml
Tags:
  - Key: Name
    Value: !Sub '${EnvironmentName}-subred-publica'
```
* En AWS, los recursos no tienen nombre por defecto en la consola (aparecen solo como un ID tipo `vpc-0a1b2c3d`).
* La etiqueta con la clave `Key: Name` es especial: **asigna el nombre visible que aparecerá en la consola web de AWS**.

---

### 📤 `Outputs` y `Export` (Compartir datos)

```yaml
Outputs:
  VpcIdOutput:
    Description: ID de la VPC creada
    Value: !Ref MiVpc             # Devuelve el ID de la VPC
    Export:
      Name: !Sub '${EnvironmentName}-VPCID' # 💡 Hace que este ID esté disponible globalmente
```
* **`Export: Name:`** Publica este dato con una clave fija (ej: `dev-VPCID`). De este modo, en el futuro tu plantilla de Base de Datos o de Servidores Web podrá leer este valor usando `Fn::ImportValue: dev-VPCID` sin tener que volver a escribir el código de la VPC.


---

## 🔑 Keywords / Conceptos clave

`keyword1`, `keyword2`, `keyword3`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

_Flashcards pendientes de crear_

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

-
-

---

## ✅ Checklist procesamiento

- [ ] Revisar y expandir contenido
- [ ] Crear flashcards si es necesario
- [ ] Hacer ejercicios relacionados
- [ ] Conectar con otras notas ([[]])
- [ ] Actualizar nivel de comprensión
- [ ] Mover a vault definitivo / Cambiar status a 🌿

---

## 💭 Notas adicionales / Ideas rápidas

<!-- Zona libre para cualquier cosa que quieras capturar rápido -->




---

## 📋 Metadata resumen

| Campo     | Valor                                    |
| --------- | ---------------------------------------- |
| Capturado | 2026-08-17 13:42                         |
| Área/Tema | `= this.area`                            |
| Prioridad | `= this.prioridad`                       |
| Estado    | Captura rápida → Pendiente procesamiento |
| Revisión  | `= this.proxima-revision`                |
|           |                                          |

---

#pendiente-procesar #captura-rapida
