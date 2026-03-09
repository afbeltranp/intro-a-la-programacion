# Funciones

#### Objetivos de Aprendizaje:
- ✅ Comprender el propósito y la estructura de las funciones en Python.
- ✅ Aprender a definir, llamar y pasar argumentos a funciones.
- ✅ Explorar ejemplos de funciones reutilizables para distintos escenarios.

---

## ¿Qué Son las Funciones?

Una **función** es un bloque de código reutilizable que realiza una tarea específica. Las funciones permiten escribir código más limpio, organizado y modular.

---

## ¿Por Qué Usar Funciones?

1. **Reutilización**: Escríbelo una vez, úsalo múltiples veces.
2. **Modularidad**: Divide programas complejos en partes más pequeñas y manejables.
3. **Legibilidad**: Hace tu código más fácil de entender.
4. **Mantenibilidad**: Actualiza la funcionalidad en un solo lugar sin cambiar todo el programa.

---

## Definir y Llamar Funciones

### Sintaxis Básica
```python
def nombre_funcion(parametros):
    """Docstring opcional que explica la función."""
    # Cuerpo de la función
    return resultado
```

### Ejemplo
```python
def saludar(nombre):
    """Saluda al usuario por su nombre."""
    return f"¡Hola, {nombre}!"

# Llamando la función
mensaje = saludar("Alicia")
print(mensaje)
```

---

## Componentes de una Función

1. **Nombre de la Función**: Identifica la función.
2. **Parámetros**: Entradas de la función (opcional).
3. **Docstring**: Describe el propósito de la función (opcional pero recomendado).
4. **Sentencia Return**: Devuelve el resultado al llamador (opcional).

---

## Tipos de Funciones

### 1. Funciones Sin Parámetros
```python
def decir_hola():
    print("¡Hola!")

decir_hola()
```

### 2. Funciones Con Parámetros
```python
def sumar_numeros(a, b):
    return a + b

resultado = sumar_numeros(3, 5)
print(f"La suma es {resultado}.")
```

### 3. Funciones Con Parámetros Por Defecto
```python
def saludar_usuario(nombre="Prof. Cruz"):
    return f"¡Bienvenido, {nombre}!"

print(saludar_usuario())        # Se usa el valor por defecto
print(saludar_usuario("Diego")) # Se usa un valor personalizado
```

### 4. Funciones Con Argumentos Variables
```python
def multiplicar(*numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

print(multiplicar(2, 3, 4))  # Salida: 24
```

---

## Paso de Parámetros

1. **Paso por Valor**: Parámetro que, al ser modificado dentro de la función, *no tiene efecto* sobre la variable original.
2. **Paso por Referencia**: Parámetro que, al ser modificado dentro de la función, *modifica directamente* la variable original.

### Ejemplo de Paso de Parámetros
```python
x = 10   # Variable inmutable
y = [10] # Variable mutable

def ejemplo(x, y):
    x = 1
    y[0] = 1

ejemplo(x, y)
print(f"Después de llamar la función: {x}, {y}")

# La salida impresa será:

# Después de llamar la función: 10, [1]
```

