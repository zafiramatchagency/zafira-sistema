# 06 · Diagnóstico de la cuenta de Meta de Zafira (solo lectura)

Fecha: 30-sep-2026, entre las 08:3x y las 08:4x (hora de Bogotá).
Autorización: Miguel, **solo lectura**.
Método: conector de Meta Ads (herramientas de consulta).
- No se creó, editó, activó, pausó ni borró nada.
- No se tocaron pagos, permisos, usuarios ni configuración.
- No se envió ninguna solicitud a Meta.

**Límite importante del conector:** muestra cuentas, campañas y anuncios, páginas, datasets y la Biblioteca de anuncios. **No** muestra:
- el método de pago, el saldo ni el límite de gasto de la cuenta;
- las restricciones de la cuenta, la página o el BM ("Calidad de la cuenta");
- el motivo de rechazo de un anuncio;
- las solicitudes de permisos especiales, como la de citas;
- los usuarios y roles.

Esos puntos quedan marcados **"no visible por el conector"**, con dónde los ve el administrador.

## 1. Cuenta
| Dato | Resultado |
|---|---|
| Nombre | **Zafira2026ADS** |
| ID | **1097030029602749** |
| Business Manager dueño | **"Zafira Match Agency"** (ID 28082287311365681) |
| ¿A nombre de Zafira Limited Edition S.A.S.? | **No confirmado.** El conector solo da el nombre visible del BM ("Zafira Match Agency"), no el nombre legal ni si el negocio está verificado. Se ve en Configuración del negocio → Información del negocio / Centro de seguridad |
| Estado | **ACTIVE** |
| Moneda | **COP** · zona horaria America/Bogota |
| Método de pago | El conector solo dice que **tiene un método de pago cargado** ("has_payment_method: true"). El tipo (tarjeta o PayPal) y los últimos dígitos no son visibles |
| Saldo pendiente | No visible por el conector (Facturación → Actividad de pagos) |
| Límite de gasto de la cuenta | No visible por el conector (Configuración de pagos → Límite de gasto de la cuenta) |
| Gasto histórico | **0 anuncios** en esta cuenta: ni activos, ni pausados, ni rechazados, ni borrados, ni archivados. El historial de actividad desde el 1-ene-2025 está **vacío** |

**Otras cuentas que ve el conector:**
- **1319526703722123**, del mismo BM "Zafira Match Agency". Está activa, en AED, con método de pago. El conector la marca "no habilitada" y no se consultó. **Revisar por qué hay una segunda cuenta en dírhams.**
- **122178923**, "Johan Sebastian". Es una cuenta personal, sin BM, en COP. **No es de Zafira y no se consultó**, porque la autorización es solo para la cuenta de Zafira.

## 2. Restricciones
- **Cuenta 1097030029602749:** estado ACTIVE. El historial de la cuenta está vacío: no hay cambios de estado ni rechazos registrados desde el 1-ene-2025.
- **Página y BM:** no visible por el conector. Se revisa en **Calidad de la cuenta** (business.facebook.com/accountquality), que muestra las restricciones activas y pasadas con su fecha.

## 3. Rechazos y los anuncios de julio y agosto
En la Biblioteca de anuncios, la página **Zafira Match Agency** (ID 1068627986343169) tiene **3 anuncios**, no 2. Los tres son en COP y los tres **empezaron a circular**, es decir, pasaron revisión al menos al principio:

| ID en la Biblioteca | Creado (Bogotá) | Empezó a circular | Título del enlace |
|---|---|---|---|
| 1965234627514579 | 29-jul-2026 14:37 | 29-jul-2026 16:16 | (sin título) |
| 1356521832648837 | 2-ago-2026 13:11 | 2-ago-2026 14:38 | (sin título) |
| 1357233529371086 | 9-ago-2026 21:58 | 9-ago-2026 23:31 | "Chatea con nosotros" |

