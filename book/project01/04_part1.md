## Parte 1 - Implementación como Script Puro
Escribe un juego funcional de "Toros y Vacas" en el archivo `bulls_cows_p1.py`

Tu programa debe exhibir exactamente el mismo comportamiento que el proporcionado en "Ejemplo de Toros y Vacas."

No hay instrucciones adicionales. Asegúrate de que tu programa coincida con lo que hemos proporcionado, incluyendo los mensajes exactos.

### Estructura del Resto de esta Página:

1. **Guía para la Ingeniería Inversa del Script de Toros y Vacas** -- algunos consejos para ayudarte a comenzar.
2. **Estructura General del Programa** -- un esquema abstracto del programa que debes usar para guiar tu implementación.
3. **Script para Generar el Código Secreto** -- este es un bloque de código de regalo que **debes** usar en tu implementación.

## Guía para la Ingeniería Inversa del Script de Toros y Vacas

Cuando realizas ingeniería inversa de un programa, lo primero que debes hacer es tomar notas sobre la funcionalidad que observas. Abre tu software de toma de notas preferido y considera las siguientes preguntas mientras interactúas con el programa:

1. **¿Qué le pregunta el programa primero?**
   - Te ofrece una opción: *generar un código secreto* o *ingresar uno tú mismo*.
   - Prueba `1` y `2`.
   - Anota el efecto inmediato (lo que ves en pantalla) y lo que ocurre en el siguiente turno.

2. **¿Qué nivel de dificultad se selecciona?**
   - Ingresa `1`, `2` o `3`.
   - Registra cómo reacciona el programa justo después de la entrada y cómo cambian las reglas para el resto de la ronda.

3. **Intento con `give up`**
   - Intenta ingresar `"give up"` como tu intento y observa qué ocurre.

4. **Intento que coincide con el código secreto**
   - Ingresa un intento igual al código secreto.
   - Observa el comportamiento del programa.

5. **Intento que no coincide**
   - Ingresa un intento incorrecto.
   - Cuenta los toros y vacas que reporta el programa.
   - Prueba varios intentos y observa cómo cambian los números. Esto demuestra la lógica detrás de la retroalimentación.

6. **Intentos restantes**
   - Después de cada intento, observa cómo se muestra y actualiza el contador de intentos restantes.

7. **Sin intentos restantes**
   - Deja que el contador llegue a cero sin haber adivinado el código secreto.
   - Observa el comportamiento del programa.

8. **Iniciar una nueva ronda**
   - Cuando se te pregunte si deseas jugar de nuevo, escribe `y` y observa qué ocurre.
   - Repite con `n` y observa el resultado.

9. **Mensajes**
   - Para cada aviso, actualización de estado y notificación de fin de juego, copia el texto exacto.
   - Ten estas cadenas a mano; serán útiles al recrear el código.


**Orientación para Tomar Notas**

- Copia los resultados de cada prueba directamente desde la terminal a tus notas para tenerlos como referencia al programar.
- Anota la **salida inmediata** que imprime el programa después de cada respuesta — nuevamente, copia el texto textualmente para saber cómo reproducirlo.
- Agrega una línea breve que resuma cómo esa entrada cambia el estado del juego (por ejemplo, "decrementa los intentos restantes" o "actualiza la dificultad actual").
- Una vez que hayas probado varias entradas diferentes, revisa tus notas y describe, con tus propias palabras, el mecanismo subyacente que usa el programa en cada paso (para que puedas reconstruirlo).

## Estructura General del Programa

1. **Inicio** - el programa muestra un banner de bienvenida e inmediatamente entra en un ciclo continuo de 'jugar ronda' usando **bucles while**.

2. **Configuración de la ronda**

   * Le pregunta al usuario si la computadora debe generar un código secreto de 4 dígitos o si el usuario lo proporcionará.
   * Si se elige la generación, el programa solicita una semilla entera, inicializa el generador de números aleatorios con esa semilla y continúa extrayendo dígitos hasta producir una cadena de cuatro dígitos distintos.
   * Si el usuario proporciona el código, el programa lee una cadena de cuatro dígitos del usuario.

3. **Selección de dificultad**

   * El usuario elige uno de tres niveles de dificultad predefinidos.
   * Cada opción corresponde a un número fijo de intentos permitidos (12, 8 o 5).
   * Este número de intentos se convierte en el contador que se decrementará después de cada intento.

4. **Bucle de intentos**

   * Solicita repetidamente al usuario un intento.
   * La entrada especial `give up` hace que la ronda termine de inmediato.
   * De lo contrario, el intento se compara con el secreto:
     * Por cada posición donde el dígito del intento coincide con el dígito secreto, se cuenta un **toro**.
     * Por cada dígito del intento que aparece en el secreto pero no en la posición correcta, se cuenta una **vaca**.
   * El programa imprime el número de toros y vacas, decrementa el contador de intentos restantes e indica al usuario cuántos intentos le quedan.
   * Si el intento coincide exactamente con el secreto, el usuario gana y la ronda termina.
   * Si el contador llega a cero sin un intento correcto, el usuario pierde y se revela el código secreto.

5. **Fin de ronda y repetición**

   * Tras concluir una ronda — ya sea por victoria, derrota o rendirse — se le pregunta al usuario si desea jugar de nuevo.
   * Responder `y` reinicia desde la configuración de la ronda; cualquier otra respuesta termina el programa.

A lo largo del programa, se utilizan simples bucles **while** y **for**, y se emplea el módulo estándar `random` para la generación del código. Todo el proceso está impulsado por una secuencia descendente de avisos y verificaciones de condiciones, así como por la entrada actual del usuario.

## Script para Generar Aleatoriamente el Código Secreto
Es importante que uses las siguientes líneas de código para generar el código secreto.

```python
seed_val = int(input("Please enter a seed:\n"))
random.seed(seed_val)
secret_code = ""
while len(secret_code) != 4:
    random_val = random.randint(0, 9)
    if str(random_val) not in secret_code:
        secret_code += str(random_val)
```
