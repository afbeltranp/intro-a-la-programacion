# ValueError (Ejemplo 1)

## Objetivo de Aprendizaje

- ✅ Comprender qué es un `ValueError`, por qué ocurre y cómo manejarlo.

---

## Errores de Valor

### ¿Qué es un ValueError?

Un **ValueError** ocurre en Python cuando una función recibe un argumento del **tipo correcto** pero con un **valor inválido**. Esto comúnmente sucede con `int()`, `float()`, u otras funciones de conversión de tipos.

### Cómo Manejar ValueError

#### 1. Usando try-except para capturar ValueError

Un enfoque común es manejar `ValueError` usando un bloque `try-except`:

```python
try:
    numero = int(input("Ingresa un número: "))
    print("Ingresaste:", numero)
except ValueError:
    print("\nValueError: Entrada inválida. Por favor ingresa un número válido.")
```

**¡Asegura que la conversión de entrada no bloquee el programa!**

---

### ¿Cómo Prevenir Errores de Valor?

- **Usa `.isdigit()` o `.isnumeric()`** antes de convertir entrada a números.
- **Envuelve conversiones riesgosas en bloques try-except**.
- **Da a los usuarios instrucciones claras** sobre el formato de entrada esperado.
- **Usa prints de depuración** para inspeccionar qué se está ingresando realmente.

Al implementar estas estrategias, los programas de Python pueden **manejar entrada inválida elegantemente y evitar bloqueos.**


