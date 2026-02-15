# Enumerate

## Objetivos de aprendizaje
- ✅ Comprender el concepto y la sintaxis de la función `enumerate` en Python.
- ✅ Aprender cómo usar `enumerate` para acceder al índice y valor de elementos en un iterable.
- ✅ Demostrar ejemplos de casos de uso comunes para `enumerate`.

---

## ¿Qué es `enumerate`?
La función `enumerate` es una función integrada en Python que te permite iterar sobre iterables (como listas y tuplas) con un contador automático. Agrega un contador a un iterable y lo devuelve en forma de objeto enumerado.

---

## Sintaxis básica
```python
enumerate(iterable, start=0)
```

---

## Ejemplos de uso de `enumerate`

### 1. Iterando sobre una lista
```python
frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas):
    print(indice, fruta)
# Salida:
# 0 manzana
# 1 banana
# 2 cereza
```

### 2. Usando un índice inicial personalizado
```python
frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas, start=1):
    print(indice, fruta)
# Salida:
# 1 manzana
# 2 banana
# 3 cereza
```

### 3. Enumerate sobre múltiples listas

Usando `zip` con `enumerate` para iterar sobre múltiples listas simultáneamente:
```python
nombres = ["Juan", "Ana", "Pedro"]
edades = [25, 30, 35]
for indice, (nombre, edad) in enumerate(zip(nombres, edades)):
    print(indice, nombre, edad)
# Salida:
# 0 Juan 25
# 1 Ana 30
# 2 Pedro 35
```

---

## Pregunta

En **`enumerate.py`**, recopilarás **dos conjuntos de 3 entradas de strings cada uno** (para un total de **6 entradas**). Cada conjunto de entradas formará una lista separada.

---

### Pasos

1. Solicita al usuario **3 veces** elementos para la **Lista 1**.
   * Cada prompt debe mostrar exactamente:
     **`"Enter item for List 1:\n"`**

2. Solicita al usuario **3 veces** elementos para la **Lista 2**.
   * Cada prompt debe mostrar exactamente:
     **`"Enter item for List 2:\n"`**

3. **Combina (zip)** las dos listas.

4. Usa **enumerate** para imprimir la salida en el formato:
```
   <indice> <elemento_lista1> <elemento_lista2>
```

---

### Ejemplo de ejecución

**Entrada:**
```plaintext
Temperature
Humidity
Pressure
21
65%
1013hPa
```

**Salida:**
```plaintext
0 Temperature 21
1 Humidity 65%
2 Pressure 1013hPa
```
