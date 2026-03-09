# Múltiples Archivos de Python

#### Objetivos de Aprendizaje:
- ✅ Comprender el concepto de usar múltiples archivos de Python en un proyecto.
- ✅ Aprender a estructurar programas de Python a través de diferentes archivos.
- ✅ Entender cómo importar funciones, clases y variables de un archivo de Python a otro.
- ✅ Explorar la variable `__name__` y cómo afecta la ejecución de archivos.

---

## ¿Por Qué Usar Múltiples Archivos de Python?

A medida que tus proyectos de Python crecen, se vuelve difícil gestionar todo en un solo archivo. Dividir el código en múltiples archivos permite:

1. **Mejor Organización**: El código puede organizarse en componentes lógicos (por ejemplo, utilidades, clases, funciones).
2. **Reutilización**: Puedes reusar código en múltiples proyectos o archivos.
3. **Colaboración**: Varios desarrolladores pueden trabajar en diferentes archivos sin conflictos.

---

## Cómo Estructurar Múltiples Archivos de Python

Considera un proyecto simple de Python que incluye un programa principal, un módulo de utilidades y una definición de clase. Así puedes organizar los archivos:

1. **Programa Principal** (`main.py`): Este archivo será el punto de entrada de tu programa.
2. **Funciones Utilitarias** (`utils.py`): Este archivo contiene funciones auxiliares.
3. **Definición de Clase** (`person.py`): Este archivo define una clase para una persona.

---

## Ejemplo 1: Organización Básica de Archivos

### 1. `utils.py`
```python
def greet(name):
    """Retorna un mensaje de saludo."""
    return f"Hello, {name}!"
```

### 2. `main.py`
```python
from utils import greet
from person import Person  # ¡Llegaremos a las clases más adelante!

# Usando la función de utils.py
print(greet("Alice"))

# Usando la clase Person de person.py
person = Person("Bob", 30)
print(person.introduce())
```

---

## Cómo Importar desde Otro Archivo de Python

Puedes importar funciones, clases o variables desde otro archivo usando la sentencia `import`. Hay varias formas de hacerlo:

1. **Importar una función o clase específica:**
```python
from nombre_modulo import nombre_funcion
```
Ejemplo:
```python
from utils import greet
```

2. **Importar todo desde un archivo (no recomendado para proyectos grandes):**
```python
from nombre_modulo import *
```
Ejemplo:
```python
from utils import *
```

3. **Importar un módulo y usar el nombre del módulo para acceder a sus funciones o clases:**
```python
import nombre_modulo
```
Ejemplo:
```python
import utils
```
Luego puedes acceder a la función `greet` como `utils.greet()`.

---

## La Variable `__name__`

En Python, la variable `__name__` determina si un archivo de Python se está ejecutando como programa independiente o si está siendo importado como módulo. Esto es útil para controlar qué código se ejecuta cuando el archivo se corre directamente frente a cuando se importa en otro archivo.

### Ejemplo: Usando `__name__`
```python
# En utils.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Este código solo se ejecuta si el archivo se corre directamente
    print("This file is being run directly.")
```

Si ejecutas `utils.py` directamente, imprimirá:
```
This file is being run directly.
```

Pero si importas `utils.py` en otro archivo:
```python
# En main.py
from utils import greet

print(greet("Alice"))
```

El código dentro de `if __name__ == "__main__":` en `utils.py` no se ejecutará, y solo obtendrás la salida:
```
Hello, Alice!
```
