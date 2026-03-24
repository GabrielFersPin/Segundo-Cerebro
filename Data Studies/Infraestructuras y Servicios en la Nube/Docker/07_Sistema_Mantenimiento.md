# 🟤 Sistema & Mantenimiento

## 📊 Información del Sistema

### Estado General
```bash
docker info                  # Info completa del daemon
docker version               # Versión de Docker
docker system df             # Uso de espacio
docker system df -v          # Detallado
```

### Monitoreo en Tiempo Real
```bash
docker stats                 # Todos los contenedores
docker stats web db          # Contenedores específicos
docker stats --no-stream     # Una vez (no live)
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"
```

### Eventos del Sistema
```bash
docker events               # Ver eventos en tiempo real
docker events --since '2024-01-01'
docker events --filter type=container
```

---

## 🧹 Limpieza y Mantenimiento

### Limpieza Rápida
```bash
# Eliminar todo lo no usado (⚠️ cuidado)
docker system prune          # Containers, networks, images

# Con volúmenes también
docker system prune -a --volumes

# Sin confirmación
docker system prune -f
```

### Limpieza Específica

#### Contenedores
```bash
docker container prune       # Solo parados
docker rm $(docker ps -aq)   # Todos (forzar primero stop)
```

#### Imágenes
```bash
docker image prune           # Dangling (sin tag)
docker image prune -a        # Todas sin usar
docker rmi $(docker images -q)  # Todas las imágenes
```

#### Volúmenes
```bash
docker volume prune          # Sin usar
docker volume ls -qf dangling=true | xargs docker volume rm
```

#### Redes
```bash
docker network prune         # Sin usar
```

### Limpieza Programada
```bash
# Añadir a crontab (Linux)
0 2 * * 0 docker system prune -af --volumes

# Script de limpieza
#!/bin/bash
echo "🧹 Limpiando Docker..."
docker container prune -f
docker image prune -af
docker volume prune -f
docker network prune -f
echo "✅ Limpieza completa"
```

---

## 💾 Backup y Restore

### Backup de Contenedor
```bash
# Commit contenedor a imagen
docker commit mi-contenedor mi-backup:v1

# Export contenedor (filesystem)
docker export mi-contenedor > contenedor-backup.tar

# Save imagen
docker save mi-imagen:tag > imagen-backup.tar
docker save -o imagen.tar imagen1 imagen2
```

### Restore
```bash
# Import filesystem
docker import contenedor-backup.tar mi-imagen:restored

# Load imagen
docker load < imagen-backup.tar
docker load -i imagen.tar
```

### Backup de Volúmenes
```bash
# Backup
docker run --rm \
  -v pgdata:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/pgdata-$(date +%Y%m%d).tar.gz -C /data .

# Restore
docker run --rm \
  -v pgdata:/data \
  -v $(pwd):/backup \
  alpine tar xzf /backup/pgdata-20240119.tar.gz -C /data
```

### Backup Completo del Sistema
```bash
#!/bin/bash
BACKUP_DIR="/backups/docker-$(date +%Y%m%d)"
mkdir -p $BACKUP_DIR

# Backup imágenes
docker images --format "{{.Repository}}:{{.Tag}}" | \
  while read image; do
    docker save $image | gzip > "$BACKUP_DIR/${image//\//_}.tar.gz"
  done

# Backup volumes
docker volume ls -q | \
  while read volume; do
    docker run --rm \
      -v $volume:/data \
      -v $BACKUP_DIR:/backup \
      alpine tar czf /backup/$volume.tar.gz -C /data .
  done

echo "✅ Backup completo en $BACKUP_DIR"
```

---

## 🔒 Seguridad

### Escaneo de Vulnerabilidades
```bash
# Docker Scout (built-in)
docker scout cves imagen:tag
docker scout quickview

# Trivy (instalar separadamente)
trivy image python:3.11
```

### Ejecutar como Usuario No-Root
```dockerfile
# En Dockerfile
RUN useradd -m -u 1000 appuser
USER appuser
```

```bash
# En docker run
docker run --user 1000:1000 imagen
docker run --user $(id -u):$(id -g) imagen
```

