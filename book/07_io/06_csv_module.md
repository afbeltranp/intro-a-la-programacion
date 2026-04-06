# Módulo CSV

## Información sobre el Módulo CSV

### Objetivos de Aprendizaje

- ✅ Comprender el propósito del módulo `csv` en Python.
- ✅ Aprender cómo **leer desde** y **escribir en** archivos CSV.
- ✅ Usar funciones básicas como `csv.reader()` y `csv.writer()` para manejar datos CSV.

---

## Leyendo un Archivo CSV

Para leer un archivo CSV, usa `csv.reader()`. Esta función trata cada fila como una lista de valores.

```python
import csv

with open("datos.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)  # Cada fila es una lista de valores
```

Para leer fuera de un bucle for puedes leer la siguiente línea con la función `next` de Python:

```python
import csv

with open("datos.csv", "r") as archivo:
    lector = csv.reader(archivo)
    primera_fila = next(lector)
```

**Puntos Clave:**

- Abre el archivo en **modo lectura (`"r"`)**.
- Usa `csv.reader()` para analizar el archivo.
- Itera a través del lector para acceder a cada fila como una lista, o usa `next()` para obtener la siguiente fila.

---

## Escribiendo en un Archivo CSV

Para escribir datos en un archivo CSV, usa `csv.writer()`.

```python
import csv

datos = [["Nombre", "Edad", "Ciudad"], ["Alicia", 25, "Ciudad de México"], ["Roberto", 30, "Bogotá"]]

with open("salida.csv", "w") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)  # Escribe múltiples filas
```

---

## Pregunta

En **`csv_module.py`**, escribe un script de Python que tome entrada del usuario y la escriba en un **archivo CSV** en formato apropiado separado por comas.

### Paso 1: Recopilar Información Básica

Solicita al usuario las siguientes entradas **en orden**:

1. El **número de columnas**.

```python
"Enter the number of columns:\n"
```

2. El **nombre del archivo de salida** (por ejemplo, `vuelos.csv`).

```python
"Enter the output file name:\n"
```

### Paso 2: Recopilar Contenido CSV

Luego, toma la **entrada de datos** un valor a la vez.

```python
"Enter data:\n"
```

- Continúa aceptando valores de entrada hasta que el usuario ingrese:

  ```plaintext
  DONE
  ```

  Esto indica el final de la entrada.

- Estás creando una versión simplificada ("delgada") de un archivo CSV — esto significa que recopilarás todos los valores de entrada uno por uno en una sola secuencia, luego los agruparás en filas según el número de columnas especificado.

### Ejemplo de Entrada

```plaintext
Flight Number
Airline
Capacity
Occupancy
0
Spirit
100
93
1
Jet Blue
250
107
2
Jet Blue
500
439
DONE
```

### Salida Esperada (Formato CSV)

```plaintext
Flight Number,Airline,Capacity,Occupancy
0,Spirit,100,93
1,Jet Blue,250,107
2,Jet Blue,500,439
```

### Consejos

- Usa el módulo **`csv`** incorporado de Python para simplificar la escritura del archivo.
- Almacena todas las entradas recopiladas en una **lista (o lista de listas)** antes de escribirlas en el archivo CSV.
- Recuerda abrir el archivo en **modo escritura (`'w'`)** al guardar tus datos.


