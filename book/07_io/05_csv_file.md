# Archivo CSV

## ¿Qué es un Archivo CSV?

### Objetivos de Aprendizaje

- ✅ Comprender qué es un archivo CSV y para qué se usa.
- ✅ Reconocer la estructura y reglas de formato de los CSV.
- ✅ Conocer aplicaciones comunes de los CSV en manejo de datos e ingeniería.

---

## CSV: Valores Separados por Comas

Un **archivo CSV** es un archivo de texto plano que almacena **datos tabulares** - datos organizados en filas y columnas - usando **comas** para separar valores.

Es uno de los formatos más comunes usados para intercambiar datos entre diferentes sistemas de software porque es:

- **Simple**
- **Legible por humanos**
- **Compatible** con muchas herramientas (Excel, bases de datos, scripts, etc.)

---

## Estructura de un Archivo CSV

- Cada **línea** en un archivo CSV es una **fila** en la tabla.
- Cada **valor** está separado por una **coma (`,`)**.
- La **primera fila** usualmente contiene **encabezados de columna** (títulos de cada columna).

```
Fecha,Producto,Ventas
2024-01-01,Manzanas,100
2024-01-01,Naranjas,80
2024-01-02,Manzanas,120
```

🔎 En este ejemplo:

- Hay 3 columnas: Fecha, Producto y Ventas.
- Cada fila es una entrada o un registro.

---

## ¿Por Qué Usar Archivos CSV?

- **Ligeros**: A diferencia de archivos Excel, los CSV son solo texto y fáciles de abrir en cualquier lugar.
- **Versátiles**: Fácilmente importados/exportados desde hojas de cálculo, bases de datos, scripts, etc.
- **Eficientes**: Ideales para registros, respaldos e intercambio de datos en flujos de trabajo de ingeniería.

---

## Limitaciones de CSV

- Sin formato (fuentes, colores, fórmulas).
- Puede ser ambiguo si los datos incluyen comas (que deben ir entre comillas).
- No es adecuado para datos muy complejos o jerárquicos.

---

## Dónde Encontrarás CSV

- Registros exportados de sensores o experimentos.
- Tablas de configuración o búsqueda.
- Datos compartidos entre equipos de investigación.
- Entrada de preprocesamiento para simulaciones o herramientas de análisis.

En resumen, los archivos CSV son el **lenguaje universal de los datos tabulares** — simples, directos y están en todas partes.

---

## Pregunta

Tu tarea es crear y llenar un archivo llamado **`data.csv`** dentro de la carpeta **`csv_file_q`**.

El archivo debe estar formateado como un archivo **CSV (Valores Separados por Comas)**, conteniendo los siguientes datos:

| ID | Username | Password    | Failed_Login_Attempts |
| -- | -------- | ----------- | --------------------- |
| 0  | Adam     | adamrocks   | 2                     |
| 1  | Bob      | mrRoss21    | 0                     |
| 2  | Cody     | &*!@#$^     | 27                    |
| 3  | Dave     | cat_lady!@# | 1                     |

---

### Instrucciones

- **No** estás escribiendo código Python para esta pregunta.
- Simplemente crea el archivo CSV e ingresa los datos anteriores **en formato CSV apropiado** (valores separados por comas).
- El archivo final debe llamarse **`data.csv`** y guardarse en la carpeta **`csv_file_q`**.

