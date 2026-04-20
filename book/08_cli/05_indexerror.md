# IndexError (Ejemplo 4)

## Objetivo de Aprendizaje

- ✅ Comprender qué es un `IndexError`, por qué ocurre y cómo manejarlo.

---

## Error de Índice Fuera de Límites

### ¿Qué es un IndexError?

Un **IndexError** ocurre en Python cuando se intenta acceder a un **índice que está fuera del rango** para una lista, tupla u otra colección indexada.

#### Causas Comunes de IndexError

1. **Acceder a un índice que no existe:**

   ```python
   mi_lista = [1, 2, 3]
   print(mi_lista[3])  # IndexError: list index out of range
   ```

2. **Usar un índice negativo demasiado pequeño:**

   ```python
   mi_lista = [10, 20, 30]
   print(mi_lista[-4])  # IndexError: list index out of range
   ```

   - `mi_lista[-3]` es válido (retorna `10`), pero `-4` va más allá del tamaño de la lista.

3. **Iterar incorrectamente sobre un rango de índices:**

   ```python
   numeros = [5, 10, 15]
   for i in range(len(numeros) + 1):  # Error de uno más
       print(numeros[i])  # IndexError cuando i = 3
   ```

---

### ¿Cómo Manejar IndexError?

#### 1. Usando Try-Except para Capturar el Error

Una forma simple de manejar acceso fuera de límites es con `try-except`:

```python
mi_lista = [4, 8, 12]

try:
    print(mi_lista[5])  # Intentando acceder a un índice inválido
except IndexError:
    print("Error: Índice fuera de límites. Por favor verifica el rango del índice.")
```

**Previene que el programa se bloquee.**

---

#### 2. Verificando la Validez del Índice Antes de Acceder

En lugar de manejar errores **después** de que ocurren, verifica si el índice es válido **antes** de acceder a él:

```python
mi_lista = [3, 6, 9]
if 0 <= -4 < len(mi_lista):
    print(mi_lista[-4])
else:
    print("Índice inválido. Por favor ingresa un rango válido.")
```

**Evita IndexError al asegurar que el índice esté dentro del rango.**

---

### Previniendo IndexError en Bucles

#### 1. Usa bucles foreach, cuando sea posible, en lugar de indexación manual

```python
numeros = [5, 10, 15]
for n in numeros:  # Nunca saldrá del rango
    print(n)
```

**Asegura iteración segura sin preocuparse por indexación incorrecta.**

#### 2. Usando `try-except` para Iteración Segura

```python
numeros = [1, 2, 3]
for i in range(len(numeros) + 1):  # Error de uno más
    try:
        print(numeros[i])
    except IndexError:
        print(f"Saltando índice inválido: {i}")
```

**Maneja errores fuera de límites elegantemente.**

---

### Mejores Prácticas para Evitar IndexError

- **Siempre verifica la validez del índice** antes de acceder a elementos.
- **Usa bucles foreach** para iteración segura.
- **Ten cuidado con bucles** que iteran más allá de la longitud de la lista.
- **Maneja errores elegantemente** con bloques `try-except`.

¡Siguiendo estas técnicas, los programas de Python pueden **prevenir y manejar errores de "Índice Fuera de Límites" efectivamente!**