### Limitar Recursos
```bash
# CPU
docker run --cpus=0.5 imagen        # 50% de 1 CPU
docker run --cpus=2 imagen          # 2 CPUs

# Memoria
docker run --memory=512m imagen
docker run --memory=1g --memory-swap=2g imagen

# I/O
docker run --device-read-bps /dev/sda:1mb imagen
```

### Read-only Filesystem
```bash
docker run --read-only \
  --tmpfs /tmp \
  imagen
```

### Capabilities (Linux)
```bash
# Quitar capabilities
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE nginx

# Ver capabilities
docker exec contenedor cat /proc/1/status | grep Cap
```

---

## 🔧 Configuración del Daemon

### Archivo de Configuración
```json
# /etc/docker/daemon.json (Linux)
# %programdata%\docker\config\daemon.json (Windows)
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  },
  "storage-driver": "overlay2",
  "default-address-pools": [
    {
      "base": "172.80.0.0/16",
      "size": 24
    }
  ]
}
```

### Reiniciar Daemon
```bash
# Linux (systemd)
sudo systemctl restart docker

# Verificar estado
sudo systemctl status docker
```

### Logging Drivers
```bash
# En docker run
docker run --log-driver=json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  imagen
```

---

## 📈 Performance & Optimization

### Build Cache
```bash
# Ver caché
docker system df -v

# Limpiar build cache
docker builder prune
docker builder prune --all  # Todo el caché

# Usar BuildKit (más rápido)
DOCKER_BUILDKIT=1 docker build .
```

### Registry Mirror
```json
// daemon.json
{
  "registry-mirrors": ["https://mirror.gcr.io"]
}
```

### Storage Driver Optimization
```bash
# Ver storage driver actual
docker info | grep "Storage Driver"

# Opciones: overlay2 (recomendado), btrfs, zfs
```

---

## 🔍 Debugging

### Ver Logs del Daemon
```bash
# Linux (systemd)
sudo journalctl -u docker.service
sudo journalctl -u docker.service --since today

# Ver últimas 100 líneas
sudo journalctl -u docker.service -n 100
```

### Inspeccionar Todo
```bash
docker inspect <contenedor|imagen|volumen|red>
docker inspect --format='{{.State.Status}}' contenedor
docker inspect --format='{{.NetworkSettings.IPAddress}}' contenedor
```

### Debug de Builds
```bash
# Ver cada paso
docker build --progress=plain --no-cache .

# Entrar en una capa específica
docker run -it <layer-id> sh
```

### Ejecutar Docker en Debug Mode
```bash
# Editar daemon.json
{
  "debug": true,
  "log-level": "debug"
}

sudo systemctl restart docker
```

---

## 🎯 Tips de Productividad

### Aliases Útiles
```bash
# Añadir a ~/.bashrc o ~/.zshrc
alias dps='docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"'
alias dimg='docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"'
alias dclean='docker system prune -af --volumes'
alias dstop='docker stop $(docker ps -q)'
alias dlogs='docker logs -f'
alias dexec='docker exec -it'
```

### Functions
```bash
# Shell en contenedor
dsh() {
  docker exec -it $1 sh
}

# Logs con tail
dlog() {
  docker logs -f --tail 100 $1
}

# Eliminar contenedor y volumen
drm() {
  docker rm -f $1
  docker volume rm $1-data 2>/dev/null
}
```

### Docker Compose Aliases
```bash
alias dc='docker-compose'
alias dcup='docker-compose up -d'
alias dcdown='docker-compose down'
alias dclogs='docker-compose logs -f'
alias dcps='docker-compose ps'
```

---

## 💡 Best Practices

1. **Limpieza regular**:
   ```bash
   # Semanalmente
   docker system prune -a
   ```

2. **Monitorear espacio**:
   ```bash
   docker system df
   ```

3. **Logs con límites**:
   ```json
   {
     "log-driver": "json-file",
     "log-opts": {
       "max-size": "10m",
       "max-file": "3"
     }
   }
   ```

4. **Backup crítico**:
   - Volúmenes de databases
   - Imágenes custom importantes
   - docker-compose.yml

5. **Seguridad**:
   - Escanear imágenes regularmente
   - Actualizar imágenes base
   - Ejecutar como no-root
   - Limitar recursos

---

**Relacionado**: [[Docker Security Best Practices]] • [[Docker in Production]]
