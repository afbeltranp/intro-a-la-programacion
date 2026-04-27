# Clases en Práctica

## Objetivos de Aprendizaje

- ✅ Comprender cómo definir y usar clases en múltiples archivos en Python.
- ✅ Explorar cómo crear múltiples objetos de la misma clase y llamar a sus métodos.

## ¿Cómo Usar Clases en Diferentes Archivos?

En Python, a menudo organizamos nuestro código separando las clases en sus propios archivos. Esto ayuda a mantener el código modular, más fácil de mantener y reutilizable en diferentes partes de un proyecto.

Guía paso a paso para usar clases en diferentes archivos:

1. Definir la clase en un archivo separado
2. Importar la clase en tu script principal
3. Crear objetos y usar métodos

### Paso 1: Definir la Clase en un Archivo Separado

Digamos que estás construyendo un programa que involucra libros. Definirías la clase `Book` en su propio archivo (por ejemplo, `book.py`).

```python
# book.py
class Book:
    def __init__(self, title, author, year):
        self.title = title      # Propiedad
        self.author = author    # Propiedad
        self.year = year        # Propiedad

    def __str__(self):          # Método
        return f"'{self.title}' by {self.author} ({self.year})"
```

**Aquí definimos una clase llamada `Book`. La clase tiene propiedades como `title`, `author` y `year`, y un método `__str__()` que devuelve una cadena formateada.**

### Paso 2: Importar la Clase en tu Script Principal

Una vez que la clase está definida en `book.py`, puedes importarla en otro archivo (por ejemplo, `main.py`) donde quieras crear y usar objetos de esa clase.

```python
# main.py
from book import Book   # Importando la clase Book desde book.py

# Creando una lista de objetos Book
books = [
    Book("1984", "George Orwell", 1949),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
]

# Iterar por la lista e imprimir los detalles de cada libro
for book in books:
    print(book)
```

En `main.py`, importamos la clase `Book` usando `from book import Book`. Luego creamos múltiples objetos `Book` y los almacenamos en una lista. El método `__str__()` se llama en cada objeto al imprimirlo.

### Paso 3: Crear Múltiples Objetos

Cada vez que instancias una clase, creas un objeto. En el ejemplo anterior, creamos tres objetos de la clase `Book`:

```python
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
```

Estos son objetos individuales con sus propios valores de `title`, `author` y `year`. Todos comparten la misma definición de clase pero almacenan datos únicos.

