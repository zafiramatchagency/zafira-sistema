# Traspaso · sesión de cambios web de Zafira (29-sep-2026)

Para: el Claude que planea (sistema de pauta, repo `gusopenbrands/stanleydesarrollo`).
De: el Claude que ejecutó la Parte 3 con Miguel (E-leaders), vía el conector de WordPress (Easy MCP AI) de zafiramatchagency.com.
Horas en hora de Colombia (UTC−5). Repo de trabajo: `zafiramatchagency/zafira-sistema`, rama `claude/focused-volta-2k142j`.

## 1. Resumen en 5 líneas

1. Copia de seguridad hecha: respaldo manual en hPanel (~21:12 del 28-sep) + copia del contenido de las páginas en el repo (`respaldo/2026-09-29/`).
2. Publicados y verificados: **C17** (pantalla final del registro de candidatas) y **C20 (parte enlaces) + C21** (/confirmacion/).
3. **C18** parcial: los 8 artículos ya estaban en borrador; cerré comentarios y pingbacks en los 8. Faltan dos cosas a mano (ajuste general de comentarios y 8 redirecciones 301).
4. Pendiente a mano de Miguel: noindex y fuera del sitemap para /checkout/ y /confirmacion/ en All in One SEO (el conector no puede tocar AIOSEO).
5. Me detuve en **C9 (/proceso/)**: la tenía leída y respaldada, pero no la preparé ni la publiqué.

## 2. Estado real del sitio antes de empezar (difiere de la guía)

La guía se escribió con la verificación del 26-sep. El 27 y 28-sep alguien ya había aplicado parte de los cambios. Escaneo del 29-sep ~01:45 UTC sobre las 11 páginas publicadas:

| Frase a eliminar (guía) | ¿Seguía? |
|---|---|
| forms.app / "Formulario Documental" (C17) | No |
| Fiestas, yates, "sin cámaras", Gala (C10) | No |
| Testimonios / "Reseñas" (C15) | No |
| "video de presentación" (C16) | No |
| "networking", "mujeres excepcionales" (C13) | No |
| "vida nocturna", "yates" (C14) | No |
| "Selectas. Verificadas. Listas.", "El Evento Zafira" (C4) | No |
| "Tu Camino hacia Evento Zafira" (C5) | No |
| "Zafira Agency." / "S.A.S. · Cartagena" (C1) | No, pero los pies no son el texto W19 (ver §6) |
| **"STEP 01…06", "distinguidas, femeninas", alt="Zafira Diamond"** (C9, C12) | **Sí, en /proceso/** |
| **"El Programa ($13,000 USD)"** (C19) | **Sí, en /checkout/** |
| **"Hemos recibido tu pago"** (C21) | Sí → **ya corregido** |
| **"Perfil reservado", `PERFILES`** (C8) | **Sí, en /caballeros/** (esperando la decisión de Dirección) |
| "Privacy Policy" en pies | Sí, en casi todas las páginas (los pies cambian el enlace según el idioma con un script) |

Blog: los 8 artículos, la portada /blog y las 8 páginas viejas "-pagina-antigua" ya estaban en borrador. El único menú de WordPress, "Cabecera Astra (vacío)", ya estaba vacío. Ninguna página publicada enlaza al blog.

Plugins relevantes: All in One SEO 5.0.2, WPConsent (banner de cookies, ya instalado), WPCode Lite, Site Kit, WooCommerce + PayPal Payments, WPForms Lite, LiteSpeed Cache (inactivo). No hay plugin de redirecciones.

## 3. Lo que hice, cambio por cambio

| Código | Página | Qué se hizo | Hora | Estado |
|---|---|---|---|---|
| Respaldo | Todo | Contenido completo (post + meta + `_elementor_data`) de 11 páginas en el repo. Miguel creó el respaldo manual en hPanel (el próximo manual se puede crear el 29-sep a las 21:12) | 21:12 | Hecho |
| C17 | /registro-candidata/ (ID 172) | Pantalla final `successMsg` con el texto W01 exacto en ES y EN: título "Primer paso completado. Gracias por registrarte.", el texto de la asesora y "Recuerda: Zafira nunca te pedirá dinero." (reemplaza la nota de confidencialidad que había, por decisión de Miguel: "acorde al plan"). El formulario y el pie no se tocaron | 21:22 | Hecho, verificado |
| C18 | 8 artículos (IDs 966–973) | `comment_status` y `ping_status` pasados a closed. Siguen en borrador | 21:23 | Hecho |
| C18 | Ajustes → Comentarios | Cerrar comentarios y pingbacks por defecto. El conector no tiene esa opción | – | **Pendiente, a mano** |
| C18 | Redirecciones 301 | 8 URLs del blog → `https://zafiramatchagency.com/caballeros/`. En Hostinger había 0 redirecciones. El conector de Hostinger se conecta y desconecta de la sesión (tiene `hosting_redirects_create-website`; usuario `u184760597`) | – | **Pendiente** (hPanel → Redirecciones, o por el conector de Hostinger con el visto bueno de Miguel) |
| C20 | /confirmacion/ (ID 132) | "Comprobar si califico" (menú y menú móvil) ahora lleva a /caballeros/ en vez de /checkout/ | 21:28 | Hecho, verificado |
| C20 | /checkout/ (125) y /confirmacion/ (132) | noindex y fuera de page-sitemap.xml en AIOSEO (Avanzado → Robots → No indexar). Estado actual: `robots_noindex=false` en las dos | – | **Pendiente, a mano (Miguel)** |
| C21 | /confirmacion/ (ID 132) | Contenido principal cambiado por W13 exacto en ES y EN: agradecimiento, "Lo que sigue" (3), "Su camino" (5, con el texto oficial de fechas), "Recuerde…", "Si usted llegó… sin haber hecho un pago…", "¿Dudas? … Melany … +1 360 227 7352 …" y el botón "Volver a la página del programa" → /caballeros/. Ajuste técnico: protegí la línea del script que buscaba `#nameSpan` (el título "Bienvenido" se quitó). No se tocaron la etiqueta `planPill` ("Programa Zafira", va en C5) ni el pie (C1) | 21:28 | Hecho, verificado |

Verificación de C17 y C21: el `_elementor_data` guardado es idéntico (comparación JSON) al que preparé. En el HTML renderizado aparecen los textos nuevos y ya no aparecen "Registro recibido", forms.app, "Hemos recibido tu pago" ni /checkout/.

**Falta en todos:** las capturas ES/EN y en móvil del sitio en vivo. Este entorno no puede abrir zafiramatchagency.com (la red lo bloquea), así que las tiene que tomar Miguel o el sistema.

## 4. Orden de la guía: dónde quedamos

1. C17 ✅ · 2. C18 ◐ (faltan el ajuste general de comentarios y las redirecciones) · 3. C20 ◐ (falta noindex/sitemap en AIOSEO) · 4. C21 ✅ · **5. C9 ← siguiente** · 6. C10 · 7. C11 · 8. C12 · 9. C15 · 10. C16 · 11. C4 · 12. C5 · 13. C13 · 14. C14 · 15. C1 · 16. C6 · 17. C7 · 18. C19 · 19. C2 · 20. C22 · 21. C3 · 22. C8 (espera la decisión de Dirección) · 23. C23 (espera el logo y los colores).

Nota de la guía: C9 no se publica antes de C20. Los enlaces de C20 ya están, pero el noindex de /checkout/ sigue pendiente. Conviene que Miguel lo haga antes de publicar C9.

### Estado actual de /proceso/ (ID 167, leída 21:13; respaldo en `respaldo/2026-09-29/167-proceso.antes-C9.full.json`)
- La portada ya no es la del 26-sep: dice "Security & Selection / Every Connection Begins With Trust." (no es el texto W30).
- Pasos: etiquetas "STEP 01" a "STEP 06" en los dos idiomas. Contenido parcialmente reescrito, sin fiestas ni yates. El paso 5 tiene "$13,000 USD" y el 6, "The Cartagena Programme" (describe los cuatro momentos de C10).
- Hay un segundo bloque "hero" más abajo con alt="Zafira Diamond" (C12), "Welcome to the Zafira Experience", "Exclusive Private Event • Cartagena • October or November 2026 (dates to be confirmed)" (no es el texto oficial exacto) y "Not another dating event… distinguished, feminine, and accomplished women…" (C9). Su imagen es `zafira_luxury_chemistry.jpg` ("Luxury rooftop conversation", C11).
- Cierre: "Begin Your Evaluation" / "Take the first step toward an elevated reality…" (no está en la guía).
- Imágenes de los pasos: `step01.png` … `step06.png` en /wp-content/uploads/2026/05/ (revisar según C11).
- El W30 de la guía trae portada + intro + 5 pasos. Hay que decidir cómo encajar la estructura actual de 6 pasos y 2 heroes en el texto W30 sin agregar nada: probablemente reemplazar el hero superior y los 6 pasos por la portada y los 5 pasos de W30, y quitar el segundo hero (su texto queda cubierto por W30).

## 5. Cómo se edita esta web (método técnico que funcionó)

- Cada página es **un único widget HTML de Elementor**: un documento HTML completo en `_elementor_data[0].elements[0].settings.html`. El idioma se maneja con atributos `data-es` / `data-en` (y `data-es-html` / `data-en-html`, `data-*-ph`) y `localStorage.zafiraLang` (por defecto `en`, así que el texto visible por defecto va en inglés).
- Proceso por página:
  1. Leer la versión actual con `wp_get_post_full(context=edit, include=[meta])`.
  2. Hacer reemplazos exactos en Python, comprobando que cada texto aparece una sola vez.
  3. Escribir con `wp_update_post_meta({_elementor_data})`.
  4. Borrar `_elementor_element_cache` con `wp_delete_post_meta` (si no, Elementor sigue mostrando la versión vieja hasta 24 h).
  5. Volver a leer y comparar el JSON con lo esperado, y revisar `content.rendered`.
- `wp_replace_in_post` **no sirve**: solo toca `post_content`, y Elementor no lo usa para mostrar la página.
- El conector no puede modificar: los ajustes generales (Comentarios), la configuración de AIOSEO (noindex/sitemap) ni las redirecciones. Las copias de seguridad de hosting compartido tampoco existen en la API de Hostinger (solo para VPS).
- /checkout/ tiene incrustada la URL del webhook de Make (funciona como credencial). En las copias del repo está tapada con `[WEBHOOK-MAKE-REDACTADO]`.

## 6. Riesgos y observaciones (no tocados, regla 1)

- **Ediciones en paralelo.** Mientras trabajaba, alguien guardó desde el editor /registro-candidata/ (21:14), /confirmacion/ (21:12), /proceso/ (21:13) y /caballeros/ (21:25). Otra sesión con el mismo conector envió a la papelera las páginas 1162 y 1235 (28-sep, ~20:37 y ~20:52). Si alguien tiene Elementor abierto y guarda, puede pisar C17 y C21. Hay que coordinar un solo editor a la vez.
- Los pies de todas las páginas enlazan a `/terminos/` y `/terminos-es/`, que dan 404. La guía dice que no se enlacen mientras no existan (se corrige en C1).
- Los pies actuales dicen "Somos una agencia privada de matchmaking con procesos verificados" + NIT, "Cl 68 # 57-21, Of. 201", teléfono **+57 310 688 3682**. El W19 no incluye el teléfono de Colombia (Zafira todavía no decide si lo publica).
- `/blog/` (portada, en borrador) no está en la lista de redirecciones de la guía; se dejó como está.
- `post_content` (texto de respaldo de WordPress) de las páginas editadas conserva el texto viejo. Lo usan AIOSEO para las descripciones y el buscador interno. Conviene regenerarlo o fijar las descripciones SEO.
- La descripción SEO de /confirmacion/ dice "Your Zafira evaluation payment has been received…" (no está en la guía).
- WPConsent ya está instalado. Tenerlo en cuenta para C3 (puede evitar instalar otro plugin).

## 7. Lo que necesito de ti (Claude que planea) o de Miguel

1. Confirmar cómo encajar W30 en la estructura actual de /proceso/ (ver §4). Si hay versión nueva de W30, W09 o la guía, mandarla.
2. C10: ¿Zafira confirmó por escrito los cuatro momentos, o va el plan B?
3. C8: la opción que eligió Dirección.
4. Decidir si se redirige /blog/.
5. Miguel: ajuste general de comentarios, noindex de AIOSEO y las 8 redirecciones 301 (o dar el visto bueno para hacerlas por el conector de Hostinger).
6. Capturas en vivo ES/EN y móvil de /registro-candidata/ (pantalla final) y /confirmacion/.

## 8. Archivos en el repo

- `REPORTE-parte3.md`: tabla de control con horas y estado.
- `respaldo/2026-09-29/`: respaldo de 11 páginas antes de empezar, más las versiones antes de cada cambio: `172-registro-candidata.antes-C17-2114.full.json`, `132-confirmacion.antes-C20.full.json`, `167-proceso.antes-C9.full.json`.
- Este archivo.
