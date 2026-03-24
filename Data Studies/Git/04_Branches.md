# 🟠 Branches (Ramas)

## Ver Ramas
```bash
git branch               # Locales
git branch -a            # Todas (locales + remotas)
git branch -v            # Con último commit
```

## Crear & Cambiar
```bash
# Forma tradicional
git branch <nombre>      # Solo crear
git checkout <rama>      # Solo cambiar
git checkout -b <nombre> # Crear y cambiar

# Forma nueva (Git 2.23+)
git switch <rama>        # Cambiar
git switch -c <nombre>   # Crear y cambiar
```

## 🔀 Fusionar Ramas

### Merge
```bash
git checkout main
git merge feature-branch

# Forzar merge commit
git merge --no-ff feature-branch
```

### Rebase
```bash
git checkout feature-branch
git rebase main

# Rebase interactivo
git rebase -i HEAD~3
```

### Cherry-pick
```bash
git cherry-pick <commit-hash>
```

## Eliminar Ramas
```bash
git branch -d <rama>     # Solo si está fusionada
git branch -D <rama>     # Forzar eliminación
```

## 🎯 Diferencias Clave

**Merge**:
- Preserva historial completo
- Crea merge commit
- Historial puede verse "sucio"

**Rebase**:
- Historial lineal limpio
- Reescribe commits (⚠️ no en público)
- "Como si hubieras trabajado en main"

---

**Regla de oro**: No hagas rebase de commits públicos
