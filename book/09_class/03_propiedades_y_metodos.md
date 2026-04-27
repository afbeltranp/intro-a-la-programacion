# Propiedades y Métodos

## Objetivos de Aprendizaje

- ✅ Comprender qué son las **propiedades (atributos)** y los **métodos (funciones)** en una clase.
- ✅ Aprender cómo las propiedades almacenan datos del objeto y los métodos definen sus comportamientos.
- ✅ Explorar cómo interactúan las propiedades y los métodos en una clase.

## ¿Qué son las Propiedades?

Las **propiedades** (también llamadas **atributos**) son **variables almacenadas dentro de un objeto** que definen sus características. Cada objeto tiene sus **propios valores** para las propiedades.

### Ejemplo

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand  # Propiedad
        self.color = color  # Propiedad
```

Aquí, `brand` y `color` son **propiedades** que almacenan información sobre un objeto `Car`.

### Usando Propiedades en un Objeto

```python
my_car = Car("Toyota", "Red")
print(my_car.brand)  # Salida: Toyota
print(my_car.color)  # Salida: Red
```

**Cada objeto almacena sus propios valores para estas propiedades.**

---

## ¿Qué son los Métodos?

Los **métodos** son **funciones dentro de una clase** que definen los **comportamientos** de un objeto. Pueden modificar propiedades, realizar acciones o devolver valores basados en los datos del objeto.

### Ejemplo: Añadir un Método a una Clase

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):  # Método
        return f"The {self.color} {self.brand} is driving."
```

### Llamando a un Método en un Objeto

```python
my_car = Car("Toyota", "Red")
print(my_car.drive())  # Salida: The Red Toyota is driving.
```

**Los métodos permiten a los objetos realizar acciones.**

---

## Propiedades vs. Métodos: Diferencias Clave

| Característica | Propiedades (Atributos) | Métodos |
|----------------|------------------------|---------|
| Definición | Almacenan datos del objeto | Definen comportamientos del objeto |
| Tipo | Variables | Funciones |
| Acceso | `objeto.propiedad` | `objeto.metodo()` |
| Ejemplo | `car.color` → `"Red"` | `car.drive()` → `"The Red Toyota is driving."` |

---

## Modificando Propiedades con Métodos

Los métodos pueden **cambiar los valores de las propiedades**, permitiendo que los objetos actualicen sus datos de forma dinámica.

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def repaint(self, new_color):
        self.color = new_color  # Modificar propiedad
        return f"The car is now {self.color}."

my_car = Car("Toyota", "Red")
print(my_car.repaint("Blue"))  # Salida: The car is now Blue.
print(my_car.color)            # Salida: Blue
```

**Los métodos pueden actualizar las propiedades del objeto y realizar acciones.**

---

## Cómo Encontrar y Usar Clases en Bibliotecas

Cuando usamos una **biblioteca de Python**, a menudo interactuamos con clases que proporciona el módulo. Para entender cómo usarlas, sigue estos pasos:

1. **Lee la Documentación Oficial**
   - Visita la documentación del módulo (por ejemplo, [módulo `csv` de Python](https://docs.python.org/3/library/csv.html)).
   - Busca secciones como **Clases** o **Métodos**.
   - En el caso del módulo `csv`, en el menú de la izquierda verás '**Objetos Reader**' y '**Objetos Writer**'.

2. **Encuentra las Clases Disponibles**
   - El módulo `csv` tiene clases como **`csv.reader`** y **`csv.writer`**.
   - Estas clases **proporcionan métodos** para leer y escribir archivos CSV.

3. **Usa la Clase y sus Métodos**
   - Crea un **objeto** a partir de la clase.
   - Llama a los **métodos** de la clase para realizar acciones.

### Ejemplo: Usando `csv.reader` y `csv.writer`

#### 1. Leyendo un Archivo CSV (`csv.reader`)

La **clase** `csv.reader` ayuda a leer archivos CSV **fila por fila**.

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)  # Creando un objeto de la clase csv.reader
    for row in reader:  
        print(row)  # Cada fila es una lista de valores
```

**Aquí, `reader` es un objeto** de la clase `csv.reader`, y usamos sus métodos para leer el contenido del archivo.

#### 2. Escribiendo en un Archivo CSV (`csv.writer`)

La **clase** `csv.writer` ayuda a escribir datos en un archivo CSV.

```python
import csv

data = [["Name", "Age"], ["Alice", 25], ["Bob", 30]]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)  # Creando un objeto de la clase csv.writer
    writer.writerows(data)     # Usando el método del objeto writer
```

**Aquí, `writer` es un objeto** de la clase `csv.writer`, y llamamos a `writerows()` para escribir múltiples filas a la vez.

---

## ¿Por qué usar Propiedades y Métodos?

**Encapsulación** — Mantiene los datos y el comportamiento juntos dentro de los objetos.  
**Reutilización** — Defínelo una vez, úsalo para múltiples objetos.  
**Integridad de Datos** — Los métodos pueden controlar cómo se modifican las propiedades.

Comprender las **propiedades y los métodos** es **esencial** para construir programas orientados a objetos bien estructurados.

