# Validación de entrada (menú)

## Objetivos de aprendizaje
- ✅ Comprender cómo usar `==` y `elif` para comparación básica de entrada.
- ✅ Aprender a hacer verificaciones de entrada sin distinguir mayúsculas y minúsculas con el método `.lower()`.

---

## ¿Qué es la validación de entrada?

La validación de entrada es el proceso de asegurar que la entrada del usuario sea apropiada antes de que sea procesada por el programa. Esto incluye verificar que la entrada sea del tipo, formato y valor correctos.

---

## Sintaxis básica
```python
opcion = input("Elige una opción (A, B, C): ").lower()  # Convertir a minúsculas para estandarizar la entrada

if opcion == 'a':
    print("Opción A seleccionada")
elif opcion == 'b':
    print("Opción B seleccionada")
elif opcion == 'c':
    print("Opción C seleccionada")
else:
    print("¡Opción inválida!")
```

Usar `==` y `elif` combinados con `.lower()` proporciona una forma simple y efectiva de manejar la validación de entrada en menús, haciendo tus programas más amigables para el usuario y menos propensos a errores. Agregar bloques `try` y `except` mejora aún más esto al capturar y manejar posibles errores relacionados con la entrada. Este enfoque es especialmente útil en aplicaciones interactivas de Python donde la entrada del usuario controla el comportamiento del programa.

---

## Pregunta

Escribe tu programa en `validation.py`.

En este programa, crearás un script de Python que muestra continuamente el mensaje:
```plaintext
Just keep swimming
```

para proporcionar motivación. Después de cada mensaje, solicita al usuario con:
```plaintext
Do you feel better now? (yes/no): 
```

### Requisitos

1. El programa debe continuar en bucle hasta que el usuario ingrese **"yes"** (en cualquier combinación de mayúsculas/minúsculas, como `"Yes"`, `"YES"`, `"yeS"`, etc.).

   * Cuando el usuario responda con `"yes"`, mostrar:
```plaintext
     Thank you for participating! Remember, come back anytime you need some encouragement.
```

     y luego terminar el programa.

2. Si el usuario ingresa `"no"` (en cualquier combinación de mayúsculas/minúsculas), el programa debe **seguir en bucle** (imprimir el mensaje de nuevo y volver a hacer la pregunta).

3. Si el usuario ingresa **cualquier cosa que no sea `"yes"` o `"no"`**, el programa debe mostrar:
```plaintext
   Invalid option. Please answer yes or no.
```

   y luego continuar el bucle.

**Pista:** Usa el método `.lower()` para hacer la verificación de entrada sin distinguir mayúsculas y minúsculas.