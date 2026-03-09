# Tipos de Funciones

#### Objetivos de Aprendizaje:
- ✅ Repasar funciones que imprimen información.
- ✅ Repasar funciones que modifican estructuras de datos.
- ✅ Repasar funciones que retornan valores calculados.

---

## ¿Cuáles Son los Tipos de Funciones?

Hay tres tipos principales de funciones:
1. **Funciones de Impresión/Registro**: Típicamente con tipo de retorno `None`, usadas únicamente para registrar información.
2. **Funciones de Mutación**: Usadas para cambiar los valores en una estructura de datos. Típicamente con tipo de retorno `None` o un tipo de retorno que coincide con la estructura de datos que se está modificando.
3. **Funciones Matemáticas/de Comportamiento**: El tipo de retorno puede ser cualquier cosa; se usan para generar un valor o un conjunto de valores a partir de alguna entrada.

---

## Ejemplos de Cada Tipo

A continuación se presentan ejemplos de cada tipo de función para ayudarte a entender cómo y cuándo se usan:

---

### 1. **Función de Impresión / Registro**

Estas funciones se usan para **mostrar información**, **depurar** o **registrar** el estado de tu programa. Por lo general, **no retornan nada**.

```python
def registrar_reporte_ventas(total_ventas):
    print(f"Ventas totales este mes: ${total_ventas}")
```

---

### 2. **Función de Mutación**

Estas funciones **modifican una estructura de datos** en su lugar (como una lista o diccionario). Pueden no retornar nada, pero afectan directamente el objeto de entrada.

```python
def aplicar_descuento(precios, descuento):
    for i in range(len(precios)):
        precios[i] *= (1 - descuento)
```

Uso:

```python
precios = [100, 200, 300]
aplicar_descuento(precios, 0.1)
# precios ahora es [90.0, 180.0, 270.0]
```

---

### 3. **Función Matemática / de Comportamiento**

Son funciones que **calculan y retornan** un nuevo valor basado en la entrada. No alteran estructuras de datos a menos que estén explícitamente diseñadas para ello.

```python
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)
```

Uso:

```python
datos = [5, 10, 15]
prom = calcular_promedio(datos)  # Retorna 10.0
```

---

## Reflexión Final

- **Usa funciones de impresión/registro** para mostrar información útil sin afectar la lógica del programa.
- **Usa funciones de mutación** cuando quieras modificar datos en su lugar.
- **Usa funciones de comportamiento** cuando necesites calcular y retornar resultados.

En la práctica, muchas funciones del mundo real pueden combinar estos estilos, pero entender estas tres categorías te ayudará a escribir código más claro y con mayor propósito.

