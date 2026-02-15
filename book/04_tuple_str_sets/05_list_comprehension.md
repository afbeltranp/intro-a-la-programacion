# Comprensión de listas

## Objetivos de aprendizaje
- ✅ Comprender el concepto y la sintaxis de la comprensión de listas en Python.
- ✅ Aprender cómo crear listas de manera eficiente usando comprensión de listas.
- ✅ Demostrar ejemplos de casos de uso comunes para la comprensión de listas.

---

## ¿Qué es la comprensión de listas?
La comprensión de listas es una forma concisa de crear listas en Python. Te permite generar nuevas listas aplicando una expresión a cada elemento en un iterable, opcionalmente filtrando elementos con una condición.

---

## Sintaxis básica
```python
nueva_lista = [expresion for elemento in iterable if condicion]
```

- **`expresion`**: La operación o valor a incluir en la nueva lista.
- **`elemento`**: Cada elemento del iterable (por ejemplo, lista, range, etc.).
- **`iterable`**: La fuente de datos sobre la cual iterar.
- **`condicion`** *(opcional)*: Un filtro que determina qué elementos se incluyen.

---

## Ejemplos de comprensión de listas

### 1. Generar una lista de cuadrados
```python
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 2. Filtrar números pares
```python
numeros_pares = [x for x in range(10) if x % 2 == 0]
print(numeros_pares)  # Salida: [0, 2, 4, 6, 8]
```

### 3. Convertir strings a mayúsculas
```python
palabras = ["hola", "mundo"]
palabras_mayusculas = [palabra.upper() for palabra in palabras]
print(palabras_mayusculas)  # Salida: ['HOLA', 'MUNDO']
```

### 4. Aplanar una lista anidada
```python
lista_anidada = [[1, 2], [3, 4], [5, 6]]
aplanada = [elemento for sublista in lista_anidada for elemento in sublista]
print(aplanada)  # Salida: [1, 2, 3, 4, 5, 6]
```

---

## ¿Por qué usar comprensión de listas?

### Concisión
Crea listas en una sola línea de código.
```python
# Sin comprensión de listas
resultado = []
for x in range(10):
    if x % 2 == 0:
        resultado.append(x)

# Con comprensión de listas
resultado = [x for x in range(10) if x % 2 == 0]
```

### Legibilidad
La sintaxis es intuitiva y más fácil de entender para casos simples.

### Eficiencia
Las comprensiones de listas son generalmente más rápidas que los bucles `for` equivalentes porque están optimizadas para rendimiento.

---

## Casos de uso avanzados

### 1. Expresión condicional en comprensión de listas
```python
numeros = [-5, -3, 0, 2, 4]
positivo_o_cero = [x if x > 0 else 0 for x in numeros]
print(positivo_o_cero)  # Salida: [0, 0, 0, 2, 4]
```

### 2. Comprensión de listas anidada
```python
matriz = [[1, 2], [3, 4], [5, 6]]
transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print(transpuesta)  # Salida: [[1, 3, 5], [2, 4, 6]]
```

### 3. Lista de tuplas
```python
pares = [(x, y) for x in range(3) for y in range(3)]
print(pares)  # Salida: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

---

## Pregunta

En el archivo **`comprehension.py`**, completa el código para que cree una lista llamada **`evens`** que contenga todos los números pares entre los dos valores de entrada (**start** y **end**, inclusive).

1. Las variables **`start`** y **`end`** ya están proporcionadas. Provienen de la entrada del usuario.
2. Usa una **comprensión de listas** para generar la lista de números pares desde **`start`** hasta **`end`**.
   * Pista: Usa el operador módulo (`%`) para verificar si un número es par.
3. Almacena esta lista en la variable **`evens`**.

### Ejemplos de ejecución

**Entrada:**
```plaintext
2  
10  
```

**Salida:**
```plaintext
[2, 4, 6, 8, 10]
```

**Entrada:**
```plaintext
3  
9  
```

**Salida:**
```plaintext
[4, 6, 8]
```
