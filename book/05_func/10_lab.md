# Laboratorio 5


# Problema 1

En `functions.py`, crea una función llamada `promedio_estudiante` que calcule el promedio de una lista de calificaciones de estudiantes.

**Requisitos de la Función:**

* **Entrada:**
    
  * `calificaciones` — una lista de números que representan las calificaciones de los estudiantes. Ejemplo: `[85, 92, 78]`

* **Salida:**

  * `promedio` — un número decimal (float) que representa la media aritmética de las calificaciones. Ejemplo: `85.0`

**Notas:**

1. El valor retornado debe ser siempre un `float`, incluso si el promedio es un número entero.
2. Para calcular el promedio, suma todas las calificaciones y divídelas entre la cantidad de calificaciones. Luego, usa una **sentencia return** para devolver el resultado al llamador.

**Pista:** Es posible que notes un `ZeroDivisionError` la primera vez que ejecutes las verificaciones. ¿Por qué podría ocurrir esto? ¿Cómo debería comportarse el programa si la lista `calificaciones` está vacía?

---

# Problema 2

En `return_types.py`, crea una función llamada `obtener_precio_usuario` que le pida al usuario ingresar un precio y lo retorne como un `float`.

**Requisitos de la Función:**

* **Entrada:**

  * La función **no recibe parámetros**.
  * Debe solicitarle al usuario con:

    ```python
    "Enter the item's price:\n"
    ```

* **Salida:**

  * Un **float** que representa el valor ingresado por el usuario.

**Notas:**

1. El valor retornado debe ser siempre un `float`, incluso si el usuario ingresa un número entero.
2. Debes convertir la entrada del usuario de cadena de texto a `float` antes de retornarla.

**Ejemplo de uso:**

```python
precio = obtener_precio_usuario()
print(precio)  # Si el usuario ingresa 25, la salida será 25.0
```

---

# Problema 3

En `function_types.py`, crea tres funciones para normalizar una lista de valores en función de su promedio:

## 1. `list_shift`

* **Propósito:** Modificar una lista sumando un valor a cada elemento.
* **Entrada:**

  * Una lista de flotantes (`float`).
  * Un valor flotante a sumar a cada elemento.
* **Salida:**

  * Sin valor de retorno.
  * La lista de entrada se **modifica en su lugar**, con cada elemento incrementado por el valor flotante.

---

## 2. `calc_avg`

* **Propósito:** Calcular el promedio de una lista de flotantes.
* **Entrada:**

  * Una lista de flotantes.
* **Salida:**

  * Un flotante que representa la media aritmética de la lista.

---

## 3. `print_normalized`

* **Propósito:** Imprimir una lista de flotantes.
* **Entrada:**

  * Una lista de flotantes.
* **Salida:**

  * Ninguna (solo imprime la lista).

---

**Ejemplo de uso:**

```python
datos = [2.0, 4.0, 6.0, 8.0]

prom = calc_avg(datos)         # 5.0
list_shift(datos, -prom)       # datos se convierte en [-3.0, -1.0, 1.0, 3.0]
print_normalized(datos)        # imprime [-3.0, -1.0, 1.0, 3.0]
```

**Nota:** Asume que la lista nunca estará vacía.

---

# Problema 4

En `scope.py`, crea dos funciones para trabajar con **variables globales**:

## 1. `set_globals(some_int, some_str)`

* **Propósito:** Almacenar un entero global y una cadena de texto global.
* **Entrada:**

  * `some_int` — un valor entero.
  * `some_str` — un valor de cadena de texto.
* **Salida:**

  * Ninguna.
* **Notas:**

  * Estos valores deben almacenarse como **variables globales**.

---

## 2. `get_globals()`

* **Propósito:** Recuperar los valores de las variables globales.
* **Entrada:**

  * Ninguna.
* **Salida:**

  * Una tupla `(int_value, str_value)` que contiene el entero global y la cadena almacenados.
  * Si las variables globales no han sido asignadas, sus valores por defecto deben ser `None`.

