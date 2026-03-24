# 🔵 Imágenes

## 📦 Buscar Imágenes

```bash
docker search python         # Buscar en Docker Hub
docker search --limit 5 postgres
```

## ⬇️ Descargar (Pull)

```bash
docker pull python:3.11      # Versión específica
docker pull python           # :latest por defecto
docker pull postgres:15-alpine  # Alpine = más ligero
```

## 👁️ Listar Imágenes Locales

```bash
docker images                # Todas
docker images python         # Filtrar por nombre
docker images -a             # Incluir intermedias
```

## 🏗️ Construir Imagen

```bash
# Desde Dockerfile en directorio actual
docker build -t mi-app:1.0 .

# Con archivo específico
docker build -f Dockerfile.dev -t mi-app:dev .

# Sin usar caché
docker build --no-cache -t mi-app:1.0 .

# Con build arguments
docker build --build-arg PYTHON_VERSION=3.11 -t mi-app .
```

## 🏷️ Etiquetar (Tag)

```bash
docker tag mi-app:1.0 mi-app:latest
docker tag mi-app:1.0 usuario/mi-app:1.0
```

## ⬆️ Publicar (Push)

```bash
# Login en Docker Hub
docker login

# Subir imagen
docker push usuario/mi-app:1.0
docker push usuario/mi-app:latest
```

## 🗑️ Eliminar Imágenes

```bash
docker rmi python:3.11       # Por nombre
docker rmi abc123            # Por ID
docker rmi -f python:3.11    # Forzar

# Eliminar imágenes sin usar
docker image prune           # Dangling (sin tag)
docker image prune -a        # Todas sin contenedor
```

## 🔍 Inspeccionar

```bash
docker image inspect python:3.11
docker history python:3.11   # Ver capas de la imagen
```

## 📊 Información de Tamaño

```bash
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"
docker system df             # Uso de espacio
```

---

**Tips**:
- Usa tags específicos en producción (no `:latest`)
- Alpine images son más pequeñas pero pueden tener problemas de compatibilidad
- Multi-stage builds reducen tamaño final

**Relacionado**: [[Dockerfile Best Practices]] • [[Docker Registry]]
