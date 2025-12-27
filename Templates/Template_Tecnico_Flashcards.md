---
cards-deck: <% await tp.system.prompt("🎴 Mazo (ej: Nube, Algoritmos, DataScience, Arquitectura):") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
status: 🌱
tipo_nota: ""
---

# <% await tp.system.prompt("📌 Título del concepto:") %>

> [!abstract] Objetivo
> <% await tp.system.prompt("🎯 ¿Qué quieres lograr con esta nota?") %>

---

<%* 
const tipoNota = await tp.system.suggester(
    ["🔬 Técnica/Científica", "📚 Filosofía/Lectura", "💡 Idea Personal", "🎯 Proyecto"],
    ["tecnica", "filosofia", "idea", "proyecto"]
);

// Variable para almacenar la asignatura
let asignaturaSeleccionada = "";
_%>

## 🎓 Contexto Académico

<%* 
if (tipoNota === "tecnica" || tipoNota === "proyecto") {
    asignaturaSeleccionada = await tp.system.suggester(
        ["Algoritmos", "Arquitectura", "Infraestructura Nube", "Fundamentos DS", "Otro (escribir)"],
        ["Algoritmos", "Arquitectura", "Infraestructura-Nube", "Fundamentos-DS", "custom"]
    );
    
    if (asignaturaSeleccionada === "custom") {
        asignaturaSeleccionada = await tp.system.prompt("📚 Nombre de la asignatura:");
    }
    
    tR += `**Asignatura/Curso**: ${asignaturaSeleccionada}\n`;
    
    const relevancia = await tp.system.prompt("🎯 Relevancia para (Examen/Proyecto/Certificación, opcional):", "");
    if (relevancia) {
        tR += `**Relevancia para**: ${relevancia}\n`;
    }
    
    const dificultad = await tp.system.suggester(
        ["⭐☆☆☆☆ Muy Fácil", "⭐⭐☆☆☆ Fácil", "⭐⭐⭐☆☆ Medio", "⭐⭐⭐⭐☆ Difícil", "⭐⭐⭐⭐⭐ Muy Difícil", "⏭️ Omitir"],
        ["⭐☆☆☆☆", "⭐⭐☆☆☆", "⭐⭐⭐☆☆", "⭐⭐⭐⭐☆", "⭐⭐⭐⭐⭐", ""]
    );
    
    if (dificultad) {
        tR += `**Dificultad percibida**: ${dificultad}\n`;
    }
} else {
    tR += `_No aplica para este tipo de nota_\n`;
}
_%>

---

## 📝 Definición

<% await tp.system.prompt("✏️ Descripción del concepto (2-3 párrafos):") %>

---

## ⚙️ Conceptos Clave

<%*
let agregarMas = true;
let contador = 1;

while (agregarMas) {
    const nombre = await tp.system.prompt(`[${contador}] Concepto clave (vacío para terminar):`);
    if (!nombre) break;
    
    const tipo = await tp.system.prompt(`Tipo (Algoritmo/Técnica/Teorema/Definición):`);
    
    let numCaracteristicas = await tp.system.prompt(`¿Cuántas características?`, "3");
    numCaracteristicas = parseInt(numCaracteristicas) || 3;
    
    let concepto = `### 📌 ${nombre}\n\n`;
    concepto += `**Tipo**: ${tipo}\n\n`;
    concepto += `**Características**:\n`;
    
    for (let i = 1; i <= numCaracteristicas; i++) {
        const caracteristica = await tp.system.prompt(`  [${i}/${numCaracteristicas}] Característica:`);
        concepto += `- ${caracteristica}\n`;
    }
    
    const relacion = await tp.system.prompt(`Notas relacionadas (separadas por comas, opcional):`);
    if (relacion) {
        const notas = relacion.split(',').map(n => n.trim());
        concepto += `\n**Relacionado**: ${notas.map(n => `[[${n}]]`).join(' • ')}\n`;
    }
    
    tR += concepto + "\n";
    contador++;
    
    const respuesta = await tp.system.suggester(
        ["✅ Agregar otro concepto", "⏭ Continuar con el template"],
        ["si", "no"]
    );
    if (respuesta === "no") agregarMas = false;
}
_%>

---

## 💻 Ejemplo Práctico

