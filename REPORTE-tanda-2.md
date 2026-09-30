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

## 29-sep · ronda W35/W36 y pie
| Hora | Qué | Estado |
|---|---|---|
| 23:4x | Respaldo de las 13 páginas antes de C1 (`respaldo/2026-09-29/*.antes-C1.json`, webhook redactado) | Hecho |
| 00:0x (29-sep) | C1 ajustado: fuera "Términos de Participación (candidatas)" (también el texto); 12 páginas listas, /caballeros/ aparte | Preparado, espera "sí" |
| 00:0x (29-sep) | /caballeros/: C1 + C6 (casillas W21, texto bajo casillas, mensaje menor de 22, mensaje al enviar) + C7 (enlace en el paso 2). Probado en local con Chromium y red bloqueada: los dos formularios abren sus pasos; sin casillas no avanza; con 20 años muestra el mensaje de W21; nada se envió | Preparado, espera "sí" |
| 00:0x (29-sep) | Home W35 (portada y pasos 01–05, cierre USD 13.400 y línea de candidatas) | Preparado, espera "sí" |
| 00:0x (29-sep) | /about/ W36 (portada) | Preparado, espera "sí" |
| 00:1x (29-sep) | "Sí" de Miguel a 1–4, con ajustes en la ventana de candidatas de /caballeros/ (quitar el título "Su perfil no será público…", "contactarla" → "contactarte", revisar que no quede usted) | Recibido |
| 00:12 | Home: C1 + W35 publicados en una escritura; caché de Elementor borrada; comparación exacta con lo preparado: igual | Hecho, verificado |
| 00:14 | /about/: C1 + W36 publicados; fondo de Unsplash retirado, fondo liso con el mismo negro de la página (`var(--about-bg)`); caché borrada; comparación exacta: igual | Hecho, verificado |
| 00:15 | /confirmacion/: C1 | Hecho, verificado |
| 00:16 | /cancelaciones/ y /cancelaciones-es/: C1 | Hecho; revisadas a ojo (la herramienta devolvió el texto en línea y no se pudo comparar por archivo) |
| 00:17 | /privacidad/ y /privacidad-es/: C1 (solo el pie; el contenido de privacidad no se tocó) | Hecho, verificado |
| 00:19 | /contact/: C1 | Hecho, verificado |
| 00:21 | /checkout/: C1 (solo el pie; el webhook, PayPal y el enlace "Términos y Condiciones" del formulario no se tocaron) | Hecho, verificado |
| 00:23 | /damas/: C1 | Hecho, verificado |
| 00:25 | /proceso/: C1 | Hecho, verificado |
| 00:28 | /registro-candidata/: C1 | Hecho, verificado |
| 00:30–00:35 | post_content (texto plano ES ——— EN, o un solo idioma en las páginas de un idioma) actualizado en las 12 páginas | Hecho |
| 00:36 | Revisión SEO (cabecera que genera AIOSEO) de la home, /about/, /proceso/ y /damas/: title, description, og:title, og:description, twitter:title y twitter:description. Ninguna tiene "eventos", "experiencias" ni "latinoamericanas". Detalle abajo | Hecho |
| 00:37 | /caballeros/: en la ventana de candidatas quedan 3 frases en usted, heredadas (no venían en W21). Se muestran a Miguel antes de publicar | Espera respuesta de Miguel |

### Revisión SEO (29-sep, 00:36)
| Página | title / og:title / twitter:title | description / og / twitter |
|---|---|---|
| Home | ZAFIRA \| Private Matchmaking Agency | "Private, invitation-only matrimonial consultancy for men in the United States and women in Colombia. Verification on both sides and consent in every case." |
| /about/ | About Zafira \| ZAFIRA | "Zafira is a private introduction agency and matrimonial consultancy with its office in Bogotá, Colombia. Who we are, how we work and what Zafira is not." |
| /proceso/ | The Process \| ZAFIRA | "Five steps, in this order: free application, preliminary review, USD 400 evaluation and verification, approval, USD 13,000 programme. No other charge." |
| /damas/ | Para Damas \| ZAFIRA | "Registro gratuito y privado para mujeres en Colombia que buscan una relación seria con intención de matrimonio. Verificación de los dos lados. Tú decides." |

