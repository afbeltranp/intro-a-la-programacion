# Listas y Range

## Objetivos de Aprendizaje
- ✅ Comprender cómo **crear** y **manipular** listas en Python.
- ✅ Aprender cómo usar la función **range()** para generar secuencias de números.
- ✅ Demostrar **indexación de listas** y **slicing** usando posiciones.
- ✅ Mostrar un caso de prueba con **entrada pre-grabada** para ilustración.

## ¿Qué Son las Listas y Range en Python?
**Listas** - Una colección de elementos ordenados y mutables que permiten duplicados y pueden almacenar múltiples tipos de datos.
**Range** - La función `range()` genera una **secuencia de números**, comúnmente usada para bucles.

---

## ¿Por Qué Usar Listas y Range?
**Flexibilidad** - Las listas pueden almacenar múltiples tipos de datos y permitir modificaciones.
**Eficiencia** - `range()` genera **secuencias numéricas** eficientemente sin almacenar todos los números en memoria.

---

## ¿Cómo Funcionan las Listas y Range en Python?
- Las **listas** se definen usando corchetes `[]` y soportan **indexación** y **slicing**.
- **Range** se usa para generar secuencias de números y a menudo se utiliza en bucles.

### Ejemplo: Creando y Accediendo a Listas
```python
# Creando una lista
fruits = ["apple", "banana", "cherry"]
print("Lista Original:", fruits)

# Accediendo a elementos de la lista por índice
print("Primera fruta:", fruits[0])  # Salida: apple

# Slicing de una lista
print("Primeras dos frutas:", fruits[0:2])  # Salida: ['apple', 'banana']
```

### Ejemplo: Usando `range()` para Generar Números
```python
# Creando una secuencia de números del 0 al 4
numbers = list(range(5))  
print("Números de range(5):", numbers)  # Salida: [0, 1, 2, 3, 4]

# Generando números pares usando range(inicio, fin, paso)
even_numbers = list(range(0, 10, 2))  
print("Números pares:", even_numbers)  # Salida: [0, 2, 4, 6, 8]
```

---

## Operaciones Comunes con Listas

| **Función** | **Descripción** | **Ejemplo** | **Resultado** |
|-------------|----------------|-------------|------------|
| `append()`  | Agrega un elemento al final de la lista | `lst.append(4)` | `[1, 2, 3, 4]` |
| `remove()`  | Elimina la primera aparición de un elemento | `lst.remove(2)` | `[1, 3]` |
| `pop()`  | Elimina y devuelve un elemento en un índice dado | `lst.pop(1)` | `2` |
| `range()`  | Genera una secuencia de números | `range(1, 5)` | `1, 2, 3, 4` |
| `len()`  | Devuelve el número de elementos en una lista | `len(lst)` | `3` |
| `sort()`  | Ordena la lista, modificando la variable misma | `lst.sort()` | `[1, 2, 3]` |
| `sorted()`  | Devuelve una lista ordenada | `sorted(lst)` | `[1, 2, 3]` |
| `list()`  | Convierte un range o iterable en una lista | `list(range(4))` | `[0, 1, 2, 3]` |

---

## Ejemplos de Uso de Listas y Ranges

### Agregando Elementos a una Lista
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  
print(fruits)  # Salida: ['apple', 'banana', 'cherry', 'orange']
```

### Usando `range()` en un Bucle
```python
for i in range(6):
    print(i)  # Salida: 0 1 2 3 4 5
```

---

## Puntos Clave
- Las **listas** almacenan múltiples elementos y soportan indexación, slicing y modificación.
- **Range** genera eficientemente secuencias de números, a menudo usadas en bucles.
- Usa funciones incorporadas como `append()`, `remove()`, `sorted()`, y `len()` para manipular listas.

🚀 **¡Ahora Inténtalo Tú Mismo!** ¡Experimenta con operaciones de listas y funciones range en Python!

---

## Pregunta:

Completa el programa `list.py`, en el cual usarás la lista dada y realizarás las siguientes operaciones:

- Agregar un valor ingresado (convierte este valor a un `int`)

> **Nota Importante:**
> Esto significa que tomas una entrada usando la función `input()`. Como no se indicó cuál es el mensaje para el usuario, significaría que no imprimes nada. Lo escribirías así: `input("")`.

- Eliminar o hacer pop del primer valor
- Ordenar la lista
- Imprimir la lista