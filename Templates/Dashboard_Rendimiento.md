TABLE WITHOUT ID
	link(file.name) as "Día",
	sueño-calidad as "Sueño",
	horas-deep-work as "Deep Work (h)",
	nivel-concentracion as "Foco (1-10)",
	choice(habito-deporte, "✅", "❌") as "Gym",
	choice(habito-codigo, "✅", "❌") as "Code",
	choice(habito-lectura, "✅", "❌") as "Leer"
FROM "Diario"
WHERE week = this.file.day.week OR file.cday >= date(today) - dur(7 days)
SORT file.name DESC

const pages = dv.pages('"Diario"').where(p => p.fecha).sort(p => p.fecha, 'desc').limit(14);

dv.header(3, "🔥 Tendencia de Deep Work (Últimos 14 días)");

let totalHoras = 0;
let dias = 0;

dv.paragraph("Cada barra representa tus horas de estudio concentrado:");

let markdownGraph = "";
for (let page of pages) {
    if (page["horas-deep-work"]) {
        let horas = page["horas-deep-work"];
        totalHoras += horas;
        dias++;
        // Creamos una barra visual con caracteres ASCII
        let barra = "█".repeat(horas * 2); 
        markdownGraph += `- **${page.file.name}**: ${barra} (${horas}h)\n`;
    }
}

dv.paragraph(markdownGraph);
dv.paragraph(`**Promedio actual:** ${(totalHoras / dias).toFixed(1)} horas/día`);