---
tipo: dashboard-asignatura
asignatura: Algoritmos
estado: 🟡 Atrasado
proxima-clase: 2025-11-20
examen: 2026-02-06
profesor: Ivan
created: 2025-11-20
---

# 📚 Algoritmo

## 📊 Estado actual

**Estado general**: 🔴 Crítico
**Próximo examen**: 2026-02-06 (en `$= Math.ceil((new Date("2026-02-06") - new Date()) / (1000 * 60 * 60 * 24))` días)
**Profesor**: Ivan

**Estadísticas rápidas**:
- 🔴 Críticos (❓/🤔): `$= dv.pages('""').where(p => p.tipo_nota == "tecnica" && p.asignatura == "Algoritmos" && (p["nivel-comprension"] == "❓" || p["nivel-comprension"] == "🤔")).length`
- 🟡 En progreso (💡): `$= dv.pages('""').where(p => p.tipo_nota == "tecnica" && p.asignatura == "Algoritmos" && p["nivel-comprension"] == "💡").length`
- 🟢 Dominados (✅/🎯): `$= dv.pages('""').where(p => p.tipo_nota == "tecnica" && p.asignatura == "Algoritmos" && (p["nivel-comprension"] == "✅" || p["nivel-comprension"] == "🎯")).length`

---

## 📋 Por urgencia de tiempo

### 🔴 REVISAR HOY

> [!danger]- 🚨 Vence hoy o ya pasó
```dataview
TABLE WITHOUT ID
  ("🔴 " + file.link) as "Tema",
  nivel-comprension as "Nivel",
  proxima-revision as "📅 Vence",
  tiempo-repaso as "⏱️"
FROM ""
WHERE tipo_nota = "tecnica"
  AND asignatura = "Algoritmos"
  AND proxima-revision <= date(today)
SORT proxima-revision ASC
```

---

### 🟠 ESTA SEMANA

> [!warning]- ⚠️ Próximos 7 días
```dataview
TABLE WITHOUT ID
  ("🟠 " + file.link) as "Tema",
  nivel-comprension as "Nivel",
  proxima-revision as "📅 Revisar",
  tiempo-repaso as "⏱️"
FROM ""
WHERE tipo_nota = "tecnica"
  AND asignatura = "Algoritmos"
  AND proxima-revision > date(today)
  AND proxima-revision <= date(today) + dur(7 days)
SORT proxima-revision ASC
```

---

## 📋 Por nivel de comprensión

### ❓🤔 NECESITAN ATENCIÓN

> [!danger]- 🔴 No entiendo / Entiendo parcialmente
```dataview
TABLE WITHOUT ID
  ("🔴 " + file.link) as "Tema",
  nivel-comprension as "Nivel",
  proxima-revision as "📅 Revisar",
  tiempo-repaso as "⏱️"
FROM ""
WHERE tipo_nota = "tecnica"
  AND asignatura = "Algoritmos"
  AND (nivel-comprension = "❓" OR nivel-comprension = "🤔")
SORT proxima-revision ASC
```

---

### 💡 EN PROGRESO

> [!warning]- 🟡 Entiendo bien
```dataview
TABLE WITHOUT ID
  ("🟡 " + file.link) as "Tema",
  proxima-revision as "📅 Revisar",
  tiempo-repaso as "⏱️"
FROM ""
WHERE tipo_nota = "tecnica"
  AND asignatura = "Algoritmos"
  AND nivel-comprension = "💡"
SORT proxima-revision ASC
```

---

### ✅🎯 DOMINADOS

> [!success]- 🟢 Domino / Puedo enseñar
```dataview
TABLE WITHOUT ID
  ("🟢 " + file.link) as "Tema",
  nivel-comprension as "Nivel",
  veces-revisado as "Repasos",
  ultima-revision as "Última vez"
FROM ""
WHERE tipo_nota = "tecnica"
  AND asignatura = "Algoritmos"
  AND (nivel-comprension = "✅" OR nivel-comprension = "🎯")
SORT veces-revisado DESC
```

---

### 📚 TODAS

> [!info]- 📖 Vista completa
```dataview
TABLE WITHOUT ID
  choice(
    nivel-comprension = "❓" OR nivel-comprension = "🤔", "🔴 ",
    choice(nivel-comprension = "💡", "🟡 ",
    choice(nivel-comprension = "✅" OR nivel-comprension = "🎯", "🟢 ", "⚪ "))
  ) + file.link as "Tema",
  status as "Estado",
  nivel-comprension as "Nivel",
  proxima-revision as "📅 Revisar"
FROM ""
WHERE tipo_nota = "tecnica"
  AND asignatura = "Algoritmos"
SORT proxima-revision ASC
```

---

## 🎯 Objetivos para el próximo examen

- [ ] Repasar todos los temas 🔴
- [ ] Subir temas 🤔 a 💡
- [ ] Hacer ejercicios prácticos
- [ ] Revisar flashcards 2 veces

---

## 🗓️ Calendario de clases

| Fecha | Tema | Asistencia | Notas |
|-------|------|------------|-------|
|  |  |  |  |

---

## 💭 Notas

**Puntos fuertes**: 
**Puntos débiles**: 
**Estrategia**: 

---

> [!tip] 💡 Leyenda
> - 🔴 Hoy = Revisar urgente
> - 🟠 Esta semana = Próximos 7 días
> - 🟡 En progreso = Entiendo pero necesito refuerzo
> - 🟢 Dominado = Solo mantenimiento