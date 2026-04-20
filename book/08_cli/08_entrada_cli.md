# Usando Entrada por Línea de Comandos

## Objetivos de Aprendizaje

- ✅ Comprender cómo aceptar **entrada por línea de comandos** en Python.
- ✅ Comprender **mejores prácticas** para manejar entrada por línea de comandos de forma segura.

---

## ¿Qué es la Entrada por Línea de Comandos?

La entrada por línea de comandos permite a los usuarios **interactuar con un script de Python** escribiendo valores en la terminal. Esto puede hacerse mediante:

1. **Entrada interactiva** usando `input()`. (¡Esto ya lo conoces!)
2. **Argumentos pasados** al ejecutar un script (`sys.argv`).

---

## 1. Entrada Interactiva con `input()`

La función `input()` permite a los usuarios ingresar datos mientras el script se está ejecutando:

```python
nombre = input("Ingresa tu nombre: ")
print(f"¡Hola, {nombre}!")
```

**Pausa la ejecución hasta que se reciba la entrada.**

### Ejemplo: Obteniendo Múltiples Entradas

```python
edad = input("Ingresa tu edad: ")
ciudad = input("¿Dónde vives? ")
print(f"Tienes {edad} años y vives en {ciudad}.")
```

**Toda la entrada se almacena como cadena.** Convierte cuando sea necesario:

```python
num = int(input("Ingresa un número: "))  # Convertir entrada a entero
print(num * 2)  # Funciona como entero
```

---

## 2. Manejando Argumentos de Línea de Comandos (`sys.argv`)

En lugar de usar `input()`, los **argumentos de línea de comandos** permiten a los usuarios pasar datos al ejecutar un script.

### Usando `sys.argv` para Argumentos

```python
import sys

print("Nombre del script:", sys.argv[0])  # El nombre del archivo del script
if len(sys.argv) > 1:
    print("Primer argumento:", sys.argv[1])  # Primer argumento
```

**Ejecuta este script:**

```sh
python script.py hola
```

**Salida:**

```
Nombre del script: script.py
Primer argumento: hola
```

---

## 3. Manejando Entrada Inválida

Dado que la entrada siempre es una **cadena**, verifica y convierte cuando sea necesario:

### Ejemplo: Validando Entrada de Enteros

```python
while True:
    try:
        num = int(input("Ingresa un número: "))
        break  # Salir del bucle si es válido
    except ValueError:
        print("Entrada inválida. Por favor ingresa un número.")
```

**Previene bloqueos si se da entrada no numérica.**

---

## Mejores Prácticas para Entrada por Línea de Comandos

- **Valida la entrada** para evitar errores.
- **Convierte tipos de entrada** cuando sea necesario (`int(), float()`).
- **Maneja errores elegantemente** usando `try-except`.
- **Usa `sys.argv`** para argumentos de línea de comandos en scripts.

¡Usar entrada por línea de comandos hace que los programas de Python sean **interactivos y amigables para el usuario!**

