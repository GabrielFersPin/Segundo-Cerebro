# 🔵 Networks (Redes)

## 🌐 Tipos de Redes

### 1. Bridge (Default)
```bash
docker network create mi-red
```
- Red privada en el host
- Contenedores pueden comunicarse entre sí
- Aislada de otros containers fuera de la red

### 2. Host
```bash
docker run --network host nginx
```
- Usa red del host directamente
- Sin aislamiento de red
- Mejor performance

### 3. None
```bash
docker run --network none alpine
```
- Sin red
- Máximo aislamiento

### 4. Overlay (Swarm)
- Para múltiples hosts Docker
- Docker Swarm / Kubernetes

---

## 🔧 Comandos de Redes

### Crear
```bash
docker network create mi-red
docker network create --driver bridge mi-red
docker network create --subnet=172.18.0.0/16 mi-red
```

### Listar
```bash
docker network ls
docker network ls --filter driver=bridge
```

### Inspeccionar
```bash
docker network inspect mi-red
# Muestra: Subnet, Gateway, Contenedores conectados
```

### Eliminar
```bash
docker network rm mi-red
docker network prune  # Eliminar sin usar
```

### Conectar/Desconectar
```bash
# Conectar contenedor a red
docker network connect mi-red mi-contenedor

# Desconectar
docker network disconnect mi-red mi-contenedor
```

---

## 📋 Uso en docker run

### Red por Defecto
```bash
# Usa la red bridge default
docker run -d --name web nginx
```

### Red Personalizada
```bash
docker network create app-network

docker run -d \
  --name web \
  --network app-network \
  nginx

docker run -d \
  --name db \
  --network app-network \
  postgres
```

### Múltiples Redes
```bash
docker run -d \
  --name proxy \
  --network frontend \
  --network backend \
  nginx
```

### Alias en Red
```bash
docker run -d \
  --name db \
  --network app-network \
  --network-alias database \
  postgres

# Otros contenedores pueden usar 'database' como hostname
```

---

## 🐳 Uso en Docker Compose

### Red por Defecto
```yaml
version: '3.8'

services:
  web:
    image: nginx
  db:
    image: postgres

# Compose crea una red default automáticamente
# Los servicios pueden comunicarse por nombre
```

### Redes Personalizadas
```yaml
version: '3.8'

services:
  web:
    image: nginx
    networks:
      - frontend
      - backend

  api:
    image: node
    networks:
      - backend

  db:
    image: postgres
    networks:
      - backend

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true  # Sin acceso externo
```

### Configuración Avanzada
```yaml
networks:
  app-network:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.28.0.0/16
          gateway: 172.28.0.1
    driver_opts:
      com.docker.network.bridge.name: br-app
```

---

## 🔗 Comunicación entre Contenedores

### Por Nombre (DNS Automático)
```yaml
services:
  web:
    image: nginx
    # Puede conectar a: http://db:5432
    
  db:
    image: postgres
    # Puede conectar a: http://web:80
```

### Ejemplo Práctico
```yaml
version: '3.8'

services:
  app:
    build: .
    environment:
      # Usa nombre del servicio como hostname
      DATABASE_URL: postgresql://user:pass@postgres:5432/mydb
      REDIS_URL: redis://redis:6379/0
    networks:
      - backend

  postgres:
    image: postgres:15
    networks:
      - backend

  redis:
    image: redis:7
    networks:
      - backend

networks:
  backend:
```

### Acceso desde Host
```bash
# Publicar puerto para acceder desde host
docker run -d \
  -p 5432:5432 \
  --name db \
  --network app-network \
  postgres

# Desde host: localhost:5432
# Desde otros contenedores: db:5432
```

---

## 🎯 Casos de Uso

### Arquitectura Frontend/Backend/Database
```yaml
version: '3.8'

services:
  frontend:
    image: nginx
    ports:
      - "80:80"
    networks:
      - frontend
    depends_on:
      - backend

  backend:
    build: ./api
    networks:
      - frontend
      - backend
    environment:
      DATABASE_URL: postgresql://db:5432/app

  database:
    image: postgres:15
    networks:
      - backend  # Solo accesible desde backend
    volumes:
      - pgdata:/var/lib/postgresql/data

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true  # Sin acceso a internet

volumes:
  pgdata:
```

### Microservicios con Proxy Reverso
```yaml
version: '3.8'

services:
  nginx:
    image: nginx
    ports:
      - "80:80"
    networks:
      - public
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro

  service1:
    build: ./service1
    networks:
      - public
      - private
    environment:
      DB_HOST: postgres

  service2:
    build: ./service2
    networks:
      - public
      - private
    environment:
      DB_HOST: postgres

  postgres:
    image: postgres:15
    networks:
      - private  # Solo servicios internos

  redis:
    image: redis:7
    networks:
      - private

networks:
  public:
    driver: bridge
  private:
    driver: bridge
    internal: true
```

### Entorno de Desarrollo con Múltiples Apps
```yaml
version: '3.8'

services:
  # Proyecto 1
  app1:
    build: ./app1
    networks:
      - shared-network
      - app1-internal

  app1-db:
    image: postgres:15
    networks:
      - app1-internal

  # Proyecto 2
  app2:
    build: ./app2
    networks:
      - shared-network
      - app2-internal

  app2-db:
    image: postgres:15
    networks:
      - app2-internal

  # Servicios compartidos
  redis:
    image: redis:7
    networks:
      - shared-network

networks:
  shared-network:
    driver: bridge
  app1-internal:
    driver: bridge
  app2-internal:
    driver: bridge
```

---

## 🔍 Troubleshooting

### Ver Contenedores en Red
```bash
docker network inspect mi-red
# Buscar sección "Containers"
```

### Test de Conectividad
```bash
# Desde un contenedor, hacer ping a otro
docker exec web ping db

# Test de puerto
docker exec web nc -zv db 5432

# Instalar herramientas en contenedor temporal
docker run --rm -it \
  --network app-network \
  nicolaka/netshoot
```

### DNS Resolution
```bash
# Ver resolución DNS
docker exec web nslookup db
docker exec web cat /etc/resolv.conf
```

### Port Mapping Issues
```bash
# Ver puertos publicados
docker ps --format "table {{.Names}}\t{{.Ports}}"

# Ver si puerto está en uso en host
netstat -tuln | grep 8080
lsof -i :8080
```

---

## 💡 Best Practices

1. **Crea redes específicas por proyecto**:
   ```bash
   docker network create proyecto-red
   ```

2. **Usa redes internas para bases de datos**:
   ```yaml
   networks:
     backend:
       internal: true
   ```

3. **Nombra tus redes descriptivamente**:
   ```yaml
   networks:
     frontend:
     backend:
     database-tier:
   ```

4. **Segmenta por capas**:
   - `frontend`: Nginx, frontend apps
   - `backend`: API services
   - `data`: Databases, caches

5. **En Docker Compose, usa nombres de servicio**:
   ```python
   # ✅ Bueno
   DATABASE_URL = "postgresql://postgres:5432/db"
   
   # ❌ Malo (hardcoded IP)
   DATABASE_URL = "postgresql://172.18.0.2:5432/db"
   ```

---

**Relacionado**: [[Docker Service Discovery]] • [[Docker Security Networking]]
