# 🔬 Docker para Data Science

## 🎯 Casos de Uso Comunes

### 1. Jupyter Lab + Dependencias
### 2. Pipeline de ML (Training + Inference)
### 3. Entorno Reproducible
### 4. Compartir Experimentos

---

## 🔬 Stack Jupyter + PostgreSQL + VS Code

```yaml
version: '3.8'

services:
  jupyter:
    image: jupyter/scipy-notebook:latest
    container_name: jupyter-lab
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/home/jovyan/work
      - ./data:/home/jovyan/data
      - ./models:/home/jovyan/models
    environment:
      JUPYTER_ENABLE_LAB: "yes"
      GRANT_SUDO: "yes"
    command: start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''
    networks:
      - data-network

  postgres:
    image: postgres:15-alpine
    container_name: postgres-db
    environment:
      POSTGRES_USER: datauser
      POSTGRES_PASSWORD: datapass
      POSTGRES_DB: analytics
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./sql:/docker-entrypoint-initdb.d
    networks:
      - data-network

  pgadmin:
    image: dpage/pgadmin4
    container_name: pgadmin
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@data.com
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

**Uso**:
```bash
docker-compose up -d
# Jupyter: http://localhost:8888
# pgAdmin: http://localhost:5050
```

---

## 🤖 Pipeline ML: Training → Validation → Serving

### Dockerfile para ML
```dockerfile
FROM python:3.11-slim

# Dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Usuario no-root
RUN useradd -m -u 1000 mluser && \
    chown -R mluser:mluser /app
USER mluser

# Punto de entrada flexible
ENTRYPOINT ["python"]
CMD ["train.py"]
```

### docker-compose.yml para Pipeline
```yaml
version: '3.8'

services:
  # 1. Preparación de datos
  preprocess:
    build: .
    command: python preprocess.py
    volumes:
      - ./data:/app/data
      - ./processed:/app/processed
    environment:
      STAGE: preprocess

  # 2. Entrenamiento
  train:
    build: .
    command: python train.py
    volumes:
      - ./processed:/app/data
      - ./models:/app/models
      - ./logs:/app/logs
    environment:
      STAGE: train
    depends_on:
      - preprocess

  # 3. Validación
  validate:
    build: .
    command: python validate.py
    volumes:
      - ./processed:/app/data
      - ./models:/app/models
      - ./logs:/app/logs
    environment:
      STAGE: validate
    depends_on:
      - train

  # 4. Serving (API)
  serve:
    build: .
    command: python serve.py
    ports:
      - "8000:8000"
    volumes:
      - ./models:/app/models:ro
    environment:
      MODEL_PATH: /app/models/best_model.pkl
    restart: unless-stopped
```

**Ejecutar pipeline**:
```bash
# Pipeline completo
docker-compose up preprocess train validate

# Solo serving
docker-compose up -d serve

# Test API
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1.0, 2.0, 3.0]}'
```

---

## 📊 Stack MLflow + MinIO (Experiment Tracking)

```yaml
version: '3.8'

services:
  mlflow:
    image: ghcr.io/mlflow/mlflow:latest
    container_name: mlflow-server
    ports:
      - "5000:5000"
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
    container_name: mlflow-db
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
    container_name: mlflow-minio
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

  # Crear bucket inicial en MinIO
  minio-setup:
    image: minio/mc:latest
    depends_on:
      - minio
    entrypoint: >
      /bin/sh -c "
      sleep 5;
      mc alias set myminio http://minio:9000 minioadmin minioadmin;
      mc mb myminio/mlflow --ignore-existing;
      exit 0;
      "
    networks:
      - ml-network

volumes:
  pgdata:
  minio_data:

networks:
  ml-network:
    driver: bridge
```

**Código Python con MLflow**:
```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier

# Configurar tracking
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("mi-experimento")

with mlflow.start_run():
    # Entrenar modelo
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    # Log parámetros
    mlflow.log_param("n_estimators", 100)
    
    # Log métricas
    accuracy = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", accuracy)
    
    # Log modelo
    mlflow.sklearn.log_model(model, "model")
```

---

## 🐍 Entorno Python Custom con Poetry

### Dockerfile
```dockerfile
FROM python:3.11-slim

