# Tuplas

## Objetivos de aprendizaje
- ✅ Comprender qué son las **tuplas** y sus características.
- ✅ Aprender cómo **crear**, **acceder** y **manipular** tuplas.
- ✅ Demostrar casos de uso de tuplas con **ejemplos**.

---

## ¿Qué son las tuplas en Python?
Una **tupla** es una secuencia inmutable utilizada para almacenar una colección de elementos. A diferencia de las **listas**, los elementos de una tupla no pueden modificarse después de su creación. Las tuplas se utilizan para representar colecciones fijas de elementos.

---

## Características de las tuplas
- **Ordenadas**: Los elementos de una tupla tienen un orden definido.
- **Inmutables**: Una vez creadas, no puedes modificar, agregar ni eliminar elementos.
- **Heterogéneas**: Las tuplas pueden contener elementos de diferentes tipos de datos (enteros, strings, etc.).
- **Eficientes**: Debido a su inmutabilidad, las tuplas son más rápidas que las listas para operaciones de solo lectura.

---

## ¿Por qué usar tuplas?
- **Integridad de datos**: Como las tuplas son inmutables, son ideales para representar datos que no deben cambiar (por ejemplo, coordenadas geográficas, valores de configuración fijos).
- **Rendimiento**: Acceder a elementos de una tupla es más rápido que acceder a elementos de una lista debido a su tamaño fijo.
- **Funcionalidad**: Las tuplas son **hashables** (si contienen elementos hashables), por lo que pueden usarse como **claves en diccionarios** o **elementos en conjuntos**.

---

## Cómo crear tuplas
Las tuplas se crean usando **paréntesis ()** o con **valores separados por comas** sin paréntesis.
```python
# Creando tuplas
tupla_vacia = ()  # Tupla vacía
un_elemento = (42,)  # Tupla con un elemento (la coma es obligatoria)
multiples_elementos = (1, 2, 3)  # Tupla con múltiples elementos

# Tupla sin paréntesis
otra_tupla = 1, 2, 3

# Tupla heterogénea
tupla_mixta = (1, "Hola", 3.14, True)
```

---

## Acceso a elementos de una tupla
Las tuplas soportan **indexación** y **slicing**, similar a las listas.
```python
# Accediendo a elementos por índice
tupla_ejemplo = (10, 20, 30, 40)
print(tupla_ejemplo[0])  # Salida: 10

# Slicing de una tupla
print(tupla_ejemplo[1:3])  # Salida: (20, 30)

# Accediendo a elementos desde el final
print(tupla_ejemplo[-1])  # Salida: 40
```

---

## Operaciones comunes con tuplas

### 1. Desempaquetado de tuplas
Puedes asignar elementos de una tupla a variables directamente.
```python
coordenadas = (10, 20)
x, y = coordenadas
print(f"x: {x}, y: {y}")  # Salida: x: 10, y: 20
```

### 2. Verificación de pertenencia
Verifica si un elemento existe en una tupla usando la palabra clave **`in`**.
```python
frutas = ("manzana", "banana", "cereza")
print("manzana" in frutas)  # Salida: True
```

### 3. Concatenación y repetición
Combina o repite tuplas usando **`+`** (concatenación) y **`*`** (repetición).
```python
tupla1 = (1, 2)
tupla2 = (3, 4)
print(tupla1 + tupla2)  # Salida: (1, 2, 3, 4)
print(tupla1 * 3)  # Salida: (1, 2, 1, 2, 1, 2)
```

---

## ¿Cómo agregar elementos a una tupla en Python?

**No puedes modificar una tupla directamente**, pero puedes **convertirla a una lista**, agregar elementos y convertirla de nuevo:
```python
mi_tupla = (1, 2, 3)

# Convertir a lista, modificar, luego convertir de nuevo a tupla
lista_temp = list(mi_tupla)
lista_temp.append(4)
nueva_tupla = tuple(lista_temp)

print(nueva_tupla)  # Salida: (1, 2, 3, 4)
```

---

## Puntos clave
- Las **tuplas** son secuencias inmutables ideales para representar colecciones fijas de datos.
- Soportan **indexación**, **slicing**, **desempaquetado de tuplas** y operaciones comunes como **concatenación** y **repetición**.
- Usa **tuplas** cuando necesites integridad de datos o cuando necesites almacenar datos como **claves en diccionarios** o **elementos en conjuntos**.

---

**¡Inténtalo tú mismo!** Crea diferentes tipos de tuplas y experimenta con sus operaciones como indexación, slicing y desempaquetado de tuplas.

---

## Pregunta

Se te proporciona un archivo **`tuples.py`**. En este archivo, crea una variable llamada **`val`** que sea una **tupla** con **dos elementos**:

1. **Primer elemento:** la variable proporcionada `num`
2. **Segundo elemento:** el valor de `num / 2`

**Ejemplo**

Si la entrada es `8`, entonces:

* `num = 8`
* `val = (8, 4.0)`

El programa imprimirá:
```plaintext
Is tuple: (8, 4.0)
