# Tipos de Retorno

#### Objetivos de Aprendizaje:
- ✅ Comprender qué son los tipos de retorno en las funciones de Python.
- ✅ Aprender a usar la sentencia `return` de manera efectiva.
- ✅ Explorar ejemplos de funciones con distintos tipos de retorno.
- ✅ Comprender cómo se pueden retornar múltiples valores.

---

## ¿Qué Son los Tipos de Retorno?

Un **tipo de retorno** es el tipo de valor que una función devuelve al llamador mediante la sentencia `return`. Las funciones pueden retornar:
1. **Un solo valor**: Por ejemplo, un número, cadena de texto o booleano.
2. **Múltiples valores**: Por ejemplo, una tupla o lista.
3. **Ningún valor**: La función retorna `None` cuando no se usa una sentencia `return`.

---

## ¿Por Qué Usar Tipos de Retorno?

1. **Resultados Reutilizables**: Permite que las funciones pasen resultados a otras partes del programa.
2. **Modularidad**: Permite que las funciones realicen cálculos u operaciones y devuelvan el resultado.
3. **Claridad**: Indica claramente qué se espera que produzca una función.

---

## Ejemplos de Tipos de Retorno

### 1. Retorno de un Solo Valor
```python
def cuadrado(num):
    """Retorna el cuadrado de un número."""
    return num ** 2

resultado = cuadrado(4)
print(resultado)  # Salida: 16
```

---

### 2. Retorno de Múltiples Valores
Las funciones de Python pueden retornar múltiples valores como una tupla.
```python
def calcular(a, b):
    """Retorna la suma y el producto de dos números."""
    return a + b, a * b

resultado_suma, resultado_producto = calcular(3, 5)
print(f"Suma: {resultado_suma}, Producto: {resultado_producto}")
```

---

### 3. Sin Valor de Retorno
Si una función no tiene sentencia `return`, retorna `None` implícitamente.
```python
def imprimir_mensaje():
    print("Este es un mensaje.")

resultado = imprimir_mensaje()
print(resultado)  # Salida: None
```

---

### 4. Retorno de Colecciones
Una función puede retornar listas, diccionarios, conjuntos u otras colecciones.
```python
def generar_numeros_pares(n):
    """Retorna una lista de números pares hasta n."""
    return [x for x in range(n + 1) if x % 2 == 0]

print(generar_numeros_pares(10))  # Salida: [0, 2, 4, 6, 8, 10]
```

---

## Verificar Tipos de Retorno

Además de manejar las entradas, a menudo es importante verificar los tipos de retorno de una función para asegurarse de que sean del tipo esperado. Aquí hay algunos métodos para verificar o comprobar el tipo de retorno:

### 1. `isdigit()`
El método `isdigit()` se usa para comprobar si una cadena de texto está compuesta únicamente por dígitos (es decir, sin espacios, signos de puntuación ni letras). Retorna `True` si todos los caracteres son dígitos, y `False` en caso contrario.

```python
def retornar_numero(valor):
    if valor.isdigit():
        return int(valor)
    return "No es un número válido"

resultado = retornar_numero("123")
print(resultado)  # Salida: 123

resultado = retornar_numero("abc")
print(resultado)  # Salida: No es un número válido
```

### 2. `isalpha()`
El método `isalpha()` comprueba si todos los caracteres de una cadena de texto son alfabéticos (es decir, sin dígitos ni caracteres especiales). Retorna `True` si todos los caracteres son alfabéticos, y `False` en caso contrario.

```python
def retornar_cadena(valor):
    if valor.isalpha():
        return valor
    return "Entrada inválida, solo se permiten caracteres alfabéticos"

resultado = retornar_cadena("Hola")
print(resultado)  # Salida: Hola

resultado = retornar_cadena("Hola123")
print(resultado)  # Salida: Entrada inválida, solo se permiten caracteres alfabéticos
```

### 3. Verificar el Tipo con `isinstance()`
Para verificar el tipo de retorno de una función, puedes usar `isinstance()`. Esta función comprueba si el valor retornado es una instancia de una clase* o tipo de dato específico.


> \*¡Las clases se cubrirán más adelante en el curso!


```python
def verificar_tipo_retorno(valor):
    resultado = valor + 10
    if isinstance(resultado, int):
        return resultado
    return "El tipo de retorno no es un entero"

resultado = verificar_tipo_retorno(5)
print(resultado)  # Salida: 15

resultado = verificar_tipo_retorno("cadena")
print(resultado)  # Salida: El tipo de retorno no es un entero
```

Estos métodos pueden ayudar a garantizar que el tipo de retorno coincida con el tipo esperado, lo cual es especialmente útil en programas más grandes donde los valores de retorno pueden pasarse a otras funciones.

---

## Buenas Prácticas para los Tipos de Retorno

1. **Usa Retornos Explícitos**: Evita retornos implícitos de `None` a menos que sea intencional.
2. **Mantén Tipos de Retorno Consistentes**: Una función debería idealmente retornar valores del mismo tipo en todos los escenarios.
3. **Documenta los Tipos de Retorno**: Usa docstrings para describir qué retorna la función.
4. **Evita Efectos Secundarios**: Asegúrate de que el propósito principal de la función esté alineado con su valor de retorno.

---

## Ejemplos de Tipos de Retorno Comunes

### 1. Retornar un Booleano
```python
def es_par(num):
    return num % 2 == 0

print(es_par(4))  # Salida: True
```

### 2. Retornar una Tupla
```python
def obtener_tercios_y_mitades(num):
    return num//3, num//2

print(obtener_tercios_y_mitades(12))  # Salida: (4, 6)
```

### 3. Retornar None para Efectos Secundarios
```python
def registrar_mensaje(mensaje):
    print(f"REGISTRO: {mensaje}")

registrar_mensaje("Esto es una prueba.")  # Sin valor de retorno
```