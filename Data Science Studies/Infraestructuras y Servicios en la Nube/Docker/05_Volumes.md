# 🟡 Volumes (Persistencia)

## 📦 Tipos de Almacenamiento

### 1. Named Volumes (Recomendado)
```bash
# Crear volume
docker volume create mi-volumen

# Usar en contenedor
docker run -v mi-volumen:/data postgres
```

**Ventajas**:
- ✅ Gestionado por Docker
- ✅ Persistente entre contenedores
- ✅ Fácil de hacer backup
- ✅ Funciona en Windows/Mac/Linux

### 2. Bind Mounts (Desarrollo)
```bash
# Montar carpeta del host
docker run -v /ruta/host:/app python

# En Windows
docker run -v C:\Users\gabriel\proyecto:/app python

# Con $(pwd) en Linux/Mac
docker run -v $(pwd):/app python
```

**Ventajas**:
- ✅ Cambios en tiempo real
- ✅ Útil para desarrollo
- ⚠️ Depende de estructura del host

### 3. tmpfs Mounts (Temporal)
```bash
docker run --tmpfs /temp python
```

**Ventajas**:
- ✅ En memoria (rápido)
- ✅ No persiste
- ✅ Datos sensibles temporales

---

## 🔧 Comandos de Volumes

### Crear
```bash
docker volume create pgdata
docker volume create --driver local --opt type=nfs mivolumen
```

### Listar
```bash
docker volume ls
docker volume ls --filter dangling=true
```

### Inspeccionar
```bash
docker volume inspect pgdata
# Muestra: Mountpoint, Driver, Labels, etc.
```

### Eliminar
```bash
docker volume rm pgdata
docker volume rm volumen1 volumen2

# Eliminar todos sin usar
docker volume prune
docker volume prune -f  # Sin confirmación
```

### Backup y Restore

#### Backup
```bash
# Crear backup de volume
docker run --rm \
  -v pgdata:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/pgdata-backup.tar.gz -C /data .
```

#### Restore
```bash
# Restaurar desde backup
docker run --rm \
  -v pgdata:/data \
  -v $(pwd):/backup \
  alpine tar xzf /backup/pgdata-backup.tar.gz -C /data
```

---

## 📋 Uso en docker run

### Named Volume
```bash
docker run -d \
  --name postgres-db \
  -v pgdata:/var/lib/postgresql/data \
  postgres:15
```

### Bind Mount (Desarrollo)
```bash
docker run -d \
  --name jupyter \
  -v $(pwd)/notebooks:/home/jovyan/work \
  -v $(pwd)/data:/data \
  jupyter/scipy-notebook
```

### Read-only Mount
```bash
docker run -d \
  -v $(pwd)/config:/app/config:ro \
  nginx
```

### Multiple Volumes
```bash
docker run -d \
  -v pgdata:/var/lib/postgresql/data \
  -v ./init-scripts:/docker-entrypoint-initdb.d:ro \
  -v ./logs:/var/log/postgresql \
  postgres:15
```

---

## 🐳 Uso en Docker Compose

### Named Volumes
```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro

  web:
    build: .
    volumes:
      - static:/app/static
      - media:/app/media

volumes:
  pgdata:
    driver: local
  static:
  media:
```

### Bind Mounts (Desarrollo)
```yaml
services:
  app:
    build: .
    volumes:
      # Hot reload - código
      - ./src:/app/src
      - ./tests:/app/tests
      
      # No montar node_modules
      - /app/node_modules
      
      # Configuración
      - ./.env:/app/.env:ro
```

### Volume Options
```yaml
volumes:
  pgdata:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /path/on/host
```

---

## 🎯 Casos de Uso

### Data Science: Compartir Datasets
```bash
# Crear volume para datasets
docker volume create datasets

# Contenedor 1: Procesar datos
docker run --rm \
  -v datasets:/data \
  -v $(pwd):/app \
  python:3.11 python /app/preprocess.py

# Contenedor 2: Entrenar modelo
docker run --rm \
  -v datasets:/data \
  -v $(pwd):/app \
  tensorflow/tensorflow python /app/train.py

# Contenedor 3: Análisis en Jupyter
docker run -d \
  -v datasets:/home/jovyan/data:ro \
  -p 8888:8888 \
  jupyter/scipy-notebook
```

### Desarrollo Web: Hot Reload
```yaml
services:
  web:
    build: .
    volumes:
      - ./app:/app              # Código fuente
      - /app/node_modules       # No sobreescribir
    environment:
      - NODE_ENV=development
    command: npm run dev
```

### Base de Datos: Persistencia
```yaml
services:
  postgres:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data          # Datos
      - ./backups:/backups                       # Backups
      - ./init:/docker-entrypoint-initdb.d:ro   # Scripts init
    environment:
      POSTGRES_PASSWORD: secret

volumes:
  pgdata:
```

### Machine Learning: Modelos y Artifacts
```yaml
services:
  training:
    build: .
    volumes:
      - models:/app/models              # Modelos entrenados
      - datasets:/app/data:ro           # Datos (solo lectura)
      - experiments:/app/experiments    # Logs y métricas
    command: python train.py

  inference:
    build: .
    volumes:
      - models:/app/models:ro           # Solo lectura
    command: python serve.py

volumes:
  models:
  datasets:
  experiments:
```

---

## 🔍 Troubleshooting

### Ver dónde está un volume
```bash
docker volume inspect pgdata
# Buscar "Mountpoint": "/var/lib/docker/volumes/pgdata/_data"
```

### Acceder a archivos del volume
```bash
# Linux
sudo ls /var/lib/docker/volumes/pgdata/_data

# Con contenedor temporal
docker run --rm -it \
  -v pgdata:/data \
  alpine sh
```

### Permisos en Bind Mounts
```bash
# Problema: Permission denied
# Solución 1: Ajustar owner en Dockerfile
RUN chown -R user:user /app

# Solución 2: Usar usuario específico
docker run --user $(id -u):$(id -g) -v $(pwd):/app python
```

### Volume lleno
```bash
# Ver uso
docker system df -v

# Limpiar volumes sin usar
docker volume prune
```

---

## 💡 Best Practices

1. **Usa Named Volumes para datos**:
   - Base de datos, uploads, modelos ML

2. **Usa Bind Mounts para desarrollo**:
   - Código fuente, configuración

3. **Backup regular de volumes importantes**:
   ```bash
   docker run --rm -v pgdata:/data -v $(pwd):/backup alpine tar czf /backup/backup.tar.gz -C /data .
   ```

4. **No mezclar node_modules**:
   ```yaml
   volumes:
     - ./app:/app
     - /app/node_modules  # Volume anónimo
   ```

5. **Read-only cuando sea posible**:
   ```bash
   -v ./config:/app/config:ro
   ```

---

**Relacionado**: [[Docker Backup Strategies]] • [[Docker Storage Drivers]]