# Instalar Poetry
RUN pip install poetry==1.7.1

# Configurar Poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

# Copiar archivos de dependencias
COPY pyproject.toml poetry.lock ./

# Instalar dependencias (sin dev)
RUN poetry install --no-dev --no-root && rm -rf $POETRY_CACHE_DIR

# Copiar código
COPY . .

# Instalar proyecto
RUN poetry install --no-dev

# Usuario no-root
RUN useradd -m -u 1000 pyuser && \
    chown -R pyuser:pyuser /app
USER pyuser

# Activar virtual env
ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "main.py"]
```

### docker-compose.yml
```yaml
version: '3.8'

services:
  app:
    build: .
    volumes:
      - ./src:/app/src  # Hot reload
      - ./data:/app/data
    environment:
      PYTHONPATH: /app
    command: python src/main.py
```

---

## 📈 Streamlit + Data Pipeline

```yaml
version: '3.8'

services:
  streamlit:
    build:
      context: .
      dockerfile: Dockerfile.streamlit
    ports:
      - "8501:8501"
    volumes:
      - ./app:/app
      - ./data:/data:ro
    environment:
      DATABASE_URL: postgresql://user:pass@postgres:5432/db
    command: streamlit run app.py --server.address=0.0.0.0
    networks:
      - app-network

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: db
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - app-network

  etl:
    build: .
    command: python etl/pipeline.py
    volumes:
      - ./data:/data
    environment:
      DATABASE_URL: postgresql://user:pass@postgres:5432/db
      SCHEDULE: "0 2 * * *"  # Cron
    networks:
      - app-network

volumes:
  pgdata:

networks:
  app-network:
```

### Dockerfile.streamlit
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
```

---

## 🔄 Makefile para Workflows

```makefile
.PHONY: help build up down logs clean train serve

help:
	@echo "Comandos disponibles:"
	@echo "  make build     - Construir imágenes"
	@echo "  make up        - Levantar servicios"
	@echo "  make down      - Bajar servicios"
	@echo "  make logs      - Ver logs"
	@echo "  make train     - Entrenar modelo"
	@echo "  make serve     - Servir modelo"
	@echo "  make clean     - Limpieza completa"

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

train:
	docker-compose run --rm train python train.py

validate:
	docker-compose run --rm validate python validate.py

serve:
	docker-compose up -d serve

jupyter:
	docker-compose up -d jupyter
	@echo "Jupyter: http://localhost:8888"

clean:
	docker-compose down -v
	docker system prune -f

backup:
	mkdir -p backups
	docker-compose exec postgres pg_dump -U user db > backups/db-$(shell date +%Y%m%d).sql
	tar czf backups/models-$(shell date +%Y%m%d).tar.gz models/
```

**Uso**:
```bash
make build      # Primera vez
make up         # Levantar todo
make train      # Entrenar modelo
make serve      # API en producción
make logs       # Ver qué pasa
make clean      # Reset completo
```

---

## 🎯 Template Proyecto Data Science

```
mi-proyecto/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── Makefile
├── .dockerignore
├── .env
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   └── exploratory/
│
├── src/
│   ├── data/
│   │   ├── preprocess.py
│   │   └── loader.py
│   ├── models/
│   │   ├── train.py
│   │   └── predict.py
│   └── api/
│       └── serve.py
│
├── models/
│   └── .gitkeep
│
├── logs/
│   └── .gitkeep
│
└── tests/
    └── test_model.py
```

---

## 💡 Best Practices Data Science

1. **Separa datos de código**:
   ```yaml
   volumes:
     - ./data:/data:ro  # Read-only en producción
   ```

2. **Versiona tus modelos**:
   ```python
   model_path = f"models/model_v{version}.pkl"
   ```

3. **Usa secrets para credenciales**:
   ```yaml
   secrets:
     - db_password
   ```

4. **Cachea dependencias pesadas**:
   ```dockerfile
   # Instala dependencias antes de copiar código
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   ```

5. **Health checks**:
   ```dockerfile
   HEALTHCHECK --interval=30s \
     CMD curl -f http://localhost:8000/health || exit 1
   ```

---

**Relacionado**: [[MLOps with Docker]] • [[Reproducible Research]] • [[Model Serving]]
