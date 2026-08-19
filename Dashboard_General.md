---
tipo: dashboard-general
created: 2025-11-19
---

# 📊 Control de Estudio

## 🎯 Vista Global de Areas
```dataviewjs
// Agrupa notas por `area` y muestra estado, hito importante y contador de notas
const pages = dv.pages('').filter(p => p.area);
const areas = {};
for (const p of pages) {
  const a = p.area;
  if (!a) continue;
  if (!areas[a]) areas[a] = {count: 0, hito: null, estado: null};
  areas[a].count += 1;
  if (p['hito-importante']) areas[a].hito = p['hito-importante'];
  if (p.estado) areas[a].estado = p.estado;
}
dv.table(["Area","Estado","🎯 Próximo Hito","Notas"], Object.entries(areas).map(([k,v]) => [k, v.estado || "", v.hito || "", v.count]));
```

## 🔴 URGENTE: Temas para HOY
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  area as "📚 Area",
  nivel-comprension as "Nivel",
  tiempo-repaso as "⏱️"
FROM ""
WHERE contains(list("tecnica", "nota_estudio", "captura_rapida"), tipo_nota)
  AND area
  AND proxima-revision <= date(today)
SORT area ASC
```

## 🟡 Esta semana (próximos 7 días)
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  area as "Area",
  proxima-revision as "📅 Fecha",
  nivel-comprension as "Nivel"
FROM ""
WHERE contains(list("tecnica", "nota_estudio", "captura_rapida"), tipo_nota)
  AND area
  AND proxima-revision
  AND proxima-revision > date(today)
  AND proxima-revision <= date(today) + dur(7 days)
SORT proxima-revision ASC
```

## 📚 Notas completas (listas para estudiar)
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  area as "Area",
  status as "Estado",
  nivel-comprension as "Nivel",
  proxima-revision as "📅 Revisar"
FROM ""
WHERE contains(list("tecnica", "nota_estudio", "captura_rapida"), tipo_nota)
  AND area
  AND nivel-comprension
  AND proxima-revision
SORT proxima-revision ASC
```

## ⚠️ Notas incompletas (necesitan actualizar)
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  status as "Estado",
  choice(area, "✅", "❌ Falta") as "Area",
  choice(nivel-comprension, "✅", "❌ Falta") as "Nivel",
  choice(proxima-revision, "✅", "❌ Falta") as "Próxima revisión"
FROM ""
WHERE contains(list("tecnica", "nota_estudio", "captura_rapida"), tipo_nota)
  AND (!area OR !nivel-comprension OR !proxima-revision)
```

## 📊 Estadísticas

- **Total notas técnicas**: `$= dv.pages('""').where(p => ["tecnica", "nota_estudio", "captura_rapida"].includes(p.tipo_nota)).length`
- **Notas completas**: `$= dv.pages('""').where(p => ["tecnica", "nota_estudio", "captura_rapida"].includes(p.tipo_nota) && p.area && p["nivel-comprension"] && p["proxima-revision"]).length`
- **Notas incompletas**: `$= dv.pages('""').where(p => ["tecnica", "nota_estudio", "captura_rapida"].includes(p.tipo_nota) && (!p.area || !p["nivel-comprension"] || !p["proxima-revision"])).length`
- **Temas dominados (✅/🎯)**: `$= dv.pages('""').where(p => p["nivel-comprension"] == "✅" || p["nivel-comprension"] == "🎯").length`
- **En progreso (💡)**: `$= dv.pages('""').where(p => p["nivel-comprension"] == "💡").length`
- **Necesitan atención (❓/🤔)**: `$= dv.pages('""').where(p => p["nivel-comprension"] == "❓" || p["nivel-comprension"] == "🤔").length`

---

## 🗓️ Por Area (ejemplos)

### Ejemplo de Area 1
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  status as "Estado",
  nivel-comprension as "Nivel",
  proxima-revision as "Revisar"
FROM ""
WHERE contains(list("tecnica", "nota_estudio", "captura_rapida"), tipo_nota) 
  AND area = "Ejemplo1"
SORT proxima-revision ASC
```

### Ejemplo de Area 2
```dataview
LIST
FROM ""
WHERE contains(list("tecnica", "nota_estudio", "captura_rapida"), tipo_nota) AND area = "Ejemplo2"
```

---


---


