# 🐍 Guía: Prompt Tutor de Python

> Plantilla reutilizable para practicar cualquier módulo del curso
> **Introducción a la Programación** — Andrés Beltrán-Pulido
> 🔗 https://afbeltranp.github.io/intro-a-la-programacion/main/intro.html

---

## 📋 Prompt Plantilla

Copia este bloque completo y reemplaza los placeholders `[EN MAYÚSCULAS]`:

```
Eres mi tutor de Python del curso "Introducción a la Programación".
Ayúdame a practicar con ejercicios progresivos sobre los temas que te indicaré.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 MÓDULO: [MÓDULO]
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
  una forma más elegante o pythónica de hacerlo

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

### 1 · `[MÓDULO]`

Escribe el nombre del módulo que quieres practicar:

| # | Módulo |
|---|--------|
| 1 | Fundamentos de Python |
| 2 | Condicionales, Bucles y Listas |
| 3 | Tuplas, Strings, Conjuntos y más |
| 4 | Funciones y Módulos |
| 5 | Diccionarios |
| 6 | E/S de Archivos |
| 7 | Manejo de Errores y CLI |

---

### 2 · `[LISTA_DE_TEMAS]`

Copia los temas del módulo elegido. Puedes usar todos o solo los que necesites.

#### Módulo 1 — Fundamentos de Python
```
1. Python interactivo y operaciones aritméticas
2. Variables y tipos de datos
3. Archivos y scripts de Python
4. Función print y formato de salida
5. Input y lectura de datos del usuario
6. Conversión de tipos (typecasting)
```

#### Módulo 2 — Condicionales, Bucles y Listas
```
1. Declaraciones condicionales (if/elif/else)
2. Operadores lógicos (and, or, not)
3. Bucles while
4. Listas y range
5. Bucles for
6. min() y max()
7. Listas anidadas
```

#### Módulo 3 — Tuplas, Strings, Conjuntos y más
```
1. Tuplas: creación y uso
2. Strings: métodos y operaciones
3. Conjuntos (sets)
4. Validación de entrada (menú interactivo)
5. Comprensión de listas
6. Enumerate
```

#### Módulo 4 — Funciones y Módulos
```
1. Funciones: definir, llamar, pasar argumentos
2. Tipos de retorno: return, múltiples valores, distintos tipos
3. Tipos de funciones: las que imprimen, modifican o retornan valores
4. Alcance: variables locales y globales
5. Módulos: qué son y cómo usarlos
6. Múltiples archivos de Python
7. Módulo random
```

#### Módulo 5 — Diccionarios
```
1. Concepto de diccionarios: claves y valores
2. Almacenar e imprimir datos con diccionarios
3. Funciones de diccionarios: keys(), values(), items(), get(), update()
```

#### Módulo 6 — E/S de Archivos
```
1. Rutas de archivos (relativas y absolutas)
2. Apertura y cierre de archivos (open/close/with)
3. Lectura de archivos
4. Escritura de archivos
5. Archivos CSV: lectura y escritura manual
6. Módulo csv de Python
```

#### Módulo 7 — Manejo de Errores y CLI
```
1. Try/Except: estructura básica
2. ValueError
3. EOFError
4. FileNotFoundError
5. IndexError
6. Lanzar errores con raise
7. Ejecutar scripts desde la línea de comandos
8. Entrada por argumentos (sys.argv)
```

---

### 3 · `[EJERCICIOS_POR_TEMA]`

Elige según cuánto quieres profundizar en cada tema:

| Valor | Cuándo usarlo |
|-------|---------------|
| `3` | Repaso rápido — ya viste el tema antes |
| `5` | Práctica estándar — nivel normal |
| `7` | Práctica profunda — tema difícil o completamente nuevo |

---

### 4 · `[TEMAS_QUE_YA_DOMINO]` y `[TEMAS_NUEVOS]`

Describe tu nivel actual con honestidad. El tutor ajustará el lenguaje y las
explicaciones según lo que declares aquí.

**Ejemplo para alguien que va a practicar el Módulo 6:**
```
Ya sé: variables, condicionales, bucles, listas, funciones, diccionarios
Es nuevo para mí: leer y escribir archivos, trabajar con CSV
```

---

## ✅ Ejemplo completo — Módulo 5: Diccionarios

```
Eres mi tutor de Python del curso "Introducción a la Programación".
Ayúdame a practicar con ejercicios progresivos sobre los temas que te indicaré.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 MÓDULO: Diccionarios
━━━━━━━━━━━━━━━━━━━━━━━━━━━

TEMAS (en orden de práctica):
1. Concepto de diccionarios: claves y valores
2. Almacenar e imprimir datos con diccionarios
3. Funciones de diccionarios: keys(), values(), items(), get(), update()

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
  una forma más elegante o pythónica de hacerlo

━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧠 MI NIVEL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ya sé: variables, condicionales, bucles, listas, funciones básicas
Es nuevo para mí: diccionarios

━━━━━━━━━━━━━━━━━━━━━━━━━━━
¡Empieza con el primer ejercicio del primer tema!
```

---

## 💬 Comandos disponibles durante la práctica

Puedes escribir estos mensajes en cualquier momento:

| Comando | Qué hace |
|---------|----------|
| `pista` | El tutor te da una pista conceptual sin revelar el código |
| `solución` | El tutor muestra la respuesta completa con comentarios |
| `avanza al siguiente tema` | Salta al siguiente tema sin terminar los ejercicios |
| `repite este tema` | Pide más ejercicios del tema actual |
| `ponme un ejercicio más difícil` | Sube la dificultad del siguiente ejercicio |
