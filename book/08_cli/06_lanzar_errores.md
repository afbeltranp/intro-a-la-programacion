# Lanzar Errores

## Tutorial: Lanzando Errores en Python

En Python, puedes **lanzar tus propios errores** usando la palabra clave `raise` y manejarlos usando un bloque **`try`/`except`**.
Esto es útil cuando quieres detener el programa si algo inesperado sucede — pero aún manejar la situación elegantemente en lugar de bloquearse.

---

## 1. Sintaxis Básica

Puedes lanzar un error usando `raise`:

```python
raise Exception("¡Algo salió mal!")
```

Esto detiene inmediatamente el programa y muestra el mensaje de error proporcionado.

---

## 2. Lanzando Errores Incorporados

También puedes lanzar **errores incorporados** como `ValueError`, `TypeError`, o `ZeroDivisionError` cuando algo sale mal.
Esto ayuda a describir exactamente qué tipo de problema ocurrió.

```python
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("¡No se puede dividir por cero!")
    return a / b
```

Si llamas a `dividir(10, 0)`, Python lanza:

```plaintext
ZeroDivisionError: ¡No se puede dividir por cero!
```

---

## 3. Capturando Errores Lanzados

Puedes capturar un error usando un bloque **`try`/`except`**.
Esto previene que el programa se detenga y te permite manejar el error en su lugar.

```python
try:
    dividir(10, 0)
except ZeroDivisionError as e:
    print("Se capturó un error:", e)
```

**Salida:**

```plaintext
Se capturó un error: ¡No se puede dividir por cero!
```