---

**Ejemplo de uso:**

```python
print(get_globals())       # Salida: (None, None)
set_globals(10, "Hello")
print(get_globals())       # Salida: (10, "Hello")
```

---

# Problema 5

En `modules.py`, completa las siguientes tareas **usando los módulos integrados de Python**:

1. **Imprime el directorio de trabajo actual**

   * Usa el módulo apropiado para obtener e imprimir el directorio de trabajo actual en el formato:
   ```plaintext
   Current working directory: <directorio>
   ```

2. **Calcula y almacena el logaritmo en base 2 de un entero ingresado**

   * Solicita al usuario que ingrese un entero con el siguiente mensaje:
   ```python
   "Enter an integer: "
   ```
   * Calcula el logaritmo en base 2 de la entrada usando una función del módulo.
   * Usa la función `math.log2(num)` en lugar de `math.log(num, 2)`.
   * Almacena este valor en una variable e imprímelo en el formato:
   ```plaintext
   Log base 2 of <entrada> is: <valor_log>
   ```

3. **Imprime el piso y el techo del valor logarítmico almacenado**

   * Usa las funciones apropiadas del módulo para imprimir:

     * El **piso** del valor logarítmico en el siguiente formato:
        ```plaintext
        Floor: <val_piso>
        ```
     * El **techo** del valor logarítmico:
        ```plaintext
        Ceiling: <val_techo>
        ```

### Ejemplo de Ejecución

```plaintext
Current working directory: C:\Users\Evelyn\Documents
Enter an integer: 10
Log base 2 of 10 is: 3.321928094887362
Floor: 3
Ceiling: 4
```

---

# Problema 6

En `multiple_files.py`, completa las siguientes tareas usando las funciones en `utils.py`:

## Paso 1 - Importar Funciones

* Importa **todas las funciones** de `utils.py` en una sola línea de código.

## Paso 2 - Codificar un Mensaje

1. Solicita al usuario que ingrese un mensaje con:

   ```python
   "Please type your message\n"
   ```
2. Codifica el mensaje usando el siguiente proceso:

   * **Invierte** el mensaje (voltea la cadena de texto).
   * **Agrega** la cantidad de letras `'a'` del mensaje original al final de la cadena invertida.
   * **Ejemplo:**

     * Mensaje de entrada: `"The sun sets behind the tall hills"`
     * Mensaje codificado: `"sllih llat eht dniheb stes nus ehT1"` (invertido + `1` que representa una `'a'`)
3. Imprime el mensaje codificado al usuario:

   ```plaintext
   Your encoded message is: <mensaje_codificado>
   ```

**Notas:**

* Usa las funciones `flip()` y `count_letters()` de `utils.py`.
* El programa debe funcionar con cualquier mensaje que ingrese el usuario.

### Ejemplo de Ejecución

```plaintext
Please type your message
The sun sets behind the tall hills
Your encoded message is: sllih llat eht dniheb stes nus ehT1
```

---

# Problema 7

En `random_q.py`, escribe un programa que genere un entero aleatorio dentro de un rango especificado por el usuario, usando una semilla fija.

## Pasos

1. **Establece la semilla aleatoria**

   * Usa `random.seed(123)` para garantizar resultados reproducibles.

2. **Solicita los datos al usuario**

   * Pide el inicio del rango con el mensaje:

     ```python
     "Enter the start value:\n"
     ```
   * Pide el fin del rango con el mensaje:

     ```python
     "Enter the end value:\n"
     ```

3. **Genera un entero aleatorio**

   * Genera un entero aleatorio entre los valores de inicio y fin (inclusive).

4. **Imprime el resultado**

   * Usa un f-string para mostrar el número:

     ```plaintext
     Generated random number: <numero_aleatorio>
     ```

### Ejemplo de Ejecución

```plaintext
Enter the start value:
10
Enter the end value:
20
Generated random number: 18
```

