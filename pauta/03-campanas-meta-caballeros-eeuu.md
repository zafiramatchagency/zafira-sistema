# 03 · Estructura de campañas de Meta: caballeros en EE. UU. (en pausa)

Estado: **solo en papel**.
- Se crea en el Administrador de anuncios **únicamente** después del permiso de citas, y **en estado pausado**.
- Nada se publica sin el "sí" de Miguel y de Zafira.
- Cuenta: **Zafira2026ADS (1097030029602749)**, en COP.
- Página: **Zafira Match Agency (1068627986343169)**. Antes hay que vincularla a la cuenta (diagnóstico 06).
- **Presupuestos: no se inventan.** Quedan como `[PRESUPUESTO_ZAFIRA]` hasta que Zafira los fije.

## Reglas de los textos (antes de cualquier anuncio)
**De Meta** (política de citas y de atributos personales):
- solo mayores de 18;
- nada sexual ni transaccional;
- no afirmar ni insinuar atributos del público: nada de "¿Está soltero?", "divorciado", "mayor de 40", religión o ingresos;
- sin personas ficticias.

**Del proyecto:**
- no se usan "event(s)/evento(s)", "experience(s)/experiencia(s)", "Latina/latinoamericana(s)", "brides/novias", "mail-order", "catalogue" ni "women" como producto;
- no se prometen resultados, visas ni cupos (los cupos están "por confirmar");
- **no hay fotos de mujeres ni de candidatas**;
- el precio se dice como en la web.

**Honestidad:** el anuncio dice que el servicio es EE. UU. y Colombia. No se esconde lo internacional.

## Estructura
```
Campaña  ZAF · Caballeros EE.UU. · Solicitudes · Cartagena 2026      [PAUSADA]
│  Objetivo: Clientes potenciales · ubicación de conversión: sitio web · evento: Lead (píxel del documento 02)
│  Presupuesto: [PRESUPUESTO_ZAFIRA] diario, a nivel de campaña (Advantage+ campaign budget)
│  Categoría especial: ninguna (citas no es categoría especial; el permiso es aparte)
│
├── Conjunto A · Amplio EE.UU.                                          [PAUSADO]
│     País: Estados Unidos · Edad: 35–64 como CONTROL (no como sugerencia) · Sexo: hombres
│     Idioma: inglés · Sin intereses (que optimice el evento Lead)
│     Ubicaciones: Facebook e Instagram (feed, stories, reels) · sin Audience Network ni Messenger
│
├── Conjunto B · Intereses                                              [PAUSADO]
│     Igual que A + intereses neutros de viaje y estilo de vida (p. ej. "Luxury travel", "Cartagena", "Colombia (travel)")
│     Sin intereses sensibles ni de "citas internacionales"
│
└── Conjunto C · Visitantes de /caballeros/ (30 días)                   [PAUSADO]
      Público personalizado del píxel (solo personas que aceptaron cookies) · excluye a quien ya envió solicitud (Lead 180 días)
      Solo se enciende cuando el público tenga más de 1.000 personas
```
- **Destino:** `https://zafiramatchagency.com/caballeros/?utm_source=meta&utm_medium=paid_social&utm_campaign=ctg26_caballeros&utm_content={{ad.name}}`
- **Creatividades:** tarjetas tipográficas en negro y dorado de la marca, sin personas. Opcional: arquitectura de Cartagena **sin gente**. Formatos 1:1, 4:5 y 9:16.
- **Si el volumen de Lead es muy bajo** (menos de 10 por semana): cambiar la optimización a "Visitas a la página de destino" durante 7 días y volver a Lead. Lo decide Miguel.

## Anuncios (inglés, EE. UU.)
**A1 · Criterio**
- Texto: Zafira doesn't hand you a list. We search on your behalf, verify every person, and make an introduction only when both sides agree. Private, by invitation, with a matchmaker who answers by name. Applying is free, takes about 4 minutes and involves no commitment.
- Título: You are hiring judgment, not access
- Descripción: Private matchmaking · United States & Colombia
- Botón: Learn more

**A2 · Claridad de precio**
- Texto: Two stages, stated before any charge: a USD 400 evaluation and verification, then a USD 13,000 programme only if you are approved. Applying costs nothing. No packages, no fine print, and no promised romantic outcome.
- Título: Know the full cost before you pay
- Descripción: Private matchmaking · United States & Colombia
- Botón: Learn more

**A3 · Discreción**
- Texto: Your name appears on no public page. Your file is seen only by the team working your case. Every introduction is private, prepared in advance and accepted by both people.
- Título: Discretion is a set of rules, not a promise
- Descripción: Private matchmaking · United States & Colombia
- Botón: Apply now

**A4 · Cartagena**
- Texto: The programme includes a private gathering in Cartagena, October–November 2026, accompanied by the Zafira team. Exact dates, venue and places to be confirmed. It starts with a free application.
- Título: Private matchmaking, accompanied in person
- Descripción: Cartagena · October–November 2026
- Botón: Learn more

*(Opcional, para hispanohablantes en EE. UU. y en "usted": las mismas cuatro piezas en español. Salen de los textos aprobados de /caballeros/ y se preparan si Zafira lo pide.)*

## Revisión de vocabulario
- Hice una revisión automática contra la lista de términos prohibidos del proyecto (script `revisar-vocabulario.py`, resultado en `revision-vocabulario-03.txt`).
- **Falta la revisión oficial** del revisor de vocabulario y cumplimiento del sistema de pauta antes de subir nada.

## Tiempo
- Documento: listo hoy.
- Crear los borradores pausados en el Administrador de anuncios: **1 día**, cuando llegue el permiso y esté el píxel.
- Revisión de anuncios de Meta: normalmente **24 h** después de enviarlos, que solo se hace con el "sí".
