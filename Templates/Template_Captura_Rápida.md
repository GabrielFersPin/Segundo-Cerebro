---
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
area: ""
tipo_nota: ""
status: 🌱
nivel-comprension: ""
proxima-revision: ""
ultima-revision: ""
veces-revisado: 0
tiempo-repaso: ""
---

# <% await tp.system.prompt("📌 Título del concepto:") %>

> [!info] Contexto captura
> **Fecha**: <% tp.date.now("YYYY-MM-DD HH:mm") %>
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> *Escribe aquí la idea principal o el concepto clave en 1-2 frases*


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->




---

## 🔑 Keywords / Conceptos clave

`keyword1`, `keyword2`, `keyword3`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

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

## ❓ Preguntas / Dudas pendientes

- [ ]
- [ ]

---

## 🧩 Conexiones potenciales

<!-- ¿Con qué otros temas se relaciona? Escribe rápido, ya harás los links después -->

-
-

---

## ✅ Checklist procesamiento

- [ ] Revisar y expandir contenido
- [ ] Crear flashcards si es necesario
- [ ] Hacer ejercicios relacionados
- [ ] Conectar con otras notas ([[]])
- [ ] Actualizar nivel de comprensión
- [ ] Mover a vault definitivo / Cambiar status a 🌿

---

## 💭 Notas adicionales / Ideas rápidas

<!-- Zona libre para cualquier cosa que quieras capturar rápido -->




---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | <% tp.date.now("YYYY-MM-DD HH:mm") %> |
| Área/Tema | `= this.area` |
| Prioridad | `= this.prioridad` |
| Estado | Captura rápida → Pendiente procesamiento |
| Revisión | `= this.proxima-revision` |

---

#pendiente-procesar #captura-rapida