---

# Problema 8: Analizador de Actividad Física

**Archivo:** `debugging.py`

## Escenario

Se te proporciona un **Analizador de Actividad Física** para resumir el conteo diario de pasos de un usuario durante una semana. El programa debe:

1. Pedir al usuario que ingrese sus pasos diarios durante 7 días (separados por espacios).
2. Convertir la entrada en enteros.
3. Usar **funciones** para calcular:

   * Total de pasos
   * Promedio diario de pasos (como **entero**)
   * Máximo de pasos
   * Mínimo de pasos
   * Si cada día se alcanzó la meta de 10,000 pasos
4. Imprimir un resumen de todos los resultados.

La versión actual del programa contiene **4 bugs distintos** relacionados con **valores de retorno de funciones, errores lógicos, errores de sintaxis y uso incorrecto de variables**.

## Tareas

1. Identifica y corrige los **errores de sintaxis** (por ejemplo, uso incorrecto de métodos integrados).
2. Corrige las **funciones que no retornan valores**.
3. Corrige los **errores lógicos**, como división entera incorrecta o retorno de la variable equivocada.
4. Asegúrate de que los **valores de retorno** sean de los tipos esperados.
5. Prueba el programa con distintas entradas semanales de pasos para verificar que todos los cálculos sean correctos. Aquí hay algunas entradas de ejemplo con sus salidas esperadas:

### Entrada de Muestra 1

```text
12000 8000 9500 11000 5000 13000 10000
```

### Salida Esperada 1

```text
Total steps: 68500
Average daily steps: 9785
Highest steps in a day: 13000
Lowest steps in a day: 5000
Goal met each day: [True, False, False, True, False, True, True]
```

---

### Entrada de Muestra 2

```text
10000 10000 10000 10000 10000 10000 10000
```

### Salida Esperada 2

```text
Total steps: 70000
Average daily steps: 10000
Highest steps in a day: 10000
Lowest steps in a day: 10000
Goal met each day: [True, True, True, True, True, True, True]
```

---

### Entrada de Muestra 3

```text
0 5000 10000 0 12000 3000 8000
```

### Salida Esperada 3

```text
Total steps: 38000
Average daily steps: 5428
Highest steps in a day: 12000
Lowest steps in a day: 0
Goal met each day: [False, False, True, False, True, False, False]
```

---

# Problema 9: Juego Descifrador de Misterios

## 🎯 Descripción

**Descifrador de Misterios** es un juego de adivinanza de números donde los jugadores deben descifrar el código secreto adivinando números entre 1 y 100. El juego guiará al jugador con pistas útiles hasta que adivine el número correcto.

## 🎮 Cómo Jugar

1. Cuando el juego comience, se te pedirá que **ingreses un número semilla**. Este se usa para inicializar el generador de números aleatorios, de modo que el juego pueda producir el mismo "número secreto" cada vez para propósitos de prueba o demostración.

    ```
    Enter a seed number:
    ```

2. Después de ingresar un número semilla (por ejemplo, `42`), el juego generará silenciosamente un número secreto entre 1 y 100.

3. Luego, se te pedirá repetidamente que adivines el número con:

    ```
    What is your guess:
    ```

4. Según tu respuesta, el juego te dará retroalimentación:
   - Si tu respuesta es **muy baja**, el juego responderá:
     ```
     Too low! Try a higher number.
     ```
   - Si tu respuesta es **muy alta**, el juego responderá:
     ```
     Too high! Try a lower number.
     ```
   - Cuando tu respuesta sea correcta:
     ```
     Correct! You guessed the number!
     ```

5. Una vez que se adivine el número correcto, el juego termina y muestra cuántos intentos tomó:

    ```
    It took you <número> tries!
    ```

## Estructura del Programa

```plaintext
Lab5/
│── game_logic.py     # Maneja el bucle del juego y la interacción con el usuario
│── secret_number.py  # Genera un número secreto aleatorio
│── response.py       # Genera la respuesta al usuario
```

