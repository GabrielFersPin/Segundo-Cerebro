# 🏷️ Tags (Etiquetas)

## ➕ Crear Tags

### Tag Ligero
```bash
git tag v1.0.0
# Solo un puntero al commit
```

### Tag Anotado (Recomendado)
```bash
git tag -a v1.0.0 -m "Version 1.0.0 - Primera release"
# Objeto completo: autor, fecha, mensaje
```

### Tag en Commit Específico
```bash
git tag -a v0.9.0 abc123 -m "Version beta"
```

## 👁️ Ver Tags

```bash
git tag                  # Listar todos
git tag -l "v1.8.5*"     # Buscar por patrón
git show v1.0.0          # Ver detalles del tag
git describe             # Tag más cercano
```

## ⬆️ Compartir Tags

```bash
git push origin v1.0.0       # Push tag específico
git push origin --tags       # Todos los tags
git push --follow-tags       # Solo tags alcanzables
```

## 🗑️ Eliminar Tags

```bash
# Local
git tag -d v1.0.0

# Remoto
git push --delete origin v1.0.0
git push origin :refs/tags/v1.0.0  # Forma antigua
```

## 🎯 Casos de Uso

### Semantic Versioning
```bash
# MAJOR.MINOR.PATCH
git tag -a v1.0.0 -m "Initial release"
git tag -a v1.1.0 -m "New features"
git tag -a v1.1.1 -m "Bug fixes"
git tag -a v2.0.0 -m "Breaking changes"
```

### Release Process
```bash
# 1. Completar desarrollo
git checkout main
git merge --no-ff release/v1.2.0

# 2. Crear tag
git tag -a v1.2.0 -m "Version 1.2.0
- Feature A
- Feature B
- Bug fixes"

# 3. Push
git push origin main --tags

# 4. Crear release en GitHub
# (puede hacerse automático con GitHub Actions)
```

### Checkout por Tag
```bash
git checkout v1.0.0      # Ver código de esa versión
git checkout -b hotfix-1.0 v1.0.0  # Crear rama desde tag
```

## 📋 Convenciones

**Semantic Versioning (SemVer)**:
- `MAJOR`: Cambios incompatibles en API
- `MINOR`: Funcionalidad nueva compatible
- `PATCH`: Bug fixes compatibles

**Ejemplos**:
- `v1.0.0`: Primera release estable
- `v1.1.0`: Nuevas features
- `v1.1.1`: Hotfix
- `v2.0.0`: Breaking changes

**Pre-releases**:
- `v1.0.0-alpha`
- `v1.0.0-beta.1`
- `v1.0.0-rc.1` (release candidate)

---

**Diferencias**:
- **Tag ligero**: Solo puntero (como branch que no cambia)
- **Tag anotado**: Objeto completo con metadata (recomendado para releases)

**Tip**: Siempre usa tags anotados para releases públicos
