# Introducción (Try-Except)

## Objetivos de Aprendizaje

- ✅ Comprender por qué el manejo de errores es importante.
- ✅ Aprender a usar `try-except` para capturar errores.
- ✅ Explorar excepciones comunes y cómo manejarlas.

---

## ¿Qué es el Manejo de Errores?

El manejo de errores permite que los programas se recuperen elegantemente de problemas inesperados en lugar de bloquearse. Python usa bloques **`try-except`** para capturar y manejar errores.

---

## 1. La Necesidad del Manejo de Errores

Sin manejo de errores, un problema como dividir por cero **detendrá todo el programa**:

```python
x = 10 / 0  # ZeroDivisionError: division by zero
```

En lugar de dejar que el programa se bloquee, podemos **manejar errores** con `try-except`.

---

## 2. Usando Try-Except

El bloque `try` contiene el **código riesgoso**, y el bloque `except` **maneja los errores**:

```python
try:
    x = 10 / 0
except:
    print("¡No se puede dividir por cero!")
```

**Salida:**

```
¡No se puede dividir por cero!
```

El programa **no se bloquea** y continúa la ejecución.

### Sin embargo, ¡puedes encontrar problemas al dejarlo muy general!

Tomemos este ejemplo:

```python
while True:
  try:
    miEntero = int(input())
    break  # sale del bucle
  except:
    print("Necesito un entero")  # intenta de nuevo
```

A primera vista esto parece seguro. **Sin embargo**, ¡tomemos la siguiente entrada como ejemplo!

```sh
no
ints
```

No encontramos un entero aquí, así que una vez que llegamos al final de la entrada ¡obtenemos un error diferente! Ese error, sin embargo, es capturado y tratado como un `ValueError` en lugar de un `EOFError`. ¡Causando que se quede atrapado en el bucle!

### ¡Intentemos de nuevo!

```python
while True:
  try:
    miEntero = int(input())
    break
  except ValueError:
    print("Necesito un entero")  # intenta de nuevo
  except EOFError:
    print("¡No se pudo completar la solicitud!")
    break  # salir del bucle
```

¡Este es un programa mucho más seguro y completo!

---

## 3. Usando una Excepción Genérica

Un `except` general captura **todos los errores**, como vimos, pero debe usarse con cuidado:

```python
try:
    x = int("hola")  # Conversión inválida
except Exception as e:
    print(f"Ocurrió un error: {e}")
```

**Salida:**

```bash
Ocurrió un error: invalid literal for int() with base 10: 'hola'
```

Esto es útil para depuración pero debería ser **específico cuando sea posible**.

---

## Mejores Prácticas para el Manejo de Errores

- Usa **excepciones específicas** (`ZeroDivisionError`, `ValueError`) en lugar de un `except` general.
- Siempre **prueba código propenso a errores** con diferentes entradas.
- Usa `except Exception as e` **solo para depuración**.

¡El manejo de errores con `try-except` ayuda a crear programas **robustos y amigables para el usuario**!