En las cuatro páginas, los seis campos coinciden entre sí. Quedan tres restos viejos fuera de esos campos:
- El nombre interno de la página /about/ en WordPress sigue siendo "The Experience". Aparece en las migas de pan del código (schema BreadcrumbList).
- El extracto de /about/ dice "engineering-grade approach…". La cabecera no lo usa.
- Siguen dentro del HTML las etiquetas `<meta name="description">` heredadas (ver Observaciones).

## 29-sep · /caballeros/, limpieza, C19 y C2
| Hora | Qué | Estado |
|---|---|---|
| 00:3x | "Sí" de Miguel a las 3 frases en tú y a la limpieza (solo quitar) | Recibido |
| 00:3x | /caballeros/ preparado: C1 + C6 + C7, las 3 frases en tú ("Revisa el WhatsApp…", "Tu registro fue enviado… Te contactamos…", "Se abrió WhatsApp con tu registro: envíalo y te contactamos… escríbenos…"). Única etiqueta heredada de cabecera: `<title>Para Caballeros \| ZAFIRA</title>`, quitada (charset y viewport intactos). Prueba en Chromium local con red bloqueada: las dos ventanas abren sus pasos, sin casillas no avanza, con 20 años sale el mensaje de W21; nada se envió | Preparado |
| 00:3x | /caballeros/ releída en vivo: sin cambios desde 28-sep 21:25:58 (igual a la copia previa) | Hecho |
| 00:4x | /caballeros/ no se escribió. La página pesa 217 KB, de los cuales 68 KB son 7 fotos incrustadas en el código (base64: Melany y las 6 tarjetas difuminadas). El conector solo permite reescribir la página entera, y copiar a mano 68 KB de base64 tiene un riesgo alto de dañar alguna foto. Se consultan las opciones con Miguel | Espera decisión de Miguel |
| 00:42 | /about/: nombre interno "The Experience" → "About Zafira" (la dirección sigue en /about/). Extracto vaciado ("engineering-grade approach…") | Hecho |
| 00:4x | Etiquetas heredadas de cabecera en las demás páginas: lista mostrada a Miguel (ver abajo) | Espera "sí" de Miguel |
| 00:4x | C19 (/checkout/): la línea la escribe el script (`planName`: "El Programa ($13,000 USD)" / "The Programme ($13,000 USD)"). La fila "Plan" está oculta hoy (`display:none`) pero el texto sigue en el código. El texto "Concepto" de W14 no está en el repo: se pide a Miguel | Espera texto W14 |
| 00:4x | C2: el menú de Astra está vacío, pero ninguna página tiene desactivados la cabecera ni el pie de Astra (ajuste de página "Encabezado/Pie" por defecto). El CSS adicional los oculta (`#masthead, #colophon … display:none !important`), así que no se ven, pero siguen en el HTML. No se pudo ver el HTML en vivo desde este entorno | Avisado a Miguel |

