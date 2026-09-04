---
created: 2026-09-02
modified: 2026-09-02
area: Redes
tipo_nota: captura_rapida
status: 🌱
nivel-comprension: ""
proxima-revision: 2026-09-05
ultima-revision: 2026-09-02
veces-revisado: 0
tiempo-repaso: 5min
---

# URL (Uniform Resource Locator)

> [!info] Contexto captura
> **Fecha**: 2026-09-02 14:56
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> Una URL (_Uniform Resource Locator_) es la dirección que identifica dónde se encuentra un recurso en Internet, como una página web, una imagen o un archivo.


### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->
```text
http://350.5th-ave.com:80/unit/243?floor=77
```
>Protocol: The means of transportation 
http: //
>Domai: The street address of the office building 
350.5th-ave.com 
>Port: The gate or door to use when entering the building 
:80
>Path: The specific office unit inside the building
/unit/243 
>Query: Any additional instructions
?floor=77

### Addind query parameters with requests

```python
# Append the query parameter to the URL string
response = requests.get('http://350.5th-ave.com:80/unit/243?floor=77elevator=True')
print(response.url)
```
### Use the params argument to add query parameters
```python
# Create dictionary
query_params = {'floor': 77, 'elevator': True}

# Pass the dictionary using the params argument
response = requests.get{
http://350.5th-ave.com:80/unit/243?floor=77, params=query_params}
```

---

## 🔑 Keywords / Conceptos clave

`URL`, `API`, `keyword3`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

_Flashcards pendientes de crear_

> 💡 **Formato recomendado**:
> - Inline: `¿Pregunta?::Respuesta #tags`
> - Reversa: `Término:::Definición #tags`
> - Cloze: `Texto con ==palabra== oculta`
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

En resumen, una URL funciona como una dirección de Internet que indica qué recurso se quiere consultar y dónde encontrarlo.



---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-09-02 14:56 |
| Área/Tema | `= this.area` |
| Estado | `= this.status` |
| Prioridad | `= this.prioridad` |
| Revisión | `= this.proxima-revision` |
| Nivel de comprensión | `= this.nivel-comprension` |

---

#pendiente-procesar #captura-rapida
