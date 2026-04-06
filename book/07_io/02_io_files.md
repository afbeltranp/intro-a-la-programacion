# E/S de Archivos

## Objetivos de Aprendizaje

- ✅ Comprender cómo trabajar con archivos en Python.
- ✅ Aprender los diferentes modos de archivo (lectura, escritura, anexar).
- ✅ Explorar las mejores prácticas para manejar archivos de forma segura.

---

## Trabajando con Archivos en Python

Los archivos son esenciales para almacenar y recuperar datos de forma persistente. Python proporciona funciones incorporadas para interactuar con archivos de manera eficiente.

### 1. Abriendo y Cerrando Archivos

Usa la función `open()` para trabajar con archivos. La función toma dos argumentos principales:

- **Nombre del archivo**: El nombre (y ruta, si es necesario) del archivo.
- **Modo**: Especifica cómo se accede al archivo (lectura, escritura, anexar, etc.).

```python
archivo = open("ejemplo.txt", "r")  # Abrir un archivo en modo lectura
archivo.close()  # Siempre cierra un archivo después de usarlo
```

> **Mejor Práctica**: Usa `with open()` para cerrar automáticamente el archivo.

```python
with open("ejemplo.txt", "r") as archivo:
    # operaciones con el archivo
    # no necesitas close()
```

---

## 2. Modos de Archivo

Python permite diferentes modos para abrir archivos:

| Modo   | Descripción                                                        |
| ------ | ------------------------------------------------------------------ |
| `'r'`  | Lectura (predeterminado) - Abre un archivo existente para lectura. |
| `'w'`  | Escritura - Crea un archivo nuevo o sobrescribe uno existente.     |
| `'a'`  | Anexar - Agrega contenido nuevo a un archivo existente.            |
| `'r+'` | Lectura y Escritura - Lee y escribe en un archivo existente.       |

---

## 3. Verificar si un Archivo Existe

Antes de leer o escribir, es buena práctica verificar si un archivo existe.

```python
import os

if os.path.exists("ejemplo.txt"):
    print("¡El archivo existe!")
else:
    print("¡Archivo no encontrado!")
```

---

## Resumen

- Usa `open()` para acceder a archivos con diferentes modos (`'r'`, `'w'`, `'a'`, etc.).
- Usa `with open()` para asegurar que los archivos se cierren correctamente.
- Usa `os.path.exists()` para verificar la existencia del archivo antes de las operaciones.

El manejo de archivos de Python proporciona **una forma simple y poderosa** de trabajar con fuentes de datos externas.

---

