---
tags: [AWS, seguridad, compliance, gobernanza, IAM]
deck: Obsidian::AWS
created: 2026-05-14 10:00
modified: 2026-05-14 10:00
status: 🟡
tipo_nota: clase
profesor: No especificado
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
cards-deck: ""
---

# 📝 AWS - Servicios de Seguridad, Compliance y Gobernanza

> [!info] Metadata de la clase
> **Fecha**: 2026-05-14
> **Hora**: 10:00
> **Profesor**: No especificado
> **Estado**: 🟡 Por procesar

---

## 🎯 Objetivo de la clase

Entender los principales servicios AWS para seguridad, compliance y gobernanza, cuándo usarlos y cómo implementarlos en infraestructuras en la nube.

---

## 📊 Captura Rápida

### ⚡ Notas Rápidas

- AWS ofrece múltiples capas de seguridad desde infraestructura hasta aplicación.
- Compliance (HIPAA, SOC 2, PCI DSS) es responsabilidad compartida.
- Gobernanza define políticas, permisos y auditoría de recursos.
- Seguridad requiere configuración correcta: no es automática por defecto.

### 🔑 Conceptos Clave

- **IAM**: control de identidades y acceso.
- **Shared Responsibility Model**: AWS asegura infraestructura, tú aseguras aplicación.
- **Compliance**: cumplimiento de regulaciones y estándares.
- **Auditoría**: registrar y monitorear todas las acciones en AWS.
- **Gobernanza**: políticas, control de costos, cumplimiento de normas.

### ❓ Dudas

- ¿Cuál es la diferencia entre IAM y SSO?
- ¿Cómo asegurar datos en tránsito vs en reposo?
- ¿Qué certifications de compliance necesito?

### 💡 Insights

- La seguridad es un proceso continuo, no un estado.
- Automatizar cumplimiento reduce errores humanos.
- El principio de menor privilegio es fundamental.

### ⚠️ Importante

- Una sola credencial mal configurada puede comprometer toda la infraestructura.
- Auditar regularmente permisos y accesos.
- Compliance requiere documentación y evidencia.

---

## 📝 Notas Detalladas

### Capas de Seguridad AWS

```
┌─────────────────────────────────────┐
│  Aplicación & Datos                 │ ← Tu responsabilidad
├─────────────────────────────────────┤
│  OS, Network, IAM, Encryption       │ ← Tu responsabilidad
├─────────────────────────────────────┤
│  Servicios AWS, Hardware            │ ← Responsabilidad AWS
└─────────────────────────────────────┘
```

---

## 🔐 Servicios principales de SEGURIDAD

### 1. **IAM (Identity and Access Management)**

Define quién puede hacer qué en AWS.

**Componentes**:

- **Users**: identidades de personas.
- **Roles**: conjuntos de permisos para servicios/usuarios.
- **Policies**: documentos JSON que definen permisos.
- **Groups**: agrupación de usuarios con permisos similares.

**Mejores prácticas**:

- ✅ Nunca usar credenciales root.
- ✅ Usar Multi-Factor Authentication (MFA).
- ✅ Implementar principio de menor privilegio.
- ✅ Rotar credenciales regularmente.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:DescribeInstances",
      "Resource": "*"
    }
  ]
}
```

---

### 2. **KMS (Key Management Service)**

Gestión centralizada de claves de cifrado.

**Uso**:

- Encriptar datos en reposo (S3, EBS, RDS).
- Encriptar datos en tránsito.
- Control granular de acceso a claves.

**Ventajas**:

- AWS gestiona la infraestructura de seguridad de claves.
- Auditoría de uso de claves.
- Rotación automática de claves.

---

### 3. **Secrets Manager**

Almacenamiento seguro de secretos (contraseñas, API keys, certificados).

**Casos de uso**:

- Credenciales de base de datos.
- API keys de terceros.
- Certificados SSL/TLS.

**Ventajas**:

- Rotación automática.
- Integración con aplicaciones.
- Auditoría completa.

---

### 4. **VPC (Virtual Private Cloud)**

Red privada aislada en AWS.

**Componentes**:

- **Subnets**: subdivisiones de la VPC (público/privado).
- **Security Groups**: firewalls a nivel de instancia.
- **Network ACLs**: control de acceso a nivel de subred.
- **VPN/Direct Connect**: conexiones seguras on-premise.

---

### 5. **WAF (Web Application Firewall)**

Protege aplicaciones web contra ataques comunes.

**Protecciones**:

- SQL Injection, XSS, DDoS.
- Rate limiting.
- Geoblocking.

---

### 6. **Shield**

Protección DDoS administrada por AWS.

- **Shield Standard**: protección automática.
- **Shield Advanced**: protección mejorada y soporte 24/7.

---

## ✅ Servicios de COMPLIANCE

### 1. **Config**

Auditora de configuraciones y cambios en recursos.

**Funcionalidad**:

- Registra configuración de recursos.
- Alerta sobre cambios no autorizados.
- Evalúa cumplimiento de reglas personalizadas.

---

### 2. **CloudTrail**

Registro de auditoría de todas las acciones en AWS.

**Información registrada**:

- Quién hizo qué.
- Cuándo se realizó.
- Resultado de la acción.

**Ventajas**:

- Compliance: evidencia para auditorías.
- Investigación de incidentes.
- Seguimiento de cambios.

---

### 3. **CloudWatch**

Monitoreo y logging centralizado.

**Monitorea**:

- Métricas de recursos (CPU, memoria, etc).
- Logs de aplicaciones.
- Eventos del sistema.

### **4.Glue DataBrew**

-  Can analyse many types of datasets, including data that's stored in Amazon S3 and in relational data bases and data warehouses. 
- Tracks data bases and data warehouses.
- Visual interface to determine its origin called the data lineage.
---

### 4. **Artifact**

Acceso a informes de compliance y certificaciones de AWS.

**Disponible**:

- SOC 1(Service Organization Control)
	- Verify if a third party is following some specific best practices.
- SOC 2:
	- Reports and controls related to security, availability, processing, integrity, confidentiality, and privacy
- SOC
- ISO 27001
- PCI DSS
- HIPAA BAA

---

## 🎛️ Servicios de GOBERNANZA

### 1. **Organizations**

Gestiona múltiples cuentas AWS centralizadamente.

**Características**:

- Consolidación de facturación.
- Políticas centralizadas (SCPs).
- Creación de cuentas automatizada.

---

### 2. **Cost Explorer**

Análisis de gastos en AWS.

**Funcionalidad**:

- Desglose por servicio, región, equipo.
- Presupuestos y alertas.
- Recomendaciones de optimización.

---

### 3. **Budget**

Fija límites de gasto y recibe alertas.

**Tipos de presupuestos**:

- Costo
- Uso
- RI (Reserved Instances)
- Savings Plans

---

### 4. **Trusted Advisor**

Recomendaciones para optimizar infraestructura.

**Áreas de revisión**:

- Seguridad (5 chequeos en versión gratuita)
- Costo
- Desempeño
- Resiliencia
- Límites de servicio

---

### 5. **Service Control Policies (SCPs)**

Límites de permisos a nivel de cuenta/OU en Organizations.

**Ejemplo**: impedir que se lance una instancia EC2 fuera de cierta región.

---

## 🔗 Matriz de Responsabilidad Compartida

| Aspecto | AWS | Cliente |
|--------|-----|--------|
| Infraestructura física | ✅ | |
| Cifrado de datos en tránsito | ✅ | ✅ |
| Cifrado de datos en reposo | | ✅ |
| Identidad y acceso (IAM) | | ✅ |
| Auditoría de acceso | ✅ | ✅ |
| Parches del SO | | ✅ |
| Configuración de firewall | | ✅ |

---

## 🛡️ Mejores prácticas integradas

1. **Seguridad**:
   - Habilitar MFA en todas las cuentas.
   - Usar KMS para cifrado.
   - Implementar least privilege en IAM.

2. **Compliance**:
   - Habilitar CloudTrail en todas las cuentas.
   - Usar Config para auditoría continua.
   - Documentar políticas y procedimientos.

3. **Gobernanza**:
   - Usar Organizations para múltiples cuentas.
   - Implementar SCPs para políticas.
   - Monitorear costos con Budget.

---

## 🔄 Procesamiento Post-Clase

### 📋 Checklist de Procesamiento

- [ ] Revisar configuración actual de IAM.
- [ ] Auditar permisos con Trusted Advisor.
- [ ] Habilitar CloudTrail y Config.
- [ ] Documentar políticas de seguridad.
- [ ] Implementar MFA en cuentas críticas.

### 🎯 Acciones Prioritarias

1. Hacer auditoría de IAM en tu cuenta.
2. Implementar KMS para datos sensibles.
3. Establecer presupuestos en Budget.

### 🔗 Conexiones

- [[EC2_Amazon_Elastic_Compute_Cloud]]
- [[Azure]]
- [[Infraestructuras y Servicios en la Nube]]

---

## 🎴 Flashcards Rápidas

¿Cuál es el principio de menor privilegio?::Dar solo los permisos mínimos necesarios para realizar una tarea. #card
¿Qué es CloudTrail?::Registro de auditoría de todas las acciones realizadas en AWS. #card
¿Cuál es la diferencia entre Security Groups y NACLs?::Security Groups a nivel de instancia; NACLs a nivel de subred. #card
¿Qué es el Shared Responsibility Model?::AWS asegura infraestructura; el cliente asegura aplicación y datos. #card