- **Ninguno salió de Zafira2026ADS**, que tiene 0 anuncios. Salieron de otra cuenta: la de AED (1319526703722123), la personal "Johan Sebastian" (COP) u otra con acceso a la página, por ejemplo una promoción hecha desde la propia página.
- **Motivo exacto de rechazo:** no visible por el conector. La Biblioteca de anuncios no publica rechazos, y los anuncios de la cuenta de Zafira no existen. Para tener el texto exacto de la política citada, el administrador de la cuenta que los publicó debe abrir **Calidad de la cuenta** o el **Administrador de anuncios → anuncio → "Ver detalles del rechazo"** y copiarlo tal cual.
- **"Chatea con nosotros"** apunta a un anuncio de mensajes, a WhatsApp o Messenger. Encaja con el dataset de WhatsApp del punto 5.

## 4. Permiso de anuncios de citas
- No visible por el conector.
- Indicios: la cuenta de Zafira nunca tuvo anuncios, y no hay registro de revisión en su historial.
- Si alguien lo pidió, habrá un correo de Meta en el buzón del administrador, o una entrada en el Servicio de ayuda para empresas (Business Support Home).

## 5. Píxel o dataset
| Dato | Resultado |
|---|---|
| Datasets del BM | **1**: "WhatsApp Marketing Message Event Sharing", ID **3403459569823863**, creado el 4-ago-2026 |
| ¿Es un píxel web? | **No.** Es el dataset de eventos de mensajes de WhatsApp |
| ¿Recibe eventos? | **Nunca ha recibido ninguno**: last_fired_time y server_last_fired_time están vacíos (1969) |
| ¿Conectado a Zafira2026ADS? | **No.** La cuenta no tiene ningún dataset asignado |
| ¿Instalado en zafiramatchagency.com? | **No.** Tampoco hay rastro de píxel en el HTML de las páginas que revisamos, ni en la lista de plugins |

**Conclusión:** hoy **no existe píxel web**. Hay que crearlo (plan en el documento 02).

## 6. Página de Facebook e Instagram
- **Página del BM:** "Zafira Match Agency", ID 1068627986343169.
- **Página vinculada a Zafira2026ADS:** ninguna, según la lista de páginas promocionadas de la cuenta. Es normal si la cuenta nunca publicó.
- **Instagram conectado a Zafira2026ADS:** ninguno, según la lista del conector. Otra posibilidad es que el conector no tenga permiso de Instagram.
- **Instagram del BM:** no visible por el conector (Configuración del negocio → Cuentas de Instagram).

## 7. Accesos
No visible por el conector. Lo ve un administrador del BM en **Configuración del negocio → Usuarios → Personas** y en **Cuentas → Cuentas publicitarias → Zafira2026ADS → Personas asignadas**.

La única pista del conector es que la persona conectada ve también una cuenta personal llamada "Johan Sebastian". Por eso, quien dio acceso al conector es, con alta probabilidad, un usuario del BM de Zafira. No podemos confirmar su rol.

## Qué impide hoy pedir el permiso de citas y qué arreglar antes
1. **No sabemos por qué rechazaron los anuncios.** Los de julio y agosto no salieron de la cuenta de Zafira. Hay que saber desde qué cuenta salieron y copiar el motivo exacto; se ve en la cuenta que los publicó.
2. **Hay tres cuentas en juego** (Zafira COP, Zafira AED y una personal). Hay que decidir que toda la pauta de Zafira sale solo de **Zafira2026ADS** (1097030029602749) y dejar de promocionar desde otras cuentas o desde la página. Una solicitud de permiso para una cuenta mientras se pauta desde otra es mala señal.
3. **Falta confirmar la verificación del negocio** y que el BM esté a nombre de **Zafira Limited Edition S.A.S.**, con Cámara de Comercio y RUT.
4. **La página no está vinculada a la cuenta publicitaria** y no hay Instagram conectado. Hay que vincular la página "Zafira Match Agency", y el Instagram si existe, a Zafira2026ADS.
5. **No hay píxel web ni dominio verificado.** No bloquea la solicitud, pero hace falta antes de lanzar. Plan en el documento 02.
6. **Pendientes del sitio que el revisor verá:** los Términos y Condiciones siguen pendientes de Dirección.
7. **Quién envía:** un administrador con control total del BM "Zafira Match Agency".

**Todo esto lo hace Zafira o su administrador en Meta. Nosotros no tocamos nada.**
