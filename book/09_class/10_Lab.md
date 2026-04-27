
# Lab 9  

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










# Pregunta

# Parte 1: Creando la Clase Base BankAccount

## Objetivo

En este laboratorio, construirás un **sistema bancario orientado a objetos** usando clases de Python.

El sistema gestionará **múltiples usuarios** con **cuentas bancarias**.
Tu objetivo final es crear un **programa principal** para gestionar usuarios y cuentas bancarias.

---

## Parte 1: Crear la Clase Base `BankAccount`

Comenzarás creando una clase llamada **`BankAccount`**, que representa una cuenta bancaria. Trabajarás en `bank_account.py`.

---

### Atributos

Cada objeto `BankAccount` debe incluir:

1. `account_number` *(int)* — un número de cuenta único de cuatro dígitos.
2. `balance` *(float)* — el saldo actual de la cuenta.

---

### Métodos

#### `__init__(self, account_number, balance=0.0)`

* Inicializa los atributos `account_number` y `balance`.
* El **saldo por defecto** debe ser `0.0`.

#### `deposit(self, amount)`

* Añade el `amount` especificado al saldo actual.

#### `withdraw(self, amount)`

* Intenta retirar el `amount` especificado.

  * Si `amount > balance`, devuelve `-1` (fondos insuficientes).
  * De lo contrario, resta el `amount` y devuelve `0` (retiro exitoso).

#### `__str__(self)`

* Devuelve una cadena formateada que muestra:

  * Solo los **últimos dos dígitos** del número de cuenta (por privacidad).
  * El saldo formateado con **dos decimales**.
  * Ejemplo de salida:

    ```plaintext
    Account Number: **<ultimos_dos_digitos>
    Current Balance: <saldo>
    ```

---

### Pistas

* Define una clase usando la palabra clave `class`.
* Siempre incluye `self` como primer parámetro en los métodos de clase.
* Accede o modifica atributos usando `self.nombre_atributo`.
* Para extraer los últimos caracteres de una cadena, usa slicing (`str[-i:]`).

---

### Programa de Ejemplo

```python
def main():
    # Crear una cuenta con número 1234 y saldo inicial de 100.0
    account = BankAccount(1234, 100.0)
    print(account)

    # Depositar 50.0
    account.deposit(50.0)
    print("After deposit of 50.0:")
    print(account)

    # Retirar 120.0 (exitoso)
    result = account.withdraw(120.0)
    print("After withdrawal of 120.0:")
    print(account)
    print("Withdrawal status:", "Success" if result == 0 else "Failed")

    # Retirar 50.0 (debe fallar por fondos insuficientes)
    result = account.withdraw(50.0)
    print("After withdrawal of 50.0:")
    print(account)
    print("Withdrawal status:", "Success" if result == 0 else "Failed")

if __name__ == "__main__":
    main()
```

---

### Salida Esperada

**Paso 1 — Crear cuenta**

```plaintext
Account Number: **34
Current Balance: 100.00
```

**Paso 2 — Depositar 50.0**

```plaintext
After deposit of 50.0:
Account Number: **34
Current Balance: 150.00
```

**Paso 3 — Retirar 120.0 (exitoso)**

```plaintext
After withdrawal of 120.0:
Account Number: **34
Current Balance: 30.00
Withdrawal status: Success
```

**Paso 4 — Retirar 50.0 (fallido)**

```plaintext
After withdrawal of 50.0:
Account Number: **34
Current Balance: 30.00
Withdrawal status: Failed
```

# Parte 2: Creando la Clase Person

## Archivo: `person.py`

En esta parte, crearás una clase **`Person`** para representar a un cliente bancario.

---

### Clase: `Person`

#### Atributos

Cada objeto `Person` debe incluir:

1. `name` *(str)* — el nombre de la persona.
2. `accounts` *(list)* — una lista que almacenará múltiples objetos `BankAccount` asociados a la persona.

---

#### Métodos

##### `__init__(self, name)`

* Inicializa el `name` de la persona.
* Inicializa `accounts` como una **lista vacía** para almacenar sus cuentas bancarias.

##### `add_account(self, account)`

* Añade un nuevo objeto `BankAccount` a la lista `accounts`.

##### `__str__(self)`

* Devuelve una cadena formateada que muestra el nombre de la persona y el número de cuentas.
  Formato de ejemplo:

  ```plaintext
  Name = <nombre>, Number of accounts = <numero_de_cuentas>
  ```

{Check It!|assessment}(code-output-compare-1926484397)

---

# Parte 3: Creando las Funciones de Utilidad

## Archivo: `utils.py`

En esta parte, implementarás dos funciones para **crear** y **resumir** datos de usuarios.

---

### Función 1: `person_data()`

Esta función debe:

1. Solicitar al usuario la siguiente información:

   * Nombre de la persona →
     `Enter the person's name:`
   * Número de cuenta →
     `Enter a 4-digit account number:`
   * Saldo inicial →
     `Enter the initial balance:`
2. Crear un objeto `BankAccount` usando los datos ingresados.
3. Añadir la nueva cuenta a la lista `accounts` de la persona.
4. Continuar solicitando al usuario añadir más cuentas hasta que responda **"yes"** a:
   `Are you done adding accounts? (yes/no):`
5. Una vez terminado, devolver el objeto `Person` completado.

{Check It!|assessment}(code-output-compare-1901648055)

---

### Función 2: `balance_summary(person_list)`

Esta función debe:

1. Recibir una **lista de objetos `Person`** como entrada.
2. Para cada persona en la lista:

   * Calcular el **saldo total** sumando los saldos de todas sus cuentas.
   * Imprimir el nombre de la persona seguido de su saldo total.

