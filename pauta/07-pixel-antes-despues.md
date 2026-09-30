# 07 · Píxel de Meta: antes → después (espera el "sí" de Miguel)

Estado: **preparado y probado en local. No instalado.** Nada se guarda sin el "sí".

## Bloqueo antes de instalar
**El píxel web todavía no existe.** El diagnóstico 06 lo confirma: el BM "Zafira Match Agency" solo tiene el dataset de WhatsApp, que nunca ha recibido eventos. Antes hay que:
1. Que un **administrador del BM de Zafira** cree el píxel "Zafira · Web" en el Administrador de eventos y lo asigne a **Zafira2026ADS (1097030029602749)**.
   - En su configuración: **coincidencia avanzada automática APAGADA** y sin API de conversiones.
   - Nosotros no lo creamos: la autorización es solo de lectura.
2. Que Zafira nos pase el **ID del píxel**. Va donde dice `PIXEL_ID`.

## Quién lo instala
- **WPCode no está disponible por el conector de WordPress**: sus fragmentos no aparecen en la API.
- **WPConsent tampoco**: sus ajustes no son visibles.
- Por eso lo **pega Miguel**, en dos pantallas del panel de WordPress. Toma unos 15 minutos.

## Respaldo (antes de tocar)
- **WPCode:** Miguel copia lo que haya hoy en *Code Snippets → Header & Footer → Header* (y en la lista de fragmentos) a un archivo o captura, y nos lo pasa. Lo guardamos en `respaldo/2026-09-30/`.
- **WPConsent:** captura de *Settings → Script Blocking* y de la lista de servicios del escáner.
- **Páginas:** **no se toca ninguna página.** /caballeros/ queda igual, porque los eventos se leen desde el propio fragmento.

## 1. WPCode: antes → después
**Antes:** no hay ningún código de Meta en el sitio (diagnóstico 06).

**Después:** un fragmento nuevo en **WPCode → Add Snippet → "Add Your Custom Code" → tipo HTML**:
- nombre "Zafira · Meta Pixel (web)";
- ubicación **Site Wide Header**;
- activo.

Código completo en `pauta/pixel-wpcode-snippet.html`. Qué hace:

| Página | Qué se envía (solo si la persona aceptó cookies de Marketing) |
|---|---|
| /damas/, /registro-candidata/, /privacidad-es/, /terminos-es/, /cancelaciones-es/ | **Nada.** El código se detiene antes de cargar el píxel |
| Resto de páginas | `PageView` |
| /caballeros/ | `PageView`; `ViewContent` al abrir la ventana de solicitud del caballero; `Lead` cuando aparece la pantalla "Solicitud recibida" de esa ventana. Una sola vez cada uno. **La ventana de candidatas no se mide** |

- **Sin datos personales:** solo `content_name: "solicitud_caballero"`. Nunca nombre, correo, teléfono ni respuestas del formulario.
- **Nota honesta:** la pantalla "Solicitud recibida" sale tanto si el envío por correo funciona como si cae al respaldo de WhatsApp. En el segundo caso, el Lead cuenta a alguien que abrió WhatsApp con su solicitud.

## 2. WPConsent: antes → después
**Antes:**
- Script Blocking prendido.
- Default Allow apagado.
- Google Consent Mode apagado.
- Hoy bloquea gtag de Site Kit y order-attribution de WooCommerce.

**Después:** mismo ajuste, y además comprobar que **`connect.facebook.net/en_US/fbevents.js`** queda bloqueado en la categoría **Marketing**.
- WPConsent reconoce el píxel de Facebook entre sus scripts conocidos y lo pone en Marketing. ([WPConsent](https://wpconsent.com/?p=745))
- Si no lo reconoce solo: **Script Blocking → Add custom script**, tipo *Script*, patrón `fbevents.js`, categoría **Marketing**.
- **No se cambia nada más:** ni Consent Mode, ni textos, ni el botón flotante.

## 3. Prueba en local (hecha, 30-sep)
Servidor local con las rutas reales y la red bloqueada. Esta prueba **no** incluye WPConsent; el bloqueo por consentimiento se verifica en vivo.

| Ruta | Resultado |
|---|---|
| /damas/ | Sin `fbq`, sin llamada a Facebook ✔ |
| /proceso/ | `init` + `PageView` ✔ |
| /caballeros/ | `init` + `PageView` + `ViewContent` (al abrir) + `Lead` (al llegar a "Solicitud recibida"). Al abrir la ventana de candidatas: **nada**. Al reabrir: **sin duplicados** ✔ |

## 4. Verificación en vivo después de instalar (Gisela o Miguel)
Se hace con navegador en incógnito, herramientas de desarrollador → Red, filtro "facebook":
1. **Sin tocar el banner:** 0 llamadas a `connect.facebook.net` y a `facebook.com/tr`. ← lo más importante
2. **"Rechazar":** 0 llamadas, también al recargar y al navegar.
3. **"Aceptar":** aparece `fbevents.js` y un `PageView` en `facebook.com/tr`.
4. **/damas/ después de aceptar:** 0 llamadas.
5. **/caballeros/ después de aceptar:** al abrir la ventana del caballero, `ViewContent`.
   - El `Lead` se prueba con **"Eventos de prueba"** del Administrador de eventos. **No se envía una solicitud real.**
   - Si hace falta ver el Lead, se simula en la consola del navegador sin enviar el formulario.
6. **/checkout/:** el botón de PayPal sigue cargando.

## 5. Tiempo
| Paso | Quién | Tiempo |
|---|---|---|
| Crear el píxel y asignarlo a la cuenta | Admin del BM de Zafira | 15 min |
| Respaldo, pegar el fragmento y revisar WPConsent | Miguel | 15–20 min |
| Verificación en vivo | Gisela o Miguel | 20 min |
| Verificar el dominio en el BM (hace falta para configurar eventos) | Miguel (meta etiqueta) o Zafira (DNS) | 1 día de propagación |

El píxel **no se usa en campañas** hasta que exista el permiso de citas.
