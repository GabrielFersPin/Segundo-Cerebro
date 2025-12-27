<%*
const file = tp.config.target_file;
const fm = app.metadataCache.getFileCache(file)?.frontmatter || {};

// 1. Seleccionar Nuevo Nivel de Comprensión
const nuevoNivel = await tp.system.suggester(
    ["❓ No entiendo", "🤔 Entiendo parcialmente", "💡 Entiendo bien", "✅ Domino el concepto", "🎯 Puedo enseñarlo"],
    ["❓", "🤔", "💡", "✅", "🎯"]
);

// 2. Seleccionar Días para Próxima Revisión
const diasParaProximaRevision = await tp.system.suggester(
    ["📅 1 día", "📅 3 días", "📅 7 días", "📅 14 días", "📅 30 días", "📅 Personalizado"],
    [1, 3, 7, 14, 30, "custom"]
);

let dias;
if (diasParaProximaRevision === "custom") {
    dias = parseInt(await tp.system.prompt("Días hasta próxima revisión:", "7"));
} else {
    dias = diasParaProximaRevision;
}

// 3. Preguntar por tiempo estimado si no existe
let tiempoEstimado = fm["tiempo-estimado"] || null;
if (!tiempoEstimado) {
    tiempoEstimado = await tp.system.prompt("Tiempo estimado para repasar (ej: 45m, 1h 30m):", "30m");
}

await app.fileManager.processFrontMatter(file, (fm) => {
    // A. Actualizaciones Esenciales
    fm["nivel-comprension"] = nuevoNivel;
    fm["proxima-revision"] = tp.date.now("YYYY-MM-DD", dias);
    fm["ultima-revision"] = tp.date.now("YYYY-MM-DD");
    fm.modified = tp.date.now("YYYY-MM-DD");
    
    // B. Actualizar Tiempo Estimado
    if (tiempoEstimado) {
        fm["tiempo-estimado"] = tiempoEstimado;
    }

    // C. Incrementar contador de repasos
    const vecesRevisado = fm["veces-revisado"] || 0;
    fm["veces-revisado"] = vecesRevisado + 1;
    
    // D. Actualizar status automáticamente según nivel
    if (nuevoNivel === "✅" || nuevoNivel === "🎯") {
        fm.status = "🌳 Maduro";
    } else if (nuevoNivel === "💡") {
        fm.status = "🌿 Creciendo";
    } else {
        fm.status = "🌱 Semilla";
    }
});

// 4. Notificación final
let mensaje = `✅ Nivel actualizado a ${nuevoNivel}\nPróxima revisión: ${tp.date.now("YYYY-MM-DD", dias)}\nRepasos totales: ${fm["veces-revisado"] + 1}`;

if (nuevoNivel === "🤔" || nuevoNivel === "❓" || nuevoNivel === "💡") {
    mensaje += `\n\n🚨 ¡Recuerda! Añade TAREAS de mejora (#mejora-...) a la sección "Plan de Mejora".`;
}

new Notice(mensaje);

// 5. MEJORA CLAVE: Crear la sección de Plan de Mejora si no existe, solo con tareas Kanban-compatibles.
if (nuevoNivel !== "✅" && nuevoNivel !== "🎯") {
    let fileContent = await app.vault.read(file);
    let targetHeader = '## 🚧 Plan de Mejora / Tareas Pendientes';
    let targetLine = fileContent.indexOf(targetHeader);

    // Si la sección NO existe, la añadimos al final.
    if (targetLine === -1) {
        
        // **ESTRUCTURA SIMPLIFICADA PARA COMPATIBILIDAD CON CARD/KANBAN**
        const planDeMejora = `

---

${targetHeader}

Define las tareas que te ayudarán a subir tu \`nivel-comprension\` en la próxima revisión. Usa los tags: \`#mejora-concepto\`, \`#mejora-practica\`, \`#mejora-analogia\`.

- [ ] Tarea para aclarar una duda de concepto. Usa #mejora-concepto
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia
`;
        
        fileContent += planDeMejora;
        await app.vault.modify(file, fileContent);
        
        // Recalcular la posición después de la modificación para mover el cursor.
        targetLine = fileContent.indexOf(targetHeader);
    }

    // Mover el cursor al inicio de la sección.
    if (targetLine !== -1) {
        const editor = app.workspace.activeEditor.editor;
        editor.setCursor(editor.offsetToPos(targetLine));
    }
}
_%>