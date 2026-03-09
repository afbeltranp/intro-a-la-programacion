# Demostración de Depuración

## **Lección: Consejos de Depuración en Python**

La depuración es el proceso de encontrar y corregir errores (bugs) en tu código. Aprender a depurar eficientemente es una habilidad fundamental para cualquier programador.

---

## **1. Tipos Comunes de Errores en Python**

1. **Errores de Sintaxis** - Errores en la estructura del código.
   Ejemplo: falta de dos puntos, paréntesis o sangría.

   ```python
   # Error de Sintaxis: falta un dos puntos
   for i in range(5)
       print(i)
   ```

2. **Errores en Tiempo de Ejecución** - Errores que ocurren mientras el programa se ejecuta.
   Ejemplo: dividir entre cero o acceder a una variable que no existe.

   ```python
   # Error en Tiempo de Ejecución: división entre 0
   x = 10
   y = 0
   print(x / y)
   ```

3. **Errores Lógicos** - El código se ejecuta sin fallar, pero produce una salida incorrecta.
   Ejemplo: usar `+` en lugar de `*` en un cálculo.

   ```python
   # Error Lógico
   def cuadrado(x):
       return x + x  # Debería ser x * x

   print(cuadrado(5))  # Salida: 10 (incorrecto)
   ```

---

## **2. Consejos y Estrategias de Depuración**

### **Consejo 1: Lee el Mensaje de Error**

* Los mensajes de error de Python suelen ser descriptivos. Busca:

  * El tipo de error (`SyntaxError`, `TypeError`, etc.)
  * El número de línea
  * Una pista sobre qué salió mal

---

### **Consejo 2: Usa Sentencias Print**

* Inserta sentencias `print()` para verificar los valores de las variables y el flujo del programa. Esto se llama apropiadamente **depuración por print**.

```python
numeros = [1, 2, 3]
for n in numeros:
    print("Número actual:", n)
    cuadrado = n + n  # Error lógico: debería ser n ** 2
    print("Cuadrado:", cuadrado)  # Las sentencias print revelan el error
```

---

### **Consejo 3: Verifica los Tipos de Datos**

* Los errores de tipo son comunes. Usa `type()` para inspeccionar variables.

```python
x = "5"
y = 2
print(type(x))  # <class 'str'>
print(x + y)    # TypeError: no se puede sumar str e int
```

---

### **Consejo 4: Divide tu Código**

* Prueba secciones pequeñas de código de forma independiente para aislar errores.

```python
# En lugar de escribir un programa calculador completo de una vez
# prueba una parte pequeña primero
def multiplicar(n, m):
    return n * m

print(multiplicar(n, m))
```

---

### **Consejo 5: Busca Errores de Desfase por Uno**

* Los bucles son una fuente común de errores sutiles.

```python
# Bug: omitirá el último elemento de la lista
nums = [1, 2, 3, 4]
for i in range(len(nums) - 1):  # Debería ser range(len(nums))
    print(nums[i])
```

---

## **3. Ejercicios de Depuración**

### **Ejercicio 1: Error de Sintaxis**

```python
for i in range(5)
    print("Number:", i)
```

* **Tarea:** Copia este código en `main.py` y corrige el error de sintaxis para que el código se ejecute.


---

### **Ejercicio 2: Error en Tiempo de Ejecución**

```python
x = 10
y = 0
print("Result:", x / y)
```

* **Tarea:** Copia este código en `main.py` y evita que el programa falle al dividir entre cero.

---

### **Ejercicio 3: Error Lógico**

```python
def average(numbers):
    return sum(numbers) / len(numbers) + 1  # Algo está mal

nums = [10, 20, 30]
print("Average:", average(nums))
```

* **Tarea:** Copia este código en `main.py` y corrige la función para que retorne el promedio correcto.

---

### **Ejercicio 4: Error de Tipo**

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Next year you will be " + (age + 1) + " years old")
```

* **Tarea:** Copia este código en `main.py` y corrige el error de tipo.

---

## **4. Conclusiones Clave**

* Lee los mensajes de error con cuidado; a menudo te indican exactamente qué salió mal.
* Imprime los valores de las variables para entender el flujo de tu programa.
* Divide el código en partes más pequeñas y pruébalas de forma incremental.
* Presta atención a errores comunes como desfases por uno o incompatibilidades de tipos.


