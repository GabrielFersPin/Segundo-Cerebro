# 🔴 Emergencias & Troubleshooting

## ⚠️ Resolver Conflictos

### Durante Merge/Rebase
```bash
# 1. Ver archivos en conflicto
git status

# 2. Editar archivos manualmente
# Buscar: <<<<<<< HEAD
#         =======
#         >>>>>>> branch-name

# 3. Marcar como resuelto
git add <archivo-resuelto>

# 4. Completar
git commit              # Si es merge
git rebase --continue   # Si es rebase

# ABORTAR si te arrepientes
git merge --abort
git rebase --abort
```

## 🔙 Recuperar Commits Perdidos
```bash
# 1. Ver historial de HEAD
git reflog

# 2. Volver a commit específico
git reset --hard HEAD@{3}
git cherry-pick abc123  # O traer commit específico
```

## 🧹 Limpiar Repositorio
```bash
# Archivos no tracked
git clean -n            # Preview
git clean -fd           # Ejecutar

# Optimizar repo
git gc                  # Garbage collection
git prune               # Eliminar objetos inaccesibles
```

## 🔐 Cambiar Historial (⚠️ PELIGROSO)

### Modificar Último Commit
```bash
git commit --amend      # Cambiar mensaje o añadir archivos
```

### Rebase Interactivo
```bash
git rebase -i HEAD~3
# Opciones:
# pick   = usar commit
# reword = cambiar mensaje
# edit   = editar commit
# squash = fusionar con anterior
# drop   = eliminar commit
```

### Eliminar Archivo del Historial
```bash
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch archivo-secreto.env" \
  --prune-empty --tag-name-filter cat -- --all
```

## 🆘 Situaciones Comunes

**Commiteé en rama equivocada**:
```bash
git reset HEAD~1        # Deshacer commit (mantener cambios)
git checkout rama-correcta
git add .
git commit -m "mensaje"
```

**Push rechazado (diverged)**:
```bash
git pull --rebase       # Mejor que merge
git push
```

**Perdí cambios después de reset**:
```bash
git reflog
git reset --hard HEAD@{n}
```

---

**⚠️ NUNCA en commits públicos**:
- `git reset --hard`
- `git push --force`
- `git rebase` (de commits pusheados)
- `git filter-branch`

**✅ SEGURO para compartido**:
- `git revert`
- `git merge`
- `git push --force-with-lease` (con cuidado)
