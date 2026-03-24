# 📈 Mi Dashboard Financiero

> *"Toda la información del patrimonio y seguimiento de gastos centralizada"*

---

## 📅 Meses Activos

Aquí aparecerán todas tus notas mensuales creadas con la `Plantilla_Finanzas_Personales`.

```dataview
TABLE 
  mes as "Mes",
  rows as "Notas"
FROM "Templates" OR ""
WHERE tags >= "finanzas" AND tags >= "mensual" AND !contains(file.name, "Plantilla")
SORT mes DESC
```

---

## 🎯 Metas y Objetivos (Status Global)

```dataview
TABLE WITHOUT ID
  file.link as "Plan / Meta",
  Estado as "Estado actual"
FROM ""
WHERE tags >= "finanzas" AND tags >= "objetivos"
```

---

## 🏛️ Accesos Rápidos

- [[Planes y Seguimiento Financiero]]: La nota maestra con los detalles de tus metas (Monovolumen, Inmuebles, SRI).
- [[Ideas y Tareas]]: Tu Kanban con las tareas pendientes de finanzas.

## 📊 Balance Automatizado

*(Próximamente: Posibilidad de script en Python para actualizar gráficas aquí)*

---

## 💡 Ideas y Notas Rápidas de Inversión

- **Explorar plataformas ESG:** [Triodos](https://www.triodos.es/), [Fiare](https://www.fiarebancaetica.coop/), [Fundeen](https://www.fundeen.com/)
- *Añade aquí cualquier idea, artículo o pódcast interesante que quieras revisar más tarde...*
-
