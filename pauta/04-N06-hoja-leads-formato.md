# 04 · N06: hoja privada de solicitudes de caballeros (formato)

Estado: **formato listo; la hoja no está creada.** Se crea el mismo día en que Zafira nombre al responsable.

## Dónde y quién
- **Dónde:** Google Sheets en la cuenta de Google **de Zafira**, no en cuentas personales ni de E-leaders. Nombre: "N06 · Solicitudes caballeros · PRIVADO".
- **Acceso:**
  - el responsable que nombre Zafira, como editor;
  - Melany (matchmaker), como editora, si Zafira lo decide;
  - Miguel, en solo lectura, si Zafira lo autoriza.
  - Sin enlace público. Sin "cualquiera con el enlace".
- **Entrada de datos:** hoy las solicitudes llegan **por correo** a business@zafiramatchagency.com, por el endpoint propio del sitio, con WhatsApp de respaldo. El responsable copia cada solicitud en una fila. Automatizarlo (del correo a la hoja) es un paso posterior y aparte, con su propio "sí".
- **Base legal:** Ley 1581 de 2012 y la Política de Privacidad publicada. La persona autorizó el tratamiento en el paso 2 del formulario.
  - Datos mínimos: los que se piden en el formulario, más el seguimiento.
  - **Nada de datos sensibles:** ni salud, ni religión, ni orientación, ni finanzas personales.
- **Candidatas (mujeres): nunca en esta hoja.** Van en un registro aparte, con su propio responsable.

## Pestaña 1 · "Solicitudes" (una fila por caballero)
| Columna | Tipo | Notas |
|---|---|---|
| A · ID | Texto | `CAB-2026-0001`, correlativo |
| B · Fecha de recepción | Fecha y hora (Bogotá) | Hora del correo |
| C · Canal | Lista | web-orgánico · meta · newsletter · podcast · creador · whatsapp-directo · referido · otro |
| D · Campaña / UTM | Texto | `utm_campaign` y `utm_content`, si llegan; si no, lo que diga en la llamada |
| E · Nombre | Texto | Como lo escribió |
| F · Correo | Texto | |
| G · Teléfono / WhatsApp | Texto | Con indicativo |
| H · Edad | Número | Para confirmar que es mayor de edad; no se usa para nada más |
| I · Ocupación | Texto | |
| J · Ciudad y país | Texto | |
| K · ¿Puede viajar a Colombia? | Lista | sí · no · no sabe |
| L · Qué busca (paso 1) | Texto | La opción que eligió |
| M · Autorización de datos | Casilla + fecha | Aceptó la Política de Privacidad en el formulario |
| N · Estado | Lista (pestaña 2) | |
| O · Responsable | Lista | Personas nombradas por Zafira |
| P · Primer contacto | Fecha y hora | **Meta: menos de 48 h hábiles** (lo que promete la web) |
| Q · Horas hasta el primer contacto | Fórmula | `=NETWORKDAYS(B;P)` o cálculo en horas; en rojo si pasa de 48 h hábiles |
| R · Próximo paso | Texto corto | |
| S · Fecha del próximo paso | Fecha | |
| T · Evaluación USD 400 | Lista + fecha | no aplica · enlace enviado · pagada (fecha) |
| U · Verificación | Lista | pendiente · en curso · completa · no superada |
| V · Decisión | Lista + fecha | aprobado · no aprobado |
| W · Programa USD 13.000 | Lista + fecha | no aplica · contrato enviado · pagado (fecha) |
| X · Encuentro Cartagena | Lista | no aplica · interesado · confirmado |
| Y · Notas | Texto | Solo hechos del proceso. **Nada de opiniones sobre la persona ni datos sensibles** |
| Z · Fecha de baja / eliminación | Fecha | Si pide que se borren sus datos: se borra la fila y queda solo el ID con la fecha |

## Pestaña 2 · "Estados" (lista cerrada, en este orden)
1. Nuevo
2. Contactado
3. En revisión preliminar
4. No encaja (fin)
5. Apto para evaluación
6. Evaluación pagada
7. Verificación en curso
8. Aprobado
9. No aprobado (fin)
10. Contrato enviado
11. Programa pagado
12. Descartado por el caballero (fin)
13. Sin respuesta tras 3 intentos (fin)

## Pestaña 3 · "IMBRA" (acceso restringido: solo el responsable y Melany)
Una fila por caballero **aprobado**, antes de compartir cualquier dato de contacto con una candidata:

| Columna | Qué se registra |
|---|---|
| ID caballero | El de la pestaña 1 |
| Búsqueda en registros de agresores sexuales (fecha, fuente) | Sí/No + fecha |
| Declaración de antecedentes penales y estado civil recibida | Sí/No + fecha |
| Información entregada a la candidata en español (fecha) | Sí/No + fecha |
| Consentimiento escrito de la candidata para compartir contacto (fecha) | Sí/No + fecha |

**Nota:** aquí solo se marca que el paso se cumplió. Los documentos van en una carpeta aparte con acceso restringido, no en la hoja.

## Pestaña 4 · "Fuentes"
Diccionario de UTM y códigos de canal, para que todos escriban igual. Por ejemplo, `meta / paid_social / ctg26_caballeros / A1`.

## Pestaña 5 · "Cambios"
Quién cambió qué y cuándo. Además del historial de versiones de Google Sheets, sirve para los cambios de estructura.

## Encabezados para importar
En `N06-encabezados.csv`. Se abre directamente en Google Sheets.

## Tiempo
**1 día** desde que Zafira nombra al responsable y da la cuenta de Google:
- crear la hoja, las listas, el formato condicional y los permisos;
- probar con 2 filas ficticias y borrarlas.
