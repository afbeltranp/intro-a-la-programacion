# FileNotFoundError (Ejemplo 3)

## Objetivo de Aprendizaje

- ✅ Comprender qué es un `FileNotFoundError`, por qué ocurre y cómo manejarlo.

---

## Archivo No Encontrado

### ¿Qué es un FileNotFoundError?

Un **FileNotFoundError** ocurre en Python cuando se intenta abrir o acceder a un archivo que **no existe** en la ubicación especificada.

#### Causas Comunes de FileNotFoundError

1. **Intentar abrir un archivo que no existe:**

   ```python
   with open("archivo_faltante.txt", "r") as archivo:  # El archivo no existe
       datos = archivo.read()
   ```

   **Error:** `FileNotFoundError: [Errno 2] No such file or directory: 'archivo_faltante.txt'`

2. **Ruta de archivo incorrecta:**

   ```python
   with open("carpeta/archivo_faltante.txt", "r") as archivo:
       datos = archivo.read()
   ```

   - Si `carpeta/` no existe, Python lanzará un **FileNotFoundError**.

3. **Nombre de archivo mal escrito:**

   ```python
   with open("archivodatos.txt", "r") as archivo:  # El archivo real es "archivo_datos.txt"
       datos = archivo.read()
   ```

---

### ¿Cómo Manejar FileNotFoundError?

#### 1. Usando Try-Except para Capturar el Error

Una forma simple de manejar archivos faltantes es usando `try-except`:

```python
try:
    with open("archivo_faltante.txt", "r") as archivo:
        datos = archivo.read()
        print(datos)
except FileNotFoundError:
    print("Error: El archivo no fue encontrado. Por favor verifica el nombre o ruta del archivo.")
```

**Previene bloqueos y permite que el programa continúe ejecutándose.**

---

#### 2. Verificando Si un Archivo Existe Antes de Abrirlo

En lugar de manejar errores después de que ocurren, verifica si el archivo existe:

```python
import os

ruta_archivo = "archivo_faltante.txt"
if os.path.exists(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        datos = archivo.read()
        print(datos)
else:
    print("El archivo no existe. Por favor verifica la ruta del archivo.")
```

**Evita FileNotFoundError al verificar la existencia del archivo antes de intentar abrirlo.**

---

### ¿Cómo Prevenir FileNotFoundError?

- **Asegura que se proporcione la ruta correcta del archivo**.
- **Usa `os.path.exists()`** para verificar la existencia del archivo antes de acceder.
- **Maneja errores elegantemente** usando bloques `try-except`.

Al implementar estas estrategias, los programas de Python pueden **manejar archivos faltantes sin problemas y evitar bloqueos.**

