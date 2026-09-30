# 02 · Plan: píxel de Meta (y Tag Manager) detrás de WPConsent

Estado: **solo plan, no se instala nada**. Cada paso en el sitio necesita el "sí" de Miguel.

## Punto de partida (30-sep)
- **WPConsent 1.1.9 está activo**, configurado por Miguel. La verificación en vivo la hizo Gisela.
  - Script Blocking está prendido.
  - Default Allow está apagado.
  - **Google Consent Mode está apagado.**
- Antes de aceptar ya no sale ninguna llamada a Google Analytics: WPConsent retiene gtag de Site Kit y order-attribution de WooCommerce.
- **No hay píxel web de Meta.** Diagnóstico 06: el único dataset es el de WhatsApp, que nunca ha recibido eventos.
- **No hay GTM** en el sitio.
- **WPCode Lite está activo.** Sirve para insertar el código sin tocar las páginas.
- **Modo básico** = nada de Meta ni de GTM carga ni envía datos antes de que la persona acepte. Si rechaza o ignora el banner, nunca carga.

## Recomendación: píxel directo, sin GTM (opción A)
- GTM no aporta nada con un solo píxel y agrega una capa más que bloquear.
- Con Consent Mode apagado, WPConsent bloquearía el contenedor GTM **entero** en una sola categoría. La propia documentación de WPConsent explica que el bloqueo de GTM asigna todo el contenedor a una categoría. ([WPConsent, bloqueo de scripts](https://wpconsent.com/?p=745))
- GTM queda como **opción B** para más adelante, si se suman más etiquetas.

### Opción A: pasos (con el "sí" de Miguel)
| # | Paso | Quién | Tiempo |
|---|---|---|---|
| 1 | Crear el **píxel/dataset web** "Zafira · Web" en el BM "Zafira Match Agency" y **asignarlo a Zafira2026ADS** | Admin del BM (Zafira) | 15 min |
| 2 | **Verificar el dominio** zafiramatchagency.com en el BM. Opción meta etiqueta: Miguel la pone con WPCode o AIOSEO. Opción DNS: Zafira; nosotros no tocamos el DNS | Miguel o Zafira | 1 día (propagación) |
| 3 | En la configuración del píxel: **"Coincidencia avanzada automática" APAGADA** y **sin API de conversiones**. No se envían correo, teléfono ni nombre | Admin del BM | 10 min |
| 4 | Snippet del píxel en **WPCode** (cabecera), con carga en **todas las páginas excepto** /damas/, /registro-candidata/, /privacidad-es/, /terminos-es/ y /cancelaciones-es/. Las páginas de candidatas no llevan píxel: no se crean públicos con mujeres y se evita cualquier señal sensible | Miguel (o Claude por el conector, con su "sí") | 30 min |
| 5 | En WPConsent: confirmar que el escáner reconoce `connect.facebook.net/.../fbevents.js` y lo pone en **Marketing**. Si no lo reconoce, crear una regla de bloqueo personalizada con esa cadena en la categoría Marketing. ([WPConsent](https://wpconsent.com/?p=745)) | Miguel | 20 min |
| 6 | **Eventos:** PageView automático. `ViewContent` al abrir la ventana de solicitud en /caballeros/. `Lead` solo cuando la solicitud se envía bien, cuando aparece el paso 4 "Solicitud recibida" y el envío por correo respondió OK. **Sin datos personales en los parámetros**; solo `content_name: "solicitud_caballero"` | Claude prepara el cambio; Miguel pega o aprueba | 1 h |
| 7 | **Prueba**, con la herramienta "Eventos de prueba" del Administrador de eventos y el navegador en modo incógnito: (a) sin aceptar: 0 llamadas a facebook.net ni a facebook.com/tr; (b) al rechazar: 0; (c) al aceptar: PageView; (d) solicitud de prueba: **no se envía** una solicitud real; el Lead se prueba con el código de prueba del Administrador de eventos | Gisela o Miguel | 1 h |
| 8 | Anotar en el reporte y dejar el píxel **sin usar** en campañas hasta que haya permiso de citas | Claude | — |

**Tiempo total: 2 días hábiles**, contando la verificación del dominio. Depende de que Zafira cree el píxel y dé acceso.

### Código de referencia (no se instala todavía)
```html
<!-- Meta Pixel · Zafira · Web · lo bloquea WPConsent (Marketing) hasta que la persona acepte -->
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','PIXEL_ID');   /* ← el ID lo da Zafira al crear el píxel */
fbq('track','PageView');
</script>
```
En /caballeros/, el evento Lead va en el mismo punto donde hoy se muestra el paso 4:
```js
if (window.fbq) fbq('track','Lead',{content_name:'solicitud_caballero'});
```
Si la persona no aceptó, `fbq` no existe y no se envía nada.

## Opción B: GTM (solo si más adelante hacen falta varias etiquetas)
- Un contenedor GTM nuevo en una cuenta de Zafira. El snippet va en WPCode.
- WPConsent bloquea `googletagmanager.com/gtm.js` en **Marketing**.
- Dentro de GTM, el píxel de Meta con los mismos eventos.
- **Advertencia:** Consent Mode está apagado, así que todo el contenedor queda bajo una sola categoría. No se puede meter Analytics ("Estadísticas") en el mismo contenedor sin volver a prender Consent Mode, y eso lo decide Miguel.
- Tiempo: 3 días hábiles.

## UTM para saber de dónde viene cada solicitud (para N06)
- Hoy el formulario de /caballeros/ **no guarda las UTM**.
- Propuesta para más adelante, con el "sí" de Miguel: guardar `utm_source`, `utm_medium` y `utm_campaign` en sessionStorage y añadirlas como filas ocultas al resumen que se envía por correo.
- Es un cambio en /caballeros/, así que Miguel tendría que volver a pegar la página.
- Alternativa sin tocar el sitio: preguntar "¿Cómo nos conoció?" en la llamada y anotarlo en N06.

## Lo que no se hace
- No se envían datos personales a Meta: ni coincidencia avanzada, ni API de conversiones con correo o teléfono.
- No va píxel en las páginas de candidatas.
- No se prende Google Consent Mode sin decisión de Miguel.
- No se toca PayPal ni /checkout/.