## 📁 Archivos y Funciones

### `secret_number.py`
Maneja la semilla y la generación del número secreto.
- `seed_secret_numbers(seed)` — Inicializa el generador de números aleatorios con la semilla.
- `generate_secret_number(start=1, end=100)` — Retorna un número aleatorio en el rango dado (inclusive).

---

### `response.py`
Maneja la comparación de las respuestas del usuario con el número secreto.
- `input_response(generate_value, user_input)` — Retorna un mensaje y un booleano que indica si la respuesta fue correcta.

---

### `game_logic.py`
Ejecuta el bucle principal del juego.
- Llama a las funciones de `secret_number.py` y `response.py`.
- Maneja la entrada del usuario e imprime los mensajes del juego.

---

# Problema 10: Calculadora

Las Partes I a V son acumulativas: todas las funciones se agregan al mismo archivo `utils.py` y se integran en `main.py` al final.

## Parte I: Suma y Resta

### En `utils.py`:
Diseña dos funciones para realizar suma y resta:
- **`add(num1, num2)`**: Retorna la suma de `num1` y `num2`.
- **`sub(num1, num2)`**: Retorna el resultado de restar `num2` a `num1`.

Ambas funciones deben manejar entradas de tipo **entero** y **decimal**. Dependiendo de la entrada, el valor de retorno puede ser un entero o un decimal.

**Ejemplo de Salida**
```python
add(3, 5)       # 8 (resultado entero)
add(3.5, 5)     # 8.5 (resultado decimal)
sub(10, 4)      # 6 (resultado entero)
sub(10.0, 4.5)  # 5.5 (resultado decimal)
```

---

## Parte II: Multiplicación y División

### En `utils.py`:

Diseña dos funciones para realizar multiplicación y división:
- **`multiply(num1, num2)`**: Retorna el producto de `num1` y `num2`.
- **`divide(num1, num2)`**: Retorna el resultado de dividir `num1` entre `num2`.
  Valida la entrada para asegurarte de que `num2` no sea cero. Si `num2` es cero, retorna un mensaje de error apropiado como cadena de texto:

  ```plaintext
  Error: Division by zero is not allowed.
  ```

Se garantiza que todas las entradas serán números (int o float).
La multiplicación retornará un entero si ambas entradas son enteros, pero un decimal si alguna entrada es decimal.
La división siempre retornará un decimal.

**Ejemplo de Salida**
```python
multiply(3, 4)    # 12 (resultado entero)
multiply(3.5, 4)  # 14.0 (resultado decimal)
divide(10, 2)     # 5.0 (resultado decimal, la división siempre retorna decimal)
divide(7, 3)      # 2.3333333333333335 (resultado decimal)
divide(4, 0)      # "Error: Division by zero is not allowed." (resultado cadena de texto)
```

---

## Parte III: Exponenciación y Módulo

### En `utils.py`:

Diseña dos funciones para realizar exponenciación y módulo:
- **`exponent(base, exp)`**: Retorna `base` elevado a la potencia de `exp`.
- **`modulo(num1, num2)`**: Retorna el residuo de dividir `num1` entre `num2`.
  Valida la entrada para asegurarte de que `num2` no sea cero. Si `num2` es cero, retorna un mensaje de error apropiado:

  ```plaintext
  Error: Modulo by zero is not allowed.
  ```

Se garantiza que todas las entradas serán números (int o float).
La exponenciación y el módulo retornarán decimales si alguna entrada es decimal; de lo contrario, retornarán enteros.

**Ejemplo de Salida**
```python
exponent(2, 3)    # 8 (resultado entero)
exponent(2.0, 3)  # 8.0 (resultado decimal)
modulo(10, 3)     # 1 (resultado entero)
modulo(10.5, 3)   # 1.5 (resultado decimal)
modulo(10, 0)     # "Error: Modulo by zero is not allowed." (resultado cadena de texto)
```

