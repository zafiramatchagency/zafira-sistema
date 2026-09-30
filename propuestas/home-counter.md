# Home (21) · error de `#counter` (propuesta, sin escribir)

## Qué pasa
- El script final de la Home tiene un bloque "Counter" que busca `document.getElementById('counter')`. Ese elemento ya no existe en la página.
- Al llegar a `co.observe(el)` con `el = null`, el navegador lanza un error. Se corta el resto de **ese mismo** `<script>`.

## Qué frena y qué no (probado en local, 30-sep 07:0x)
| Script | ¿Funciona hoy? |
|---|---|
| Cambio de idioma (script de la cabecera) | Sí |
| Enlaces del pie según idioma (script propio del pie) | Sí |
| Aparición al hacer scroll (`.fade`, va antes del contador) | Sí |
| Partículas del encabezado (script propio) | Sí |
| **Parallax del fondo del encabezado** (va justo después del contador) | **No, queda bloqueado** |

## Arreglo mínimo (una línea, en el script final)
**Antes:**
```js
(function(){const el=document.getElementById('counter');let go=false;...
```
**Después:**
```js
(function(){const el=document.getElementById('counter');if(!el)return;let go=false;...
```
- Si no hay contador, el bloque se salta sin error.
- El parallax vuelve a funcionar: con la página bajada 400 px, el fondo se mueve `translateY(120px)`.
- No cambia ningún texto.
- Probado en local: ES y EN correctos, enlaces del pie correctos y 0 errores.

Sin cambios en `post_content`, porque no hay texto nuevo.
