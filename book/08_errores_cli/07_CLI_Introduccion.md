# Ejecutando Archivos Python (CLI)

## Objetivos de Aprendizaje

- ✅ Aprender qué es la Interfaz de Línea de Comandos.
- ✅ Aprender a ejecutar scripts de Python desde la línea de comandos.
- ✅ Comprender cómo pasar argumentos a un script.
- ✅ Explorar mejores prácticas para ejecutar scripts eficientemente.

---

## ¿Qué es la Línea de Comandos (CLI)?

La **Interfaz de Línea de Comandos (CLI)** permite a los usuarios ejecutar scripts de Python escribiendo comandos en una terminal o símbolo del sistema.

---

## 1. Ejecutando un Script de Python

Para ejecutar un archivo de Python, navega a su directorio en la terminal y usa:

```sh
python3 script.py
```

Esto ejecuta `script.py` usando Python.

### Ejemplo de Script (`hola.py`):

```python
print("¡Hola, Mundo!")
```

### Ejecutándolo en CLI:

```sh
python3 hola.py
```

**Salida:**

```
¡Hola, Mundo!
```

>**Importante**
Cuando ejecutamos un archivo de Python usamos `python3`. Esto es porque es más específico para las versiones más nuevas de `python`. Sin embargo, dependiendo del sistema, `python3` puede no ser un alias válido, en cuyo caso puedes intentar solo `python`.

---

## 2. Pasando Argumentos a un Script de Python

Los scripts de Python pueden aceptar argumentos de línea de comandos usando el módulo `sys`:

### Ejemplo de Script (`saludar.py`):

```python
import sys  # Profundizaremos en esto después

if len(sys.argv) > 1:
    print(f"¡Hola, {sys.argv[1]}!")
else:
    print("¡Hola, usuario!")
```

### Ejecutar con un argumento:

```sh
python3 saludar.py Alicia
```

**Salida:**

```sh
¡Hola, Alicia!
```

- `sys.argv[0]` es el nombre del script.
- `sys.argv[1]` es el primer argumento.

