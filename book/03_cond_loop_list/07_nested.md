# Listas Anidadas

## Objetivos de Aprendizaje
- ✅ Aprender cómo se estructuran las listas 2D en Python
- ✅ Comprender cómo acceder y modificar elementos en una lista 2D
- ✅ Usar bucles anidados para iterar a través de listas 2D

---

## ¿Qué es una Lista 2D?

Una **lista 2D** en Python es esencialmente una lista de listas. Puedes pensarla como una tabla con filas y columnas. Cada sublista representa una fila, y los elementos en esas sublistas representan columnas.
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Esto crea una matriz de 3x3, donde `matrix[0]` es `[1, 2, 3]`, y `matrix[1][2]` es `6`.

---

## Accediendo y Modificando Elementos

Para **acceder** a un elemento en una lista 2D, usa dos índices: `matrix[fila][columna]`.
Para **modificar**, simplemente asigna un nuevo valor a ese índice.
```python
# Acceder al elemento en la fila 1, columna 2
value = matrix[1][2]  # Esto es 6

# Cambiar el elemento en la fila 0, columna 1 a 20
matrix[0][1] = 20
```

---

## Recorriendo una Lista 2D

Puedes usar **bucles anidados** para recorrer cada fila y columna en una lista 2D.
```python
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

Para imprimir cada fila en una línea puedes hacer esto:
```python
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

Si necesitas rastrear los índices de fila y columna:
```python
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"Elemento en [{i}][{j}] es {matrix[i][j]}")
```

---

## Pregunta:

Escribe un programa, `2Dlists.py`, en el cual uses 9 entradas para crear una lista 2D llamada `board` con 3 filas y 3 columnas. Luego, usa **bucles `for` anidados** para imprimir cada fila en una línea separada así:

### Entrada
```bash
1
2
3
4
5
6
7
8
9
```

### Salida
```bash
1 2 3
4 5 6
7 8 9
```

> **Pista:**
> Asegúrate de que cada elemento esté separado por un espacio. Puedes usar `end=" "` en tus llamadas a `print()` para controlar el formato como se mencionó arriba.