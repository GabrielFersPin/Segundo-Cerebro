# 🟣 Remoto & Colaboración

## ⬇️ Obtener Cambios

### Fetch (traer sin fusionar)
```bash
git fetch origin         # Actualizar referencias
git fetch origin <rama>  # Rama específica
```

### Pull (traer y fusionar)
```bash
git pull origin <rama>
git pull                 # Rama actual
git pull --rebase        # Fetch + rebase en vez de merge
```

**Pull = Fetch + Merge**

## ⬆️ Enviar Cambios

```bash
git push origin <rama>
git push -u origin <rama>  # Primera vez (set upstream)
git push                   # Siguientes veces

# Peligrosos ⚠️
git push --force           # Sobreescribir remoto
git push --force-with-lease # Más seguro que --force
```

## Eliminar Rama Remota
```bash
git push --delete origin <rama>
git push origin :<rama>     # Forma antigua
```

## 🔍 Inspeccionar Remoto
```bash
git remote -v               # Ver URLs
git remote show origin      # Info detallada
git ls-remote origin        # Referencias remotas
```

## 📊 Estado de Ramas
```bash
git branch -vv              # Ver tracking branches
git fetch --prune           # Limpiar referencias obsoletas
```

---

**Workflow típico**:
1. `git fetch` → ver cambios
2. `git pull` → traer e integrar
3. `git push` → compartir trabajo

**Regla**: Siempre pull antes de push
