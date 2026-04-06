# Demo de Depuración

## Depuración de E/S de Archivos en Python

¡Bienvenido a tu **Demo de Depuración de E/S de Archivos**!
En esta lección, aprenderás cómo identificar y corregir errores comunes de manejo de archivos en Python — y luego aplicar ese conocimiento para depurar un programa de biblioteca con errores.

---

## Parte 1: Errores Comunes de E/S de Archivos

Antes de depurar el programa de biblioteca, revisarás los errores más comunes que cometen los programadores al trabajar con archivos.

---

### 1. FileNotFoundError (Archivo No Encontrado)

**Escenario:**
Un programa intenta leer un archivo de configuración que debería estar en una carpeta específica, pero la **ruta del archivo es incorrecta** o el **archivo no existe** en el directorio del proyecto.

```python
# lector_config.py

with open("config/configuracion.txt", "r") as f:
    configuracion = f.read()

print("¡Configuración cargada exitosamente!")
```

**Mensaje de Error:**

```plaintext
FileNotFoundError: [Errno 2] No such file or directory: 'config/configuracion.txt'
```

**¿Qué Pasó?**
Python no puede encontrar el archivo en la ruta que especificaste.
Ya sea que la carpeta `config/` no existe, o `configuracion.txt` no ha sido creado aún.

---

**Cómo Solucionarlo:**

✅ **Opción 1 — Corregir la Ruta del Archivo en el Código**
Si el archivo está realmente en otro lugar, ajusta la ruta:

```python
with open("configuracion.txt", "r") as f:  # Se eliminó 'config/' ya que está en el mismo directorio
    configuracion = f.read()
```

✅ **Opción 2 — Crear el Archivo en el Árbol de Archivos (GUI)**
Si la ruta es correcta pero el archivo falta:

1. En tu IDE o explorador de archivos, abre la carpeta del proyecto.
2. Crea una nueva carpeta llamada **`config`** (si no existe).
3. Dentro de ella, crea un archivo llamado **`configuracion.txt`**.
4. Agrega algo de texto (por ejemplo, `tema=oscuro`).
5. Ejecuta el programa de nuevo — ahora debería encontrar el archivo.

---

**Punto Clave:**
Un `FileNotFoundError` no siempre significa que el nombre del archivo está mal — a menudo significa que tu **estructura de directorios** no coincide con tu código.

---

### 2. UnsupportedOperation: not writable (Operación No Soportada: no escribible)

**Escenario:**
Un registrador de temperatura intenta escribir en un archivo que fue abierto en **modo lectura**.

```python
# registrador_temperatura.py

with open("temperaturas.txt", "r") as f:
    f.write("22°C - Sala de Estar\n")
```

**Mensaje de Error:**

```plaintext
io.UnsupportedOperation: not writable
```

**¿Qué Pasó?**
Abriste el archivo con `'r'`, que permite solo lectura — no escritura.

**Solución:**
Abre el archivo en modo anexar (`'a'`) o escritura (`'w'`) en su lugar:

```python
with open("temperaturas.txt", "a") as f:
    f.write("22°C - Sala de Estar\n")
```

---

### 3. AttributeError o TypeError: 'builtin_function_or_method' object is not iterable

**Escenario:**
Un programa intenta iterar a través de las líneas de un archivo pero olvida los paréntesis en `.readlines()`.

```python
# visor_tareas.py

with open("tareas.txt", "r") as f:
    for tarea in f.readlines:
        print(tarea.strip())
```

**Mensaje de Error:**

```
TypeError: 'builtin_function_or_method' object is not iterable
```

**¿Qué Pasó?**
`.readlines` es un **método** — necesita paréntesis (`.readlines()`) para retornar la lista de líneas.

**Solución:**

```python
with open("tareas.txt", "r") as f:
    for tarea in f.readlines():
        print(tarea.strip())
```

---

### 4. Sobrescribir Datos por Error

**Escenario:**
Un recolector de comentarios sigue eliminando respuestas antiguas porque abre el archivo en **modo escritura** cada vez.

```python
# recolector_comentarios.py

comentario = input("Ingresa tu comentario: ")

with open("respuestas.txt", "w") as f:
    f.write(comentario + "\n")

print("¡Comentario guardado!")
```

**¿Qué Pasó?**
El modo `'w'` limpia el archivo antes de escribir — todos los datos anteriores se pierden.

**Solución:**
Usa el modo `'a'` para **anexar** en lugar de sobrescribir:

```python
with open("respuestas.txt", "a") as f:
    f.write(comentario + "\n")
```

---

## Parte 2: Actividad de Depuración — "Registros de Biblioteca Perdidos"

¡Ahora es tu turno de depurar un programa real!
Este programa debería almacenar y mostrar títulos de libros para una biblioteca — pero está lleno de errores.

Tu tarea es identificar y corregir los problemas de E/S de Archivos para que funcione correctamente.

---

### Escenario

El programa debería:

1. Permitirte agregar libros a un archivo de texto.
2. Permitirte mostrar todos los libros almacenados.

Sin embargo, actualmente se bloquea o da resultados incorrectos.

Encontrarás **cuatro errores principales** que cada uno se conecta con uno de los errores que aprendiste en la **Parte 1**.

---

### ¡Depura el Programa!

Una vez corregido, tu programa debería:

- Agregar exitosamente nuevos libros al archivo.
- Mostrar todos los libros cuando se seleccione "Mostrar Todos los Libros".

Ejemplo de salida:

```plaintext
Menú de Biblioteca
1. Agregar Libro
2. Mostrar Todos los Libros
3. Salir
Ingresa tu opción: 2

Colección de la Biblioteca:
El Hobbit por J.R.R. Tolkien
1984 por George Orwell
Dune por Frank Herbert
```

---

### Restaurar el Archivo de Datos (si es necesario)

Si accidentalmente eliminaste o sobrescribiste el archivo de datos, aquí está el contenido original para **`library_data.txt`**:

**Ruta del Archivo:** `debugging_files/library_data.txt`

```plaintext
The Hobbit by J.R.R. Tolkien
1984 by George Orwell
Pride and Prejudice by Jane Austen
Dune by Frank Herbert
```