<%*
const tipoEjemplo = await tp.system.suggester(
    ["💻 Código", "📊 Caso práctico", "🧮 Ejercicio matemático", "⏭ Sin ejemplo"],
    ["codigo", "caso", "matematico", "ninguno"]
);

if (tipoEjemplo === "codigo") {
    const lenguaje = await tp.system.prompt("Lenguaje:", "python");
    const codigo = await tp.system.prompt("Código de ejemplo:");
    tR += "```" + lenguaje + "\n" + codigo + "\n```\n";
    
    const explicacion = await tp.system.prompt("Explicación del código (opcional):");
    if (explicacion) {
        tR += `\n**Explicación**: ${explicacion}\n`;
    }
} else if (tipoEjemplo === "caso") {
    const caso = await tp.system.prompt("Describe el caso práctico:");
    tR += `${caso}\n`;
} else if (tipoEjemplo === "matematico") {
    const formula = await tp.system.prompt("Fórmula o ejercicio:");
    tR += `$$${formula}$$\n`;
} else {
    tR += `_No se incluyó ejemplo en esta nota_\n`;
}
_%>

---

## 💭 Reflexiones & Conexiones

<% await tp.system.prompt("🧠 Reflexiones personales, conexiones con otros temas, insights:") %>

---

## 🎴 Flashcards

<%*
let contadorFlashcards = 0;
let agregarFlashcard = true;

const crearFlashcards = await tp.system.suggester(
    ["✅ Crear flashcards ahora", "⏭ Crear flashcards después"],
    ["si", "no"]
);

if (crearFlashcards === "si") {
    tR += `> 💡 **Formato**: Usa \`Pregunta::Respuesta\` para flashcards inline\n\n`;
    
    while (agregarFlashcard) {
        contadorFlashcards++;
        
        const tipoFlashcard = await tp.system.suggester(
            [`[${contadorFlashcards}] 📝 Básica inline (Pregunta::Respuesta)`, 
             `[${contadorFlashcards}] 📝 Básica multilínea (con ?)`,
             `[${contadorFlashcards}] 🔄 Reversa (Término:::Definición)`,
             `[${contadorFlashcards}] 🧩 Cloze (==texto==)`,
             "✅ Terminar flashcards"],
            ["basica-inline", "basica-multilinea", "reversa", "cloze", "terminar"]
        );
        
        if (tipoFlashcard === "terminar") {
            contadorFlashcards--;
            break;
        }
        
        // BÁSICA INLINE
        if (tipoFlashcard === "basica-inline") {
            const pregunta = await tp.system.prompt(`[${contadorFlashcards}] 📝 Pregunta:`);
            if (!pregunta) {
                contadorFlashcards--;
                break;
            }
            
            const respuesta = await tp.system.prompt(`Respuesta:`);
            const tags = await tp.system.prompt(`Tags (separados por espacio, opcional):`, "");
            
            if (tags) {
                tR += `${pregunta}::${respuesta} #${tags.replace(/ /g, ' #')}\n\n`;
            } else {
                tR += `${pregunta}::${respuesta}\n\n`;
            }
        }
        
        // BÁSICA MULTILÍNEA
        else if (tipoFlashcard === "basica-multilinea") {
            const pregunta = await tp.system.prompt(`[${contadorFlashcards}] 📝 Pregunta:`);
            if (!pregunta) {
                contadorFlashcards--;
                break;
            }
            
            const respuesta = await tp.system.prompt(`Respuesta:`);
            const tags = await tp.system.prompt(`Tags (opcional):`, "");
            
            tR += `${pregunta}\n`;
            tR += `?\n`;
            tR += `${respuesta}`;
            if (tags) {
                tR += ` #${tags.replace(/ /g, ' #')}`;
            }
            tR += `\n\n`;
        }
        
        // REVERSA (BIDIRECCIONAL)
        else if (tipoFlashcard === "reversa") {
            const termino = await tp.system.prompt(`[${contadorFlashcards}] 🔄 Término/Concepto:`);
            if (!termino) {
                contadorFlashcards--;
                break;
            }
            
            const definicion = await tp.system.prompt(`Definición/Explicación:`);
            const tags = await tp.system.prompt(`Tags (opcional):`, "");
            
            if (tags) {
                tR += `${termino}:::${definicion} #${tags.replace(/ /g, ' #')}\n\n`;
            } else {
                tR += `${termino}:::${definicion}\n\n`;
            }
        }
        
        // CLOZE
        else if (tipoFlashcard === "cloze") {
            tR += `> 💡 Usa ==texto== para ocultar partes. Ejemplo: "El algoritmo ==QuickSort== tiene complejidad ==O(n log n)=="\n\n`;
            
            const textoCloze = await tp.system.prompt(`[${contadorFlashcards}] 🧩 Texto con partes ocultas (usa == ==):`);
            if (!textoCloze) {
                contadorFlashcards--;
                break;
            }
            
            const tags = await tp.system.prompt(`Tags (opcional):`, "");
            
            if (tags) {
                tR += `${textoCloze} #${tags.replace(/ /g, ' #')}\n\n`;
            } else {
                tR += `${textoCloze}\n\n`;
            }
        }
    }
    
    if (contadorFlashcards > 0) {
        tR += `---\n\n`;
        tR += `**📊 Total de flashcards**: ${contadorFlashcards}\n\n`;
        tR += `> 🎯 **Para revisar**: Cmd/Ctrl+P → "Flashcards: Review flashcards"\n`;
    }
} else {
    tR += `_Flashcards pendientes de crear_\n\n`;
    tR += `> 💡 **Formato recomendado**:\n`;
    tR += `> - Inline: \`¿Pregunta?::Respuesta #tags\`\n`;
    tR += `> - Reversa: \`Término:::Definición #tags\`\n`;
    tR += `> - Cloze: \`Texto con ==palabra== oculta\`\n`;
}
_%>

