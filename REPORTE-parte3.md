# Reporte Parte 3 · cambios de la web (29-sep-2026)

Aprobador: Miguel (E-leaders). Horas en hora de Colombia.

| Código | Página | Qué se hizo | Hora | Estado |
|---|---|---|---|---|
| Respaldo | Todo | Contenido de 11 páginas en `respaldo/2026-09-29/`; respaldo manual en hPanel creado por Miguel (~21:12 del 28-sep; el próximo manual se puede crear el 29-sep 21:12) | 21:12 | Hecho |
| C17 | /registro-candidata/ | Pantalla final con el texto W01 exacto (ES y EN): título, texto y "Recuerda: Zafira nunca te pedirá dinero." (reemplaza la nota de confidencialidad). Verificado: el HTML guardado es idéntico al esperado; en la página ya no aparecen "Registro recibido", "forms.app" ni "Formulario Documental". Caché de Elementor limpiada | 21:22 | Hecho (falta captura ES/EN y móvil) |
| C18 | Blog | Los 8 artículos ya estaban en borrador (y /blog y las páginas "-pagina-antigua"). Comentarios y pingbacks cerrados en los 8 artículos | 21:23 | Parcial |
| C18 | Ajustes → Comentarios | Cerrar comentarios y pingbacks por defecto: el conector no tiene esa opción | – | Pendiente (a mano, Miguel) |
| C18 | Redirecciones 301 | 8 direcciones del blog → /caballeros/. No hay plugin de redirecciones; el conector de Hostinger se desconectó de la sesión | – | Pendiente (hPanel o reconectar Hostinger) |

## Observaciones (no tocadas, regla 1)
- Durante el trabajo hubo otras ediciones en paralelo: /registro-candidata/ guardada desde el editor a las 21:14 y /confirmacion/ a las 21:12; otra sesión con el mismo conector envió a la papelera las páginas 1162 y 1235. C17 se aplicó sobre la versión de las 21:14.
- Los pies de página enlazan a /terminos/ y /terminos-es/, que no existen (404). Se resuelve en C1.
- /blog/ (portada del blog, en borrador) no está en la lista de redirecciones de la guía; se dejó como está.
- El texto de respaldo de WordPress (`post_content`) de /registro-candidata/ conserva el texto anterior; la página se muestra desde Elementor, que sí tiene el nuevo.
