# Lectura

## Objetivos de Aprendizaje

- ✅ Comprender cómo leer archivos en Python.
- ✅ Aprender las diferentes funciones disponibles para un objeto de archivo en modo lectura.
- ✅ Explorar las mejores prácticas para leer archivos.

---

## 1. Leyendo desde Archivos

Python proporciona múltiples formas de leer archivos:

```python
with open("ejemplo.txt", "r") as miArchivo:
    print(miArchivo.read())  # Lee el archivo completo

with open("ejemplo.txt", "r") as miArchivo:
    print(miArchivo.readline())  # Lee una línea a la vez

with open("ejemplo.txt", "r") as miArchivo:
    print(miArchivo.readlines())  # Lee todas las líneas en una lista
```

---

## 2. ¿Cómo Detectar el Final de un Archivo?

Hay un par de formas de usar `readline()` de manera iterativa en Python y detectar el final del archivo.

```python
with open("ejemplo.txt", "r") as miArchivo:
    linea = miArchivo.readline()  # Retorna una cadena vacía si no hay más líneas
    while linea:  # ¡Puedes usar la cadena como condición!
        # Lógica por línea
        linea = miArchivo.readline()  # Retorna una cadena vacía si no hay más líneas

with open("ejemplo.txt", "r") as miArchivo:
    for linea in miArchivo:  # Itera línea por línea
        # Lógica por línea
```

---

## Resumen

- Usa `read()` o `readlines()` para leer un archivo completo en una cadena o lista de cadenas respectivamente.
- Usa `readline()` para leer la siguiente línea en un archivo.
- Usa un bucle for-each o un bucle while para leer un archivo línea por línea.

---

## Pregunta

En **`reading.py`**, escribe un programa que:

1. Solicite al usuario un nombre de archivo usando el siguiente mensaje:

   ```python
   "Input File:\n"
   ```

2. Abra el archivo especificado en **modo lectura**.

3. Lea e imprima cada línea del archivo en el formato mostrado abajo.

### Ejemplo

**Archivo ingresado:**

```plaintext
this is line 1
This is line 2
and line 3
```

**Salida Esperada:**

```plaintext
Line 1: this is line 1
Line 2: This is line 2
Line 3: and line 3
```

Imprime todas las líneas en este formato numerado, continuando hasta el final del archivo.

