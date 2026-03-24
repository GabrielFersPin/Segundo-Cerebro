# 🟢 Contenedores

## ▶️ Ejecutar Contenedor

### Básico
```bash
docker run python:3.11       # Ejecuta y sale
docker run -it python:3.11   # Interactivo con terminal
docker run -d nginx          # Detached (background)
```

### Con Nombre
```bash
docker run --name mi-contenedor nginx
```

### Con Puertos
```bash
docker run -p 8080:80 nginx  # Host:Container
docker run -p 5432:5432 postgres
```

### Con Variables de Entorno
```bash
docker run -e POSTGRES_PASSWORD=secret postgres
docker run --env-file .env mi-app
```

### Con Volúmenes
```bash
# Bind mount (carpeta del host)
docker run -v /ruta/host:/ruta/container python

# Named volume
docker run -v mi-volumen:/data postgres

# Solo lectura
docker run -v /ruta/host:/ruta/container:ro python
```

### Comando Personalizado
```bash
docker run python:3.11 python -c "print('Hola')"
docker run -it python:3.11 bash
```

## 👁️ Listar Contenedores

```bash
docker ps                    # Solo activos
docker ps -a                 # Todos (incluye parados)
docker ps -q                 # Solo IDs
docker ps --filter "status=exited"
```

## ⏸️ Controlar Contenedores

```bash
docker start mi-contenedor   # Iniciar parado
docker stop mi-contenedor    # Detener (SIGTERM)
docker kill mi-contenedor    # Matar (SIGKILL)
docker restart mi-contenedor # Reiniciar
docker pause mi-contenedor   # Pausar
docker unpause mi-contenedor # Reanudar
```

## 🔍 Inspeccionar

```bash
docker logs mi-contenedor    # Ver logs
docker logs -f mi-contenedor # Seguir logs (tail -f)
docker logs --tail 50 mi-contenedor

docker inspect mi-contenedor # Info completa (JSON)
docker top mi-contenedor     # Procesos
docker stats                 # Uso de recursos (live)
docker stats --no-stream     # Una vez
```

## 💻 Ejecutar Comandos

```bash
# Ejecutar comando en contenedor activo
docker exec mi-contenedor ls /app
docker exec -it mi-contenedor bash
docker exec -it mi-contenedor python manage.py shell

# Como root
docker exec -u root -it mi-contenedor bash
```

## 📋 Copiar Archivos

```bash
# Del host al contenedor
docker cp archivo.txt mi-contenedor:/app/

# Del contenedor al host
docker cp mi-contenedor:/app/logs.txt ./logs.txt
```

## 🗑️ Eliminar Contenedores

```bash
docker rm mi-contenedor      # Parado
docker rm -f mi-contenedor   # Forzar (aunque esté activo)
docker rm $(docker ps -aq)   # Todos los parados

# Eliminar contenedores parados
docker container prune
```

## 🔄 Actualizar Contenedor

```bash
# Recrear con nueva imagen
docker stop mi-contenedor
docker rm mi-contenedor
docker pull mi-app:latest
docker run --name mi-contenedor mi-app:latest
```

---

## 🎯 Flags Útiles

```bash
--name          # Nombre del contenedor
-d              # Detached (background)
-it             # Interactive + TTY
-p              # Port mapping (host:container)
-v              # Volume mounting
-e              # Environment variable
--rm            # Auto-eliminar al parar
--restart       # Política de reinicio (always, unless-stopped)
--network       # Red específica
--memory        # Límite de RAM
--cpus          # Límite de CPU
```

## 💡 Ejemplos Completos

### Jupyter Notebook
```bash
docker run -d \
  --name jupyter \
  -p 8888:8888 \
  -v $(pwd):/home/jovyan/work \
  jupyter/scipy-notebook
```

### PostgreSQL
```bash
docker run -d \
  --name postgres-db \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_USER=admin \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  postgres:15
```

### App Python con Hot Reload
```bash
docker run -d \
  --name python-app \
  -p 5000:5000 \
  -v $(pwd):/app \
  -e FLASK_ENV=development \
  --restart unless-stopped \
  mi-python-app
```

---

**Relacionado**: [[Docker Compose para Multi-Container]] • [[Docker Networking]]