---

## 📚 Referencias & Enlaces

**Enlaces internos**: 
**Referencias externas**: 
**Fuente**: 

---

## 📋 Metadata

<%*
// Calcular fecha de próxima revisión basada en el estado
const estadoNota = await tp.system.suggester(
    ["🌱 Semilla (revisar en 3 días)", "🌿 Creciendo (revisar en 1 semana)", "🌳 Maduro (revisar en 1 mes)"],
    ["semilla", "creciendo", "maduro"]
);

let diasRevision;
let emojiEstado;

if (estadoNota === "semilla") {
    diasRevision = 3;
    emojiEstado = "🌱 Semilla";
} else if (estadoNota === "creciendo") {
    diasRevision = 7;
    emojiEstado = "🌿 Creciendo";
} else {
    diasRevision = 30;
    emojiEstado = "🌳 Maduro";
}

const nivelComprension = await tp.system.suggester(
    ["❓ No entiendo", "🤔 Entiendo parcialmente", "💡 Entiendo bien", "✅ Domino el concepto", "🎯 Puedo enseñarlo"],
    ["❓", "🤔", "💡", "✅", "🎯"]
);

const tiempoRepaso = await tp.system.suggester(
    ["⚡ 5 minutos", "📖 15 minutos", "📚 30 minutos", "🔬 +1 hora"],
    ["5min", "15min", "30min", "+1h"]
);

tR += `- **Estado**: ${emojiEstado}\n`;
tR += `- **Última revisión**: ${tp.date.now("YYYY-MM-DD")}\n`;
tR += `- **Próxima revisión**: ${tp.date.now("YYYY-MM-DD", diasRevision)}\n`;
tR += `- **Veces revisado**: 0\n`;
tR += `- **Nivel de comprensión**: ${nivelComprension}\n`;
tR += `- **Tiempo estimado de repaso**: ${tiempoRepaso}\n`;

// ACTUALIZAR FRONTMATTER con los campos necesarios para el tracking
await app.fileManager.processFrontMatter(tp.config.target_file, (fm) => {
    // Campos básicos ya existentes
    fm.tipo_nota = tipoNota;
    fm.status = emojiEstado;
    
    // NUEVOS CAMPOS para integración con dashboards
    if (asignaturaSeleccionada) {
        fm.asignatura = asignaturaSeleccionada;
    }
    fm["nivel-comprension"] = nivelComprension;
    fm["proxima-revision"] = tp.date.now("YYYY-MM-DD", diasRevision);
    fm["ultima-revision"] = tp.date.now("YYYY-MM-DD");
    fm["veces-revisado"] = 0;
    fm["tiempo-repaso"] = tiempoRepaso;
});
_%>

---

> [!tip] 💡 Próximos pasos
> _Cuando revises esta nota, actualiza el contador de revisiones y ajusta la próxima fecha según tu comprensión_