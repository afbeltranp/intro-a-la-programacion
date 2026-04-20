# Demo General

## Laboratorio: Construyendo una Calculadora CLI con Manejo de Errores

### Objetivo

En este demo, los estudiantes construirán una simple **calculadora de 4 funciones basada en CLI** (`calculator.py`) que toma dos números y una operación del usuario. Implementarán **manejo de errores** para entrada inválida y división por cero.

---

## Instrucciones

### Paso 1: Tomar Entrada CLI para Números y Operador

Escribe un script de Python que **acepte tres argumentos de línea de comandos**:

- Un primer número
- Un operador (`+`, `-`, `x`, `/`)
- Un segundo número

El programa debe imprimir el resultado del cálculo.

Ejemplo de uso:

```bash
python calculator.py 10 + 5
```

Salida Esperada:

```
Result: 15
```

En caso de número incorrecto de entradas:

```bash
python calculator.py 10 +
```

Salida Esperada:

```
Invalid usage, should be:
python3 calculator.py <number 1> <operator> <number two>
```

---

### Paso 2: Manejar Entrada Inválida

Modifica tu script para verificar si:

- El usuario proporcionó exactamente tres argumentos
- Los números son válidos (verificación con `isdigit()` o `float()`)
- El operador es uno de `+`, `-`, `x`, o `/`

Si la entrada es **inválida**, imprime un mensaje de error y sal del programa.

Ejemplo (operador inválido):

```bash
python calculator.py 10 x 5
```

Salida Esperada:

```
Error: Invalid operator. Use +, -, x, or /.
```

Ejemplo (número inválido):

```bash
python calculator.py one + 5
```

Salida Esperada:

```
Error: Invalid number!
```

---

### Paso 3: Manejar División por Cero

Modifica tu script para **capturar división por cero** y mostrar un mensaje de error apropiado en lugar de bloquearse.

Ejemplo:

```bash
python calculator.py 10 / 0
```

**Salida Esperada:**

```
Error: Cannot divide by zero.
```
