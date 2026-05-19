---
created: <% tp.date.now("YYYY-MM-DD HH:mm") %>
modified: <% tp.date.now("YYYY-MM-DD HH:mm") %>
area: <% await tp.system.prompt("📚 Área/Tema (ej: ML, Estadística, Deep Learning):") %>
tipo_nota: nota_estudio
status: 🔴
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
cards-deck: <% await tp.system.prompt("🎴 Mazo para Flashcards:") %>
tags: [nota_estudio, <% tp.date.now("YYYY-MM-DD") %>]
---

# 📝 <% await tp.system.prompt("📚 Área:") %> - <% await tp.system.prompt("📌 Tema de la sesión:") %>

> [!info] Metadata de la nota
> **Fecha**: <% tp.date.now("YYYY-MM-DD") %>
> **Hora**: <% tp.date.now("HH:mm") %>
> **Estado**: 🔴 En vivo | 🟡 Por procesar | 🟢 Procesada

---

## 🎯 Objetivo de la sesión

<%* 
const objetivo = await tp.system.prompt("🎯 ¿Cuál es el objetivo principal de esta sesión de estudio? (opcional - presiona Enter para omitir):", "");
if (objetivo) {
    tR += objetivo;
} else {
    tR += `_[A completar durante o después de la clase]_`;
}
_%>

---

## 📊 Captura Rápida

<%*
// Sistema de captura rápida durante la sesión
tR += `> 💡 **Modo captura rápida**: Usa los atajos para agregar contenido sin interrumpir el flujo\n\n`;

// Crear secciones vacías para captura rápida
tR += `### ⚡ Notas Rápidas\n`;
tR += `<!-- Escribe aquí cualquier cosa que necesites capturar rápidamente -->\n\n`;
tR += `- \n\n`;

tR += `### 🔑 Conceptos Clave\n`;
tR += `<!-- Marca con ** los conceptos importantes -->\n\n`;
tR += `- \n\n`;

tR += `### ❓ Dudas\n`;
tR += `<!-- Preguntas que surjan durante el estudio -->\n\n`;
tR += `- [ ] \n\n`;

tR += `### 💡 Insights\n`;
tR += `<!-- Conexiones o ideas que se te ocurran -->\n\n`;
tR += `- \n\n`;

tR += `### ⚠️ Importante\n`;
tR += `<!-- Información crítica para exámenes o proyectos -->\n\n`;
tR += `- \n\n`;

tR += `### 📚 Referencias Mencionadas\n`;
tR += `<!-- Papers, libros, recursos -->\n\n`;
tR += `- \n\n`;
_%>

---

## 📝 Notas Detalladas

<%*
// Sección para desarrollo posterior o si hay tiempo durante la sesión
tR += `<!-- Desarrolla aquí los conceptos con más detalle cuando tengas tiempo -->\n\n`;

const iniciarDetalle = await tp.system.suggester(
    ["➕ Agregar sección detallada ahora", "⏭️ Dejar para después de la sesión"],
    ["si", "no"]
);

if (iniciarDetalle === "si") {
    let agregarMas = true;
    let contador = 1;
    
    while (agregarMas) {
        const tipoContenido = await tp.system.suggester(
            [`[${contador}] 📐 Teorema/Definición`,
             `[${contador}] 🧮 Fórmula/Ecuación`,
             `[${contador}] 💻 Código/Algoritmo`,
             `[${contador}] 📊 Ejemplo/Caso`,
             `[${contador}] 🔄 Proceso/Método`,
             "✅ Terminar"],
            ["teorema", "formula", "codigo", "ejemplo", "proceso", "terminar"]
        );
        
        if (tipoContenido === "terminar") break;
        
        if (tipoContenido === "teorema") {
            const nombre = await tp.system.prompt(`[${contador}] Nombre del teorema/definición:`);
            const descripcion = await tp.system.prompt(`Descripción breve:`);
            
            tR += `### 📐 ${nombre}\n\n`;
            tR += `${descripcion}\n\n`;
            
        } else if (tipoContenido === "formula") {
            const nombre = await tp.system.prompt(`[${contador}] Nombre de la fórmula:`);
            const formula = await tp.system.prompt(`Fórmula en LaTeX:`);
            
            tR += `### 🧮 ${nombre}\n\n`;
            tR += `$$${formula}$$\n\n`;
            
        } else if (tipoContenido === "codigo") {
            const descripcion = await tp.system.prompt(`[${contador}] ¿Qué hace este código?:`);
            const lenguaje = await tp.system.prompt(`Lenguaje:`, "python");
            const codigo = await tp.system.prompt(`Código:`);
            
            tR += `### 💻 ${descripcion}\n\n`;
            tR += "```" + lenguaje + "\n";
            tR += codigo + "\n";
            tR += "```\n\n";
            
        } else if (tipoContenido === "ejemplo") {
            const titulo = await tp.system.prompt(`[${contador}] Título del ejemplo:`);
            const ejemplo = await tp.system.prompt(`Describe el ejemplo:`);
            
            tR += `### 📊 Ejemplo: ${titulo}\n\n`;
            tR += `${ejemplo}\n\n`;
            
        } else if (tipoContenido === "proceso") {
            const nombre = await tp.system.prompt(`[${contador}] Nombre del proceso:`);
            const numPasos = await tp.system.prompt(`¿Cuántos pasos tiene?`, "3");
            
            tR += `### 🔄 ${nombre}\n\n`;
            
            for (let i = 1; i <= parseInt(numPasos); i++) {
                const paso = await tp.system.prompt(`Paso ${i}:`);
                tR += `${i}. ${paso}\n`;
            }
            tR += `\n`;
        }
        
        contador++;
        
        const continuar = await tp.system.suggester(
            ["➕ Agregar más contenido", "✅ Terminar"],
            ["si", "no"]
        );
        if (continuar === "no") break;
    }
} else {
    tR += `_[Sección para desarrollar después de la sesión]_\n`;
}
_%>

