# Quiz 3 - Condicionales y Bucles

---

## Pregunta 1

Observa el siguiente fragmento de código:
```python
total = 0
goal = 50

while total < goal:
    coin = int(input("Insert coin: "))
    total = total + coin

print("Done!")
```

**¿Cuántas veces se ejecutará el bucle si el usuario ingresa los valores `25`, `25` en ese orden?**

- A) 1 vez
- B) 2 veces
- C) 3 veces
- D) El bucle nunca termina

---

## Pregunta 2

¿Cuál es el propósito de la condición en un bucle `while`?

- A) Definir qué valor se imprimirá al final del programa
- B) Determinar cuántas variables se pueden usar dentro del bucle
- C) Establecer la condición que debe ser verdadera para que el bucle continúe ejecutándose
- D) Indicar qué tipo de datos puede recibir el programa

---

## Pregunta 3

Considera el siguiente código:
```python
coin = 10

if coin == 25 or coin == 10 or coin == 5 or coin == 1:
    print("Valid")
else:
    print("Invalid")
```

**¿Qué imprimirá este código?**

- A) `Valid`
- B) `Invalid`
- C) `10`
- D) No imprime nada

---

## Pregunta 4

Observa el siguiente código con un error:
```python
total = 0
goal = 30

while total < goal:
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10:
        total = total + coin
    print(total)
```

Si el usuario ingresa `5`, ¿qué sucederá?

- A) Se suma 5 al total y el bucle continúa
- B) El total no cambia pero el bucle continúa indefinidamente (si solo ingresa 5)
- C) El programa termina con un error
- D) Se imprime "Invalid coin"

---

## Pregunta 5

¿Cuál de las siguientes condiciones es correcta para verificar si una variable `coin` tiene un valor de 25, 10, 5 o 1?

- A) `if coin == 25 and 10 and 5 and 1:`
- B) `if coin == 25 or coin == 10 or coin == 5 or coin == 1:`
- C) `if coin = 25 or coin = 10 or coin = 5 or coin = 1:`
- D) `if coin == (25, 10, 5, 1):`

---

## Pregunta 6

Dado el siguiente código:
```python
numbers = []
count = 3

i = 0
while i < count:
    num = int(input("Enter a number: "))
    numbers.append(num)
    i = i + 1
```

Si el usuario ingresa `10`, `20`, `30`, ¿cuál será el contenido de la lista `numbers` al finalizar?

- A) `[10]`
- B) `[30, 20, 10]`
- C) `[10, 20, 30]`
- D) `[]`

---

## Pregunta 7

¿Qué sucede si olvidamos incrementar la variable de control en un bucle `while`?
```python
i = 0
while i < 5:
    print(i)
    # Falta: i = i + 1
```

- A) El bucle se ejecuta 5 veces y termina
- B) El bucle se ejecuta una vez y termina
- C) El bucle se ejecuta infinitamente
- D) El programa muestra un error de sintaxis

---

## Pregunta 8

Considera el siguiente código:
```python
total = 75
goal = 50

if total == goal:
    print("Exact payment")
else:
    change = total - goal
    print("Change owed:", change)
```

**¿Qué imprimirá este código?**

- A) `Exact payment`
- B) `Change owed: 25`
- C) `Change owed: 75`
- D) `Change owed: 50`

---

## Pregunta 9

¿Cuál es la diferencia principal entre `if` y `while`?

- A) `if` usa condiciones y `while` no
- B) `if` ejecuta su bloque una vez si la condición es verdadera; `while` repite su bloque mientras la condición sea verdadera
- C) `while` solo funciona con números y `if` funciona con cualquier tipo de dato
- D) No hay diferencia, son intercambiables

---

## Pregunta 10

Observa el siguiente código:
```python
numbers = [10, 20, 5, 15, 30]
total = 0

for num in numbers:
    total = total + num

print(total)
```

**¿Qué valor imprimirá?**

- A) `30`
- B) `5`
- C) `80`
- D) `0`

---

## Pregunta 11

¿Qué condición usarías para que un bucle `while` continúe ejecutándose **hasta que** `total` sea **mayor o igual a** `goal`?

- A) `while total > goal:`
- B) `while total >= goal:`
- C) `while total < goal:`
- D) `while total == goal:`

---

## Pregunta 12

Dado el siguiente código incompleto:
```python
numbers = [4, 8, 2, 9, 1]
minimum = numbers[0]

for num in numbers:
    if _______________:
        minimum = num

print(minimum)
```

**¿Qué condición debe ir en el espacio en blanco para encontrar el valor mínimo?**

- A) `num > minimum`
- B) `num < minimum`
- C) `num == minimum`
- D) `num >= minimum`