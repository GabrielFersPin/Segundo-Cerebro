```dataview
TABLE WITHOUT ID
  file.link as "Nota Rápida",
  area as "Área/Tema",
  prioridad as "Prioridad",
  origen as "Fuente"
FROM ""
WHERE (tipo_nota = "captura_rapida" OR procesamiento = "CAPTURA-RAPIDA")
  AND (status = "🔴 Por procesar" OR nivel-comprension = "❓")
SORT prioridad ASC, file.ctime DESC
```
