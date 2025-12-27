# 🟡 Stash (Guardar Temporal)

## 💾 Guardar
```bash
git stash                # Guardar cambios
git stash save "mensaje" # Con descripción
```

## 👁️ Ver Stashes
```bash
git stash list
# Resultado:
# stash@{0}: WIP on main: abc123 mensaje
# stash@{1}: On feature: xyz789 otro mensaje
```

## 🔄 Recuperar
```bash
git stash pop            # Aplica último y elimina
git stash apply          # Aplica pero mantiene
git stash apply stash@{2} # Recuperar específico
```

## 🗑️ Eliminar
```bash
git stash drop stash@{1} # Eliminar específico
git stash clear          # Eliminar todos
```

## 🎯 Casos de Uso

**Cambiar de rama urgente**:
```bash
git stash
git checkout hotfix
# ... arreglar bug ...
git checkout feature
git stash pop
```

**Probar algo sin commit**:
```bash
git stash
# ... experimento ...
git stash pop  # volver a estado anterior
```

**Limpiar working directory**:
```bash
git stash
# working directory limpio para pull/merge
```

---

**Tip**: Stash también guarda archivos no staged  
**Truco**: `git stash show -p` para ver contenido del stash
