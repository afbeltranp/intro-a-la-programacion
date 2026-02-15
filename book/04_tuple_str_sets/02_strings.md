# Strings

## Objetivos de aprendizaje
- ✅ Comprender qué son los **strings** y sus características.
- ✅ Aprender cómo **crear**, **manipular** y **usar** strings de manera efectiva.
- ✅ Demostrar operaciones comunes con **strings** mediante ejemplos.

---

## ¿Qué son los strings en Python?
Los strings son secuencias de caracteres utilizadas para representar texto. Son uno de los tipos de datos más utilizados en Python y se definen usando comillas simples (`'`) o comillas dobles (`"`).

---

## Características de los strings
- **Ordenados**: Los strings son secuencias, por lo que sus caracteres tienen un orden definido.
- **Inmutables**: Una vez que se crea un string, no puede modificarse. Cualquier modificación crea un nuevo string.
- **Versátiles**: Los strings soportan muchos métodos integrados para manipulación de texto.

---

## ¿Por qué usar strings?
- **Representación de texto**: Los strings son la forma principal de manejar texto en Python.
- **Flexibilidad**: Python proporciona amplia funcionalidad para manipulación de strings, incluyendo formato, slicing y búsqueda.
- **Interoperabilidad**: Los strings pueden combinarse fácilmente con otros tipos de datos usando conversión de tipos.

---

## Cómo crear strings
Los strings pueden crearse usando comillas simples, dobles o triples.
```python
# Creando strings
comilla_simple = 'Hola'
comilla_doble = "Mundo"
comilla_triple = """Este es un 
string de múltiples líneas."""
```

### Caracteres de escape
Los caracteres especiales pueden incluirse en strings usando barras invertidas (`\`).
```python
escapado = "Él dijo, \"¡Python es increíble!\""
nueva_linea = "Primera línea\nSegunda línea"
```

A continuación se muestran algunas secuencias de escape comunes:

| Secuencia de escape | Resultado |
| - | - |
| `"\t"` | Un carácter de tabulación |
| `"\n"` | Un carácter de nueva línea |
| `"\""` | El carácter de comillas dobles |
| `'\''` | El carácter de comilla simple |

---

## Acceso a elementos de un string
Los strings soportan **indexación** y **slicing**, similar a las listas y tuplas.
```python
# Accediendo a caracteres por índice
texto = "Python"
print(texto[0])  # Salida: P

# Slicing de strings
print(texto[1:4])  # Salida: yth

# Accediendo a caracteres desde el final
print(texto[-1])  # Salida: n
```

---

## Operaciones comunes con strings
Python proporciona muchos métodos integrados y operadores para trabajar con strings.

### Concatenación y repetición
Los strings pueden combinarse o repetirse usando **`+`** y **`*`**.
```python
saludo = "Hola"
nombre = "Alicia"
print(saludo + " " + nombre)  # Salida: Hola Alicia
print(saludo * 3)  # Salida: HolaHolaHola
```

### Verificación de pertenencia
Verifica si una subcadena existe en un string usando **`in`**.
```python
oracion = "El rápido zorro marrón"
print("zorro" in oracion)  # Salida: True
```

### Métodos de strings
Los strings tienen una variedad de métodos para manipulación.
```python
texto = "Programación Python"

# Cambiando mayúsculas/minúsculas
print(texto.lower())  # Salida: programación python
print(texto.upper())  # Salida: PROGRAMACIÓN PYTHON

# Eliminando espacios en blanco
texto_con_espacios = "   Python   "
print(texto_con_espacios.strip())  # Salida: Python

texto_raro = "pYtHoN pRoGrAmAcIóN"
print(texto_raro.title())  # Salida: Python Programación

# Buscando y reemplazando
print(texto.find("Python"))  # Salida: 13
print(texto.replace("Programación", "es divertido"))  # Salida: es divertido Python
```

---

## Casos de uso para strings

### Manipulación de texto
- Almacenar y procesar entrada del usuario.
- Formatear salida en reportes o registros.

### Manejo de archivos
- Leer y escribir en archivos de texto.

### Análisis de datos
- Dividir y unir strings para transformación de datos.

---

## Puntos clave
- Los **strings** son secuencias inmutables utilizadas para representar texto.
- Python proporciona un rico conjunto de operaciones para manipulación de strings, como **concatenación**, **slicing**, **verificación de pertenencia** y una variedad de **métodos**.
- Los strings son versátiles, soportando tanto **operaciones de texto simples** como **manipulaciones complejas** como búsqueda, reemplazo y formato.

**¡Inténtalo tú mismo!** Experimenta con operaciones de strings e intenta manipular diferentes tipos de datos de texto usando los métodos de strings de Python.

---

## Pregunta

Se te proporciona un archivo **`strings.py`**. Tu tarea es tomar **tres strings** como entrada, formatearlos con el uso correcto de mayúsculas/minúsculas y luego combinarlos en un solo string.

---

### Pasos

1. **Solicita al usuario tres entradas:**

   * **Título del libro** → debe estar en **Title Case** (Capitalización de Título)
     * Prompt: `"Input title here:\n"`
   * **Editorial** → debe estar en **Upper Case** (Mayúsculas)
     * Prompt: `"Input publisher here:\n"`
   * **Género** → debe estar en **Lower Case** (Minúsculas)
     * Prompt: `"Input genre here:\n"`

2. **Aplica los métodos correctos de mayúsculas/minúsculas** a cada entrada:

   * `title()` para Title Case
   * `upper()` para Upper Case
   * `lower()` para Lower Case

3. **Concatena** los tres strings en una variable, con cada parte separada por un **carácter de nueva línea (`\n`)**.

4. **Imprime** el resultado final.

---

### Ejemplo de ejecución

**Entrada:**
```plaintext
harry potter and the philosopher's stone
BLOOMSBURY
Fantasy
```

**Salida:**
```plaintext
Harry Potter And The Philosopher's Stone
BLOOMSBURY
fantasy
```
