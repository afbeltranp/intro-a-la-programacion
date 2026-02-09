# Bucles While

## Objetivos de Aprendizaje
- ✅ Comprender cómo usar **bucles while** en Python para realizar acciones repetidas basadas en una condición.
- ✅ Aprender cómo implementar y controlar bucles usando **declaraciones condicionales**.
- ✅ Demostrar un caso de prueba con **entrada pre-grabada** para mostrar cómo funcionan los bucles while.

## ¿Qué Son los Bucles `while` en Python?
Un **bucle while** en Python ejecuta repetidamente un bloque de código mientras una condición dada sea **verdadera**. Es especialmente útil para tareas donde el número de iteraciones no se conoce de antemano.

---

## ¿Por Qué Usar Bucles While?
- **Control**: Los bucles while dan un control preciso sobre cómo y cuándo ocurren las iteraciones, haciéndolos ideales para escenarios donde la condición de terminación depende de una situación dinámica (por ejemplo, entrada del usuario o cambio en el estado del sistema).
- **Flexibilidad**: Estos bucles son particularmente útiles cuando deseas que el bucle se ejecute hasta que se cumpla una condición específica, como esperar la entrada del usuario o monitorear el estado del sistema.

---

## ¿Cómo Funcionan los Bucles `while` en Python?
Un **bucle while** verifica una condición antes de ejecutar el bloque de código. Si la condición evalúa a **`True`**, se ejecuta el cuerpo del bucle. El proceso se repite hasta que la condición se vuelve **`False`**.

---

## Ejemplos de Bucles While

### 1. Bucle While Simple
```python
counter = 0
while counter < 5:
    print("El contador es", counter)
    counter += 1
```

### 2. Bucle Infinito con Break
```python
n = 0
while True:
    print("Iteración", n)
    if n == 3:
        print("Saliendo del bucle")
        break
    n += 1
```

### 3. Usando un Bucle While con Entrada del Usuario
```python
number = None
while number != "q":
    number = input("Ingresa un número o 'q' para salir: ")
    if number != "q":
        print("Ingresaste:", number)
    else:
        print("¡Adiós!")
```

### 4. Combinando Bucles `while` con Condiciones (Intento de Inicio de Sesión)
```python
attempts = 0
password = ""
correct_password = "admin123"
while password != correct_password and attempts < 3:
    password = input("Ingresa tu contraseña: ")
    attempts += 1
    if password == correct_password:
        print("Acceso concedido.")
    else:
        print("Contraseña incorrecta, intenta de nuevo.")
if attempts == 3:
    print("Acceso denegado, demasiados intentos.")
```

---

## Break y Continue en Python

En Python, la declaración **`break`** termina un bucle por completo, lo cual es útil cuando no es necesaria más iteración. La declaración **`continue`** omite la iteración actual y procede a la siguiente, permitiendo saltar selectivamente dentro de los bucles.

### Ejemplo de `break`
```python
numbers = [1, 2, 3, 4, 5, -1, 6, 7]
for number in numbers:
    if number < 0:
        print("Número negativo detectado:", number)
        break
    print("Procesando número:", number)
```

### Ejemplo de `continue`
```python
numbers = [1, 2, -1, 4, -5, 6]
for number in numbers:
    if number < 0:
        continue  # Omitir la iteración actual si el número es negativo
    print("Número positivo:", number)
```

### Ejemplo de `continue` con Bucle While
```python
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Omitir el resto del bucle para números pares
    print("Número impar:", count)
```

---

## Puntos Clave
- Los **bucles `while`** permiten la ejecución repetida de código basada en una condición que se verifica antes de cada iteración.
- Usa **`break`** para salir de un bucle anticipadamente cuando no son necesarias más iteraciones.
- Usa **`continue`** para omitir una iteración basada en una condición y continuar el bucle.

---

🚀 **¡Inténtalo Tú Mismo!** Modifica los ejemplos para probar **bucles `while`** con diferentes condiciones o escenarios de entrada personalizados.

---

## Pregunta:
Crea un programa de Python en `while.py` que continuamente solicite al usuario ingresar los nombres de sus películas favoritas. El programa debe operar bajo las siguientes condiciones:

- El programa se ejecuta en un bucle y solicita al usuario ingresar el nombre de una película.
    - `"Enter the name of your favorite movie (type 'exit' to stop or 'skip' to skip):\n"`

- Si el usuario ingresa `"exit"`, el programa debe dejar de solicitar más películas e imprimir `"Goodbye!"`.
    - Usa la declaración break para manejar la salida del bucle.
    - Esto también debe finalizar el programa

- Si el usuario ingresa `"skip"`, solicita inmediatamente otro nombre de película sin romper el bucle ni modificar la lista.
    - Usa la declaración continue para manejar este caso.

- Si el usuario ingresa cualquier otra cosa, el programa debe imprimirlo en el siguiente formato:
```python
  You entered: <movie>
```

  donde `<movie>` representa lo que sea que el usuario haya ingresado.