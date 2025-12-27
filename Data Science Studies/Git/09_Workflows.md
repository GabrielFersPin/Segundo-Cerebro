# 🎓 Workflows Comunes

## 🌱 Feature Branch Workflow

```bash
# 1. Actualizar main
git checkout main
git pull origin main

# 2. Crear feature branch
git checkout -b feature/nueva-funcionalidad

# 3. Trabajar y commitear
git add .
git commit -m "Implementar funcionalidad X"
git commit -m "Añadir tests"
git commit -m "Actualizar docs"

# 4. Actualizar con cambios de main
git checkout main
git pull origin main
git checkout feature/nueva-funcionalidad
git merge main
# o: git rebase main

# 5. Push y crear Pull Request
git push -u origin feature/nueva-funcionalidad
# Crear PR en GitHub/GitLab
```

## 🔄 Actualizar Feature con Main

### Opción A: Merge (preserva historial)
```bash
git checkout main
git pull origin main
git checkout feature/mi-rama
git merge main
```

### Opción B: Rebase (historial limpio)
```bash
git checkout feature/mi-rama
git fetch origin
git rebase origin/main
```

## 🚀 Gitflow (Proyectos Grandes)

### Estructura de Ramas
- `main`: Producción
- `develop`: Integración
- `feature/*`: Nuevas funcionalidades
- `release/*`: Preparación de releases
- `hotfix/*`: Arreglos urgentes

### Feature Completa
```bash
# Empezar feature
git checkout develop
git checkout -b feature/login

# Trabajar...
git add .
git commit -m "mensaje"

# Terminar feature
git checkout develop
git merge --no-ff feature/login
git branch -d feature/login
git push origin develop
```

### Hotfix Urgente
```bash
# Crear hotfix desde main
git checkout main
git checkout -b hotfix/bug-critico

# Arreglar bug
git add .
git commit -m "Fix: bug crítico"

# Aplicar a main Y develop
git checkout main
git merge --no-ff hotfix/bug-critico
git tag -a v1.0.1 -m "Hotfix 1.0.1"

git checkout develop
git merge --no-ff hotfix/bug-critico

git branch -d hotfix/bug-critico
```

### Release
```bash
# Crear release desde develop
git checkout develop
git checkout -b release/v1.2.0

# Preparar release (actualizar versions, changelog)
git commit -am "Bump version to 1.2.0"

# Fusionar a main
git checkout main
git merge --no-ff release/v1.2.0
git tag -a v1.2.0 -m "Version 1.2.0"

# Fusionar a develop
git checkout develop
git merge --no-ff release/v1.2.0

git branch -d release/v1.2.0
git push origin main develop --tags
```

## ⚡ GitHub Flow (Más Simple)

```bash
# 1. Rama = main siempre deployable
# 2. Crear feature branch descriptiva
git checkout -b add-user-authentication

# 3. Commits con mensajes claros
git commit -m "feat: add JWT authentication"

# 4. Push frecuente
git push -u origin add-user-authentication

# 5. Pull Request cuando esté listo
# 6. Revisión + merge a main
# 7. Deploy automático desde main
```

## 🎯 Convenciones de Commits

### Conventional Commits
```bash
feat: nueva funcionalidad
fix: arreglo de bug
docs: cambios en documentación
style: formato, sin cambios de código
refactor: refactorización
test: añadir o modificar tests
chore: tareas de mantenimiento

# Ejemplos:
git commit -m "feat: añadir autenticación OAuth"
git commit -m "fix: resolver bug en cálculo de totales"
git commit -m "docs: actualizar README con ejemplos"
```

---

**Elegir workflow según**:
- **GitHub Flow**: Proyectos simples, deploy continuo
- **Feature Branch**: Equipos medianos
- **Gitflow**: Proyectos grandes, releases programados
