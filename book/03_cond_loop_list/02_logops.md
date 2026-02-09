# Operadores Lógicos

## Objetivos de Aprendizaje
- ✅ Comprender cómo usar operadores lógicos (`and`, `or`, `not`) en Python.
- ✅ Aprender cómo combinar múltiples condiciones usando operadores lógicos.
- ✅ Demostrar un caso de prueba con entrada pre-grabada para mostrar cómo funcionan los operadores lógicos.

## ¿Qué Son los Operadores Lógicos en Python?
Los operadores lógicos te permiten **combinar múltiples condiciones** en declaraciones de toma de decisiones (`if`, `elif`, `else`). Python proporciona tres operadores lógicos principales:

- **`and`** - Devuelve `True` si *ambas* condiciones son `True`.
- **`or`** - Devuelve `True` si *al menos una* condición es `True`.
- **`not`** - Invierte el valor de verdad de una condición.

### Analogía del Mundo Real: Pasar un Control de Seguridad en un Aeropuerto ✈️
- **`and`** → Solo puedes abordar el avión si tienes *un boleto válido* **y** *tu pasaporte*.
- **`or`** → Puedes pasar la seguridad si tienes *un pase de abordar* **o** *una identificación del personal del aeropuerto*.
- **`not`** → Si *no* tienes artículos prohibidos, se te permite pasar.

---

## ¿Por Qué Usar Operadores Lógicos?
**Condiciones Complejas** - Combina múltiples condiciones para toma de decisiones avanzada.
**Eficiencia** - Simplifica la estructura de las declaraciones condicionales, haciendo el código más limpio.
**Legibilidad del Código** - Mejora la claridad al trabajar con múltiples condiciones.

---

## Operadores Lógicos en Python

| **Operador** | **Descripción** | **Ejemplo** | **Resultado** |
|-------------|----------------|------------|------------|
| **`and`** | Devuelve `True` si *ambas* declaraciones son `True` | `True and False` | `False` |
| **`or`** | Devuelve `True` si *al menos una* declaración es `True` | `True or False` | `True` |
| **`not`** | Invierte el estado lógico de su operando | `not True` | `False` |

Los operadores lógicos a menudo trabajan junto con **operadores de comparación**:

| **Operador** | **Descripción** | **Ejemplo** | **Resultado** |
|-------------|----------------|------------|------------|
| `==` | Verifica si los valores son iguales | `5 == 3` | `False` |
| `!=` | Verifica si los valores no son iguales | `5 != 3` | `True` |
| `>` | Verifica si el valor izquierdo es mayor | `5 > 3` | `True` |
| `<` | Verifica si el valor izquierdo es menor | `5 < 3` | `False` |
| `>=` | Verifica si el valor izquierdo es mayor o igual | `5 >= 5` | `True` |
| `<=` | Verifica si el valor izquierdo es menor o igual | `5 <= 5` | `True` |

---

## Ejemplos de Operadores Lógicos

### Usando `and` (Ambas Condiciones Deben Ser True)
```python
age = int(input("Ingresa tu edad: "))
has_id = input("¿Tienes una identificación? (yes/no): ").lower() == "yes"

if age >= 18 and has_id:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")
```

**Ejemplo de Salida:**
```
Ingresa tu edad: 20
¿Tienes una identificación? (yes/no): no
Acceso denegado.
```

---

### Usando `or` (Al Menos Una Condición Debe Ser True)
```python
is_raining = input("¿Está lloviendo? (yes/no): ").lower() == "yes"
has_umbrella = input("¿Tienes un paraguas? (yes/no): ").lower() == "yes"

if is_raining or has_umbrella:
    print("Puedes salir.")
else:
    print("Mejor quédate adentro.")
```

**Ejemplo de Salida:**
```
¿Está lloviendo? (yes/no): no
¿Tienes un paraguas? (yes/no): yes
Puedes salir.
```

---

### Usando `not` (Invirtiendo el Valor de una Condición)
```python
wants_coffee = input("¿Quieres café? (yes/no): ").lower() == "yes"

if not wants_coffee:
    print("¡Está bien, no hay café para ti!")
else:
    print("¡Aquí está tu café!")
```

**Ejemplo de Salida:**
```
¿Quieres café? (yes/no): no
¡Está bien, no hay café para ti!
```

---

## Puntos Clave
- Los operadores lógicos ayudan a tomar **decisiones complejas** en programas de Python.
- **`and`** requiere que todas las condiciones sean `True`, **`or`** necesita al menos una, y **`not`** niega la condición.
- Comúnmente usados en **declaraciones if** para un mejor flujo del programa y toma de decisiones.

🚀 **¡Ahora Inténtalo Tú Mismo!** ¡Modifica los ejemplos y experimenta con diferentes condiciones para ver cómo funcionan los operadores lógicos!

---

## Pregunta:

Estás programando un script, `logical.py`, para clasificar correctamente a las personas según las condiciones de creación de su cuenta.

El código inicial ya ha sido proporcionado. Le hace al usuario una serie de preguntas de sí/no y almacena las respuestas como valores booleanos (`True` si el usuario escribe `"yes"`, y `False` en caso contrario). Estas variables — `is_verified`, `is_banned`, `is_eligible`, y `meets_requirements` — están listas para ser usadas en tu lógica condicional.

Tu tarea es completar la lógica del programa siguiendo estas reglas:

* Imprime `"Success"` si la persona está verificada, independientemente de cualquier otra condición.
* Si la persona no está prohibida, cumple con todos los requisitos de elegibilidad y cumple con las condiciones necesarias, también imprime `"Success"`.
* En todos los demás casos, imprime `"Failure"`.