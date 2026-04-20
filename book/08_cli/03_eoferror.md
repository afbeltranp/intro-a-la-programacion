# EOFError (Ejemplo 2)

## Objetivo de Aprendizaje

- ✅ Comprender qué es un `EOFError`, por qué ocurre y cómo manejarlo.

---

## ¿Qué significa EOF?

**EOF** significa **End Of File** (Fin de Archivo). En programación, representa el punto donde ya no hay más datos disponibles para leer.

Imagina que estás leyendo un libro: EOF es como llegar a la última página y no tener más páginas que leer.

---

## ¿Qué es un EOFError?

Un **EOFError** ocurre en Python cuando el programa intenta leer entrada con `input()`, pero **no hay más datos disponibles**. Es decir, Python esperaba recibir algo, pero se encontró con el "final" del flujo de entrada.

---

## ¿Cuándo Ocurre un EOFError?

### Escenario 1: Entrada Redirigida desde un Archivo

Cuando ejecutas un script y le pasas datos desde un archivo:

```bash
python mi_script.py < datos.txt
```

Si tu script pide más `input()` de los que hay líneas en `datos.txt`, obtendrás un EOFError.

**Ejemplo:**

```python
# mi_script.py
nombre = input("Nombre: ")
edad = input("Edad: ")
ciudad = input("Ciudad: ")  # ¡EOFError si datos.txt solo tiene 2 líneas!
```

**datos.txt:**
```
Juan
25
```

Al ejecutar `python mi_script.py < datos.txt`, el tercer `input()` causa EOFError porque el archivo solo tiene 2 líneas.

---

### Escenario 2: Entrada por Pipeline

Cuando pasas datos a través de un pipe:

```bash
echo "Hola" | python mi_script.py
```

Si el script intenta leer más de una línea, la segunda llamada a `input()` causará EOFError.

---

### Escenario 3: El Usuario Cierra la Entrada Manualmente

En una terminal interactiva, el usuario puede indicar "fin de entrada" presionando:
- **Ctrl+D** en Linux/macOS
- **Ctrl+Z + Enter** en Windows

```python
texto = input("Escribe algo: ")  # Usuario presiona Ctrl+D sin escribir nada
# EOFError!
```

---

### Escenario 4: Bucles que Leen Más de lo Esperado

Este es el caso más común en tareas de programación:

```python
while True:
    linea = input()  # Eventualmente se acabará la entrada
    print(linea)
# EOFError cuando no hay más líneas
```

---

## Cómo Manejar EOFError

### Método 1: Usando try-except

```python
try:
    entrada = input("Ingresa algo: ")
    print(f"Escribiste: {entrada}")
except EOFError:
    print("No se recibió entrada.")
```

---

### Método 2: En un Bucle de Lectura

Cuando necesitas leer múltiples líneas hasta que se acaben:

```python
lineas = []
while True:
    try:
        linea = input()
        lineas.append(linea)
    except EOFError:
        break  # Salir del bucle cuando no hay más entrada

print(f"Leíste {len(lineas)} líneas")
```

---

## Diferencia entre EOFError y Cadena Vacía

Es importante no confundir EOFError con una entrada vacía:

| Situación | Resultado |
|-----------|-----------|
| Usuario presiona Enter sin escribir | `input()` retorna `""` (cadena vacía) |
| No hay más datos disponibles | `input()` lanza `EOFError` |

```python
try:
    entrada = input("Escribe algo: ")
    if entrada == "":
        print("Entrada vacía, pero SÍ hubo entrada")
    else:
        print(f"Escribiste: {entrada}")
except EOFError:
    print("No había datos para leer (EOF)")
```

---

## Errores Comunes que Causan EOFError

### Error 1: Usar `input()` donde debería ser `print()`

```python
# ❌ INCORRECTO - pide entrada innecesariamente
bienvenida = input("¡Bienvenido al programa!")

# ✅ CORRECTO - solo muestra el mensaje
print("¡Bienvenido al programa!")
```

### Error 2: Condición de Salida que Nunca se Cumple

```python
# ❌ INCORRECTO - si la entrada nunca es exactamente "done", bucle infinito → EOFError
while True:
    opcion = input("Opción ('done' para salir): ")
    if opcion == "done":
        break

# ✅ CORRECTO - maneja variaciones de mayúsculas/minúsculas
while True:
    opcion = input("Opción ('done' para salir): ")
    if opcion.lower() == "done":
        break
```

### Error 3: No Leer las Instrucciones del Problema

```python
# Las instrucciones dicen: "ingresa -1 para terminar"
# Pero el programador escribió:
while True:
    opcion = input()
    if opcion == "salir":  # ❌ Debería ser "-1"
        break
```

---

## Depuración de EOFError

Si encuentras un EOFError inesperado, sigue estos pasos:

1. **Imprime cada entrada** para ver qué estás recibiendo:
   ```python
   entrada = input()
   print(f"DEBUG - Recibí: '{entrada}'")
   ```

2. **Cuenta tus llamadas a `input()`** — ¿estás pidiendo más entradas de las que recibes?

3. **Verifica tus condiciones de salida** — ¿el bucle puede terminar correctamente?

4. **Revisa las instrucciones** — ¿qué valor exacto indica el fin de la entrada?

---

## Resumen

| Concepto | Descripción |
|----------|-------------|
| **EOF** | "End Of File" - No hay más datos para leer |
| **EOFError** | Error que ocurre cuando `input()` no tiene datos disponibles |
| **Causa común** | Pedir más entrada de la que existe |
| **Solución** | Usar `try-except EOFError` para manejar el fin de datos |
