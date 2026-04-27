
## Pregunta

En `song.py`, crearás una clase **`Song`** que cumpla las siguientes especificaciones:

### Atributos

Cada objeto `Song` debe tener los siguientes atributos:

* `name` *(str)* — el título de la canción
* `artist` *(str)* — el nombre del artista
* `length` *(float)* — la duración de la canción en minutos

### Métodos

#### `__init__(self, name, artist, length)`

* El constructor de la clase.
* Inicializa un nuevo objeto `Song` usando los valores dados de `name`, `artist` y `length`.

#### `get_length_in_seconds(self)`

* Devuelve la duración de la canción convertida de minutos a segundos.
* Ejemplo:

  ```python
  my_song = Song("tv off", "Kendrick Lamar", 3.7)
  print(my_song.get_length_in_seconds())
  ```

  Salida:

  ```plaintext
  222.0
  ```
---

## Pregunta

Se te proporciona una clase en `movie.py` que ya tiene un constructor. Tu tarea es **definir el método `__str__`** para que cuando se imprima un objeto de esta clase, muestre una descripción bien formateada de una película. Luego, construirás un objeto `Movie` basado en la entrada del usuario e imprimirás con tu método recién definido.

### Instrucciones

1. Define el método `__str__` dentro de la clase `Movie`.
2. El método debe devolver una cadena que describa la película en el formato:
   `"Movie: <title> (Directed by <director>, <year>)"`
3. Llama al constructor de la clase para crear un objeto `Movie` basado en la entrada del usuario.
4. Llama a tu método `__str__` recién definido usando `print()`.

## Pregunta

Ahora **expandirás la clase `Song`** en `song.py` y la usarás en tu programa principal `practice.py`.

### Parte 1: Expandiendo la Clase `Song`

En `song.py`, actualiza tu clase **`Song`** para incluir lo siguiente:

#### Atributos

Cada objeto `Song` debe tener:

* `name` *(str)* — el título de la canción
* `artist` *(str)* — el nombre del artista
* `length` *(float)* — la duración de la canción en minutos

#### Métodos

##### `__init__(self, name, artist, length)`

* Inicializa un nuevo objeto `Song` con los valores proporcionados de `name`, `artist` y `length`.

##### `__str__(self)`

* **Este es el nuevo método que estás añadiendo.**
* Devuelve una cadena con el siguiente formato:

  ```
  '<name>' by <artist> (<length>)
  ```

* **Pista:** Revisa la sección *Métodos Especiales* si necesitas ayuda para definir `__str__`.

##### Nota: No usarás `get_length_in_seconds()` en esta pregunta.

---

### Parte 2: Usando la Clase `Song`

En `practice.py`, haz lo siguiente:

1. **Importa** la clase `Song` desde `song.py`.
2. Crea una función llamada `print_songs()` que:
   * Tome una lista de objetos `Song` como argumento.
   * Imprima cada canción en la lista usando la cadena devuelta por su método `__str__`.

---

### Ejemplo

```python
# practice.py

from song import Song

def print_songs(song_list):
    for song in song_list:
        print(song)

# Ejemplo de uso:
songs = [
    Song("tv off", "Kendrick Lamar", 3.7),
    Song("Alright", "Kendrick Lamar", 3.5)
]

print_songs(songs)
```

**Salida Esperada:**

```
'tv off' by Kendrick Lamar (3.7)
'Alright' by Kendrick Lamar (3.5)
```


# Demo General

## Objetivo

El objetivo de este ejercicio es implementar una clase `Car` en `car.py` que modele vehículos del mundo real usando atributos y comportamientos. Luego usarás esta clase en un archivo separado, `overall.py`, para crear objetos de coche a partir de la entrada del usuario, almacenarlos en un diccionario por sus identificadores únicos y permitir a los usuarios modificar sus propiedades durante la sesión. Para lograr este objetivo, asegúrate de usar la ayuda proporcionada en `overall.py` y en `utils.py`.


## Paso 1: Definir la Clase `Car` (`car.py`)

Crea la clase `Car` en el archivo **`car.py`**.

### Atributos

Cada objeto `Car` debe incluir los siguientes atributos:

* **car_id** (`str`): Un identificador único para el coche (por ejemplo, `"CAR001"`).
* **brand** (`str`): El fabricante del coche (por ejemplo, `"Toyota"`, `"Ford"`).
* **year** (`int`): El año en que se fabricó el coche.
* **color** (`str`): El color del coche.
* **mileage** (`float`): Los kilómetros totales recorridos. Por defecto es `0.0`.

### Métodos

Implementa los siguientes métodos:

* `__init__(self, car_id, brand, year, color, mileage=0.0)`
  Inicializa todos los atributos con los valores proporcionados.

* `change_color(self, new_color)`
  Actualiza el color del coche a `new_color`.

* `drive(self, miles)`
  Aumenta el kilometraje del coche en el número de millas especificado.

