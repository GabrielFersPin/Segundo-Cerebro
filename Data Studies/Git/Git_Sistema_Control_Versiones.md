---
cards-deck: Herramientas
created: 2025-01-19
modified: 2025-01-19
status: 🌱
tipo_nota: tecnica
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
---

# Git - Sistema de Control de Versiones

> [!abstract] Objetivo
> Nota de referencia rápida sobre Git: comandos esenciales, flujos de trabajo y conceptos fundamentales para consulta diaria

---

## 📚 Definición

Git es un sistema de control de versiones distribuido diseñado por Linus Torvalds en 2005. A diferencia de sistemas centralizados como SVN, cada desarrollador tiene una copia completa del repositorio con todo su historial.

**¿Por qué distribuido?** Cada clone es un backup completo. Puedes trabajar offline, hacer commits localmente, y sincronizar cuando quieras. No hay un "servidor central" necesario (aunque GitHub/GitLab actúan como tal por convención).

**Filosofía core**: Git piensa en los datos como instantáneas (snapshots) del sistema de archivos, no como diferencias entre archivos. Cada commit es una foto completa de tu proyecto en ese momento.

---

## ⚙️ Conceptos Fundamentales

### 📌 Las Tres Áreas de Git

**Tipo**: Arquitectura interna

**Características**:
- **Working Directory**: Archivos que estás modificando actualmente en tu sistema
- **Staging Area (Index)**: Zona intermedia donde preparas los cambios antes del commit
- **Repository (.git)**: Base de datos con todo el historial de commits

**Flujo básico**: Modificas archivos → `git add` (staging) → `git commit` (repository)

**Relacionado**: [[Flujos de Trabajo Git]] • [[Git Reset vs Revert]]

---

### 📌 Estados de los Archivos

**Tipo**: Concepto fundamental

**Características**:
- **Untracked**: Git no conoce el archivo (nunca ha sido añadido)
- **Unmodified**: Archivo en el último commit, sin cambios
- **Modified**: Archivo modificado pero no en staging
- **Staged**: Archivo preparado para el próximo commit

**Comandos relacionados**:
```bash
git status          # Ver estado actual
git diff            # Cambios no staged
git diff --staged   # Cambios en staging
```

---

### 📌 Branches (Ramas)

**Tipo**: Estructura de datos

**Características**:
- Una rama es simplemente un puntero móvil a un commit
- `HEAD` es un puntero especial que indica dónde estás ahora
- Las ramas son extremadamente ligeras en Git (solo 41 bytes)
- Crear/cambiar ramas es instantáneo

**Flujo típico**:
```bash
git branch feature-login    # Crear rama
git checkout feature-login  # Cambiar a rama
# o en un solo comando:
git checkout -b feature-login

git branch                  # Listar ramas locales
git branch -a               # Listar todas (locales + remotas)
```

**Relacionado**: [[Git Merge vs Rebase]] • [[Feature Branch Workflow]]

---

## 💻 Comandos Esenciales

### 🔧 Configuración Inicial

```bash
# Identidad (necesario antes del primer commit)
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Editor por defecto
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "vim"          # Vim

# Ver configuración
git config --list
git config user.name
```

---

### 🔧 Crear y Clonar Repositorios

```bash
# Inicializar repo nuevo
git init
git init nombre-proyecto

# Clonar repositorio existente
git clone https://github.com/user/repo.git
git clone https://github.com/user/repo.git nuevo-nombre
```

---

### 🔧 Workflow Básico

```bash
# Ver estado
git status
git status -s  # Formato corto

# Añadir archivos al staging
git add archivo.py
git add .                    # Todos los archivos modificados
git add *.js                 # Todos los .js
git add -p                   # Modo interactivo (elegir chunks)

# Commit
git commit -m "Mensaje descriptivo"
git commit -am "mensaje"     # Add + commit (solo tracked files)
git commit --amend           # Modificar último commit

# Ver historial
git log
git log --oneline            # Una línea por commit
git log --graph --oneline    # Con gráfico de ramas
git log -5                   # Últimos 5 commits
git log --author="Gabriel"   # Por autor
git log --since="2 weeks"    # Últimas 2 semanas
```