---

## Parte IV: División Entera y Valor Absoluto

### En `utils.py`:
Diseña dos funciones para realizar división entera y retornar valores absolutos:
- **`floor_divide(num1, num2)`**: Retorna el entero más grande menor o igual al resultado de dividir `num1` entre `num2`.
  Valida la entrada para asegurarte de que `num2` no sea cero. Si `num2` es cero, retorna un mensaje de error apropiado:
  ```plaintext
  Error: Division by zero is not allowed.
  ```
- **`absolute(num)`**: Retorna el valor absoluto de `num`.

Se garantiza que todas las entradas serán números (int o float).
La división entera retornará un entero si ambas entradas son enteros, pero un decimal si alguna entrada es decimal.
El valor absoluto coincidirá con el tipo de la entrada.

**Ejemplo de Salida**
```python
floor_divide(10, 3)   # 3 (resultado entero)
floor_divide(10.5, 3) # 3.0 (resultado decimal)
floor_divide(5, 0)    # "Error: Division by zero is not allowed." (resultado cadena de texto)
absolute(-5)          # 5 (resultado entero)
absolute(-5.5)        # 5.5 (resultado decimal)
```

---

## Parte V: Calculadora Completa

### En `main.py`:
Combina todas las funciones en una calculadora completamente funcional que soporte enteros y decimales.

Para hacerlo, importa las funciones de `utils.py` usando una sentencia de importación. Consulta la sección **Múltiples Archivos**.

La calculadora debe:

1. **Elegir una Operación**: Solicita al usuario que seleccione una operación:
   ```plaintext
   Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):
   ```
   Si el usuario selecciona una **operación inválida**, imprime:
   ```plaintext
   Invalid option!
   ```
   **Solicita al usuario que seleccione una opción** hasta que elija una válida.

2. **Aceptar Entradas**:

   `add`, `subtract`, `multiply`, `divide`, `exponent`, `modulo` y `floor_divide` requieren que el programa solicite al usuario **dos números**:
   ```plaintext
   Enter the first number:
   Enter the second number:
   ```

   `absolute` solo requiere **un número**:
   ```plaintext
   Enter the number:
   ```

   > **NOTA:** Se garantiza que todas las entradas serán números válidos. Solo es necesario verificar la división, el módulo o la división entera entre cero.

3. **Mostrar Resultados**: Realiza el cálculo y muestra la **salida sin procesar** (es decir, el resultado con precisión completa) sin redondear:
   ```plaintext
   The result is: <resultado>
   ```
   Reemplaza `<resultado>` con el resultado del cálculo.

   Si `divide`, `modulo` o `floor_divide` encuentra un divisor igual a cero, imprime un mensaje de error en lugar del resultado.

4. **Opción de Salida:** Permite al usuario salir del programa escribiendo `exit` en el mensaje de operación.

5. **Entrada sin Distinción de Mayúsculas/Minúsculas:** Todas las entradas (nombres de operaciones) deben tratarse sin distinguir entre mayúsculas y minúsculas.

---

**Ejemplo de Entrada**

```plaintext
add
3
5
subtract
8.5
4
divide
10
0
exponent
3
2
modulo
9
4
absolute
-9
exit
```

**Ejemplo de Salida**

```plaintext
Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):
Enter the first number:
Enter the second number:
The result is: 8.0
Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):
Enter the first number:
Enter the second number:
The result is: 4.5
Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):
Enter the first number:
Enter the second number:
Error: Division by zero is not allowed.
Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):
Enter the first number:
Enter the second number:
The result is: 9.0
Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):
Enter the first number:
Enter the second number:
The result is: 1.0
Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):
Enter the number:
The result is: 9.0
Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):
```

---

# Problema 11: MáximoDeTres

## Tarea
Se te ha proporcionado un script de inicio **con errores** para **"MáximoDeTres"**.
El programa debe solicitar al usuario **tres enteros**, determinar el **mayor** usando una función, e imprimir el resultado.