* `__str__(self)`
  Devuelve una descripción formateada del coche con este formato:

  ```plaintext
  CAR001 - 2020 Red Toyota with 15000.0 miles
  ```

---

## Paso 2: Revisar las Funciones Auxiliares (`utils.py`)

En un archivo separado llamado **`utils.py`** se definen las siguientes funciones de utilidad. Estas funciones te ayudarán a interactuar con la clase `Car` en tu programa principal.

### Funciones

#### `create_car_from_input()`

Usa esta función en el **Paso 3 (Añadir un nuevo coche)**.  
Solicita al usuario los detalles del coche, construye un objeto `Car` y lo devuelve.

```python
from car import *

def create_car_from_input():
    car_id = input("Enter car ID (e.g., CAR001):\n")
    brand = input("Enter car brand:\n")
    year = int(input("Enter car year:\n"))
    color = input("Enter car color:\n")
    mileage = float(input("Enter mileage:\n"))
    return Car(car_id, brand, year, color, mileage)
```

#### `display_cars(car_dict)`

Usa esta función en el **Paso 4 (Ver todos los coches)**.  
Toma un diccionario de coches e imprime cada coche usando su método `__str__`.

```python
def display_cars(car_dict):
    for car in car_dict.values():
        print(car)
```

---

## Paso 3: Completar el Programa Principal (`overall.py`)

Se te proporciona un programa principal parcialmente completado en **`overall.py`**. Este script proporciona un menú para que los usuarios interactúen con la clase `Car` y gestionen múltiples objetos de coche.

Tu tarea es **completar las partes faltantes (marcadas con comentarios TODO)** usando las funciones de `utils.py` y los métodos de la clase `Car`.

### 1. Declaraciones de Importación

Al comienzo de `overall.py`, importa `utils.py` y `car.py`.

Estas importaciones te permiten:

* Crear nuevos coches usando la función auxiliar `create_car_from_input()`
* Mostrar todos los coches usando la función auxiliar `display_cars()`
* Acceder a la clase `Car` y sus métodos (`drive` y `change_color`)

### 2. Configuración del Diccionario

La variable `cars` ya está proporcionada:

```python
cars = {}
```

Este diccionario almacenará todos los objetos `Car` que crees.

* **Clave:** El identificador del coche (por ejemplo, `"CAR001"`)
* **Valor:** El objeto `Car` correspondiente

Ejemplo:

```python
cars["CAR001"] = Car("CAR001", "Toyota", 2020, "Red", 15000.0)
```

### 3. Completando Cada Opción del Menú

Completarás el código faltante para cada opción del menú en la función `main()`.

#### Opción 1 — Añadir un Nuevo Coche

Usa la función `create_car_from_input()` de `utils.py` para obtener un nuevo objeto `Car` a partir de la entrada del usuario. Luego imprime el objeto coche.

Almacénalo en el diccionario `cars` usando su `car_id` como clave. Luego imprime:

```plaintext
Car added.
```

#### Opción 2 — Ver Todos los Coches

Usa la función `display_cars()` de `utils.py` para imprimir todos los coches actualmente en el diccionario.

#### Opción 3 — Conducir un Coche

El programa ya pregunta al usuario qué coche quiere conducir y cuántas millas recorrer. Tu tarea es buscar el coche en el diccionario y llamar al método `drive()` en ese objeto `Car`.

Luego imprime:

```plaintext
Mileage updated.
```

Por último, imprime la información actualizada del coche.

#### Opción 4 — Pintar un Coche

El programa ya pregunta al usuario qué coche quiere pintar y el color deseado. Tu tarea es buscar el coche en el diccionario y llamar al método `change_color()`.

Luego imprime:

```plaintext
Color updated.
```

Por último, imprime la información actualizada del coche.

#### Opción 5 — Salir

Esta opción ya está completa — termina el programa con un mensaje de despedida:

```plaintext
Goodbye!
```

---

## Ejemplos de Ejecución

#### Ejemplo 1 — Añadir un Nuevo Coche

**Entrada:**

```plaintext
1
CAR001
Toyota
2020
Red
15000
```

**Salida:**

```plaintext
CAR001 - 2020 Red Toyota with 15000.0 miles
Car added.
```

#### Ejemplo 2 — Ver Todos los Coches

**Entrada:**

```plaintext
2
```

**Salida:**

```plaintext
CAR001 - 2020 Red Toyota with 15000.0 miles
```

#### Ejemplo 3 — Conducir un Coche

**Entrada:**

```plaintext
3
CAR001
200
```

**Salida:**

```plaintext
Mileage updated.
CAR001 - 2020 Red Toyota with 15200.0 miles
```

#### Ejemplo 4 — Pintar un Coche

**Entrada:**

```plaintext
4
CAR001
Blue
```

**Salida:**

```plaintext
Color updated.
CAR001 - 2020 Blue Toyota with 15200.0 miles
```

#### Ejemplo 5 — Salir del Programa

**Entrada:**

```plaintext
5
```

**Salida:**

```plaintext
Goodbye!
```
