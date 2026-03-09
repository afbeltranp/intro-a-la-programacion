# Alcance

#### Objetivos de Aprendizaje:

- ✅ Comprender la diferencia entre el alcance global y local.
- ✅ Reconocer cómo se comportan las variables en funciones, bucles y condicionales.
- ✅ Aprender buenas prácticas para evitar errores relacionados con el alcance.

---

## ¿Qué Es el Alcance?

El **alcance** se refiere a la parte de un programa donde una variable es **accesible**.

Hay dos tipos principales de alcance:

1. **Alcance Global** - Variables definidas **fuera** de las funciones.
2. **Alcance Local** - Variables definidas **dentro** de una función o bloque (como un bucle o condicional).

---

## Alcance Global

Las variables declaradas **fuera de las funciones** son accesibles globalmente en todo el archivo.

```python
x = 5  # Variable global

def mostrar_x():
    print(x)  # Puede acceder a la variable global

mostrar_x()  # Salida: 5
```

---

## Alcance Local

Las variables declaradas **dentro de una función** solo existen dentro de esa función.

```python
def asignar_valor():
    y = 10  # Variable local
    print(y)

asignar_valor()  # Salida: 10
# print(y) → Error: y no está definida
```

---

## Sombreado y Conflictos

Si una variable local tiene el **mismo nombre** que una global, la local tiene prioridad dentro de esa función.

```python
z = 100

def actualizar_z():
    z = 50
    print(z)  # Salida: 50 (z local)

actualizar_z()
print(z)  # Salida: 100 (z global)
```

---

## Alcance en Bucles y Condicionales

En Python, las variables declaradas dentro de bloques `for`, `while` o `if` **no están aisladas** como en algunos otros lenguajes.

```python
for i in range(3):
    var_bucle = i

print(var_bucle)  # Salida: 2 (sigue siendo accesible)
```

---

## Modificar Variables Globales (No Recomendado)

Puedes modificar una variable global dentro de una función usando la palabra clave `global`, pero esto se **desaconseja** a menos que sea estrictamente necesario.

```python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # Salida: 1
```

---

## Buenas Prácticas

- Evita usar `global` a menos que sea absolutamente necesario.
- Pasa variables como argumentos en lugar de depender de globales.
- Limita el alcance de las variables al lugar donde se necesitan.

Mantener un alcance limpio hace que tu código sea **más fácil de leer, depurar y probar**.

