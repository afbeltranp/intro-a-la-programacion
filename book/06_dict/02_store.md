# Almacenar e Imprimir con Diccionarios

## **Objetivos de Aprendizaje:**  
- ✅ Aprender a crear y almacenar pares clave-valor en un diccionario.  
- ✅ Comprender las distintas formas de acceder e imprimir datos de un diccionario.  
- ✅ Explorar opciones de formato para mostrar el contenido de un diccionario de manera efectiva.  

### **Crear un Diccionario**  
Como vimos, un diccionario se define usando llaves `{}` con pares clave-valor separados por dos puntos `:`.  

```python
# Crear un diccionario
student_info = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}
```

Las claves deben ser **únicas e inmutables** (p. ej., cadenas de texto, números o tuplas), mientras que los valores pueden ser de cualquier tipo de dato.

---

### **Acceder a Valores en un Diccionario**  
Para obtener valores, usa la clave entre corchetes `[]` o el método `get()`.  

```python
# Acceder a valores del diccionario
print(student_info["name"])  # Salida: Alice
print(student_info.get("age"))  # Salida: 22
```

Usar `get()` evita errores si una clave no existe, devolviendo `None` en lugar de lanzar una excepción.

---

### **Imprimir un Diccionario**  
Python ofrece múltiples formas de imprimir un diccionario para mejorar su legibilidad.  

```python
# Impresión básica
print(student_info)

# Imprimir pares clave-valor con un bucle
for key, value in student_info.items():
    print(f"{key}: {value}")
```

---

### **Modificar y Agregar Entradas**  
Los diccionarios son mutables, lo que permite agregar, actualizar o eliminar pares clave-valor.  

```python
# Agregar un nuevo par clave-valor
student_info["promedio"] = 3.8

# Actualizar un valor existente
student_info["major"] = "Data Science"

# Eliminar una clave
del student_info["age"]

print(student_info)
```

---

### **Resumen**  
- Los diccionarios almacenan pares clave-valor y permiten una recuperación de datos rápida.  
- **Usa `get()` para acceder a valores de forma segura.**  
- Imprime diccionarios usando bucles, cadenas formateadas o impresión en formato JSON.  
- Modifica diccionarios dinámicamente agregando, actualizando y eliminando pares clave-valor.  

Los diccionarios ofrecen una forma **poderosa y flexible** de almacenar y mostrar datos estructurados de manera eficiente.
