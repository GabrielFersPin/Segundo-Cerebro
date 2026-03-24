# 🔍 Inspección & Búsqueda

## 📜 Historial Detallado
```bash
git log --oneline --graph --all
git log --since="2 weeks ago"
git log --author="Gabriel"
git log -- <archivo>      # Historial de archivo
git log -p                # Con diffs
```

## 🔬 Reflog (Recuperación)
```bash
git reflog
# Muestra TODO lo que ha pasado con HEAD
# Útil para recuperar commits "perdidos"

git reset --hard HEAD@{3}  # Volver a estado anterior
```

## 👤 Blame (Quién modificó)
```bash
git blame <archivo>
git blame -L 10,20 <archivo>  # Solo líneas 10-20
git blame -C <archivo>        # Detectar código movido
```

## 🔎 Buscar en Código
```bash
git grep "función"        # En working directory
git grep "función" HEAD~3 # En commit específico
git grep -n "función"     # Con números de línea
git grep --count "TODO"   # Contar ocurrencias
```

## 📊 Comparar
```bash
git diff <commit1> <commit2>
git diff main feature
git diff --stat           # Resumen de cambios
git show <commit>         # Ver commit específico
```

## 🔬 Bisect (Encontrar Bug)
```bash
git bisect start
git bisect bad            # Commit actual está malo
git bisect good <commit>  # Commit que funcionaba
# Git irá probando commits
git bisect good/bad       # Marcar cada uno
git bisect reset          # Terminar búsqueda
```

---

**Más útiles**:
- `reflog`: Recuperar trabajo perdido
- `blame`: Ver contexto de cambios
- `grep`: Buscar patrones en código
- `bisect`: Debugging histórico
