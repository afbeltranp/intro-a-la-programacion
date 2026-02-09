# Bucles `for`

## Objetivos de Aprendizaje
- ✅ Comprender cómo usar **bucles for** en Python para iterar sobre secuencias.
- ✅ Aprender cómo recorrer **listas**, **strings** y usar la función **range()**.
- ✅ Demostrar un caso de prueba con **entrada pre-grabada** para mostrar cómo funcionan los bucles for.

## ¿Qué Son los Bucles `for` en Python?
Un **bucle for** en Python se usa para **iterar sobre una secuencia** (como una lista, tupla, string o range) y **ejecutar un bloque de código múltiples veces** para cada elemento en la secuencia.

---

## ¿Por Qué Usar Bucles `for`?
- **Eficiencia** - Automatiza tareas repetitivas, reduciendo la necesidad de repetición manual en el código.
- **Versatilidad** - Puede usarse con varias estructuras de datos como **listas**, **strings** y **ranges**.

---

## ¿Cómo Funcionan los Bucles `for` en Python?
- Un bucle `for` recorre **cada elemento** en una secuencia y realiza acciones sobre ese elemento hasta que la secuencia se agota (es decir, el bucle se completa).

---

## Ejemplos de Bucles For

### Recorriendo una Lista
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Me gusta", fruit)
```

### Recorriendo un String
```python
word = "hello"
for letter in word:
    print(letter)
```

### Usando `range()` en un Bucle For
```python
for number in range(5):  # Itera del 0 al 4
    print("Número:", number)
```

### Bucle con `range(inicio, fin, paso)`
```python
for even in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print("Número par:", even)
```
> ¡Nota que la variable paso puede ser negativa!

---

## Puntos Clave
- Usa bucles `for` para iterar a través de secuencias como **listas**, **strings** y **ranges**.
- La función **`range()`** puede ayudar a generar secuencias de números para bucles.
- **Eficiencia** y **versatilidad** hacen de los bucles `for` una herramienta poderosa para automatizar tareas repetitivas.

---

## Pregunta:

**Instrucciones:**
En el archivo **`for.py`**, escribe un programa que:

1. **Tome dos entradas enteras del usuario.**

   * La **primera entrada** será el número mayor.
   * La **segunda entrada** será el número menor.
2. **Use un bucle `for` con un range inverso** para iterar desde el número mayor hasta el número menor.

   * Asegúrate de que el bucle sea **inclusivo** de ambos números, el mayor y el menor.
3. **Imprima cada número** en esta secuencia descendente en su propia línea.

**Ejemplo de Ejecución:**

Entrada:
```plaintext
10
6
```

Salida:
```plaintext
10
9
8
7
6
```