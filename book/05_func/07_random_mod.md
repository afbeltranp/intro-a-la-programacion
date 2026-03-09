# Módulo Random

#### Objetivos de Aprendizaje:
- ✅ Comprender el propósito del módulo `random`.
- ✅ Aprender a generar números aleatorios usando el módulo `random`.
- ✅ Explorar las distintas funciones disponibles en el módulo `random`.
- ✅ Entender cómo usar el módulo `random` para selección aleatoria y mezcla de elementos.

---

## ¿Qué Es el Módulo `random`?

El módulo `random` en Python proporciona un conjunto de funciones para generar números pseudoaleatorios y realizar operaciones aleatorias, como seleccionar elementos al azar de una lista, mezclar una secuencia, y más. Es particularmente útil en simulaciones, juegos y situaciones donde se necesita aleatoriedad en los programas.

---

## Funciones Comunes del Módulo `random`

A continuación se presentan algunas de las funciones más utilizadas del módulo `random`:

### 1. `random.random()`

Genera un número decimal aleatorio entre 0.0 y 1.0.

```python
import random

# Generar un float aleatorio entre 0.0 y 1.0
float_aleatorio = random.random()
print(float_aleatorio)
```

### 2. `random.randint(a, b)`

Genera un entero aleatorio entre los valores `a` y `b`, inclusive.

```python
import random

# Generar un entero aleatorio entre 1 y 10 (inclusive)
entero_aleatorio = random.randint(1, 10)
print(entero_aleatorio)
```

### 3. `random.uniform(a, b)`

Genera un número decimal aleatorio entre `a` y `b`.

```python
import random

# Generar un float aleatorio entre 1.5 y 5.5
float_aleatorio = random.uniform(1.5, 5.5)
print(float_aleatorio)
```

### 4. `random.choice(sequence)`

Retorna un elemento seleccionado aleatoriamente de una secuencia no vacía (como una lista, tupla o cadena de texto).

```python
import random

# Seleccionar aleatoriamente un elemento de una lista
colores = ["rojo", "verde", "azul", "amarillo"]
color_aleatorio = random.choice(colores)
print(color_aleatorio)
```

### 5. `random.shuffle(sequence)`

Mezcla los elementos de una secuencia en su lugar, es decir, reorganiza el orden de los elementos.

```python
import random

# Mezclar los elementos de una lista
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros)
```

### 6. `random.sample(population, k)`

Retorna una lista de `k` elementos únicos seleccionados aleatoriamente de la población dada. La población puede ser cualquier secuencia (lista, tupla, etc.).

```python
import random

# Seleccionar 3 elementos aleatorios de la lista sin repetición
numeros = [1, 2, 3, 4, 5, 6]
muestra_aleatoria = random.sample(numeros, 3)
print(muestra_aleatoria)
```

### 7. `random.choices(population, weights=None, k=1)`

Retorna una lista de `k` elementos seleccionados de la población, con ponderación opcional. Los elementos pueden repetirse y puedes controlar la probabilidad de que cada elemento sea elegido mediante pesos.

```python
import random

# Seleccionar 3 elementos con probabilidad ponderada
items = ["manzana", "banana", "cereza"]
pesos = [0.1, 0.5, 0.4]
elecciones_aleatorias = random.choices(items, weights=pesos, k=3)
print(elecciones_aleatorias)
```

### 8. `random.seed(a=None)`

Establece la semilla del generador de números aleatorios, garantizando la reproducibilidad. Si se usa la misma semilla, la secuencia de números aleatorios será la misma cada vez que se ejecute el programa.

```python
import random

# Establecer la semilla en 10
random.seed(10)

# Generar números aleatorios con la misma semilla
print(random.random())  # Producirá la misma salida cada vez con la semilla 10
```

---

## Aplicaciones Prácticas del Módulo `random`

### 1. Simular el Lanzamiento de un Dado

Puedes simular el lanzamiento de un dado usando `random.randint()` para generar enteros aleatorios entre 1 y 6.

```python
import random

# Simular el lanzamiento de un dado
lanzamiento = random.randint(1, 6)
print(f"Lanzamiento del dado: {lanzamiento}")
```

### 2. Seleccionar Aleatoriamente un Ganador

Si tienes una lista de participantes y quieres seleccionar un ganador aleatoriamente, puedes usar `random.choice()`.

```python
import random

# Lista de participantes
participantes = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Seleccionar un ganador aleatorio
ganador = random.choice(participantes)
print(f"El ganador es: {ganador}")
```

### 3. Mezclar una Baraja de Cartas

Puedes mezclar una baraja de cartas usando `random.shuffle()`.

```python
import random

# Una baraja de cartas
baraja = ["As de Picas", "2 de Picas", "3 de Picas", "4 de Picas", "5 de Picas", "6 de Picas", "7 de Picas", "8 de Picas", "9 de Picas", "10 de Picas", "J de Picas", "Q de Picas", "K de Picas"]

# Mezclar la baraja
random.shuffle(baraja)
print("Baraja mezclada:", baraja)
```

### 4. Generar Contraseñas Aleatorias

Puedes generar contraseñas aleatorias seleccionando caracteres al azar de una lista de caracteres.

```python
import random
import string

# Generar una contraseña aleatoria de longitud 8
longitud_contrasena = 8
contrasena = ''.join(random.choices(string.ascii_letters + string.digits, k=longitud_contrasena))
print(f"Contraseña generada: {contrasena}")
```