---

### 🔧 Trabajar con Remotos

```bash
# Ver remotos configurados
git remote -v

# Añadir remoto
git remote add origin https://github.com/user/repo.git

# Cambiar URL del remoto
git remote set-url origin nueva-url

# Obtener cambios (no fusiona)
git fetch origin

# Obtener y fusionar cambios
git pull origin main
git pull                     # Desde rama actual

# Subir cambios
git push origin main
git push -u origin main      # Primera vez (set upstream)
git push                     # Siguientes veces

# Subir nueva rama
git push -u origin feature-nueva
```

---

### 🔧 Branches y Merging

```bash
# Crear y cambiar de rama
git checkout -b nueva-rama
git switch -c nueva-rama     # Nuevo comando (Git 2.23+)

# Cambiar de rama
git checkout main
git switch main              # Nuevo comando

# Fusionar rama
git checkout main
git merge feature-login

# Eliminar rama
git branch -d feature-login  # Solo si está fusionada
git branch -D feature-login  # Forzar eliminación
```

---

### 🔧 Deshacer Cambios

```bash
# Descartar cambios en working directory
git checkout -- archivo.py
git restore archivo.py       # Nuevo comando

# Quitar archivo del staging (mantener cambios)
git reset HEAD archivo.py
git restore --staged archivo.py  # Nuevo comando

# Volver a commit anterior (peligroso)
git reset --soft HEAD~1      # Mantiene cambios en staging
git reset --mixed HEAD~1     # Mantiene cambios en working dir
git reset --hard HEAD~1      # BORRA CAMBIOS (cuidado!)

# Revertir commit (crea nuevo commit)
git revert HEAD              # Más seguro que reset
git revert abc123            # Revertir commit específico
```

---

### 🔧 Stash (Guardar Temporalmente)

```bash
# Guardar cambios temporalmente
git stash
git stash save "Descripción"

# Ver stashes guardados
git stash list

# Recuperar último stash
git stash pop                # Aplica y elimina
git stash apply              # Aplica pero mantiene en stash

# Recuperar stash específico
git stash apply stash@{2}

# Eliminar stash
git stash drop stash@{1}
git stash clear              # Eliminar todos
```

---

### 🔧 Comandos Avanzados

```bash
# Rebase (reescribir historial)
git rebase main              # Rebase rama actual sobre main
git rebase -i HEAD~3         # Rebase interactivo (últimos 3)

# Cherry-pick (traer commit específico)
git cherry-pick abc123

# Ver diferencias
git diff                     # Working dir vs staging
git diff --staged            # Staging vs último commit
git diff main feature        # Entre ramas
git diff HEAD~2 HEAD         # Entre commits

# Buscar en el código
git grep "función"           # Buscar en working directory
git grep "función" HEAD~3    # Buscar en commit específico

# Blame (ver quién modificó cada línea)
git blame archivo.py
git blame -L 10,20 archivo.py  # Solo líneas 10-20
```

---

## 💭 Workflows Comunes

### Feature Branch Workflow

```bash
# 1. Actualizar main
git checkout main
git pull origin main

# 2. Crear feature branch
git checkout -b feature-nueva-funcionalidad

# 3. Trabajar y hacer commits
git add .
git commit -m "Implementar funcionalidad X"

# 4. Actualizar con cambios de main (si hay)
git checkout main
git pull origin main
git checkout feature-nueva-funcionalidad
git merge main               # o git rebase main

# 5. Push y crear Pull Request
git push -u origin feature-nueva-funcionalidad
# Luego crear PR en GitHub/GitLab
```

---

### Gitflow (Para Proyectos Grandes)

**Ramas principales**:
- `main/master`: Producción, siempre estable
- `develop`: Integración, siguiente release

