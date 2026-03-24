# 🟣 Docker Compose

## 📝 ¿Qué es?
Herramienta para definir y ejecutar aplicaciones multi-contenedor usando YAML

## 🎯 Archivo docker-compose.yml

### Estructura Básica
```yaml
version: '3.8'

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:

networks:
  default:
    name: mi-red
```

## ⚙️ Comandos Principales

### Iniciar Servicios
```bash
docker-compose up              # Foreground
docker-compose up -d           # Background (detached)
docker-compose up --build      # Rebuild images
docker-compose up --force-recreate
docker-compose up web          # Solo servicio específico
```

### Detener Servicios
```bash
docker-compose stop            # Detener (mantiene containers)
docker-compose down            # Detener y eliminar containers
docker-compose down -v         # + eliminar volumes
docker-compose down --rmi all  # + eliminar images
```

### Ver Estado
```bash
docker-compose ps              # Listar servicios
docker-compose ps -a           # Incluir parados
docker-compose top             # Procesos de cada servicio
```

### Logs
```bash
docker-compose logs            # Todos los servicios
docker-compose logs -f         # Seguir logs (tail -f)
docker-compose logs web        # Servicio específico
docker-compose logs --tail=50 web
```

### Ejecutar Comandos
```bash
docker-compose exec web sh     # Shell en servicio activo
docker-compose run web python manage.py migrate
docker-compose run --rm web pytest  # Eliminar después
```

### Rebuild & Restart
```bash
docker-compose build           # Rebuild todos
docker-compose build web       # Rebuild servicio específico
docker-compose restart         # Reiniciar servicios
docker-compose restart web     # Reiniciar uno específico
```

### Escalar Servicios
```bash
docker-compose up -d --scale web=3  # 3 instancias de web
```

---

## 📋 Configuración de Servicios

### Imagen o Build
```yaml
services:
  # Desde imagen
  web:
    image: nginx:alpine
  
  # Desde Dockerfile
  app:
    build: .
    
  # Build con contexto específico
  api:
    build:
      context: ./api
      dockerfile: Dockerfile.dev
      args:
        PYTHON_VERSION: 3.11
```

### Puertos
```yaml
services:
  web:
    ports:
      - "8080:80"           # host:container
      - "443:443"
      - "127.0.0.1:8000:8000"  # Solo localhost
```

### Variables de Entorno
```yaml
services:
  db:
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_USER: admin
    # O desde archivo
    env_file:
      - .env
      - .env.local
```

### Volúmenes
```yaml
services:
  app:
    volumes:
      # Named volume
      - pgdata:/var/lib/postgresql/data
      
      # Bind mount
      - ./src:/app/src
      - ./data:/data
      
      # Solo lectura
      - ./config:/app/config:ro
      
      # Volume anónimo
      - /app/node_modules

volumes:
  pgdata:
    driver: local
```

### Redes
```yaml
services:
  web:
    networks:
      - frontend
      - backend
  
  db:
    networks:
      - backend

networks:
  frontend:
  backend:
    driver: bridge
```

### Dependencias
```yaml
services:
  web:
    depends_on:
      - db
      - redis
    # Con health checks
    depends_on:
      db:
        condition: service_healthy
  
  db:
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
```

### Restart Policy
```yaml
services:
  web:
    restart: always          # Siempre reiniciar
    # no (default)
    # always
    # on-failure
    # unless-stopped
```

### Límites de Recursos
```yaml
services:
  web:
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

---

## 🎯 Ejemplos Completos

### Stack Data Science (Jupyter + PostgreSQL)
```yaml
version: '3.8'

services:
  jupyter:
    image: jupyter/scipy-notebook:latest
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/home/jovyan/work
      - ./data:/home/jovyan/data
    environment:
      JUPYTER_ENABLE_LAB: "yes"
    networks:
      - data-network
    depends_on:
      - postgres

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_USER: datauser
      POSTGRES_DB: analytics
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"
    networks:
      - data-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U datauser"]
      interval: 10s
      timeout: 5s
      retries: 5

  pgadmin:
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@example.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "5050:80"
    networks:
      - data-network
    depends_on:
      - postgres

volumes:
  pgdata:

networks:
  data-network:
    driver: bridge
```

### Stack Web (Flask + Redis + PostgreSQL)
```yaml
version: '3.8'

services:
  web:
    build: .
    command: flask run --host=0.0.0.0
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    environment:
      FLASK_ENV: development
      DATABASE_URL: postgresql://user:pass@db:5432/mydb
      REDIS_URL: redis://redis:6379/0
    depends_on:
      - db
      - redis
    networks:
      - backend

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - backend

  redis:
    image: redis:7-alpine
    networks:
      - backend

volumes:
  postgres_data:

networks:
  backend:
```

### Stack MLflow + MinIO (Tracking + Storage)
```yaml
version: '3.8'

services:
  mlflow:
    image: ghcr.io/mlflow/mlflow:latest
    ports:
      - "5001:5000"
    environment:
      MLFLOW_S3_ENDPOINT_URL: http://minio:9000
      AWS_ACCESS_KEY_ID: minioadmin
      AWS_SECRET_ACCESS_KEY: minioadmin
    command: >
      mlflow server
      --backend-store-uri postgresql://mlflow:mlflow@postgres:5432/mlflow
      --default-artifact-root s3://mlflow
      --host 0.0.0.0
    depends_on:
      - postgres
      - minio
    networks:
      - ml-network

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: mlflow
      POSTGRES_PASSWORD: mlflow
      POSTGRES_DB: mlflow
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - ml-network

  minio:
    image: minio/minio:latest
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    command: server /data --console-address ":9001"
    volumes:
      - minio_data:/data
    networks:
      - ml-network

volumes:
  pgdata:
  minio_data:

networks:
  ml-network:
```

---

## 🔧 Variables y Overrides

### Usar múltiples archivos
```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
```

### docker-compose.override.yml (automático)
```yaml
# docker-compose.yml (base)
services:
  web:
    image: nginx

# docker-compose.override.yml (desarrollo, se carga automático)
services:
  web:
    volumes:
      - .:/app
    environment:
      DEBUG: "true"
```

### Variables desde .env
```bash
# .env
POSTGRES_VERSION=15
DB_PASSWORD=secret
```

```yaml
# docker-compose.yml
services:
  db:
    image: postgres:${POSTGRES_VERSION}
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
```

---

## 💡 Tips

**Desarrollo local**:
```bash
# Rebuild cuando cambias código
docker-compose up --build

# Ver logs de un servicio
docker-compose logs -f web

# Ejecutar tests
docker-compose run --rm web pytest
```

**Debugging**:
```bash
# Ver configuración resultante
docker-compose config

# Validar archivo
docker-compose config -q

# Ver qué cambiaría
docker-compose up --dry-run
```

---

**Relacionado**: [[Docker Networks]] • [[Docker Volumes Deep Dive]]