**Ejemplo de Salida:**

```plaintext
Daniel : 90.00
Alice : 150.25
```

> 💡 *Pista:* Usa los atributos `Person.accounts` y `BankAccount.balance` para acceder al saldo de cada cuenta al calcular los totales.

# Parte 4: Usando BankAccount, Person y Utils

## Objetivo

En esta parte, construirás un **programa interactivo en Python** que le permita al usuario:

* Añadir nuevas personas *(a una lista de objetos `Person`)*
* Añadir cuentas a personas existentes
* Ver todos los saldos de cada persona

Esta sección combina todo tu trabajo de las **Partes 1 a 3**.

---

## Archivo: `main.py`

### Descripción General

Escribirás un **programa interactivo** que muestra continuamente un menú de opciones usando un **bucle while**.

El programa seguirá ejecutándose hasta que el usuario elija salir.

Antes de hacer cualquier otra cosa, importa tus funciones de utilidad, así como tus clases `Person` y `BankAccount` si las necesitas.

---

### Opciones del Menú

Cuando el programa se ejecute, debe mostrar el siguiente menú:

```plaintext
Choose an option:
1. Add a new person
2. Add an account to a person
3. Show all balances
4. Quit
```

---

### Comportamiento del Menú

Actualmente, debajo de cada instrucción `if`, hay una palabra clave `pass`. Esto solo evita que el programa falle cuando lo ejecutas sin tener código bajo la instrucción `if`. **Elimina esta palabra clave** cuando implementes cada opción del menú.

#### Opción 1 — Añadir una Nueva Persona

* Llama a la función `person_data()`.
* Añade el objeto `Person` devuelto a la lista de todas las personas.

---

#### Opción 2 — Añadir una Cuenta a una Persona

* Solicita al usuario el nombre de la persona:
  `Enter the person's name:`
* Si la persona existe:

  1. Solicita el número de cuenta → `Enter a 4-digit account number:`
  2. Solicita el saldo inicial → `Enter the initial balance:`
  3. Crea un nuevo objeto `BankAccount`.
  4. Añádelo a la lista `accounts` de la persona.
* Si la persona **no existe**, muestra:
  `Person not found.`

---

#### Opción 3 — Mostrar Todos los Saldos

* Llama a la función `balance_summary(person_list)`.
* Esta función debe imprimir el nombre de cada persona y su **saldo total**.
* Si no hay objetos `Person` en la lista, imprime:

```plaintext
No data to show.
```

---

#### Opción 4 — Salir

* Sale del bucle e imprime un mensaje de despedida:
  `Goodbye!`

---

### Ejemplo de Entrada

```plaintext
1
Daniel
1234
100.0
yes
3
4
```

---

### Salida Esperada

```plaintext
Choose an option:
1. Add a new person
2. Add an account to a person
3. Show all balances
4. Quit
Enter the person's name:
Enter a 4-digit account number:
Enter the initial balance:
Are you done adding accounts? (yes/no):
Choose an option:
1. Add a new person
2. Add an account to a person
3. Show all balances
4. Quit
Daniel : 100.00
Choose an option:
1. Add a new person
2. Add an account to a person
3. Show all balances
4. Quit
Goodbye!
```

---

### Pistas

* Usa una **lista** para almacenar todos los objetos `Person`.
* Usa un **bucle while** e instrucciones **if/elif** para manejar las opciones del menú.
* Importa todas las **clases** y **funciones** necesarias (`Person`, `BankAccount`, `person_data`, `balance_summary`).
* Añade validación de entrada cuando sea apropiado (por ejemplo, asegurándote de que el número de cuenta tenga 4 dígitos).


# Pregunta

# Controlando la Altitud de una Aeronave

Un **simulador de vuelo** usa una clase `Aircraft` para rastrear la altitud de un avión. El usuario debe poder ajustar la altitud repetidamente ingresando comandos.

Trabajarás en `aircraft_altitude.py` para esta pregunta. También necesitarás usar la clase `Aircraft` en `aircraft.py` para responderla.

> **Importante: Importando la Clase**
Asegúrate de usar una instrucción `import` para importar la clase `Aircraft` desde `aircraft.py`.


### Tarea

1. Pide al usuario el **modelo de la aeronave** y crea un objeto `Aircraft`.
   ```plaintext
   Enter aircraft model:
   ```
2. En un bucle, pregunta repetidamente al usuario que ajuste la altitud:
   ```plaintext
   Enter command (A for ascent, D for descent, X to exit):
   ```
   - El usuario escribe `A <pies>` para subir (por ejemplo, `A 5000`).
   - El usuario escribe `D <pies>` para descender (por ejemplo, `D 2000`).
   - El bucle debe detenerse cuando el usuario ingrese `X`.
3. Imprime la **altitud final** después de que termine el bucle.

### Pistas de Sintaxis

- Usa `input()` para obtener el modelo de la aeronave antes de entrar al bucle.
- Usa un bucle `while` para pedir entradas repetidamente.
- Usa `.split()` para separar el comando (`A` o `D`) del número de pies.
- Convierte el valor de los pies a entero antes de llamar al método correspondiente.
- Sale del bucle si el usuario ingresa `X`.

### Ejemplo de Uso

```plaintext
Enter aircraft model: Boeing 747
Enter command (A for ascent, D for descent, X to exit): A 5000
Enter command (A for ascent, D for descent, X to exit): D 2000
Enter command (A for ascent, D for descent, X to exit): X
Final altitude: 3000 feet
```

