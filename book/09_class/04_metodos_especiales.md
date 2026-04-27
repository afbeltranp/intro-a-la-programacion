# Métodos Especiales

## Objetivos de Aprendizaje

- ✅ Comprender los métodos especiales como `__init__`, `__str__` y cómo funcionan.
- ✅ Aprender cómo definir getters y setters en una clase.

## Métodos Especiales en las Clases de Python

Las clases de Python tienen métodos especiales que permiten definir el comportamiento para operaciones como la inicialización de objetos, la representación en cadena y el acceso a datos. Estos métodos hacen que tus objetos se comporten como los tipos incorporados de Python y permiten un mayor control sobre cómo se manejan los datos.

### [1] `__init__`: El Método Constructor

El método `__init__` es un método especial que se usa para inicializar objetos. Se llama automáticamente cuando se crea un objeto a partir de una clase.

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title      # Propiedad
        self.author = author    # Propiedad
        self.year = year        # Propiedad
```

El método `__init__` inicializa las propiedades del objeto cuando se crea. Recibe argumentos (por ejemplo, `title`, `author`, `year`) y los asigna a la instancia.

### [2] `__str__`: Método de Representación en Cadena

El método `__str__` define cómo se representa un objeto cuando se imprime o se convierte en una cadena. Este método es útil para hacer tus objetos más legibles cuando se muestran.

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"
```

Ahora, cuando imprimas un objeto `Book`, Python llamará al método `__str__` para proporcionar una representación en cadena legible:

```python
my_book = Book("1984", "George Orwell", 1949)
print(my_book)  # Salida: '1984' by George Orwell (1949)
```

### [3] Getters y Setters

Los getters y setters son métodos que permiten obtener o establecer el valor de un atributo de un objeto. Este enfoque es parte del principio de **encapsulación**, donde los detalles internos del objeto están ocultos y controlados.

```python
class Book:
    def __init__(self, title, author, year):
        self._title = title    # Usar _ para indicar atributo privado
        self._author = author
        self._year = year

    # Getter para title
    def get_title(self):
        return self._title

    # Setter para title
    def set_title(self, title):
        if len(title) > 1:
            self._title = title
        else:
            print("¡El título es demasiado corto!")

    def __str__(self):
        return f"'{self._title}' by {self._author} ({self._year})"
```

Aquí, el método `get_title` recupera el valor del título, y el método `set_title` establece el valor mientras aplica una condición (por ejemplo, el título debe tener más de un carácter).

```python
my_book = Book("1984", "George Orwell", 1949)

# Acceder al título usando el getter
print(my_book.get_title())  # Salida: 1984

# Cambiar el título usando el setter
my_book.set_title("Animal Farm")
print(my_book.get_title())  # Salida: Animal Farm

# Intentar establecer un título inválido
my_book.set_title("A")  # Salida: ¡El título es demasiado corto!
```

