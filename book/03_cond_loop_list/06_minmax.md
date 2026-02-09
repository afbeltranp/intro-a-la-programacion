# `min()` y `max()` en Python

## Objetivos de Aprendizaje
- ✅ Comprender **algoritmos de comparación** básicos para encontrar los valores más pequeños y más grandes en una colección.
- ✅ Aprender cómo usar las funciones **`min()`** y **`max()`** de Python para encontrar eficientemente los valores más pequeños y más grandes.
- ✅ Demostrar un caso de prueba con **entrada pre-grabada** para mostrar cómo funcionan estas funciones.

## Entendiendo Algoritmos de Comparación Básicos
Antes de profundizar en las funciones incorporadas de Python, es importante entender el **método tradicional** de encontrar valores mínimos y máximos. Esto típicamente implica iterar a través de cada elemento en una colección y compararlos uno por uno.

### Método Tradicional para Encontrar el Valor Mínimo en una Lista
```python
numbers = [5, 2, 9, 1, 7]
minimum = numbers[0]  # Asume que el primer número es el más pequeño
for number in numbers:
    if number < minimum:
        minimum = number
print("Número mínimo:", minimum)  # Salida: 1
```
**Explicación:**
- El código asume que el primer número es el más pequeño.
- Luego itera a través de la lista, actualizando la variable `minimum` si se encuentra un valor menor.

---

## ¿Qué son `min()` y `max()` en Python?

- **`min()`**: Devuelve el elemento **más pequeño** en un iterable o el más pequeño de dos o más argumentos.
- **`max()`**: Devuelve el elemento **más grande** en un iterable o el más grande de dos o más argumentos.

---

## ¿Por Qué Usar `min()` y `max()`?

- **Eficiencia**: Estas funciones identifican rápidamente los valores más pequeños o más grandes en un conjunto de datos sin requerir lógica de comparación manual.
- **Simplicidad**: Simplifican el código al manejar automáticamente comparaciones entre diferentes tipos de datos como números, strings y listas.

---

## ¿Cómo Funcionan `min()` y `max()` en Python?
Ambas funciones pueden usarse con **listas**, **tuplas** o **múltiples argumentos individuales** para determinar el valor mínimo o máximo. Simplifican el proceso al abstraer la lógica de iteración y comparación en una sola llamada de función.

---

## Ejemplos de Uso de `min()` y `max()`

### Usando `min()` y `max()` con una Lista de Números
```python
numbers = [5, 2, 9, 1, 7]
print("Número mínimo:", min(numbers))  # Salida: 1
print("Número máximo:", max(numbers))  # Salida: 9
```
**Salida:**
```
Número mínimo: 1
Número máximo: 9
```

### Usando `min()` y `max()` con Strings
```python
words = ["apple", "banana", "cherry"]
print("Primera palabra alfabéticamente:", min(words))  # Salida: apple
print("Última palabra alfabéticamente:", max(words))   # Salida: cherry
```
**Salida:**
```
Primera palabra alfabéticamente: apple
Última palabra alfabéticamente: cherry
```

---

## Puntos Clave
- **Eficiencia**: Las funciones **`min()`** y **`max()`** de Python eliminan la necesidad de comparaciones manuales.
- Estas funciones son fáciles de usar con varios tipos de datos, incluyendo **números**, **strings** y **listas**.
- **`min()`** encuentra el valor más pequeño, mientras que **`max()`** encuentra el valor más grande en cualquier iterable o conjunto de argumentos.

---

## Pregunta (`minmax.py`)

Escribe un programa que recopile una lista de nombres del usuario y luego informe qué nombre viene primero alfabéticamente y cuál viene último.

**Instrucciones:**

1. Solicita continuamente al usuario que ingrese nombres uno a la vez.
2. Si el usuario escribe `"DONE"` (en mayúsculas), deja de pedir más entradas.
3. Almacena cada nombre ingresado (excepto `"DONE"`) en una lista.
4. Después de que el usuario haya terminado:

   * Imprime el nombre que viene **primero** alfabéticamente.
   * Imprime el nombre que viene **último** alfabéticamente.