# Conjuntos

## Objetivos de aprendizaje
- ✅ Comprender qué son los conjuntos y sus características.
- ✅ Aprender cómo crear, manipular y usar conjuntos de manera efectiva.
- ✅ Demostrar operaciones comunes con conjuntos mediante ejemplos.

---

## ¿Qué son los conjuntos en Python?
Un **conjunto** es una **colección desordenada de elementos únicos**. A diferencia de las listas o tuplas, los conjuntos no permiten valores duplicados y están optimizados para pruebas de pertenencia y operaciones matemáticas como uniones e intersecciones.

### Características de los conjuntos
1. **Desordenados**: Los conjuntos no mantienen el orden de los elementos.
2. **Elementos únicos**: Cada elemento en un conjunto debe ser distinto.
3. **Mutables**: Los conjuntos pueden modificarse después de su creación (por ejemplo, agregar o eliminar elementos).
4. **Eficientes**: Los conjuntos se implementan usando tablas hash, lo que hace que las pruebas de pertenencia sean rápidas.

---

## ¿Por qué usar conjuntos?
1. **Eliminar duplicados**: Los conjuntos eliminan automáticamente los valores duplicados, lo que los hace útiles para limpieza de datos.
2. **Operaciones matemáticas**: Los conjuntos soportan operaciones como unión, intersección y diferencia, que son útiles en diversas aplicaciones.
3. **Pruebas de pertenencia**: Verificar si un elemento existe en un conjunto es más rápido que en listas o tuplas.

---

## Cómo crear conjuntos
Los conjuntos pueden crearse usando llaves `{}` o el constructor `set()`.
```python
# Creando un conjunto
frutas = {"manzana", "banana", "cereza"}
print(frutas)  # Salida: {'manzana', 'banana', 'cereza'}

# Usando el constructor set()
numeros_unicos = set([1, 2, 2, 3, 4])
print(numeros_unicos)  # Salida: {1, 2, 3, 4}

# Conjunto vacío
conjunto_vacio = set()
print(conjunto_vacio)  # Salida: set()
```

> **Nota**: `{}` crea un diccionario vacío, no un conjunto vacío.

---

## Operaciones comunes con conjuntos
Python proporciona métodos integrados y operadores para trabajar con conjuntos.

### Agregar y eliminar elementos
```python
# Agregando elementos
mi_conjunto = {1, 2, 3}
mi_conjunto.add(4)
print(mi_conjunto)  # Salida: {1, 2, 3, 4}

# Eliminando elementos
mi_conjunto.remove(2)
print(mi_conjunto)  # Salida: {1, 3, 4}

# Eliminando elementos de forma segura
mi_conjunto.discard(5)  # Sin error si el elemento no existe
print(mi_conjunto)  # Salida: {1, 3, 4}
```

### Pruebas de pertenencia
```python
print(3 in mi_conjunto)  # Salida: True
print(5 in mi_conjunto)  # Salida: False
```

---

## Operaciones matemáticas con conjuntos
Los conjuntos de Python soportan unión, intersección, diferencia y diferencia simétrica.
```python
A = {1, 2, 3}
B = {3, 4, 5}

# Unión
print(A | B)  # Salida: {1, 2, 3, 4, 5}

# Intersección
print(A & B)  # Salida: {3}

# Diferencia
print(A - B)  # Salida: {1, 2}

# Diferencia simétrica
print(A ^ B)  # Salida: {1, 2, 4, 5}
```

---

## Métodos de conjuntos
Además de los operadores, Python proporciona métodos para manipulación de conjuntos.
```python
# Copiando un conjunto
C = A.copy()
print(C)  # Salida: {1, 2, 3}

# Vaciando un conjunto
A.clear()
print(A)  # Salida: set()

# Verificando subconjuntos y superconjuntos
print({1, 2}.issubset(B))  # Salida: False
print(B.issuperset({3, 4}))  # Salida: True
```

---

## Casos de uso para conjuntos

### Deduplicación de datos
Elimina rápidamente duplicados de una lista.
```python
duplicados = [1, 2, 2, 3, 4, 4]
unicos = set(duplicados)
print(unicos)  # Salida: {1, 2, 3, 4}
```

### Pruebas de pertenencia
Los conjuntos proporcionan búsquedas rápidas comparados con listas o tuplas.
```python
nombres = {"Alicia", "Roberto", "Carlos"}
print("Alicia" in nombres)  # Salida: True
```

### Cálculos matemáticos
Realiza operaciones como encontrar elementos comunes o distintos entre conjuntos de datos.

---

## Pregunta

Crea un script de Python llamado **`sets.py`** que elimine entradas de correo electrónico duplicadas de una base de datos de inicio de sesión.

1. **Recopila 5 entradas de correo electrónico del usuario.**

   * Usa el siguiente prompt cada vez:
```python
     "Enter an email:\n"
```

2. **Almacena las entradas en un conjunto** para que cualquier dirección de correo electrónico duplicada se elimine automáticamente.

3. **Imprime el conjunto final de correos electrónicos únicos.**

   * Como los conjuntos son desordenados, asegúrate de que tu salida sea consistente imprimiendo una **versión ordenada** del conjunto:
```python
     print(sorted(<tu_variable_conjunto>))
```

### Ejemplo de ejecución
```plaintext
Enter an email:
a@unisabana.edu.co
Enter an email:
b@unisabana.edu.co
Enter an email:
a@unisabana.edu.co
Enter an email:
c@unisabana.edu.co
Enter an email:
b@unisabana.edu.co
['a@unisabana.edu.co', 'b@unisabana.edu.co', 'c@unisabana.edu.co']
```

**Nota:** `sorted()` siempre devuelve una lista, así que el resultado final siendo una lista es el comportamiento esperado.