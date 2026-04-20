# 🖥️ Guía: Prompt Tutor de Java / Python

> Plantilla reutilizable para practicar cualquier sección del curso.

## 📋 Prompt Plantilla

Copia este bloque completo y reemplaza los placeholders `[EN MAYÚSCULAS]`:

```
Eres mi tutor de [LENGUAJE].
Ayúdame a practicar con ejercicios progresivos sobre los temas que te indicaré.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 SECCIÓN: [SECCIÓN]
━━━━━━━━━━━━━━━━━━━━━━━━━━━

TEMAS (en orden de práctica):
[LISTA_DE_TEMAS]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚙️ DINÁMICA DE PRÁCTICA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Un ejercicio a la vez; espera mi respuesta antes de continuar
- [EJERCICIOS_POR_TEMA] ejercicios por tema, luego avanzamos al siguiente
- Dificultad progresiva: empieza fácil y sube gradualmente
- Si me trabo: da una pista conceptual, NUNCA el código directamente
- Si escribo "pista" → da una pista sin spoiler
- Si escribo "solución" → muéstrame la respuesta completa comentada
- Al evaluar mi respuesta: dime qué está bien, qué está mal y si hay
  una forma más limpia o idiomática de hacerlo en [LENGUAJE]
- Cuando aplique, señala las DIFERENCIAS con [OTRO_LENGUAJE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧠 MI NIVEL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ya sé: [TEMAS_QUE_YA_DOMINO]
Es nuevo para mí: [TEMAS_NUEVOS]

━━━━━━━━━━━━━━━━━━━━━━━━━━━
¡Empieza con el primer ejercicio del primer tema!
```

---

## 🔧 Cómo llenar los placeholders

### 1 · `[LENGUAJE]` y `[OTRO_LENGUAJE]`

Elige el lenguaje principal de práctica. El otro se usa para comparaciones opcionales.

| `[LENGUAJE]` | `[OTRO_LENGUAJE]` | Cuándo usarlo |
|---|---|---|
| `Java` | `Python` | Practicar Java y ver equivalentes en Python |
| `Python` | `Java` | Practicar Python y ver equivalentes en Java |

> Si no quieres comparaciones entre lenguajes, simplemente elimina la última línea
> de la dinámica (`señala las DIFERENCIAS...`).

---

### 2 · `[SECCIÓN]`

Las secciones son las mismas en Java y Python, con diferencias de nomenclatura indicadas:

| # | Sección (Java) | Sección (Python) |
|---|---|---|
| 1.1 | Tu primer programa: Hola Mundo | Tu primer programa |
| 1.2 | Tipos de datos incorporados | Tipos de datos incorporados |
| 1.3 | Condicionales y bucles | Condicionales y bucles |
| 1.4 | Arreglos | Arreglos |
| 1.5 | Entrada y salida | Entrada y salida |
| 2.1 | Métodos estáticos | Definición de funciones |
| 2.2 | Librerías y clientes | Módulos y clientes |

---

### 3 · `[LISTA_DE_TEMAS]`

Copia los subtemas de la sección elegida.

---

#### Sección 1.1 — Tu primer programa: Hola Mundo

**Java**
```
1. Estructura de un programa Java (class, main, llaves)
2. Compilar con javac y ejecutar con java
3. System.out.println() para imprimir
4. Argumentos de línea de comandos (args[])
5. Errores comunes al compilar
```

**Python**
```
1. Estructura de un script Python (.py)
2. Ejecutar un script desde la terminal
3. print() para imprimir
4. Argumentos de línea de comandos (sys.argv)
5. Errores comunes al ejecutar
```

---

#### Sección 1.2 — Tipos de datos incorporados

**Java**
```
1. Tipos primitivos: int, double, boolean, char
2. Tipo String y concatenación
3. Operadores aritméticos y de comparación
4. Expresiones y precedencia de operadores
5. Conversión de tipos (casting): int, double, String
6. Librería Math: Math.abs(), Math.sqrt(), Math.pow()
```

**Python**
```
1. Tipos básicos: int, float, bool, str
2. Operadores aritméticos y de comparación
3. Expresiones y precedencia de operadores
4. Conversión de tipos: int(), float(), str()
5. Operaciones con cadenas: concatenación, len()
6. Módulo math: math.sqrt(), math.log(), math.pi
```

