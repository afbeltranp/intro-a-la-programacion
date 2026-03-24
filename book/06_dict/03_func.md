# Funciones de Diccionarios

## **Objetivos de Aprendizaje:**
- Aprender sobre las funciones integradas de los diccionarios en Python.
- Comprender cómo obtener claves, valores y elementos.
- Explorar métodos para actualizar, eliminar y verificar el contenido de un diccionario.


### **Funciones Comunes de los Diccionarios**

#### **1. Obtener Claves, Valores y Elementos**
Python ofrece funciones integradas para extraer distintas partes de un diccionario.

```python
student_info = {"name": "Alice", "age": 22, "major": "Computer Science"}

# Obtener todas las claves
print(student_info.keys())  
# Salida: dict_keys(['name', 'age', 'major'])

# Obtener todos los valores
print(student_info.values())  
# Salida: dict_values(['Alice', 22, 'Computer Science'])

# Obtener todos los pares clave-valor
print(student_info.items())  
# Salida: dict_items([('name', 'Alice'), ('age', 22), ('major', 'Computer Science')])
```

---

#### **2. Verificar si una Clave Existe**
Usa la palabra clave `in` para comprobar si una clave existe en un diccionario.

```python
if "age" in student_info:
    print("La edad está disponible en el diccionario.")
```

---

#### **3. Agregar y Actualizar Datos**
El método `update()` permite agregar múltiples pares clave-valor o actualizar valores existentes.

```python
student_info.update({"promedio": 3.8, "age": 23})
print(student_info)
# Salida: {'name': 'Alice', 'age': 23, 'major': 'Computer Science', 'promedio': 3.8}
```

---

#### **4. Eliminar Elementos**
Los diccionarios admiten múltiples formas de eliminar elementos.

```python
# Eliminar y retornar un valor
removed_value = student_info.pop("promedio")
print(removed_value)  # Salida: 3.8

# Eliminar el último elemento insertado (Python 3.7+)
student_info.popitem()

# Vaciar completamente el diccionario
student_info.clear()
print(student_info)  # Salida: {}
```

---

#### **5. Obtener un Valor por Defecto**  
La función `get()` evita errores al retornar un valor por defecto si la clave no existe.

```python
print(student_info.get("promedio", "No disponible"))  # Salida: No disponible
```

---

### **Resumen**
- `.keys()`, `.values()` y `.items()` extraen componentes del diccionario.
- `in` verifica si una clave existe.
- `.update()` agrega o modifica pares clave-valor.
- `.pop()`, `.popitem()` y `.clear()` eliminan elementos.
- `.get()` obtiene valores de forma segura sin causar errores.
