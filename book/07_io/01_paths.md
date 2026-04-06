# Rutas de Archivos

## Objetivos de Aprendizaje

- ✅ Comprender qué son las rutas de archivos y cómo funcionan en Python.
- ✅ Aprender la diferencia entre rutas de archivo absolutas y relativas.
- ✅ Explorar las mejores prácticas para manejar rutas de archivos en diferentes sistemas operativos.

---

## ¿Qué es una Ruta de Archivo?

Una **ruta de archivo** es una cadena de texto que especifica la ubicación de un archivo o directorio en el sistema de archivos de una computadora. Le indica a Python dónde encontrar, crear o modificar un archivo.

---

## Rutas de Archivo Absolutas vs. Relativas

Python soporta dos tipos de rutas de archivo:

### 1. Ruta de Archivo Absoluta

Una **ruta absoluta** especifica la ubicación completa de un archivo desde el directorio raíz del sistema. Siempre comienza desde el directorio base del sistema (por ejemplo, `C:\` en Windows o `/` en Linux/macOS).

**Ejemplo:**

- Windows: `C:\Users\Usuario\Documentos\archivo.txt`
- Linux/macOS: `/home/usuario/Documentos/archivo.txt`

Usa rutas absolutas cuando la ubicación del archivo es fija y conocida.

---

### 2. Ruta de Archivo Relativa

Una **ruta relativa** describe la ubicación del archivo en relación con el directorio de trabajo actual. **No** comienza desde el directorio raíz.

**Ejemplo:**

- `documentos/archivo.txt` (Relativa a la ubicación del script actual)
- `../datos/archivo.txt` (Sube un directorio antes de buscar `archivo.txt`)

Las rutas relativas son útiles cuando trabajas con archivos de proyecto que pueden moverse entre sistemas.

---

## Manejo de Rutas de Archivos en Diferentes Sistemas

Dado que diferentes sistemas operativos usan diferentes formatos de ruta (`\` para Windows, `/` para Linux/macOS), Python proporciona los módulos `os` y `pathlib` para manejar rutas de archivos de manera confiable.

### Usando `os.path` (Enfoque Tradicional)

```python
import os
ruta = os.path.join("carpeta", "subcarpeta", "archivo.txt")  # Funciona en todos los SO
print(ruta)  # Windows: carpeta\subcarpeta\archivo.txt | Linux/macOS: carpeta/subcarpeta/archivo.txt
```

### Usando `pathlib` (Enfoque Recomendado para Python 3.6+)

```python
from pathlib import Path
ruta = Path("carpeta") / "subcarpeta" / "archivo.txt"
print(ruta)  # Muestra una ruta de archivo apropiada para el sistema
```

---

## Resumen

- Las **rutas absolutas** comienzan desde el directorio raíz y siempre apuntan a la misma ubicación.
- Las **rutas relativas** dependen del directorio de trabajo actual y hacen el código más portable.
- **Usa `pathlib` para un manejo moderno y multiplataforma de rutas de archivos.**
