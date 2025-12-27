# ↩️ Deshacer Cambios

## Descartar Cambios en Working
```bash
git restore <archivo>
git checkout -- <archivo>  # Forma antigua
```

## Quitar del Staging
```bash
git restore --staged <archivo>
```

## Deshacer Commits
```bash
# Opción 1: Reset (local, peligroso)
git reset --soft HEAD~1   # Mantiene staging
git reset --mixed HEAD~1  # Mantiene working dir
git reset --hard HEAD~1   # ⚠️ BORRA TODO

# Opción 2: Revert (público, seguro)
git revert HEAD           # Crea nuevo commit
git revert <commit-hash>
```

## Limpiar No Tracked
```bash
git clean -n              # Preview
git clean -fd             # Ejecutar
```

## ⚠️ Cuándo Usar Cada Uno

**restore**: Cambios locales que no quieres  
**reset**: Commits locales (no pusheados)  
**revert**: Commits ya pusheados (público)  
**clean**: Archivos nuevos no deseados  

---

**Peligro**: 🔴 `reset --hard` y `clean -fd` son destructivos  
**Seguro**: 🟢 `revert` crea nuevo commit, no reescribe
