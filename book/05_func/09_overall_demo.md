# Demostración General

# Juego Descifrador de Misterios

# 🎯 Descifrador de Misterios

**Descifrador de Misterios** es un juego de adivinanza de números donde los jugadores deben descifrar el código secreto adivinando números entre 1 y 100. El juego guiará al jugador con pistas útiles hasta que adivine el número correcto.

---

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
- `seed_secret_numbers(seed)`
  Inicializa el generador de números aleatorios con la semilla.
- `generate_secret_number(start=1, end=100)`
  Retorna un número aleatorio en el rango dado (inclusive).

---

### `response.py`
Maneja la comparación de las respuestas del usuario con el número secreto.
- `input_response(generate_value, user_input)`
  Retorna un mensaje y un booleano que indica si la respuesta fue correcta.

---

### `game_logic.py`
Ejecuta el bucle principal del juego.
- Llama a las funciones de `secret_number.py` y `response.py`.
- Maneja la entrada del usuario e imprime los mensajes del juego.
