# Módulos

#### Objetivos de Aprendizaje:
- ✅ Comprender qué son los módulos en Python.
- ✅ Explorar los módulos integrados de Python.
- ✅ Aprender a organizar y estructurar módulos de Python para proyectos más grandes.

---

## ¿Qué Es un Módulo?

Un **módulo** en Python es un archivo que contiene definiciones y sentencias de Python, que pueden incluir funciones, clases y variables. Los módulos permiten organizar el código de manera lógica en componentes más pequeños, manejables y reutilizables.

### ¿Por Qué Usar Módulos?
- **Reutilización**: Puedes reusar código en múltiples proyectos o archivos.
- **Organización**: Los módulos ayudan a dividir programas grandes en partes más pequeñas y manejables.
- **Colaboración**: Distintos desarrolladores pueden trabajar en diferentes módulos sin interferir entre sí.

---

## Módulos Integrados de Python

Python ofrece un amplio conjunto de **módulos integrados** que puedes usar en tus programas. Estos módulos proporcionan funcionalidad para diversas tareas, como trabajar con archivos, manejar fechas y horas, operaciones matemáticas, y más.

 > **Módulos Integrados.** Estamos usando módulos integrados como ejemplos y los cubriremos con mayor profundidad, con más documentación, más adelante en el curso. Por ahora, haz tu mejor esfuerzo usando lo que se muestra en los ejemplos.


### Ejemplo: Usando el Módulo `math`

```python
import math

# Calcular la raíz cuadrada de un número
resultado = math.sqrt(16)
print(f"Raíz cuadrada: {resultado}")

# Calcular el factorial de un número
resultado = math.factorial(5)
print(f"Factorial: {resultado}")
```

### Ejemplo: Usando el Módulo `datetime`

```python
import datetime

# Obtener la fecha y hora actuales
hora_actual = datetime.datetime.now()
print(f"Fecha y hora actuales: {hora_actual}")
```

### Ejemplo: Usando el Módulo `os`

```python
import os

# Obtener el directorio de trabajo actual
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")

# Listar los archivos en el directorio actual
archivos = os.listdir()
print(f"Archivos en el directorio actual: {archivos}")
```

---

## Cómo Usar Módulos

Para usar un módulo, simplemente impórtalo en otro archivo de Python mediante la sentencia `import`.

### Importación Regular
```python
import math

resultado = math.floor(1.234)
print(f"Número redondeado hacia abajo: {resultado}")

resultado = math.ceil(1.234)
print(f"Número redondeado hacia arriba: {resultado}")

# Calcular el logaritmo
resultado = math.log(16, 2)
print(f"Log_2 16: {resultado}")
```

### Importar Funciones Específicas

Si solo necesitas una función específica de un módulo, ¡puedes importarla directamente! Aquí está el mismo ejemplo usando esta característica.

```python
from math import floor, ceil, log

resultado = floor(1.234)
print(f"Número redondeado hacia abajo: {resultado}")

resultado = ceil(1.234)
print(f"Número redondeado hacia arriba: {resultado}")

# Calcular el logaritmo
resultado = log(16, 2)
print(f"Log_2 16: {resultado}")
```

### Importar Todas las Funciones

Si necesitas muchas funciones de un módulo, ¡puedes importarlas todas a la vez! Aquí está el mismo ejemplo usando esta característica.

```python
from math import *

resultado = floor(1.234)
print(f"Número redondeado hacia abajo: {resultado}")

resultado = ceil(1.234)
print(f"Número redondeado hacia arriba: {resultado}")

# Calcular el logaritmo
resultado = log(16, 2)
print(f"Log_2 16: {resultado}")
```

