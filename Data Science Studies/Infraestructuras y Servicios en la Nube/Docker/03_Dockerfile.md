# 🟠 Dockerfile

## 📝 Estructura Básica

```dockerfile
# 1. Imagen base
FROM python:3.11-slim

# 2. Metadata
LABEL maintainer="tu@email.com"
LABEL version="1.0"

# 3. Variables de entorno
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/app

# 4. Directorio de trabajo
WORKDIR /app

# 5. Copiar archivos
COPY requirements.txt .
COPY . .

# 6. Ejecutar comandos (build time)
RUN pip install --no-cache-dir -r requirements.txt

# 7. Exponer puerto
EXPOSE 5000

# 8. Usuario (seguridad)
USER nonroot

# 9. Comando por defecto (runtime)
CMD ["python", "app.py"]
```

## 🔧 Instrucciones Principales

### FROM
```dockerfile
FROM python:3.11              # Imagen oficial
FROM python:3.11-slim         # Versión ligera
FROM python:3.11-alpine       # Muy ligera (pero cuidado)
FROM ubuntu:22.04             # Desde OS base
```

### WORKDIR
```dockerfile
WORKDIR /app                  # Crea y se mueve ahí
# Todos los comandos siguientes serán relativos a /app
```

### COPY vs ADD
```dockerfile
# COPY (preferido) - Solo copia
COPY archivo.txt /app/
COPY src/ /app/src/
COPY --chown=user:group archivo.txt /app/

# ADD (evitar) - Copia + descomprime
ADD archivo.tar.gz /app/      # Se descomprime automáticamente
ADD https://url.com/file /app/ # Descarga de URL
```

### RUN
```dockerfile
# Ejecuta comandos durante el build
RUN apt-get update && apt-get install -y curl

# Múltiples comandos (mejor práctica)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        git \
    && rm -rf /var/lib/apt/lists/*

# Con shell script
RUN bash -c "source ~/.bashrc && command"
```

### ENV
```dockerfile
ENV NODE_ENV=production
ENV PATH="/app/bin:${PATH}"
ENV DATABASE_URL="postgresql://localhost/db"

# Múltiples en una línea
ENV VAR1=value1 VAR2=value2
```

### ARG
```dockerfile
# Variables solo en build-time
ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}

ARG BUILD_DATE
LABEL build_date=${BUILD_DATE}

# Uso: docker build --build-arg PYTHON_VERSION=3.12
```

### EXPOSE
```dockerfile
EXPOSE 5000                   # Documenta puerto
EXPOSE 5000/tcp
EXPOSE 53/udp
# No publica el puerto (necesitas -p en docker run)
```

### USER
```dockerfile
# Crear usuario no-root (seguridad)
RUN useradd -m -u 1000 appuser
USER appuser

# Volver a root si es necesario
USER root
```

### CMD vs ENTRYPOINT

```dockerfile
# CMD - Comando por defecto (se puede sobreescribir)
CMD ["python", "app.py"]
CMD python app.py             # Shell form (evitar)

# ENTRYPOINT - Comando fijo (no se sobreescribe fácilmente)
ENTRYPOINT ["python", "app.py"]

# Combinación (mejor práctica)
ENTRYPOINT ["python"]
CMD ["app.py"]
# docker run imagen other.py  → ejecuta python other.py
```

### VOLUME
```dockerfile
VOLUME /data                  # Define mount point
VOLUME ["/var/log", "/var/db"]
```

### HEALTHCHECK
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:5000/health || exit 1
```

---

## 🎯 Ejemplos Completos

### Python Data Science
```dockerfile
FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Instalar Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Usuario no-root
RUN useradd -m -u 1000 datauser && \
    chown -R datauser:datauser /app
USER datauser

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser"]
```

### Flask API
```dockerfile
FROM python:3.11-slim as base

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Desarrollo
FROM base as development
ENV FLASK_ENV=development
CMD ["flask", "run", "--host=0.0.0.0"]

# Producción
FROM base as production
ENV FLASK_ENV=production
RUN useradd -m appuser
USER appuser
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

### Node.js
```dockerfile
FROM node:18-alpine

WORKDIR /app

# Solo package files primero (cache layer)
COPY package*.json ./
RUN npm ci --only=production

# Luego el resto
COPY . .

RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001
USER nodejs

EXPOSE 3000

CMD ["node", "server.js"]
```

---

## 🚀 Best Practices

### 1. Orden de Capas (para aprovechar caché)
```dockerfile
# ❌ Malo - invalida caché cada vez
COPY . .
RUN pip install -r requirements.txt

# ✅ Bueno - solo reinstala si cambia requirements
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

### 2. Multi-stage Build
```dockerfile
# Stage 1: Build
FROM python:3.11 as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]
```

### 3. Minimizar Capas
```dockerfile
# ❌ Malo - 3 capas
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get clean

# ✅ Bueno - 1 capa
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

### 4. .dockerignore
```
# Archivo .dockerignore
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
.env
.venv
venv/
.git/
.gitignore
.dockerignore
node_modules/
*.md
.DS_Store
```

### 5. Usuario No-Root
```dockerfile
# Siempre crea un usuario específico
RUN adduser --disabled-password --gecos '' appuser
USER appuser
```

---

## 🔍 Debugging

### Ver imagen construida paso a paso
```bash
docker build --progress=plain --no-cache -t test .
```

### Ejecutar hasta cierto paso
```bash
docker build --target builder -t test-builder .
```

### Inspeccionar capa específica
```bash
docker history mi-imagen
docker run -it <layer-id> sh
```

---

**Relacionado**: [[Docker Multi-stage Builds]] • [[Docker Build Optimization]]