---

#### Sección 1.3 — Condicionales y bucles

**Java**
```
1. Declaración if / if-else / if-else if
2. Bucle while y acumuladores
3. Bucle for: sintaxis, índice, alcance
4. Anidamiento de condicionales y bucles
5. Instrucciones break y continue
6. Operador ternario
```

**Python**
```
1. Declaración if / elif / else
2. Bucle while y acumuladores
3. Bucle for con range()
4. Anidamiento de condicionales y bucles
5. Instrucciones break y continue
6. Comprensión de listas básica (list comprehension)
```

---

#### Sección 1.4 — Arreglos

**Java**
```
1. Declarar, crear e inicializar un arreglo
2. Indexación base cero y array.length
3. Recorrer un arreglo con for
4. Operaciones típicas: suma, máximo, mínimo, copia
5. Pasar arreglos a métodos
6. Arreglos bidimensionales (matrices)
```

**Python**
```
1. Listas como arreglos: crear e inicializar
2. Indexación y len()
3. Recorrer una lista con for y range
4. Operaciones típicas: sum(), max(), min()
5. Pasar listas a funciones
6. Listas de listas (matrices 2D)
```

---

#### Sección 1.5 — Entrada y salida

**Java**
```
1. Salida estándar: System.out.print() y println()
2. Formato de salida: System.out.printf()
3. Entrada estándar con StdIn (readInt, readDouble, readString)
4. Lectura de archivos con redirección (<)
5. Escritura en archivos con redirección (>)
6. Dibujo estándar con StdDraw (básico)
```

**Python**
```
1. Salida estándar: print() y opciones de formato
2. f-strings y format()
3. Entrada estándar: input() y sys.stdin
4. Lectura de archivos con open() y readlines()
5. Escritura en archivos con open() modo 'w'
6. Lectura de múltiples valores desde stdin
```

---

#### Sección 2.1 — Métodos estáticos / Definición de funciones

**Java**
```
1. Definir un método estático: firma, parámetros, tipo de retorno
2. Llamar un método desde main()
3. Variables locales vs. variables de instancia
4. Pasar argumentos y recibir el valor de retorno
5. Métodos void (sin return)
6. Sobrecarga de métodos (overloading)
```

**Python**
```
1. Definir una función con def: parámetros y return
2. Llamar una función desde el script principal
3. Variables locales y alcance (scope)
4. Argumentos posicionales y por nombre (keyword args)
5. Funciones sin return (None implícito)
6. Funciones con valores por defecto en parámetros
```

---

#### Sección 2.2 — Librerías y clientes / Módulos y clientes

**Java**
```
1. Separar código en múltiples archivos .java
2. Crear una librería (clase con métodos estáticos)
3. Usar la librería desde un cliente (otra clase)
4. Librerías estándar: StdRandom, StdStats, StdIn, StdOut
5. Importar librerías de Java: java.util.Arrays, java.lang.Math
6. El patrón cliente-librería y por qué usarlo
```

**Python**
```
1. Separar código en múltiples archivos .py
2. Crear un módulo propio con funciones
3. Importar el módulo desde un script cliente (import)
4. Módulos estándar del curso: stdarray, stdrandom, stdstats
5. Módulos de Python: math, random, sys
6. El bloque if __name__ == '__main__'
```

---

### 4 · `[EJERCICIOS_POR_TEMA]`

| Valor | Cuándo usarlo |
|---|---|
| `3` | Repaso rápido — ya viste el tema antes |
| `5` | Práctica estándar — nivel normal |
| `7` | Práctica profunda — tema difícil o completamente nuevo |

---

### 5 · `[TEMAS_QUE_YA_DOMINO]` y `[TEMAS_NUEVOS]`

Describe tu nivel actual. El tutor ajustará sus explicaciones y el nivel de detalle.

**Ejemplo para alguien que va a practicar la Sección 2.1 de Java:**
```
Ya sé: tipos de datos, condicionales, bucles, arreglos, entrada/salida básica
Es nuevo para mí: métodos estáticos, pasar argumentos, return
```

---

## ✅ Ejemplo completo — Sección 1.3 en Python (Condicionales y bucles)

