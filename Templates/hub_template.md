---
cards-deck: <% await tp.system.prompt("🎴 Mazo (ej: Nube, Algoritmos, DataScience, Arquitectura):") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
tipo_nota: hub
status: 🗂️
---

# 🗂️ <% await tp.system.prompt("📌 Título del Hub (ej: CPU - Índice General):") %>

> [!info] Propósito del Hub
> <% await tp.system.prompt("🎯 ¿Qué organiza este hub? (ej: Organiza todas las notas sobre CPU y su arquitectura)") %>

---

## 🎓 Contexto Académico

<%* 
const asignatura = await tp.system.suggester(
    ["Algoritmos", "Arquitectura", "Infraestructura Nube", "Fundamentos DS", "Otro (escribir)"],
    ["Algoritmos", "Arquitectura", "Infraestructura-Nube", "Fundamentos-DS", "custom"]
);

let asignaturaFinal;
if (asignatura === "custom") {
    asignaturaFinal = await tp.system.prompt("📚 Nombre de la asignatura:");
} else {
    asignaturaFinal = asignatura;
}

tR += `**Asignatura**: ${asignaturaFinal}\n`;

const unidad = await tp.system.prompt("📖 Unidad/Tema (ej: UD2 - Estructura CPU, opcional):", "");
if (unidad) {
    tR += `**Unidad**: ${unidad}\n`;
}

const fechaExamen = await tp.system.prompt("📅 Fecha de examen/entrega (YYYY-MM-DD, opcional):", "");
if (fechaExamen) {
    tR += `**Fecha relevante**: ${fechaExamen}\n`;
}

const importancia = await tp.system.suggester(
    ["⭐⭐⭐⭐⭐ Crítico (muy preguntable)", "⭐⭐⭐⭐☆ Importante", "⭐⭐⭐☆☆ Normal", "⭐⭐☆☆☆ Complementario", "⏭️ Omitir"],
    ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐☆", "⭐⭐⭐☆☆", "⭐⭐☆☆☆", ""]
);

if (importancia) {
    tR += `**Importancia para examen**: ${importancia}\n`;
}
_%>

---

## 🗺️ Mapa Conceptual

<%*
const verMapa = await tp.system.suggester(
    ["✅ Crear estructura de notas ahora", "⏭️ Crear estructura después"],
    ["si", "no"]
);

if (verMapa === "si") {
    tR += `\n> [!tip] Orden de Estudio Recomendado\n`;
    tR += `> Las notas están numeradas en el orden sugerido de lectura\n\n`;
    
    let agregarNota = true;
    let contador = 1;
    
    while (agregarNota) {
        const titulo = await tp.system.prompt(`[${contador}] 📝 Título de la nota (vacío para terminar):`);
        if (!titulo) break;
        
        const slug = titulo
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
            .replace(/[^\w\s-]/g, "")
            .replace(/\s+/g, "-");
        
        const tipoNota = await tp.system.suggester(
            ["📘 Concepto fundamental", "🔧 Técnica/Procedimiento", "📊 Comparativa", "💡 Ejemplo aplicado", "🔗 Conexión/Síntesis"],
            ["📘", "🔧", "📊", "💡", "🔗"]
        );
        
        const descripcion = await tp.system.prompt(`   Descripción breve (1 línea):`);
        
        const tiempo = await tp.system.suggester(
            ["⚡ 5-10 min", "📖 15-20 min", "📚 30-40 min", "🔬 +1 hora"],
            ["5-10min", "15-20min", "30-40min", "+1h"]
        );
        
        const prioridad = await tp.system.suggester(
            ["🔴 Alta (estudiar primero)", "🟡 Media", "🟢 Baja (opcional)"],
            ["🔴", "🟡", "🟢"]
        );
        
        tR += `### ${contador}. ${tipoNota} [[${slug}|${titulo}]]\n`;
        tR += `- **Descripción**: ${descripcion}\n`;
        tR += `- **Tiempo estimado**: ${tiempo}\n`;
        tR += `- **Prioridad**: ${prioridad}\n`;
        tR += `- **Estado**: [ ] Pendiente\n\n`;
        
        contador++;
        
        if (contador > 10) {
            const continuar = await tp.system.suggester(
                ["✅ Continuar agregando", "⏹️ Terminar aquí"],
                ["si", "no"]
            );
            if (continuar === "no") break;
        }
    }
    
    if (contador > 1) {
        tR += `---\n\n`;
        tR += `**📊 Total de notas planeadas**: ${contador - 1}\n\n`;
    }
} else {
    tR += `\n### Notas del tema\n`;
    tR += `_Pendiente de estructurar_\n\n`;
    tR += `> 💡 **Sugerencia**: Usa el formato:\n`;
    tR += `> - [[nota-1]] - Descripción breve\n`;
    tR += `> - [[nota-2]] - Descripción breve\n\n`;
}
_%>

