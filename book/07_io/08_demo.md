# Demo General

## Recuperación de Datos de Experimentos de Laboratorio

### Descripción General

Los ingenieros químicos frecuentemente revisan datos de experimentos pasados para analizar tendencias y asegurar consistencia en el trabajo de laboratorio. Este programa recupera y analiza experimentos registrados desde un archivo CSV.

**Nota:** esta demo solo evalúa tu conocimiento de archivos CSV... ¡Puedes asumir entrada correcta!

---

## Tarea

Desarrolla un programa en Python, `overall.py`, que:

- Lea y muestre datos estructurados de experimentos desde un archivo CSV.
- Identifique la temperatura promedio entre todos los experimentos.

---

## Ejemplo de Archivo / Entrada / Salida

### Estructura CSV de Ejemplo

```text
Experiment Name, Reaction Type, Temperature (Celsius), Observations
Electrolysis of Water, Redox, 25, Gas bubbles formed
Combustion of Methane, Exothermic, 800, Blue flame observed
Decomposition of H2O2, Catalytic, 30, Bubbles formed rapidly
Oxidation of Iron, Redox, 200, Rust formation
```

### Ejemplo de Entrada / Salida

```plaintext
Welcome, enter the file you would like to open:
path/to/my/csv.csv

Select one of the following:
1. Print all
2. Print avg temperature
3. Exit
Enter number here:
1

All Experiments:
1: [Electrolysis of Water, Redox, 25, Gas bubbles formed]
2: [Combustion of Methane, Exothermic, 800, Blue flame observed]
3: [Decomposition of H2O2, Catalytic, 30, Bubbles formed rapidly]
4: [Oxidation of Iron, Redox, 200, Rust formation]

Select one of the following:
1. Print all
2. Print avg temperature
3. Exit
Enter number here:
2

Average temperature (Celsius): 263.75

Select one of the following:
1. Print all
2. Print avg temperature
3. Exit
Enter number here:
3

Goodbye!
```