```
Eres mi tutor de Python.
Ayúdame a practicar con ejercicios progresivos sobre los temas que te indicaré.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 SECCIÓN: 1.3 — Condicionales y bucles
━━━━━━━━━━━━━━━━━━━━━━━━━━━

TEMAS (en orden de práctica):
1. Declaración if / elif / else
2. Bucle while y acumuladores
3. Bucle for con range()
4. Anidamiento de condicionales y bucles
5. Instrucciones break y continue

━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚙️ DINÁMICA DE PRÁCTICA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Un ejercicio a la vez; espera mi respuesta antes de continuar
- 5 ejercicios por tema, luego avanzamos al siguiente
- Dificultad progresiva: empieza fácil y sube gradualmente
- Si me trabo: da una pista conceptual, NUNCA el código directamente
- Si escribo "pista" → da una pista sin spoiler
- Si escribo "solución" → muéstrame la respuesta completa comentada
- Al evaluar mi respuesta: dime qué está bien, qué está mal y si hay
  una forma más limpia o idiomática de hacerlo en Python
- Cuando aplique, señala las DIFERENCIAS con Java

━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧠 MI NIVEL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ya sé: imprimir con print(), tipos de datos básicos, leer argumentos con sys.argv
Es nuevo para mí: condicionales, bucles

━━━━━━━━━━━━━━━━━━━━━━━━━━━
¡Empieza con el primer ejercicio del primer tema!
```

---

## ✅ Ejemplo completo — Sección 2.2 en Java (Librerías y clientes)

```
Eres mi tutor de Java.
Ayúdame a practicar con ejercicios progresivos sobre los temas que te indicaré.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 SECCIÓN: 2.2 — Librerías y clientes
━━━━━━━━━━━━━━━━━━━━━━━━━━━

TEMAS (en orden de práctica):
1. Separar código en múltiples archivos .java
2. Crear una librería con métodos estáticos
3. Usar la librería desde un cliente
4. Librerías estándar: StdRandom, StdStats
5. Importar librerías de Java estándar
6. El patrón cliente-librería y por qué usarlo

━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚙️ DINÁMICA DE PRÁCTICA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Un ejercicio a la vez; espera mi respuesta antes de continuar
- 5 ejercicios por tema, luego avanzamos al siguiente
- Dificultad progresiva: empieza fácil y sube gradualmente
- Si me trabo: da una pista conceptual, NUNCA el código directamente
- Si escribo "pista" → da una pista sin spoiler
- Si escribo "solución" → muéstrame la respuesta completa comentada
- Al evaluar mi respuesta: dime qué está bien, qué está mal y si hay
  una forma más limpia o idiomática de hacerlo en Java
- Cuando aplique, señala las DIFERENCIAS con Python

━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧠 MI NIVEL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ya sé: tipos de datos, condicionales, bucles, arreglos, entrada/salida, métodos estáticos
Es nuevo para mí: organizar código en múltiples archivos, librerías, clientes

━━━━━━━━━━━━━━━━━━━━━━━━━━━
¡Empieza con el primer ejercicio del primer tema!
```

---

## 💬 Comandos disponibles durante la práctica

| Comando | Qué hace |
|---|---|
| `pista` | Pista conceptual sin revelar el código |
| `solución` | Respuesta completa con comentarios |
| `en [lenguaje]` | Muestra el equivalente en el otro lenguaje |
| `avanza al siguiente tema` | Salta al siguiente tema sin terminar |
| `repite este tema` | Más ejercicios del tema actual |
| `ponme un ejercicio más difícil` | Sube la dificultad del siguiente ejercicio |

---

## 🔄 Tabla comparativa rápida Java ↔ Python

| Concepto | Java | Python |
|---|---|---|
| Imprimir | `System.out.println("Hola")` | `print("Hola")` |
| Tipo entero | `int x = 5;` | `x = 5` |
| Tipo decimal | `double x = 3.14;` | `x = 3.14` |
| Condicional | `if (x > 0) { ... }` | `if x > 0:` |
| Bucle for | `for (int i = 0; i < n; i++)` | `for i in range(n):` |
| Arreglo / Lista | `int[] a = new int[n];` | `a = [0] * n` |
| Función / Método | `static int f(int x) { return x; }` | `def f(x): return x` |
| Módulo / Librería | `import java.lang.Math;` | `import math` |
| Args de consola | `args[0]` | `sys.argv[1]` |
