<%*
const file = tp.config.target_file;

new Notice("🔧 Actualizando frontmatter de nota técnica...");

// Verificar si tiene los campos básicos
const fm = app.metadataCache.getFileCache(file)?.frontmatter;

const asignatura = await tp.system.suggester(
    ["Algoritmos", "Arquitectura", "Infraestructura-Nube", "Fundamentos-DS"],
    ["Algoritmos", "Arquitectura", "Infraestructura-Nube", "Fundamentos-DS"]
);

const nivelComprension = await tp.system.suggester(
    ["❓ No entiendo", "🤔 Entiendo parcialmente", "💡 Entiendo bien", "✅ Domino el concepto", "🎯 Puedo enseñarlo"],
    ["❓", "🤔", "💡", "✅", "🎯"]
);

const diasHastaRevision = await tp.system.prompt(
    "📅 Días hasta próxima revisión:",
    "7"
);

const tiempoRepaso = await tp.system.suggester(
    ["⚡ 5 minutos", "📖 15 minutos", "📚 30 minutos", "🔬 +1 hora"],
    ["5min", "15min", "30min", "+1h"]
);

const status = await tp.system.suggester(
    ["🌱 Semilla", "🌿 Creciendo", "🌳 Maduro"],
    ["🌱 Semilla", "🌿 Creciendo", "🌳 Maduro"]
);

// Calcular estado basado en la próxima revisión
const proximaRevision = tp.date.now("YYYY-MM-DD", parseInt(diasHastaRevision));
const hoy = new Date();
const fechaRevision = new Date(proximaRevision);
let estadoCalculado;

if (fechaRevision < hoy) {
    estadoCalculado = "🔴 Atrasado";
} else if ((fechaRevision - hoy) / (1000 * 60 * 60 * 24) <= 2) {
    estadoCalculado = "🟠 Próximo";
} else {
    estadoCalculado = "🟢 Al día";
}

// Aplicar cambios
await app.fileManager.processFrontMatter(file, (frontmatter) => {
    // Campos obligatorios ordenados como Big_O
    frontmatter["cards-deck"] = asignatura;
    frontmatter.created = frontmatter.created || tp.date.now("YYYY-MM-DD");
    frontmatter.modified = tp.date.now("YYYY-MM-DD");
    frontmatter.status = status;
    frontmatter.tipo_nota = frontmatter.tipo_nota || "tecnica";
    frontmatter.asignatura = asignatura;
    frontmatter["nivel-comprension"] = nivelComprension;
    frontmatter["proxima-revision"] = proximaRevision;
    frontmatter["ultima-revision"] = tp.date.now("YYYY-MM-DD");
    frontmatter["veces-revisado"] = frontmatter["veces-revisado"] || 0;
    frontmatter.estado = estadoCalculado;
    frontmatter["tiempo-repaso"] = tiempoRepaso;
});

new Notice(`✅ Nota técnica actualizada: ${asignatura} - ${nivelComprension}`);
_%>