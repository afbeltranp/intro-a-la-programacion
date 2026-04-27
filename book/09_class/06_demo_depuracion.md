# Depuración

## Objetivo de Aprendizaje

Al final de esta actividad, podrás **identificar y corregir errores comunes relacionados con clases en Python**, incluyendo:

* `self` faltante o incorrecto
* Atributos no inicializados o referenciados incorrectamente
* Nombres de atributos mal escritos
* Listas de parámetros de métodos incorrectas
* Métodos `__str__` que imprimen en lugar de devolver

---

## Errores Comunes en Clases (Usando una Clase `Student`)

Comencemos con algunos ejemplos usando una clase `Student`.

---

### Error #1 — `self` Faltante en las Definiciones de Métodos

#### Problema

```python
class Student:
    def __init__(name, major):
        name = name
        major = major
```

Falta `self`, por lo que nada queda vinculado a la instancia.

Cuando intentas crear un objeto `Student` así:

```python
s1 = Student("Alice", "Math")
```

Obtendrás este error:

```
TypeError: Student.__init__() takes 2 positional arguments but 3 were given
```

#### Por Qué Ocurre

* Python siempre proporciona la instancia (`self`) como primer argumento para los métodos de instancia.
* Si olvidas incluirlo en la definición del método, la llamada pasa un argumento extra.
* La discrepancia provoca un `TypeError`.

#### Solución

Añade `self` como primer parámetro en el constructor (y en todos los métodos de instancia):

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
```

---

### Error #2 — Olvidar `self.` al Asignar o Acceder a Atributos

#### Problema

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def introduce(self):
        print(name)
```

Llamar a `introduce` no imprimirá nada.

Si en cambio olvidas `self.` durante la asignación:

```python
class Student:
    def __init__(self, name, major):
        name = name
        self.major = major

    def introduce(self):
        print(self.name)
```

Al llamar a `introduce`, obtienes este error:

```
AttributeError: 'Student' object has no attribute 'name'
```

#### Solución

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def introduce(self):
        print(self.name)
```

Usa `self.` para que cada atributo pertenezca a la instancia.

---

### Error #3 — Nombres de Atributos Mal Escritos

#### Problema

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

s1 = Student("Alice", "Math")
print(s1.nam)
```

Genera:

```
AttributeError: 'Student' object has no attribute 'nam'
```

#### Solución

Siempre verifica la ortografía — Python distingue entre mayúsculas y minúsculas.

---

### Error #4 — `__str__` Imprime en Lugar de Devolver

#### Problema

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def __str__(self):
        print(f"{self.name} majors in {self.major}")
```

Cuando haces `print(student1)`, se imprime `None`.

#### Solución

```python
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def __str__(self):
        return f"{self.name} majors in {self.major}"
```