### Etiquetas heredadas de cabecera dentro del HTML (29-sep)
| Página | Etiqueta | Dice |
|---|---|---|
| Home | title | ZAFIRA — Where Verification Meets Matrimony |
| Home | description | ZAFIRA curated introductions, and a private Colombia event. Not a dating app. |
| /about/ | title | The Experience \| ZAFIRA |
| /about/ | description | Zafira is not simply an event. It is access to a different reality. Discover our elite lifestyle and destinations. |
| /checkout/ | title | Evaluation &amp; Verification \| ZAFIRA |
| /checkout/ | description | USD 400 evaluation and verification payment. Not a reservation and not part of the programme. |
| /confirmacion/ | title | Payment Received \| ZAFIRA |
| /confirmacion/ | description | Your Zafira evaluation payment has been received. Next steps of your process. |
| /contact/ | title | Contact \| ZAFIRA |
| /contact/ | description | Contact the Zafira team for confidential inquiries about our verified matrimonial consultancy services. |
| /damas/ | title | Para Damas \| ZAFIRA |
| /damas/ | description | Zafira conecta mujeres latinas verificadas con hombres americanos serios a través de un proceso seguro, acompañamiento real y un evento privado en Colombia. |
| /privacidad/ | title | Privacy Policy \| ZAFIRA |
| /privacidad/ | description | Zafira privacy policy, security protocols, terms of conduct, and refund policy. |
| /privacidad-es/ | title | Política de Privacidad \| ZAFIRA |
| /privacidad-es/ | description | Política de privacidad de Zafira: protocolos de seguridad, tratamiento de datos y términos de conducta. |
| /proceso/ | title | The Process \| ZAFIRA |
| /proceso/ | description | Discover the selective Zafira verification and event-matching process. Every connection begins with trust. |
| /registro-candidata/ | title | Registro de Candidata \| ZAFIRA |
| /registro-candidata/ | description | Completa tu registro como candidata verificada en Zafira. Proceso seguro, confidencial y acompañado. |
| /cancelaciones-es/ | title | Política de Cancelaciones y Reembolsos \| ZAFIRA |
| /cancelaciones/ | title | Cancellation & Refund Policy \| ZAFIRA |

Ninguna página tiene keywords, og: ni twitter: dentro del HTML. /terminos/ y /terminos-es/ no se revisaron (no se tocan).

### Pendiente
- /caballeros/: decisión de Miguel sobre cómo escribir la página (fotos incrustadas).
- Limpieza de etiquetas heredadas: "sí" de Miguel a la lista.
- C19: texto "Concepto" de W14.
- C2: Miguel decide si desactiva la cabecera y el pie de Astra en los ajustes.
- Después: C22.

## 29-sep · /caballeros/ opción A, etiquetas heredadas y C19
| Hora | Qué | Estado |
|---|---|---|
| 00:4x | Miguel elige la opción A para /caballeros/: él pega el HTML en Elementor. Archivo subido a la rama: `para-pegar/caballeros-para-pegar.html` (sin webhook). No se escribe /caballeros/ mientras Miguel pega | Espera "ya lo pegué" |
| 00:4x | Revisión previa: ningún script usa `<title>` ni `<meta name="description">` (no hay `document.title` ni selectores de esas etiquetas en las 12 páginas) | Hecho |
| 00:4x | Relectura en vivo de las 12 páginas: todas iguales a lo publicado por nosotros | Hecho |
| 00:48–01:04 | Quitados `<title>` y `<meta name="description">` heredados en 11 páginas (home, /about/, /confirmacion/, /contact/, /damas/, /privacidad/, /privacidad-es/, /proceso/, /registro-candidata/, /cancelaciones/, /cancelaciones-es/; en las dos de cancelaciones solo había `<title>`). Charset y viewport intactos. Caché de Elementor borrada en cada una. Comparación byte a byte: 9 iguales; /cancelaciones/ y /cancelaciones-es/ revisadas con la respuesta del guardado (idénticas a lo preparado) | Hecho, verificado |
| 01:0x | /checkout/: C19 preparado junto con la limpieza de su `<title>` y description, para una sola escritura. Fila "Plan" (oculta) → visible, con la línea "Concepto"/"Item" de W14 tal cual; el script escribe el mismo texto. Probado en local en EN y ES | Espera "sí" de Miguel |
| — | C2: Miguel lo comprueba él en el código; no se tocan los ajustes del tema | A cargo de Miguel |

