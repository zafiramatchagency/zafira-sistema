# Reporte tanda 2 · web de Zafira (28/29-sep-2026, hora de Colombia)

Aprobador: Miguel (E-leaders). Método: relectura antes de escribir, `_elementor_data` completo, limpieza de `_elementor_element_cache`, verificación JSON exacta, `post_content` con texto plano ES + EN.

## Pendientes manuales (sección 1 de las instrucciones)
| Punto | Quién | Estado verificado |
|---|---|---|
| noindex /checkout/ y /confirmacion/ | Miguel | Hecho. AIOSEO `robots_noindex=true` en las dos; meta robots "noindex, nofollow" |
| Fuera del sitemap | Miguel | Hecho. Captura de page-sitemap.xml: 13 URL, sin /checkout/ ni /confirmacion/ |
| Descripción SEO de /confirmacion/ | Miguel | Borrada (AIOSEO usa ahora el texto nuevo de la página) |
| Comentarios y pingbacks por defecto | Miguel | Hecho (ajustes vacíos = cerrados) |
| 9 redirecciones 301 → /caballeros/ | Miguel (hPanel) | Hecho. El conector de Hostinger lista las 9 (no muestra el tipo; Miguel las probó como 301). El conector no permitía elegir 301, por eso no las creé yo |

## Tabla por código
| Código | Página | Qué se hizo | Hora | Estado |
|---|---|---|---|---|
| C15 | /damas/ | W07 "Lo que te prometemos" agregado donde estaban los testimonios (ya retirados el 27-28 sep; quedaba un hueco) | 22:54 | Hecho, verificado |
| C16 | /damas/ | "Tu proceso" reemplazado por W29 (antes: 5 pasos reescritos por otra persona; paso 5 "Evento Zafira en Colombia") | 22:54 | Hecho, verificado |
| post_content | /damas/ | Texto plano ES + EN de la versión nueva | 22:55 | Hecho |
| C9 | /proceso/ | Portada W30 (antes: "Security & Selection / Every Connection Begins With Trust.", reescrita el 27-28 sep) y 5 pasos W30 "Paso 1…5" (antes: 6 "STEP 01…06" con fotos) | 23:09 | Hecho, verificado |
| C10 | /proceso/ | W09 con plan B (sin los cuatro momentos) en lugar del sexto paso "The Cartagena Programme" (que describía los cuatro momentos, puestos el 27-28 sep) | 23:09 | Hecho, verificado |
| C11 | /proceso/ | Fuera las fotos step01–06.png, la de la terraza (zafira_luxury_chemistry.jpg) y el fondo de la portada (Unsplash); portada sin imagen. No se subieron fotos | 23:09 | Hecho |
| C12 | /proceso/ | Segundo bloque de portada eliminado entero (alt="Zafira Diamond", "distinguished, feminine…"); cierre "Begin Your Evaluation" eliminado, queda solo el botón a /caballeros/ | 23:09 | Hecho |
| post_content | /proceso/ | Texto plano ES + EN | 23:10 | Hecho |
| W34 | /damas/ | Portada (etiqueta, título, párrafo), introducción y 3 pilares de "¿Qué es Zafira?"; en "Tu Seguridad es Prioridad" solo la frase 2 (reglas c y d); frases 1 y 3 sin cambio. Sin botón nuevo en la portada | 23:13 | Hecho, verificado |
| post_content | /damas/ | Texto plano ES + EN de la versión W34 | 23:14 | Hecho |
| C5 | Home | Título de pasos → "Su camino, en cinco pasos" / "Your path, in five steps" (W15). Pasos 01–05 sin tocar (esperan textos nuevos) | 23:29 | Hecho, verificado |
| C4 | Home | Bloque del evento → W32: etiqueta "CARTAGENA, COLOMBIA · SOLO POR INVITACIÓN", título "El encuentro de Cartagena", párrafo W32, línea "Verificación de ambos lados…", etiqueta inferior "ENCUENTRO PRIVADO · ACOMPAÑADO POR ZAFIRA" (antes: "El Evento Zafira" y etiquetas de evento). Portada sin tocar | 23:29 | Hecho, verificado |
| post_content | Home | Texto plano ES + EN | 23:29 | Hecho |
| C5 | /confirmacion/ | Etiqueta `planPill`: "Programa Zafira" → "Evaluación y verificación"; "Zafira Programme" → "Evaluation & Verification" | 23:30 | Hecho, verificado |
| post_content | /confirmacion/ | Texto plano ES + EN (el anterior era el texto de antes de C20) | 23:31 | Hecho |
| C13 / C14 | /about/ | Todo lo que había después de la portada se reemplazó por W10 (Quiénes somos, Misión y Visión, Cómo trabajamos, Lo que Zafira no es, Dónde con la fecha oficial y los enlaces a /caballeros/ y /damas/). Retirados: tarjetas de destinos, programa de Cartagena, fotos de cenas, filosofía y cierre viejo. Portada sin tocar (esperan textos nuevos) | 23:32 | Hecho, verificado |
| post_content | /about/ | Texto plano ES + EN | 23:33 | Hecho |

## Observaciones
- Descripción SEO de /proceso/ (AIOSEO): "Five stages from the initial application to the private event in Colombia…" — trae "event"; Miguel decide si la cambia.
- Descripción SEO de /damas/: ya cambiada por Miguel al texto de W34 (23:04).
- Dentro del HTML de las páginas hay etiquetas `<meta name="description">` heredadas (p. ej. /proceso/: "event-matching process"; /damas/: "mujeres latinas verificadas… evento privado"). No las usa Google (AIOSEO pone la suya en la cabecera), pero quedan en el código; se pueden limpiar en una pasada técnica.
- /terminos/ y /terminos-es/ publicadas por el equipo de Zafira el 28-sep 21:02; copia de texto en `revision/`. No se tocaron.
- Home y /about/: las portadas y los pasos 01–05 de la home quedan como estaban, por instrucción de Miguel (prepara textos nuevos). En la portada de la home siguen "Evento Privado Exclusivo" y "privacidad absoluta".
- /about/: la descripción SEO de AIOSEO y el `<meta name="description">` heredado todavía hablan de "event"/"destinations"; Miguel decide si cambia la de AIOSEO.

## 29-sep · ronda W35/W36 y pie (preparado, esperando "sí" de Miguel)
| Hora | Qué | Estado |
|---|---|---|
| 23:45 | Respaldo de las 13 páginas antes de C1 (`respaldo/2026-09-29/*.antes-C1.json`, webhook redactado) | Hecho |
| 23:50 | C1 ajustado: fuera "Términos de Participación (candidatas)" (también el texto); 12 páginas listas, /caballeros/ aparte | Preparado, espera "sí" |
| 23:55 | /caballeros/: C1 + C6 (casillas W21, texto bajo casillas, mensaje menor de 22, mensaje al enviar) + C7 (enlace en el paso 2). Probado en local con Chromium y red bloqueada: los dos formularios abren sus pasos; sin casillas no avanza; con 20 años muestra el mensaje de W21; nada se envió | Preparado, espera "sí" |
| 23:58 | Home W35 (portada y pasos 01–05, cierre USD 13.400 y línea de candidatas) | Preparado, espera "sí" |
| 23:58 | /about/ W36 (portada) | Preparado, espera "sí" |
