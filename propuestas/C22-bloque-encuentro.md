# C22 · Datos del encuentro de Cartagena (propuesta, sin escribir)

Estado (30-sep, 06:5x): **/proceso/ (167) publicado** con el bloque de cinco filas. **Home (21)**: una línea, espera el "sí" de Miguel. **/caballeros/ (120)**: no se toca ahora; se actualiza cuando haya fechas reales (ver la lista del final).
Etiquetas nuevas aprobadas por Miguel: "Encuentro"/"Gathering" y "Fechas exactas"/"Exact dates".
Regla: solo se usa lo ya publicado, "Cartagena · Octubre–Noviembre 2026". Todo lo demás va como "Por confirmar" / "To be confirmed". No se inventa ningún dato.

## Bloque (igual en las 3 páginas)

| ES | EN |
|---|---|
| Encuentro: Cartagena · Octubre–Noviembre 2026 | Gathering: Cartagena · October–November 2026 |
| Fechas exactas: Por confirmar | Exact dates: To be confirmed |
| Sede: Por confirmar | Venue: To be confirmed |
| Cupos: Por confirmar | Places: To be confirmed |
| Cierre de solicitudes: Por confirmar | Applications close: To be confirmed |

Hay dos etiquetas nuevas: "Encuentro"/"Gathering" y "Fechas exactas"/"Exact dates". Las demás etiquetas y todos los valores ya están publicados en /caballeros/.

## Un solo lugar por página

Cada dato aparece **una sola vez** en la página, en su fila del bloque. El bloque va entre dos marcas:
`<!-- C22 · DATOS DEL ENCUENTRO · cambiar solo aquí -->` … `<!-- /C22 -->`

Cuando haya fechas, se cambia solo el valor de la fila, en sus `data-es` y `data-en` y en el texto visible. Cada fila usa nodos sin hijos, así que funciona tanto con `applyLang` (home y /proceso/) como con `traduce()` (/caballeros/).

### HTML para la home (21) y /proceso/ (167)
```html
<!-- C22 · DATOS DEL ENCUENTRO · cambiar solo aquí -->
<div class="zf-enc" style="max-width:560px;margin:28px auto;border:1px solid rgba(201,168,76,.25);border-radius:12px;padding:6px 20px;text-align:left">
  <div style="display:flex;justify-content:space-between;gap:16px;padding:10px 0;border-bottom:1px solid rgba(201,168,76,.12)"><span class="text-legal" data-es="Encuentro" data-en="Gathering">Gathering</span><span data-es="Cartagena · Octubre–Noviembre 2026" data-en="Cartagena · October–November 2026">Cartagena · October–November 2026</span></div>
  <div style="display:flex;justify-content:space-between;gap:16px;padding:10px 0;border-bottom:1px solid rgba(201,168,76,.12)"><span class="text-legal" data-es="Fechas exactas" data-en="Exact dates">Exact dates</span><span data-es="Por confirmar" data-en="To be confirmed">To be confirmed</span></div>
  <div style="display:flex;justify-content:space-between;gap:16px;padding:10px 0;border-bottom:1px solid rgba(201,168,76,.12)"><span class="text-legal" data-es="Sede" data-en="Venue">Venue</span><span data-es="Por confirmar" data-en="To be confirmed">To be confirmed</span></div>
  <div style="display:flex;justify-content:space-between;gap:16px;padding:10px 0;border-bottom:1px solid rgba(201,168,76,.12)"><span class="text-legal" data-es="Cupos" data-en="Places">Places</span><span data-es="Por confirmar" data-en="To be confirmed">To be confirmed</span></div>
  <div style="display:flex;justify-content:space-between;gap:16px;padding:10px 0"><span class="text-legal" data-es="Cierre de solicitudes" data-en="Applications close">Applications close</span><span data-es="Por confirmar" data-en="To be confirmed">To be confirmed</span></div>
</div>
<!-- /C22 -->
```
En /proceso/ se usan las clases de esa página (`p-step-desc`) en lugar de `text-legal`. El contenido es el mismo.

### /caballeros/ (120)
Se reutiliza el bloque `.ev` que ya existe: se cambia la fila "Fecha" y se añade la fila "Fechas exactas". Se mantienen las mismas clases (`mono`).

## Antes → después por página

