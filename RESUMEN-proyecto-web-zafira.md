# Proyecto web de Zafira · resumen completo

Sitio: zafiramatchagency.com (WordPress + Elementor, tema Astra).
Aprueba: Miguel (E-leaders). Planea: el sistema de pauta de Zafira. Ejecuta: Claude, por el conector de WordPress.
Repo de trabajo: `zafiramatchagency/zafira-sistema`, rama `claude/focused-volta-2k142j`.
Periodo: 28 al 29 de septiembre de 2026 (hora de Colombia, UTC−5). Estado a la pausa del 29-sep.

---

## 1. En pocas líneas

- Se aplicó casi toda la guía de cambios en las 12 páginas públicas. Estas son la home, /about/, /proceso/, /damas/, /registro-candidata/, /contact/, /checkout/, /confirmacion/, /privacidad/, /privacidad-es/, /cancelaciones/ y /cancelaciones-es/.
- Se publicó el pie legal nuevo (C1) en esas 12 páginas.
- Se quitaron las etiquetas de cabecera heredadas en 11 de ellas.
- Se actualizó el texto de respaldo de WordPress (`post_content`) de las 12.
- Quedan tres cosas en curso:
  - **/caballeros/**: Miguel pega el HTML final en Elementor y después se verifica.
  - **C19** en /checkout/: preparado, espera el "sí" de Miguel.
  - **C22**: pendiente.

---

## 2. Reglas del proyecto

**Método de trabajo**
- Respaldo antes de tocar nada.
- Volver a leer cada página justo antes de guardar. Si alguien la cambió entre medio, no se escribe y se avisa a Miguel.
- Mostrar el cambio en español e inglés y esperar el "sí" de Miguel.
- Pegar los textos tal cual, sin agregar nada.
- Después de guardar:
  - borrar la caché de Elementor;
  - comparar lo guardado con lo preparado;
  - actualizar `post_content` con el texto plano (español, "———", inglés).
- Anotar cada paso con hora en el reporte y subirlo a la rama.

**Prohibido**
- Copiar la dirección del webhook de Make, que está en /checkout/. En las copias del repo va tapada.
- Escribir contraseñas o tokens.
- Borrar cualquier cosa.
- Tocar:
  - PayPal, forms.app, usuarios, plugins, DNS, actualizaciones o precios;
  - el contenido de privacidad y de términos, en particular /terminos/ y /terminos-es/;
  - el enlace "Términos y Condiciones" del formulario de /checkout/;
  - los ajustes del tema.
- Enviar formularios de prueba.
- Subir fotos nuevas de mujeres.
- Tocar C3, C8 ni C23 sin su decisión.

---

## 3. Cómo está hecha la web y cómo se edita

**Estructura**
- Cada página es un solo widget HTML de Elementor, con el documento completo en `_elementor_data[0].elements[0].settings.html`.
- El idioma se cambia con atributos `data-es` / `data-en` (también `-html` y `-ph`) y `localStorage.zafiraLang`.
- Hay dos mecanismos de idioma:
  - la mayoría de las páginas usa `applyLang`;
  - /caballeros/ usa `traduce()`, que solo cambia los nodos sin hijos.

**Cómo se escribe**
- Con `wp_update_post_meta` (`_elementor_data`) y después `wp_delete_post_meta` (`_elementor_element_cache`).
- Se verifica volviendo a leer con `wp_get_post_full` y comparando el JSON exacto.

**Lo que el conector no puede hacer**
- Ajustes de All in One SEO, ajustes generales de WordPress ni redirecciones 301. Eso lo hizo Miguel a mano.
- Abrir el sitio en vivo: la red de este entorno lo bloquea. Las pruebas de formularios se hacen en un navegador local con la red bloqueada.

**Límite práctico**
- Una página se reescribe entera en cada guardado.
- /caballeros/ pesa 217 KB, con 7 fotos incrustadas en el código. Por eso la pega Miguel en Elementor.

**IDs de las páginas**

| Página | ID |
|---|---|
| Home | 21 |
| /about/ | 27 |
| /caballeros/ | 120 |
| /checkout/ | 125 |
| /confirmacion/ | 132 |
| /contact/ | 137 |
| /damas/ | 142 |
| /privacidad/ | 156 |
| /privacidad-es/ | 162 |
| /proceso/ | 167 |
| /registro-candidata/ | 172 |
| /cancelaciones-es/ | 983 |
| /cancelaciones/ | 984 |
| /terminos/ | 1242 |
| /terminos-es/ | 1243 |

---

## 4. Estado por código

| Código | Qué es | Página | Estado |
|---|---|---|---|
| C1 | Pie legal nuevo (W19), sin "Términos de Participación" | 12 páginas | ✅ Hecho y verificado. /caballeros/ va en el archivo para pegar |
| C2 | Cabecera y pie de Astra en el código | Todas | Los oculta el CSS. Miguel lo comprueba; no se tocan los ajustes del tema |
| C3 | Banner de cookies (WPConsent ya instalado) | — | ⏸ Espera el visto bueno de Miguel |
| C4 | Bloque del encuentro de Cartagena (W32) | Home | ✅ Hecho |
| C5 | Título de pasos (W15) y etiqueta `planPill` | Home, /confirmacion/ | ✅ Hecho |
| C6 | Casillas y textos de W21 en la ventana de candidatas | /caballeros/ | ⏳ En el archivo para pegar |
| C7 | Enlace a privacidad en el paso 2 | /caballeros/ | ⏳ En el archivo para pegar |
| C8 | "Perfil reservado" / perfiles | /caballeros/ | ⏸ Espera la decisión de Dirección |
| C9–C12 | Portada W30, 5 pasos, itinerario W09 (plan B), fuera fotos y segundo bloque | /proceso/ | ✅ Hecho |
| C13–C14 | Contenido W10 y fuera destinos, fotos y filosofía | /about/ | ✅ Hecho |
| C15–C16 | "Lo que te prometemos" (W07) y "Tu proceso" (W29) | /damas/ | ✅ Hecho |
| C17 | Pantalla final del registro (W01) | /registro-candidata/ | ✅ Hecho |
| C18 | Blog en borrador, comentarios cerrados, 9 redirecciones 301 | Blog | ✅ Hecho (redirecciones y ajustes por Miguel) |
| C19 | Línea "Concepto" / "Item" de W14 en el resumen, fila visible | /checkout/ | ⏳ Preparado y probado en local, espera el "sí" |
| C20 | Botón a /caballeros/; noindex y fuera del sitemap | /confirmacion/, /checkout/ | ✅ Hecho (noindex por Miguel) |
| C21 | Textos W13 de la confirmación del pago | /confirmacion/ | ✅ Hecho |
| C22 | Bloque de datos del encuentro | 3 páginas | ⏳ Pendiente |
| C23 | Logo y colores | — | ⏸ Espera material |

**Otros cambios**

| Cambio | Página | Estado |
|---|---|---|
| W34: portada, introducción y pilares | /damas/ | ✅ Hecho |
| W35: portada y pasos 01–05 | Home | ✅ Hecho |
| W36: portada, con fondo liso en lugar de la foto de Unsplash | /about/ | ✅ Hecho |
| W37 (SEO en All in One SEO, hecho por Miguel) | Home, /about/, /proceso/ | ✅ Revisado: sin "eventos", "experiencias" ni "latinoamericanas" |
| Quitar `<title>` y description heredados | 11 páginas | ✅ Hecho y verificado. /checkout/ va junto con C19 |
| Nombre interno "The Experience" → "About Zafira"; extracto vaciado | /about/ | ✅ Hecho (la dirección sigue siendo /about/) |
| `post_content` con texto plano ES/EN | 12 páginas | ✅ Hecho. /caballeros/ va después de que Miguel pegue |

---

## 5. Cronología resumida

**28-sep, noche (parte 3)**
- Respaldo en hPanel y en el repo.
- C17, C18 (parcial), C20 (enlaces) y C21.
- Se detectaron ediciones en paralelo de otra persona. Desde entonces rige "un solo editor a la vez".

**28-sep, 22:54 a 23:33 (tanda 2)**
- C15 y C16.
- C9 a C12.
- W34.
- C4 y C5.
- C13 y C14.

**Madrugada del 29-sep**
- 00:12 a 00:28: C1 en las 12 páginas, W35 y W36.
- 00:30 a 00:35: texto plano en las 12 páginas.
- 00:36: revisión del SEO.
- 00:42: /about/, nombre interno y extracto.
- 00:48 a 01:04: se quitaron las etiquetas heredadas en 11 páginas.
- 01:0x: C19 preparado.

**Pausa**
- Miguel paró el trabajo.
- No se escribe /caballeros/ ni /checkout/ hasta el día siguiente.

---

## 6. Próximos pasos, en orden

1. **/caballeros/.** Miguel pega `para-pegar/caballeros-para-pegar.html` en el widget HTML de Elementor y avisa "ya lo pegué". El archivo incluye:
   - C1, C6 y C7;
   - las tres frases pasadas a tú;
   - la quita del `<title>` heredado.

   Después: borrar la caché, comparar byte a byte con el archivo, actualizar el texto plano y probar las dos ventanas sin enviar nada.
