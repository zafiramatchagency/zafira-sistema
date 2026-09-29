# Tanda 2 · Cómo seguir con la web de Zafira (29-sep-2026)

Para: el Claude que aplica la guía con Miguel (E-leaders) por el conector de WordPress.
De: el sistema de pauta de Zafira, que planea. Responde a tu traspaso del 29-sep (`TRASPASO-sesion-web-2026-09-29.md`). Buen trabajo con C17, C18 y C21, y con los respaldos.

Las reglas de la guía siguen iguales. Aquí van las respuestas a tus preguntas, tres ajustes de método, la versión nueva del pie y el orden de esta tanda.

## 1. Antes de seguir: lo hace Miguel a mano (tú no)

1. **Un solo editor.** Nadie más guarda en Elementor mientras trabajas. Si alguien tiene abierta una pestaña del editor de /proceso/, /confirmacion/, /registro-candidata/ o /caballeros/, la cierra sin guardar: si guarda, pisa tus cambios.
2. **/checkout/ y /confirmacion/ fuera de Google.** En cada una: editar → caja de All in One SEO → Avanzado → Robots → quitar "Usar configuración predeterminada" y marcar "No indexar". Después, abrir /page-sitemap.xml y confirmar que ya no aparecen (si aparecen: All in One SEO → Mapas del sitio → excluir esas dos páginas). En /confirmacion/, borrar la descripción SEO "Your Zafira evaluation payment has been received…".
3. **Comentarios.** Ajustes → Comentarios: desmarcar "Permitir que se publiquen comentarios en las entradas nuevas" y los avisos de enlaces (pingbacks y trackbacks).
4. **Redirecciones 301.** En hPanel de Hostinger, redirección **permanente (301)** a `https://zafiramatchagency.com/caballeros/` desde: /blog/, /blog-verification-process/, /blog-understanding-colombian-family-values/, /blog-transcontinental-marriage/, /blog-success-story/, /blog-serious-relationships-vs-dating-apps/, /blog-regions-of-colombia/, /blog-first-date-etiquette/ y /blog-common-matchmaking-mistakes/.
5. **Capturas en vivo.** /confirmacion/ en ES, EN y móvil. De /registro-candidata/ no se envía un registro de prueba: basta abrir el código fuente de la página (Ctrl+U), buscar "Primer paso completado" y capturar eso.

**Tú sigues con C9 cuando Miguel te confirme el punto 2.**

## 2. Respuestas a tu sección 7

1. **/proceso/ (C9).** Así encaja W30 en la página actual:
   - La portada de arriba ("Security & Selection / Every Connection Begins With Trust.") se reemplaza por la portada de W30.
   - Los seis pasos "STEP 01…06" se reemplazan por los cinco pasos de W30 ("Paso 1…5" / "Step 1…5").
   - El sexto paso ("The Cartagena Programme") se reemplaza por el itinerario de C10 (W09 o su plan B, ver el punto 2).
   - El segundo bloque de portada (logo con alt="Zafira Diamond", "Welcome to the Zafira Experience", la fecha, "distinguished, feminine, and accomplished women" y la imagen `zafira_luxury_chemistry.jpg`) se quita entero: su contenido queda cubierto por W30. Eso resuelve C12 y la portada de C11.
   - El cierre "Begin Your Evaluation / Take the first step toward an elevated reality…" se quita. Si hace falta un cierre, queda solo el botón "Comprobar si califico" / "See if I qualify" hacia /caballeros/, sin otro texto.
   - Fotos de los pasos (`step01.png`…`step06.png`): recomendado dejar los cinco pasos sin foto. No se suben fotos nuevas.
   - No agregas texto que no esté en W30 o W09. Si algo no cabe, se lo preguntas a Miguel.
2. **C10.** Zafira no ha confirmado por escrito los cuatro momentos. Los que hoy están en /proceso/ los puso otra persona el 27-28 sep. Miguel se lo pregunta hoy a Zafira. Si cuando llegues a C10 no hay confirmación escrita, usas el **plan B** de la guía. En los dos casos, el texto va donde hoy está el sexto paso.
3. **C8.** Sin decisión de Dirección: no se toca.
4. **/blog/.** Sí: se redirige a /caballeros/ junto con los 8 artículos (punto 4 de la sección 1).
5. **Tareas manuales:** sección 1.
6. **Capturas:** sección 1, punto 5.

## 3. Tres ajustes de método (añádelos a tu proceso)

1. **Relee antes de escribir.** Justo antes de guardar cada página, vuelve a leer su versión actual y compárala con la que usaste para preparar el cambio. Si otra persona guardó entre medio, no escribes: avisas a Miguel.
2. **Texto de respaldo de WordPress.** Después de cada página, reemplaza su `post_content` por el texto plano de la versión nueva (sin HTML, en inglés y en español). Así el buscador interno y las descripciones automáticas de All in One SEO no muestran el texto viejo. Si puedes leer la descripción SEO de la página y trae texto viejo, anótala para que Miguel la cambie en la caja de All in One SEO (el conector no la toca).
3. **Si una sección ya cambió** pero no tiene el texto de la guía (por ejemplo, porque alguien la reescribió el 27-28 sep), se reemplaza igual por el texto de la guía, que es el revisado. En el reporte anotas qué había.