### Pendiente
- /caballeros/: cuando Miguel diga "ya lo pegué": caché, comparación byte a byte, texto plano y prueba de las ventanas.
- /checkout/: "sí" de Miguel a C19 → una escritura (C19 + limpieza de cabecera), caché, verificación y texto plano.
- Después: C22.

## 30-sep · retoma
| Hora | Qué | Estado |
|---|---|---|
| 06:1x | Revisión sin escribir. /caballeros/ (120): aún no pegado; igual a la versión del 28-sep 21:25:58, distinto del archivo para pegar. /checkout/ (125): idéntico a lo publicado el 29-sep 00:32:20 (con C1); nadie lo cambió desde la pausa | Hecho |
| 06:19 | Miguel cambia el orden: primero B (/checkout/), luego C22 en borrador; A espera su "ya lo pegué". No se toca la página 120 | Recibido |
| 06:2x | B: C19 + quita de `<title>` y description de /checkout/ mostrados como antes → después (ES y EN), preparados sobre la versión viva actual | Espera "sí" de Miguel |
| 06:2x | C22: borrador del bloque de datos del encuentro, solo con textos ya aprobados ("Por confirmar" donde falta el dato). No se escribió nada | Espera datos y páginas de Miguel |

| 06:27:54 | Miguel pega `para-pegar/caballeros-para-pegar.html` en Elementor y publica /caballeros/ (120). Avisa "ya lo pegué" | Hecho por Miguel |
| 06:2x | Comparación byte a byte del HTML en vivo con `para-pegar/caballeros-para-pegar.html`: idénticos (206.003 caracteres) | Hecho, verificado |
| 06:2x | Caché de Elementor borrada en 120 | Hecho |
| 06:30 | Relectura justo antes de guardar: sin cambios desde las 06:27:54 | Hecho |
| 06:32:18 | `post_content` de 120 actualizado con texto plano (ES ——— EN), con el pie limpio igual que en las demás páginas. Comparado con lo preparado: idéntico. Sin fotos en base64 ni webhook. El HTML de Elementor sigue idéntico al archivo | Hecho, verificado |
| 06:32:47 | Prueba de las dos ventanas en navegador local con la red bloqueada, **sin enviar formularios**. Ventana del caballero: abre en el paso 1 y pasa al paso 2; el enlace de privacidad del paso 2 (C7) lleva a /privacidad-es/; sin datos muestra "Faltan datos…". Ventana de candidata: sin casillas muestra "Faltan datos para poder contactarte." y sigue en el paso 1; con 20 años muestra el mensaje de menores de 22. En inglés, la casilla (C6) sale en inglés y enlaza a /privacidad/, y el pie sale en inglés (C1). Solo 2 peticiones bloqueadas (fuentes de Google y un archivo de wp-content); ninguna es de envío | Hecho |
| 06:37 | B: relectura en vivo de /checkout/ (125), sin escribir. Sigue igual a lo publicado el 29-sep 00:32:20. Se muestra a Miguel el antes → después de C19 y de la quita del `<title>` y la description. Lo preparado solo cambia el HTML del widget, y la línea de C19 coincide palabra por palabra con W14 en ES y EN | Espera "sí" de Miguel |
| 06:38 | Miguel da el "sí" a B | Recibido |
| 06:40:01 | Relectura de /checkout/ (125) justo antes de guardar: sin cambios desde el 29-sep 00:32:20 | Hecho |
| 06:41:42 | B escrito en una sola escritura: C19 (línea "Concepto"/"Item" de W14 visible en el resumen; el script escribe el mismo texto) y quitados `<title>` y `<meta name="description">`. Webhook de Make y enlace "Términos y Condiciones" del formulario sin cambios | Hecho |
| 06:41 | Caché de Elementor borrada en 125. Comparación byte a byte con lo preparado: idéntico (20.157 caracteres) | Hecho, verificado |
| 06:4x | Prueba local con la red bloqueada, sin enviar el formulario. EN: se ve "Item: Evaluation & Verification – USD 400…" y el enlace de términos lleva a /terminos/. ES: se ve "Concepto: Evaluación y verificación – USD 400…" y el enlace lleva a /terminos-es/. Al cambiar de idioma se cambia la línea. Único error: "paypal is not defined", esperado porque se bloqueó el script de PayPal | Hecho |
| 06:42:43 | `post_content` de 125 actualizado con la línea Concepto/Item (ES ——— EN). Comparado: idéntico; sin webhook | Hecho, verificado |
| 06:4x | C22 en propuesta, sin escribir: `propuestas/C22-bloque-encuentro.md` (páginas propuestas: home 21, /proceso/ 167, /caballeros/ 120) | Espera "sí" de Miguel |
| 06:47 | Miguel da el "sí" a C22 con ajustes: aprueba las etiquetas "Encuentro"/"Gathering" y "Fechas exactas"/"Exact dates"; /proceso/ tal cual; Home con una sola línea (espera "sí"); /caballeros/ no se toca ahora | Recibido |
| 06:49:12 | Relectura de /proceso/ (167) justo antes de guardar: sin cambios desde el 29-sep 00:56:52 | Hecho |
| 06:51:00 | C22 en /proceso/ (una escritura): portada → "Cartagena · Octubre–Noviembre 2026"; bloque de cinco filas entre marcas C22 en "Un programa privado y acompañado". Caché borrada. Comparación byte a byte: idéntico (31.019 caracteres) | Hecho, verificado |
| 06:51 | Prueba local de /proceso/ (red bloqueada): ES y EN correctos, sin errores; en móvil (375 px) sin desbordes | Hecho |
| 06:52:08 | `post_content` de 167 actualizado con el bloque y la portada nueva (ES ——— EN). También se corrigieron dos espacios que faltaban en el título del texto plano ("Bienvenido al proceso Zafira" / "Welcome to the Zafira process"). Comparado: idéntico | Hecho, verificado |
| 06:5x | Home (21): relectura (sin cambios desde el 29-sep 00:58:51) y línea C22 preparada y probada en local ES/EN. No se escribió | Espera "sí" de Miguel |
| 06:5x | Lista para el día de las fechas reales anotada en `propuestas/C22-bloque-encuentro.md` | Hecho |
| 07:00 | Miguel da el "sí" a la línea C22 de la Home | Recibido |
| 07:01:26 | Relectura de la Home (21) justo antes de guardar: sin cambios desde el 29-sep 00:58:51 | Hecho |
| 07:03:16 | C22 en la Home (una escritura): línea entre marcas C22 debajo de "Verificación de ambos lados…". Caché borrada. Comparación byte a byte: idéntico (30.140 caracteres) | Hecho, verificado |
| 07:03 | Prueba local de la Home: la línea sale en ES y EN, sin desbordes en móvil (375 px). Único error: el de `#counter`, que ya existía | Hecho |
| 07:04:23 | `post_content` de 21 actualizado con la línea C22 (ES ——— EN). También se corrigió un espacio que faltaba en el título del texto plano ("Una decisión seria merece…" / "A serious decision deserves…"). Comparado: idéntico | Hecho, verificado |
| 07:0x | Análisis del error `#counter` (sin escribir): solo bloquea el parallax del fondo del encabezado; idioma, enlaces, aparición al hacer scroll y partículas funcionan. Arreglo de una línea en `propuestas/home-counter.md` | Espera decisión de Miguel |

### Pendiente
- A (/caballeros/) cerrado. Falta que Miguel tome las capturas en vivo (ES, EN y móvil).
- B (/checkout/) cerrado. Falta que Miguel tome las capturas en vivo.
- C22: /proceso/ y Home hechos. /caballeros/, /about/ y /confirmacion/: cuando haya fechas reales (lista en `propuestas/C22-bloque-encuentro.md`).
- Home, error `#counter`: arreglo de una línea propuesto en `propuestas/home-counter.md`; espera decisión de Miguel.
