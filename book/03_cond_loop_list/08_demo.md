# Demostración General

## Verificador de Asientos para Examen

Para este problema, estás programando un script para que los profesores asignen asientos de examen. El objetivo es minimizar el plagio de estudiantes mirando a sus compañeros. En `overall.py`, harás un programa que hace lo siguiente:

## ¿Qué necesitas hacer?

- Crea un arreglo 2D a partir de entradas
  - Primero recibirás dos números indicando el número de filas y columnas respectivamente.
  - Luego recibirás suficientes entradas de 1's y 0's para llenar toda la matriz. Estos se darán uno por uno, por lo que tendrás que llamar `input("Enter number: ")` (fila * columna) veces.
  
  > **Pista:** Usa un bucle for para aceptar la entrada.
  
    - 0 → Vacío
    - 1 → Ocupado
- Verifica que los estudiantes estén sentados en asientos alternos.
  - Ningún estudiante puede estar sentado en el borde.
    - Se recomienda que verifiques esto primero.
  - Ningún estudiante puede estar sentado a una columna de distancia de otro o a una fila de distancia de otro.
  - Imprime uno de los siguientes:
    - `"No violations!"`
    - `"Invalid seating!"`
- Luego imprime el número de asientos vacíos. (independientemente de su validez)