2. **/checkout/.** Con el "sí" de Miguel a C19, una sola escritura con C19 y la quita del `<title>` y la description. Después: caché, verificación y texto plano.
3. **C22.**
4. **En espera de terceros:**
   - C3: visto bueno de Miguel;
   - C8: decisión de Dirección;
   - C23: logo y colores;
   - la línea bajo el botón de pago, que espera los Términos;
   - el nombre del cobro en PayPal, que lo cambia Zafira.
5. **Capturas en vivo** (español, inglés y móvil). Las toma Miguel, porque este entorno no abre el sitio.

---

## 7. Observaciones abiertas

- **Descripciones SEO de las páginas legales.** All in One SEO genera las de /cancelaciones/ y /cancelaciones-es/ a partir del contenido de la página, y no son textos cuidados. Las decide Miguel si quiere fijarlas.
- **Imágenes de pasos que ya no se usan en /proceso/.** Siguen en la biblioteca de medios. No se borran, porque no se borra nada.

---

## 8. Archivos del repo

| Archivo | Qué contiene |
|---|---|
| `REPORTE-parte3.md` | Reporte de la primera sesión (C17, C18, C20, C21) |
| `TRASPASO-sesion-web-2026-09-29.md` | Traspaso al sistema que planea, con el método técnico |
| `INSTRUCCIONES-tanda-2-2026-09-29.md` | Instrucciones de la tanda 2 |
| `INSTRUCCIONES-W34-damas-portada.md` | Instrucciones de W34 |
| `INSTRUCCIONES-W35-W36-y-pie.md` | Instrucciones de W35, W36 y el pie |
| `NOTA-pie-y-terminos-2026-09-29.md` | Enlaces a /terminos/ en el pie; el contenido de términos no se toca |
| `PROPUESTA-terminos-2026-09-29.md` | Propuesta de cambios a los términos (no aplicada) |
| `REPORTE-tanda-2.md` | Registro detallado de cada paso con hora |
| `textos/` | Textos aprobados: W14, W19, W34, W35, W36 |
| `respaldo/2026-09-29/` | Copias de las páginas antes de cada cambio (webhook tapado) |
| `revision/` | Copia de texto de /terminos/ y /terminos-es/ |
| `para-pegar/caballeros-para-pegar.html` | HTML final de /caballeros/ para pegar en Elementor |
| `RESUMEN-proyecto-web-zafira.md` | Este resumen |
