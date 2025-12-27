# 🟢 Trabajo Diario Local

## 📊 Ver Estado
```bash
git status               # Estado completo
git status -s            # Formato corto
```

## ➕ Staging Area
```bash
git add .                # Todos los cambios
git add <archivo>        # Archivo específico
git add *.py             # Por patrón
git add -p               # Interactivo (chunks)
```

## Quitar del Staging
```bash
git restore --staged <archivo>
git reset HEAD <archivo>  # Forma antigua
```

## 💾 Commits
```bash
git commit -m "mensaje"
git commit -am "mensaje"  # add + commit (tracked)
git commit --amend        # Modificar último commit
```

## 🔍 Ver Historial
```bash
git log                  # Historial completo
git log --oneline        # Una línea por commit
git log --graph --all    # Con gráfico de ramas
git log -5               # Últimos 5 commits
git log --author="nombre"
```

## Ver Diferencias
```bash
git diff                 # Working vs Staging
git diff --staged        # Staging vs último commit
git diff HEAD~2 HEAD     # Entre commits
```

---

**Usar**: Todos los días  
**Frecuencia**: Múltiples veces por sesión  
**Flujo típico**: `status → add → commit`