---

## 🎯 Objetivos de Aprendizaje

<%*
const crearObjetivos = await tp.system.suggester(
    ["✅ Definir objetivos ahora", "⏭️ Agregar después"],
    ["si", "no"]
);

if (crearObjetivos === "si") {
    tR += `\n> [!success] Al completar este tema, deberías ser capaz de:\n\n`;
    
    let numObjetivos = await tp.system.prompt("¿Cuántos objetivos de aprendizaje? (3-5 recomendado)", "4");
    numObjetivos = parseInt(numObjetivos) || 4;
    
    for (let i = 1; i <= numObjetivos; i++) {
        const objetivo = await tp.system.prompt(`[${i}/${numObjetivos}] Objetivo:`);
        tR += `- [ ] ${objetivo}\n`;
    }
    tR += `\n`;
} else {
    tR += `\n_Objetivos pendientes de definir_\n\n`;
}
_%>

---

## 🔗 Conexiones Importantes

<%*
const agregarConexiones = await tp.system.suggester(
    ["✅ Agregar conexiones ahora", "⏭️ Agregar después"],
    ["si", "no"]
);

if (agregarConexiones === "si") {
    tR += `\n### Con otros temas\n`;
    const otrosTemas = await tp.system.prompt("Temas relacionados (separados por comas, ej: Memoria, Buses, SO):", "");
    if (otrosTemas) {
        const temas = otrosTemas.split(',').map(t => t.trim());
        temas.forEach(tema => {
            tR += `- [[${tema}]] - `;
            const relacion = tp.system.prompt(`¿Cómo se relaciona con "${tema}"?`, "");
            tR += `${relacion}\n`;
        });
    }
    
    tR += `\n### Con proyectos/aplicaciones\n`;
    const proyectos = await tp.system.prompt("¿Se relaciona con algún proyecto tuyo? (ej: App RPG, Sistema recomendación):", "");
    if (proyectos) {
        tR += `- ${proyectos}\n`;
    }
    tR += `\n`;
} else {
    tR += `\n**Con otros temas**: _Pendiente_\n`;
    tR += `**Con proyectos**: _Pendiente_\n\n`;
}
_%>

---

## 📚 Recursos & Referencias

<%*
const fuente = await tp.system.prompt("📖 Fuente principal (ej: PDF UD2, Libro capítulo 3):", "");
if (fuente) {
    tR += `**Fuente principal**: ${fuente}\n`;
}

const recursosExtra = await tp.system.prompt("🔗 Recursos adicionales (URLs, vídeos, separados por comas, opcional):", "");
if (recursosExtra) {
    const recursos = recursosExtra.split(',').map(r => r.trim());
    tR += `\n**Recursos adicionales**:\n`;
    recursos.forEach(rec => {
        tR += `- ${rec}\n`;
    });
}

tR += `\n`;
_%>

---

## 📊 Progreso del Tema

<%*
await app.fileManager.processFrontMatter(tp.config.target_file, (fm) => {
    fm.asignatura = asignaturaFinal;
    fm["total-notas"] = 0;
    fm["notas-completadas"] = 0;
    fm["progreso"] = "0%";
    fm["ultima-revision"] = tp.date.now("YYYY-MM-DD");
});
_%>

- **Notas creadas**: 0 / 0
- **Progreso**: 0%
- **Última revisión**: <% tp.date.now("YYYY-MM-DD") %>

> [!warning] Recordatorio
> Actualiza este hub cada vez que completes una nota atómica del tema

---

## 📝 Notas Rápidas

<%*
const notasIniciales = await tp.system.prompt("💭 ¿Alguna observación inicial? (opcional):", "");
if (notasIniciales) {
    tR += `\n${notasIniciales}\n\n`;
} else {
    tR += `\n_Espacio para ideas, dudas o insights mientras estudias este tema_\n\n`;
}
_%>

---

## 🎴 Flashcards del Tema

> [!info] Gestión de Flashcards
> Este hub NO contiene flashcards propias.
> Las flashcards están en cada nota atómica individual.
> 
> **Para repasar todo el tema**: 
> - En Obsidian: `Cmd/Ctrl+P` → "Flashcards: Review" → Selecciona el mazo **<% asignaturaFinal %>**

---

<% `<!--` %>
## 🔧 Metadata Técnica

- **Tipo de nota**: Hub/Índice
- **Nivel**: Tema completo
- **Notas vinculadas**: Se actualizan automáticamente con backlinks
- **Template usado**: Template_Hub_Tematico.md
<% `-->` %>
