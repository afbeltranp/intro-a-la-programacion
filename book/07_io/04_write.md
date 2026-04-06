# Escritura

## Escritura y Anexado de Archivos en Python

### Objetivos de Aprendizaje

- ✅ Aprender cómo abrir y escribir en un archivo.
- ✅ Comprender la diferencia entre escribir y anexar.
- ✅ Saber cuándo usar cada modo y cómo evitar sobrescribir datos.

---

## Escribiendo en un Archivo (modo `'w'`)

Cuando abres un archivo en modo `'w'`, este:

- **Creará** el archivo si no existe.
- **Sobrescribirá** el archivo si ya existe.

```python
with open("salida.txt", "w") as f:
    f.write("¡Hola, mundo!\n")
    f.write("Esto sobrescribirá el contenido anterior.\n")
```

📝 Cada vez que ejecutes esto, reemplaza el contenido del archivo.

---

## Anexando a un Archivo (modo `'a'`)

Cuando abres un archivo en modo `'a'`, este:

- **Creará** el archivo si no existe.
- **Agregará** contenido al final del archivo sin eliminar lo que ya está ahí.

```python
with open("salida.txt", "a") as f:
    f.write("Agregando otra línea.\n")
```

📝 Cada ejecución agrega más líneas al archivo sin eliminar las anteriores.

---

## Casos de Uso

| Modo  | Usar Cuando...                                              |
| ----- | ----------------------------------------------------------- |
| `'w'` | Quieres empezar desde cero (sobrescribir datos antiguos)    |
| `'a'` | Quieres preservar datos antiguos y agregar contenido nuevo  |

---

## Mejores Prácticas

- Usa `with open(...)` para cerrar automáticamente el archivo.
- Siempre escribe `\n` manualmente si quieres nuevas líneas.
- Ten cuidado al usar `'w'` — borra permanentemente el contenido existente.

---

## Pregunta

En **`writing.py`**, escribe dos funciones: `begin(...)` y `sign(...)`.

### 1. Función 1: `begin(filename, header_text)`

Esta función debe **crear un archivo nuevo** y escribir un encabezado en él.
Si el archivo ya existe, debe ser **sobrescrito**.

**Parámetros:**

- Una cadena `filename` que representa el **nombre del archivo** a crear.
- Una cadena `header_text` que contiene el **texto del encabezado** a escribir en el archivo.

**Salida:**

- Sin valor de retorno.
- La función debe crear un archivo con el nombre dado y escribir el texto del encabezado proporcionado.

---

### 2. Función 2: `sign(filename, name)`

Esta función debe **anexar una firma** al final de un archivo existente.

**Parámetros:**

- Una cadena `filename` que representa el **nombre del archivo** a modificar.
- Una cadena `name` que contiene el **nombre para firmar**.

**Salida:**

- Sin valor de retorno.
- La función debe actualizar el archivo agregando una firma en el siguiente formato:

```plaintext
Regards,
<nombre aquí>
```

---

Cada función debe manejar la escritura de archivos apropiadamente, asegurando que `begin(...)` cree o sobrescriba archivos, mientras que `sign(...)` anexe texto sin eliminar contenido existente.
