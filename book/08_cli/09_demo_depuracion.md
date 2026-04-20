# Demo de Depuración

## Parte 1: Depurando Manejo de Excepciones

Aunque ya sabes cómo usar `try-except`, es fácil introducir errores sutiles. Exploremos algunos comunes.

---

### Error #1 — Capturando la Excepción Incorrecta

**Código con Problema:**

```python
try:
    num = int(input("Ingresa un número: "))
except TypeError:
    print("¡Eso no era un número!")
```

**¿Qué está mal?**

- El error es que `int(input())` no lanza un `TypeError`. Lanza un `ValueError` cuando la entrada no puede convertirse.

**Solución:**

```python
try:
    num = int(input("Ingresa un número: "))
except ValueError:
    print("¡Eso no era un número!")
```

**Consejo de Depuración:**
Siempre verifica *qué tipo* de error Python realmente lanza. Usa pequeños fragmentos de prueba y lee los mensajes de error cuidadosamente.

---

### Error #2 — Ocultando Todos los Errores

**Código con Problema:**

```python
try:
    print(10 / 0)
except:
    print("¡Algo salió mal!")
```

**¿Qué está mal?**

- El `except:` genérico oculta todos los posibles errores, incluso los serios.
- Es difícil saber qué realmente salió mal.

**Solución:**

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("¡No puedes dividir por cero!")
```

**Consejo de Depuración:**
Evita declaraciones `except:` vacías — siempre especifica el tipo de error para que no enmascares accidentalmente errores no relacionados.

---

### Error #3 — Excepción en el Lugar Incorrecto

**Código con Problema:**

```python
num = int(input("Ingresa un número: "))
try:
    print(num / 2)
except ValueError:
    print("¡Número inválido!")
```

**¿Qué está mal?**

- La conversión a `int` sucede *antes* del bloque `try`. Si la entrada no es numérica, el programa se bloquea antes de que el error sea capturado.

**Solución:**

```python
try:
    num = int(input("Ingresa un número: "))
    print(num / 2)
except ValueError:
    print("¡Número inválido!")
```

**Consejo de Depuración:**
Pon todo el código que podría lanzar la excepción *dentro* del bloque `try`.

---

## Parte 2: Depurando Entrada por Línea de Comandos

Veamos errores relacionados con argumentos de línea de comandos usando `sys.argv`.

---

### Error #4 — Olvidando Importar `sys`

**Código con Problema:**

```python
filename = sys.argv[1]
print(f"Abriendo {filename}")
```

**¿Qué está mal?**

- El módulo `sys` no está importado, causando `NameError: name 'sys' is not defined`.

**Solución:**

```python
import sys
filename = sys.argv[1]
print(f"Abriendo {filename}")
```

**Consejo de Depuración:**
Cuando uses `sys.argv`, siempre asegúrate de que `import sys` aparezca al principio.

---

### Error #5 — No Verificar la Longitud de Argumentos

**Código con Problema:**

```python
import sys
filename = sys.argv[1]
print(f"Abriendo {filename}")
```

**¿Qué está mal?**

- Si el usuario ejecuta `python script.py` sin argumentos, esto lanza `IndexError: list index out of range`.

**Solución:**

```python
import sys

if len(sys.argv) < 2:
    print("Uso: python script.py <nombre_archivo>")
    sys.exit(1)

filename = sys.argv[1]
print(f"Abriendo {filename}")
```

**Consejo de Depuración:**
Siempre verifica la longitud de `sys.argv` antes de acceder a elementos.

