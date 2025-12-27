---
tipo: dashboard-general
created: 2025-11-19
---

# 📊 Control Académico - Semestre 2024-25

## 🎯 Vista Global de Asignaturas
```dataview
TABLE WITHOUT ID
  file.link as "Asignatura",
  estado as "Estado",
  examen as "🎯 Examen"
FROM ""
WHERE tipo = "dashboard-asignatura"
SORT estado ASC
```

## 🔴 URGENTE: Temas para HOY
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  asignatura as "📚 Asignatura",
  nivel-comprension as "Nivel",
  tiempo-repaso as "⏱️"
FROM ""
WHERE tipo_nota = "tecnica"
  AND asignatura
  AND proxima-revision <= date(today)
SORT asignatura ASC
```

## 🟡 Esta semana (próximos 7 días)
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  asignatura as "Asignatura",
  proxima-revision as "📅 Fecha",
  nivel-comprension as "Nivel"
FROM ""
WHERE tipo_nota = "tecnica"
  AND asignatura
  AND proxima-revision
  AND proxima-revision > date(today)
  AND proxima-revision <= date(today) + dur(7 days)
SORT proxima-revision ASC
```

## 📚 Notas completas (listas para estudiar)
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  asignatura as "Asignatura",
  status as "Estado",
  nivel-comprension as "Nivel",
  proxima-revision as "📅 Revisar"
FROM ""
WHERE tipo_nota = "tecnica"
  AND asignatura
  AND nivel-comprension
  AND proxima-revision
SORT proxima-revision ASC
```

## ⚠️ Notas incompletas (necesitan actualizar)
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  status as "Estado",
  choice(asignatura, "✅", "❌ Falta") as "Asignatura",
  choice(nivel-comprension, "✅", "❌ Falta") as "Nivel",
  choice(proxima-revision, "✅", "❌ Falta") as "Próxima revisión"
FROM ""
WHERE tipo_nota = "tecnica"
  AND (!asignatura OR !nivel-comprension OR !proxima-revision)
```

## 📊 Estadísticas

- **Total notas técnicas**: `$= dv.pages('""').where(p => p.tipo_nota == "tecnica").length`
- **Notas completas**: `$= dv.pages('""').where(p => p.tipo_nota == "tecnica" && p.asignatura && p["nivel-comprension"] && p["proxima-revision"]).length`
- **Notas incompletas**: `$= dv.pages('""').where(p => p.tipo_nota == "tecnica" && (!p.asignatura || !p["nivel-comprension"] || !p["proxima-revision"])).length`
- **Temas dominados (✅/🎯)**: `$= dv.pages('""').where(p => p["nivel-comprension"] == "✅" || p["nivel-comprension"] == "🎯").length`
- **En progreso (💡)**: `$= dv.pages('""').where(p => p["nivel-comprension"] == "💡").length`
- **Necesitan atención (❓/🤔)**: `$= dv.pages('""').where(p => p["nivel-comprension"] == "❓" || p["nivel-comprension"] == "🤔").length`

---

## 🗓️ Por Asignatura (solo completas)

### Algoritmos
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  status as "Estado",
  nivel-comprension as "Nivel",
  proxima-revision as "Revisar"
FROM ""
WHERE tipo_nota = "tecnica" 
  AND asignatura = "Algoritmos"
SORT proxima-revision ASC
```

### Arquitectura
```dataview
LIST
FROM ""
WHERE tipo_nota = "tecnica" AND asignatura = "Arquitectura"
```

### Infraestructura Nube
```dataview
LIST
FROM ""
WHERE tipo_nota = "tecnica" AND asignatura = "Infraestructura-Nube"
```

### Fundamentos DS
```dataview
LIST
FROM ""
WHERE tipo_nota = "tecnica" AND asignatura = "Fundamentos-DS"
```

---


---