### Home (21), sección "El encuentro de Cartagena" (W32)
- **Antes:** sin datos del encuentro.
- **Después:** el bloque va debajo de "Verificación de ambos lados. Consentimiento en cada caso. Acompañamiento en cada encuentro." y encima de la etiqueta "ENCUENTRO PRIVADO · ACOMPAÑADO POR ZAFIRA". Es el único lugar de la home con datos del encuentro.

### /proceso/ (167)
- **Antes (portada):** "Octubre o noviembre de 2026. Fechas exactas, sede y cupos por confirmar; se confirman antes de abrir los cupos." / "October or November 2026. Exact dates, venue and places to be confirmed before places open."
- **Después (portada):** "Cartagena · Octubre–Noviembre 2026" / "Cartagena · October–November 2026". Se queda en el nivel de mes, así que sigue siendo cierta cuando haya fechas.
- **Después (sección "Un programa privado y acompañado"):** el bloque, debajo del párrafo "El programa detallado se entrega…" y antes de "Reglas de privacidad…".

### /caballeros/ (120), sección "Cartagena, octubre o noviembre de 2026"
- **Antes:** Fecha: "Octubre o noviembre de 2026 · fechas exactas por confirmar" / "October or November 2026 · exact dates to be confirmed" · Sede / Cupos / Cierre de solicitudes: Por confirmar.
- **Después:** las 5 filas del bloque.
- Para escribirlo hace falta que Miguel vuelva a pegar la página, porque pesa 206 KB. Se prepararía un archivo nuevo en `para-pegar/`.
- Otra frase de esta página habrá que revisarla cuando haya fechas: la del botón final, "Las fechas exactas y el cierre de solicitudes se confirman antes de abrir los cupos." El título y la etiqueta de portada se quedan en el nivel de mes y siguen siendo ciertos.

## Fuera del bloque
- /about/ (27) y /confirmacion/ (132) tienen una sola frase: "Octubre o noviembre de 2026. Fechas exactas, sede y cupos por confirmar…". No llevan el bloque.
- Cuando haya fechas, esa frase también se cambia (una por página).

## Decisión de Miguel (30-sep)
- /proceso/ (167): bloque de cinco filas y portada con "Cartagena · Octubre–Noviembre 2026". **Publicado a las 06:51.**
- Home (21): no lleva las cinco filas. Lleva una sola línea entre las marcas C22, debajo de "Verificación de ambos lados…":
  - ES: "Encuentro · Cartagena · Octubre–Noviembre 2026 · Fechas, sede y cupos por confirmar"
  - EN: "Gathering · Cartagena · October–November 2026 · Dates, venue and places to be confirmed"
- /caballeros/ (120): no se toca ahora.

## Lista para el día en que haya fechas reales (una sola pasada)
Solo con los datos que confirme Zafira: fechas exactas, sede, cupos y cierre de solicitudes.

| Página (ID) | Qué se cambia | Cómo |
|---|---|---|
| /proceso/ (167) | Las filas "Fechas exactas", "Sede", "Cupos" y "Cierre de solicitudes" del bloque C22 | Escritura normal, entre las marcas C22 |
| Home (21) | La línea C22 ("… · Fechas, sede y cupos por confirmar") | Escritura normal, entre las marcas C22 |
| /caballeros/ (120) | Las filas del bloque `.ev` ("Fecha", "Sede", "Cupos", "Cierre de solicitudes"), en un solo cambio con la frase del botón final: "El encuentro de Cartagena está previsto para octubre o noviembre de 2026. Las fechas exactas y el cierre de solicitudes se confirman antes de abrir los cupos." / "The Cartagena gathering is planned for October or November 2026. Exact dates and the application deadline are confirmed before places open." | Archivo nuevo en `para-pegar/` y Miguel lo pega en Elementor (la página pesa 206 KB) |
| /about/ (27) | "Octubre o noviembre de 2026. Fechas exactas, sede y cupos por confirmar; se confirman antes de abrir los cupos." / "October or November 2026. Exact dates, venue and places to be confirmed before places open." | Escritura normal |
| /confirmacion/ (132) | Punto 5: "Cartagena: Octubre o noviembre de 2026. Fechas exactas, sede y cupos por confirmar; se confirman antes de abrir los cupos." (y su versión en inglés) | Escritura normal |

Los títulos y etiquetas que solo dicen el mes siguen siendo ciertos cuando haya fechas, y no hace falta cambiarlos: "Cartagena · Octubre–Noviembre 2026" en /caballeros/ y en la portada de /proceso/, y "Cartagena, octubre o noviembre de 2026" en /caballeros/.
