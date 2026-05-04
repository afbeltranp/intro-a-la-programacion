# Introducción a las Bibliotecas

## Objetivos de Aprendizaje

- Entender qué son las **bibliotecas de Python** y por qué son útiles.
- Aprender cómo **instalar e importar bibliotecas** en Python.
- Explorar cómo **encontrar y leer documentación** de bibliotecas.

---

## ¿Qué Son las Bibliotecas de Python?

Una **biblioteca** es una colección de **código preescrito** que provee funciones, clases y herramientas útiles. En lugar de escribir todo desde cero, puedes usar **bibliotecas** para acelerar el desarrollo y evitar reinventar la rueda.

**Ejemplo:** En lugar de manejar archivos CSV manualmente, la biblioteca **`csv`** provee métodos integrados para leerlos y escribirlos.

---

## ¿Por Qué Usar Bibliotecas?

Las bibliotecas ayudan al:

- **Ahorrar tiempo** - No es necesario escribir funciones comunes por tu cuenta.
- **Ofrecer rendimiento optimizado** - Muchas bibliotecas son más rápidas que implementaciones personalizadas.
- **Ampliar las capacidades de Python** - Existen bibliotecas especializadas para tareas como análisis de datos, aprendizaje automático y redes.

---

## Instalando Bibliotecas con `pip`

Python incluye **algunas bibliotecas integradas**, pero otras deben instalarse por separado en la **terminal** usando `pip`, el gestor de paquetes de Python. Esto **debe hacerse** antes de ejecutar el script que necesita las bibliotecas.

*Dato curioso:* pip es en realidad un acrónimo recursivo de "`pip` instala paquetes" (*"pip installs packages"*), por lo que técnicamente podrían haberle puesto cualquier otra letra al inicio.

### Instalando una Biblioteca

```sh
pip install numpy
```

Esto instala **NumPy**, una popular biblioteca para computación numérica.

---

## Importando y Usando Bibliotecas

Después de la instalación, las bibliotecas deben **importarse** en tu script antes de usarlas.

### Ejemplo: Importar y Usar una Biblioteca

```python
import math  

print(math.sqrt(25))  # Salida: 5.0
```

**`math` es una biblioteca integrada** que provee funciones matemáticas como `sqrt()`.

También puedes ver bibliotecas importadas con un **alias (un nombre más corto)**. Esto es muy común con bibliotecas de terceros.

### Ejemplo: Importar una Biblioteca de Terceros con Alias

```python
import numpy as np  

numbers = np.array([10, 20, 30, 40])
mean_value = np.mean(numbers)

print("Arreglo:", numbers)
print("Media:", mean_value)
```

Aquí:

- `numpy` es el nombre completo de la biblioteca.
- `np` es un alias convencional usado por la mayoría de programadores de Python. Podrías usar uno diferente.
- `np.array()` crea un arreglo.
- `np.mean()` calcula el promedio.

Usar alias hace que tu código sea más corto, más limpio y más fácil de leer, especialmente cuando trabajas con bibliotecas que se usan frecuentemente como `numpy`, pandas `(pd)` o `matplotlib.pyplot` `(plt)`.

---

## Cómo Encontrar y Leer Documentación

Para usar una biblioteca de manera efectiva, necesitas entender sus **funciones y clases**.

### Formas de Encontrar Documentación

1. **Documentación Oficial de Python** - Visita [docs.python.org](https://docs.python.org/3/library/) para módulos integrados.
2. **Documentación Específica de la Biblioteca** - Ejemplo: la documentación de NumPy en [numpy.org/doc](https://numpy.org/doc/).
3. **Función `help()` en Python** - Ver documentación dentro de Python:
   ```python
   import math
   help(math)
   ```
4. **Google y Stack Overflow** - Busca ejemplos y soluciones a problemas.

---

## Resumen

- **Las bibliotecas amplían las capacidades de Python** al proveer código preescrito.
- **Algunas bibliotecas están integradas**, mientras que otras requieren instalación (`pip install`).
- **Importa las bibliotecas** antes de usarlas en tu código.
- **Lee la documentación** para entender las funciones disponibles y las mejores prácticas.

---

## ❓ Pregunta sobre Biblioteca Faltante

En el archivo `lib_intro.py` encontrarás código que usa `numpy`, `math`, `pandas` y `Faker`. Algunas de estas bibliotecas se usan comúnmente en problemas de ingeniería. El código en sí no contiene errores. Sin embargo, al ejecutar el código se produce un **ModuleNotFoundError**.

Usando lo que has aprendido sobre la instalación de bibliotecas, depura el programa para que no falle. No olvides que el problema **debe resolverse** en la terminal.

```python
import numpy as np
import pandas as pd
import math
from faker import Faker  # Likely not installed by default
 
fake = Faker()
Faker.seed(37)
number = float(input("Enter a number: "))
 
square_root = math.sqrt(number)
factorial = math.factorial(int(number)) if number.is_integer() and number >= 0 else None
 
np_array = np.array([number, square_root])
mean_value = np.mean(np_array)
 
# Generate fake data (requires faker library)
fake_name = fake.name()
fake_email = fake.email()
 
data = {
    "Original Number": [number],
    "Square Root": [square_root],
    "Mean Value": [mean_value],
    "Fake Name": [fake_name],
    "Fake Email": [fake_email]
}
 
df = pd.DataFrame(data)
 
print("\nResults:")
print("Square Root:", square_root)
print("Factorial:" , factorial if factorial is not None else "Not applicable")
print("NumPy Mean:", mean_value)
 
print("\nFake User Info:")
print("Name:", fake_name)
print("Email:", fake_email)
 
print("\nPandas DataFrame:")
print(df)
```