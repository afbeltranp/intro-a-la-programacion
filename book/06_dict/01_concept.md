# Concepto de Diccionarios

## **Objetivos de Aprendizaje:**  
- ✅ Comprender qué son los diccionarios en Python y cómo almacenan datos.
- ✅ Aprender el concepto de pares clave-valor y en qué se diferencian de otras estructuras de datos.
- ✅ Reconocer casos de uso comunes para los diccionarios en la programación con Python.


### **¿Qué es un Diccionario en Python?**  
Un **diccionario** es una estructura de datos integrada en Python que almacena información en **pares clave-valor**. A diferencia de las listas o las tuplas, que guardan elementos en un orden secuencial, los diccionarios permiten **asociar** claves únicas a valores específicos, lo que hace que la recuperación de datos sea más eficiente.  

---

### **Pares Clave-Valor Explicados**  
- **Clave**: Un identificador único para un valor. Las claves deben ser de tipos **inmutables**, como cadenas de texto, números o tuplas.  
- **Valor**: El dato asociado, que puede ser de cualquier tipo (números, cadenas, listas, otros diccionarios, etc.).  
- Los diccionarios son **desordenados** antes de Python 3.7, pero mantienen el orden de inserción a partir de Python 3.7.  

---

### **¿Por qué usar Diccionarios?**  
- **Búsquedas Rápidas**: Acceder a un valor mediante su clave es mucho más rápido que recorrer una lista.  
- **Representación Descriptiva de Datos**: En lugar de depender de índices numéricos (como en las listas), los diccionarios ofrecen etiquetas con significado para los datos.  
- **Almacenamiento Flexible**: Guarda distintos tipos de datos de forma eficiente y organizada.  

---

### **¿En qué se Diferencian los Diccionarios de Otras Estructuras de Datos?**  
- Las **listas** almacenan valores en una secuencia ordenada, a los que se accede por índice, mientras que los diccionarios usan claves para búsquedas directas.  
- Las **tuplas** son secuencias inmutables, mientras que los diccionarios permiten modificar sus valores.  
- Los **conjuntos** almacenan valores únicos sin claves específicas, mientras que los diccionarios asocian cada clave a un valor.  

---

### **Casos de Uso Comunes**  
- Almacenar configuraciones (p. ej., `{ "theme": "dark", "font_size": 12 }`)  
- Contar ocurrencias de elementos en un conjunto de datos (p. ej., `{ "apple": 3, "banana": 2 }`)  

# Pista de Sintaxis

Los diccionarios en Python se pueden crear, como se muestra arriba, usando el siguiente formato: `{<clave>:<valor>, ...}`.