Tu trabajo es **depurar el código** para que cumpla con todos los requisitos y pase el calificador automático. Hay **3 líneas** de código que son incorrectas.

## Requisitos

1. Define una función `find_max(a, b, c)` que:
   * Retorne el mayor de los tres números usando sentencias **if/elif/else**.
2. Solicita al usuario **tres veces**, cada vez con:
   ```plaintext
   Enter a number:
   ```
3. Convierte cada entrada del usuario a un **entero**.
4. Llama a la función con las tres entradas y almacena el resultado.
5. Imprime el resultado en este formato:
   ```plaintext
   Maximum value: <num>
   ```
   donde `<num>` es el mayor de los tres enteros.

### Ejemplo de Ejecución

#### Entrada
```plaintext
10
25
13
```
#### Salida
```plaintext
Enter a number:
Enter a number:
Enter a number:
Maximum value: 25
```

---

# Problema 12: Celsius a Fahrenheit

## Función de Conversión de Celsius a Fahrenheit
Escribe una función de Python llamada `celsius_to_fahrenheit(temp)` que tome una temperatura en Celsius como parámetro y retorne la temperatura equivalente en Fahrenheit. La función debe usar la fórmula:

```plaintext
F = (C * 9/5) + 32
```

**Requisitos:**
- La función debe llamarse **`celsius_to_fahrenheit`**.
- Debe tomar **un parámetro**, un valor decimal o entero que represente grados en Celsius.
- Debe **retornar** un número decimal que represente la temperatura en Fahrenheit.
- La función **no debe imprimir** nada; solo debe retornar el valor.

**Ejemplo de Uso:**
```python
print(celsius_to_fahrenheit(0))    # Salida esperada: 32.0
print(celsius_to_fahrenheit(100))  # Salida esperada: 212.0
print(celsius_to_fahrenheit(-40))  # Salida esperada: -40.0
```

---

# Firma de una Función

Una **firma de función** es la primera línea de una función: su nombre y los parámetros que acepta. Es básicamente el "contrato" de la función — te dice qué necesita y qué te va a dar a cambio, sin mostrarte cómo lo hace internamente.

```python
def transform_data(x: int, y: float, z: str) -> float:
    # Lógica de la función (oculta para ti)
```

## Componentes de la Firma

### `def transform_data`
El nombre de la función.

### `(x: int, y: float, z: str)`
Los tres parámetros que recibe. Los `: tipo` después de cada nombre son **anotaciones de tipo** (*type hints*), que indican qué tipo de dato se espera en cada posición:

| Parámetro | Tipo    | Descripción          |
|-----------|---------|----------------------|
| `x`       | `int`   | Un número entero     |
| `y`       | `float` | Un número decimal    |
| `z`       | `str`   | Una cadena de texto  |

### `-> float`
Indica el **tipo de retorno**, es decir, que la función va a devolver un número decimal.

## Nota

En Python, las anotaciones de tipo son **informativas, no obligatorias**. Python no te va a detener si pasas un `float` donde dice `int` — es solo una guía para el programador.

En otros lenguajes como Java o C++, los tipos sí son estrictamente obligatorios.

---

# Problema 13: Módulo Misterioso

Se te proporciona un módulo de Python preescrito llamado **`mystery_module.py`** que contiene una función llamada `transform_data`. La implementación exacta de `transform_data` es desconocida, pero solo necesitas conocer su firma (lee la sección anterior).

```python
def transform_data(x: int, y: float, z: str) -> float:
    # Lógica de la función (oculta para ti)
```

Tu tarea es **importar y llamar** esta función en `caller.py`.

Tu script debe hacer lo siguiente:
1. Llamar a `transform_data` con:
   - La entrada `x` como primer parámetro `x`.
   - La entrada `y` como segundo parámetro `y`.
   - **La cadena de texto `"quiz_test"`** como tercer parámetro `z`.
2. Imprimir el valor de retorno de tu llamada a la función.