**Ramas auxiliares**:
- `feature/*`: Nuevas funcionalidades
- `release/*`: Preparación de releases
- `hotfix/*`: Arreglos urgentes en producción

```bash
# Empezar feature
git checkout develop
git checkout -b feature/login

# Terminar feature
git checkout develop
git merge --no-ff feature/login
git branch -d feature/login

# Hotfix urgente
git checkout main
git checkout -b hotfix/bug-critico
# ... fix ...
git checkout main
git merge --no-ff hotfix/bug-critico
git checkout develop
git merge --no-ff hotfix/bug-critico
```

---

## 🎯 Mejores Prácticas

### Commits

- **Atómicos**: Un cambio lógico por commit
- **Mensajes claros**: 
  - Primera línea: resumen (50 chars max)
  - Línea en blanco
  - Descripción detallada si es necesario
  - Ejemplo: `feat: Añadir autenticación JWT`
- **Usa prefijos**: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`

### Branches

- `main`: Solo código en producción
- `develop`: Rama de integración
- `feature/*`: Una por funcionalidad
- Nombres descriptivos: `feature/user-authentication`, no `feature/cambios`

### Pull Requests

- Revisión por pares antes de merge
- Descripción clara de qué y por qué
- Tests pasando antes de aprobar
- Conflictos resueltos localmente

---

## 🔍 Troubleshooting Común

### Conflictos en Merge

```bash
# Durante un merge/pull/rebase aparecen conflictos
# 1. Ver archivos en conflicto
git status

# 2. Editar archivos (buscar <<<<<<, ======, >>>>>>)
# 3. Marcar como resuelto
git add archivo-resuelto.py

# 4. Completar merge
git commit  # (si es merge)
git rebase --continue  # (si es rebase)

# Abortar si te arrepientes
git merge --abort
git rebase --abort
```

### Borré un Commit por Error

```bash
# Recuperar usando reflog
git reflog                   # Ver historial de HEAD
git reset --hard HEAD@{3}    # Volver a posición anterior
```

### Archivo Sensible Commiteado

```bash
# Eliminar del historial (peligroso)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch archivo-sensible.env" \
  --prune-empty --tag-name-filter cat -- --all

# Mejor: usar .gitignore desde el inicio
echo "*.env" >> .gitignore
git add .gitignore
git commit -m "Añadir .gitignore"
```

---

## 🧩 .gitignore Esencial

```gitignore
# Python
*.pyc
__pycache__/
*.py[cod]
*$py.class
.Python
env/
venv/
.venv
.env

# Node
node_modules/
npm-debug.log
yarn-error.log

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Datos y modelos (data science)
*.csv
*.xlsx
data/raw/
models/*.pkl
*.h5

# Jupyter
.ipynb_checkpoints/
```

---

## 📚 Referencias & Enlaces

**Enlaces internos**: 
- [[GitHub vs GitLab vs Bitbucket]]
- [[Git Hooks para Automatización]]
- [[Semantic Versioning]]

**Referencias externas**: 
- [Pro Git Book](https://git-scm.com/book/en/v2) - Libro oficial gratuito
- [Git Documentation](https://git-scm.com/docs)
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Para cuando metes la pata
- [Learn Git Branching](https://learngitbranching.js.org/) - Tutorial interactivo

**Fuente**: Documentación oficial de Git, experiencia práctica

---

## 📋 Metadata

- **Estado**: 🌱 Semilla
- **Última revisión**: 2025-01-19
- **Próxima revisión**: 2025-01-22
- **Veces revisado**: 0
- **Nivel de comprensión**: 💡 Entiendo bien
- **Tiempo estimado de repaso**: 📖 15 minutos

---

> [!tip] 💡 Próximos pasos
> - Practicar rebase interactivo para limpiar historial
> - Experimentar con Git Hooks para automatización
> - Conectar con notas sobre CI/CD y DevOps practices
> - Añadir ejemplos de resolución de conflictos complejos