---

## 🔄 Procesamiento Post-Sesión

### 📋 Checklist de Procesamiento
- [ ] Revisar y organizar notas rápidas
- [ ] Clarificar conceptos confusos
- [ ] Resolver dudas pendientes
- [ ] Crear notas atómicas de conceptos clave
- [ ] Generar flashcards de lo importante
- [ ] Conectar con conocimiento previo
- [ ] Identificar gaps de conocimiento
- [ ] Planificar repaso con Active Recall

### 🎯 Acciones Prioritarias
<%*
tR += `<!-- Identifica 3 acciones clave después de la sesión -->\n`;
tR += `1. \n`;
tR += `2. \n`;
tR += `3. \n\n`;
_%>

### 🔗 Conexiones con otras notas
<%*
tR += `<!-- Enlaces a notas relacionadas -->\n`;
tR += `- Conceptos previos: \n`;
tR += `- Temas relacionados: \n`;
tR += `- Aplicaciones: \n\n`;
_%>

---

## 🎴 Flashcards Rápidas

<%*
const crearFlashcardsAhora = await tp.system.suggester(
    ["🎴 Crear flashcards ahora", "⏭️ Crear después"],
    ["si", "no"]
);

if (crearFlashcardsAhora === "si") {
    tR += `> 💡 **Tip**: Crea flashcards de los conceptos más importantes mientras están frescos\n\n`;
    
    let timestampBase = Date.now();
    let numFlashcards = await tp.system.prompt("¿Cuántas flashcards quieres crear?", "3");
    
    for (let i = 1; i <= parseInt(numFlashcards); i++) {
        const pregunta = await tp.system.prompt(`[${i}] Pregunta:`);
        if (!pregunta) break;
        
        const respuesta = await tp.system.prompt(`Respuesta:`);
        const idUnico = `${timestampBase}-${i}`;
        
        tR += `START\n`;
        tR += `Basic\n`;
        tR += `${pregunta}\n`;
        tR += `Back: ${respuesta}\n`;
        tR += `Tags: nota_estudio, ${tp.frontmatter.deck.split("::")[1]}\n`;
        tR += `<!--ID: ${idUnico}-->\n`;
        tR += `END\n\n`;
    }
} else {
    tR += `_[Flashcards pendientes - Crear después del procesamiento]_\n\n`;
}
_%>

---

## 📊 Resumen y Takeaways

### 🎯 Los 3 puntos clave
1. 
2. 
3. 

### 💭 Reflexión personal
_¿Qué es lo más importante/útil/interesante de esta sesión?_

### 🔮 Aplicaciones futuras
_¿Dónde y cómo puedo aplicar este conocimiento?_

---

## 📈 Métricas de Estudio

<%*
const comprension = await tp.system.suggester(
    ["😵 No entendí nada", "🤔 Entendí poco", "👍 Entendí bastante", "💪 Entendí todo", "🚀 Podría explicarlo"],
    ["0%", "25%", "50%", "75%", "100%"]
);

const importancia = await tp.system.suggester(
    ["⭐ Poco importante", "⭐⭐ Algo importante", "⭐⭐⭐ Importante", "⭐⭐⭐⭐ Muy importante", "⭐⭐⭐⭐⭐ Crítico"],
    ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"]
);

const dificultad = await tp.system.suggester(
    ["🟢 Fácil", "🟡 Medio", "🟠 Difícil", "🔴 Muy difícil"],
    ["🟢", "🟡", "🟠", "🔴"]
);

tR += `- **Comprensión inicial**: ${comprension}\n`;
tR += `- **Importancia global**: ${importancia}\n`;
tR += `- **Dificultad percibida**: ${dificultad}\n`;
tR += `- **Tiempo estimado de estudio**: \n`;
tR += `- **Próxima revisión**: ${tp.date.now("YYYY-MM-DD", 2)}\n`;
_%>

---

## 🏷️ Tags Semánticos

<%*
// Sistema de tags para mejor organización
const tags = await tp.system.prompt("Tags adicionales (separados por coma):", "");
if (tags) {
    const tagList = tags.split(',').map(t => `#${t.trim()}`).join(' ');
    tR += `${tagList}\n`;
} else {
    tR += `#pendiente_procesar\n`;
}
_%>

---

> [!tip] 💡 Flujo de trabajo recomendado
> 1. **Durante la sesión**: Usa la sección de Captura Rápida
> 2. **Justo después**: Completa dudas y conexiones mientras está fresco
> 3. **Mismo día**: Procesa las notas, crea flashcards
> 4. **24-48h después**: Primera revisión con Active Recall
> 5. **Semanal**: Integra con tu sistema Zettelkasten

> [!warning] ⏰ Recordatorio
> Procesa estas notas en las próximas 24 horas para máxima retención