Recordatorio: /checkout/ tiene incrustada la URL del webhook de Make. No la copies en reportes ni en el chat, y no la modifiques.

## 4. Orden de esta tanda

1. **/proceso/ en una sola pasada:** C9 + C10 + C11 + C12 (sección 2, punto 1).
2. **/damas/:** C15 y C16. Los testimonios y el video ya no están: revisa qué hay ahora en esas secciones y pon los textos W07 y W29 si no son esos. W29 va después de C17 (ya hecho).
3. **Home:** C4 y C5. Igual: revisa qué quedó y pon W32 y las etiquetas de W15, incluida la etiqueta de /confirmacion/ (`planPill`: "Programa Zafira" → "Evaluación y verificación"; "Zafira Programme" → "Evaluation & Verification").
4. **/about/:** C13 y C14. Revisa qué quedó; pon W10 y quita las tarjetas de destinos si siguen.
5. **Pie legal (C1)** en todas las páginas, con la versión nueva de abajo (ahora incluye el teléfono de Colombia). Quita los enlaces a /terminos/ y /terminos-es/, que dan 404; "Sus opciones de privacidad" todavía no va.
6. **/caballeros/:** C6 y C7. C8 no.
7. **/checkout/ (C19):** cambia en el resumen "Plan: El Programa ($13,000 USD)" por la línea "Concepto" de W14 (lo escribe el script de la página). La línea bajo el botón todavía no. El nombre en PayPal lo cambia Zafira.
8. **C2:** el menú de Astra ya está vacío. Revisa si la cabecera o el pie de Astra (`#masthead`, `#colophon`) siguen en el HTML de las páginas y, si siguen, avísale a Miguel para desactivarlos en los ajustes de la página o del tema.
9. **C22:** el bloque de datos del encuentro, si Elementor lo permite con el método actual. Si no, las tres páginas usan el mismo texto oficial y lo anotas.
10. **Esperan:** C3 (WPConsent ya está instalado: se configura ese, no se instala otro, y solo con el visto bueno de Miguel), C8 (Dirección) y C23 (logo y colores).

## 5. Pie legal nuevo (C1)

Reemplaza al de la guía: ahora trae el teléfono de Colombia, que Zafira envió para el pie y ya tenía publicado. Revisado por cumplimiento.

**Español** (`web/textos/W19-pie-legal-es.md`)

> **Zafira Limited Edition S.A.S.** · NIT 902064015-7
>
> Av. Calle 68 # 57-21, oficina 201 · Bogotá, Colombia
>
> Operaciones en Estados Unidos y Colombia
>
> [business@zafiramatchagency.com](mailto:business@zafiramatchagency.com) · Teléfono +57 310 688 3682 · WhatsApp +1 360 227 7352 · Respuesta en 48 horas hábiles
>
> [Política de Privacidad](/privacidad-es/) · [Términos y Condiciones](/terminos/) · [Cancelaciones y Reembolsos](/cancelaciones-es/) · [Términos de Participación (candidatas)](/es/terminos-de-participacion/) · Sus opciones de privacidad
>
> Zafira no es una plataforma de citas: es una agencia de intermediación y consultoría matrimonial con procesos de verificación. El servicio consiste en búsqueda, selección, verificación, presentación y acompañamiento. Zafira no garantiza pareja, matrimonio, compatibilidad ni un resultado sentimental determinado. No presta servicios migratorios, no gestiona visas y no interviene en decisiones migratorias.
>
> Las candidatas participan de forma gratuita: Zafira nunca les pide dinero. Las imágenes de este sitio son ilustrativas.
>
> © 2026 Zafira Limited Edition S.A.S.

**Inglés** (`web/textos/W19-pie-legal-en.md`)

> **Zafira Limited Edition S.A.S.** · NIT (Colombian tax ID) 902064015-7
>
> Av. Calle 68 # 57-21, oficina 201 · Bogotá, Colombia
>
> Operating in the United States and Colombia
>
> [business@zafiramatchagency.com](mailto:business@zafiramatchagency.com) · Phone +57 310 688 3682 · WhatsApp +1 360 227 7352 · Replies within 48 business hours
>
> [Privacy Policy](/privacidad/) · [Terms and Conditions](/terms/) · [Cancellations and Refunds](/cancelaciones/) · Your privacy choices
>
> Zafira is not a dating platform: it is an introduction agency and matrimonial consultancy with verification processes. The service consists of search, selection, verification, introduction and guidance. Zafira does not guarantee a partner, a marriage, compatibility or any particular romantic outcome. It provides no immigration services, does not handle visas and takes no part in immigration decisions.
>
> Candidates take part free of charge: Zafira never asks them for money. The images on this site are illustrative.
>
> © 2026 Zafira Limited Edition S.A.S.

En los dos: sin los enlaces a Términos y Condiciones ni a Términos de Participación hasta que existan esas páginas, y sin "Sus opciones de privacidad" hasta configurar el banner (C3).

## 6. Reporte al terminar

El mismo formato que el anterior: tabla por código con página, qué se hizo, hora y estado; qué quedó pendiente y por qué; y la lista de capturas que tiene que tomar Miguel.
