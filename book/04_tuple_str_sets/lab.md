# Laboratorio 4

## Problema 1

Se te proporciona un archivo **`tuples.py`**. En este archivo, crea una variable llamada **`val`** que sea una **tupla** con **dos elementos**:

1. **Primer elemento:** la variable proporcionada `num`
2. **Segundo elemento:** el valor de `num / 2`

### Ejemplo

Si la entrada es `8`, entonces:

* `num = 8`
* `val = (8, 4.0)`

El programa imprimirá:
```plaintext
Is tuple: (8, 4.0)
```

---

## Problema 2

Se te proporciona un archivo **`strings.py`**. Tu tarea es tomar **tres strings** como entrada, formatearlos con el uso correcto de mayúsculas/minúsculas y luego combinarlos en un solo string.

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

---

## Problema 3

Crea un script de Python llamado **`sets.py`** que elimine entradas de correo electrónico duplicadas de una base de datos de inicio de sesión.

1. **Recopila 5 entradas de correo electrónico del usuario.**
   * Usa el siguiente prompt cada vez:
    ```python
        "Enter an email:\n"
    ```

2. **Almacena las entradas en un conjunto** para que cualquier dirección de correo electrónico duplicada se elimine automáticamente.

3. **Imprime el conjunto final de correos electrónicos únicos.**
   * Como los conjuntos son desordenados, asegúrate de que tu salida sea consistente imprimiendo una **versión ordenada** del conjunto:
    ```python
        print(sorted(<tu_variable_conjunto>))
    ```

### Ejemplo de ejecución
```plaintext
Enter an email:
a@unisabana.edu.co
Enter an email:
b@unisabana.edu.co
Enter an email:
a@unisabana.edu.co
Enter an email:
c@unisabana.edu.co
Enter an email:
b@unisabana.edu.co
['a@unisabana.edu.co', 'b@unisabana.edu.co', 'c@unisabana.edu.co']
```

> **Nota:** `sorted()` siempre devuelve una lista, así que el resultado final siendo una lista es el comportamiento esperado.

---

## Problema 4

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

> **Pista:** Usa el método `.lower()` para hacer la verificación de entrada sin distinguir mayúsculas y minúsculas.

---

## Problema 5

En el archivo **`comprehension.py`**, completa el código para que cree una lista llamada **`evens`** que contenga todos los números pares entre los dos valores de entrada (**start** y **end**, inclusive).

1. Las variables **`start`** y **`end`** ya están proporcionadas. Provienen de la entrada del usuario.
2. Usa una **comprensión de listas** para generar la lista de números pares desde **`start`** hasta **`end`**.
   * Pista: Usa el operador módulo (`%`) para verificar si un número es par.
3. Almacena esta lista en la variable **`evens`**.

### Ejemplos de ejecución

**Entrada:**
```plaintext
2  
10  
```

**Salida:**
```plaintext
[2, 4, 6, 8, 10]
```

**Entrada:**
```plaintext
3  
9  
```

**Salida:**
```plaintext
[4, 6, 8]
```

---

## Problema 6

En **`enumerate.py`**, recopilarás **dos conjuntos de 3 entradas de strings cada uno** (para un total de **6 entradas**). Cada conjunto de entradas formará una lista separada.

### Pasos

1. Solicita al usuario **3 veces** elementos para la **Lista 1**.
   * Cada prompt debe mostrar exactamente:
     **`"Enter item for List 1:\n"`**

2. Solicita al usuario **3 veces** elementos para la **Lista 2**.
   * Cada prompt debe mostrar exactamente:
     **`"Enter item for List 2:\n"`**

3. **Combina (zip)** las dos listas.

4. Usa **enumerate** para imprimir la salida en el formato:
```
   <indice> <elemento_lista1> <elemento_lista2>
```

### Ejemplo de ejecución

**Entrada:**
```plaintext
Temperature
Humidity
Pressure
21
65%
1013hPa
```

**Salida:**
```plaintext
0 Temperature 21
1 Humidity 65%
2 Pressure 1013hPa
```

---

## Problema 7

Juego de trivia de cultura pop para dos jugadores

Archivo: `quiz_game.py`

### Objetivo

El objetivo de este proyecto es crear un juego de trivia interactivo para dos jugadores en Python para evaluar el conocimiento de los jugadores sobre cultura pop a través de una serie de preguntas de verdadero o falso. Los jugadores se turnarán para responder todas las preguntas, y el juego rastreará y comparará sus puntuaciones para determinar su experiencia en cultura pop. Además, nos dirá cuántas preguntas respondió correctamente cada jugador, cuántas respondió correctamente cada uno de forma única, y cuántas preguntas respondieron ambos correctamente.

### Instrucciones

#### Paso 1: Inicializar el cuestionario

Define una lista de tuplas donde cada tupla contenga una pregunta relacionada con cultura pop y su respuesta correcta ("true" o "false").
```python
questions = [
    ("Taylor Swift has more than 10 Grammy Awards. True or False?", "true"),
    ("The TV show 'Stranger Things' is set in the 1990s. True or False?", "false"),
    ("Snapchat was originally called Picaboo. True or False?", "true"),
    ("The symbol for Iron in the periodic table is Fe. True or False?", "true"),
    ("Kanye West's debut album was titled 'The College Dropout.' True or False?", "true"),
    ("The capital of Australia is Sydney. True or False?", "false"),
]
```

#### Paso 2: Configurar el seguimiento de jugadores

Inicializa conjuntos para cada jugador para rastrear los índices de las preguntas que respondan correctamente.

#### Paso 3: Mensaje de bienvenida

Imprime un mensaje de bienvenida para presentar a los jugadores el juego y explicar que el Jugador 1 responderá todas las preguntas primero, seguido del Jugador 2.
```plaintext
Welcome to the Pop Culture True or False Quiz - Two Player Edition!
Player 1 will answer all questions first, followed by Player 2.
```

#### Paso 4: Realizar el cuestionario

**Turno del Jugador 1**

Itera a través de la lista de preguntas y solicita al Jugador 1 que responda cada una. Valida sus respuestas, proporciona retroalimentación inmediata y rastrea sus respuestas correctas.

Una ronda debe desarrollarse de la siguiente manera:
```plaintext
Player 1, your turn:
Question 1: <La pregunta va aquí>
Your answer (true/false):
<el jugador ingresa su respuesta aquí>
Correct!

Player 1, your turn:
Question 2: <La pregunta va aquí>
Your answer (true/false):
<el jugador ingresa su respuesta aquí>
Wrong!
...
```

**Turno del Jugador 2**

Repite el proceso para el Jugador 2 después de que el Jugador 1 haya completado su turno.

Una ronda debe desarrollarse de la siguiente manera:
```plaintext
Player 2, your turn:
Question 1: <La pregunta va aquí>
Your answer (true/false):
<el jugador ingresa su respuesta aquí>
Correct!

Player 2, your turn:
Question 2: <La pregunta va aquí>
Your answer (true/false):
<el jugador ingresa su respuesta aquí>
Wrong!
...
```

#### Paso 5: Comparar resultados

Usa operaciones de conjuntos para determinar qué preguntas respondieron correctamente ambos jugadores y cuáles fueron respondidas correctamente de forma única por cada jugador.

> **Pista:** Usa intersección y diferencia de conjuntos.

#### Paso 6: Mostrar resultados finales

Resume y muestra los resultados, indicando cuántas preguntas fueron respondidas correctamente por ambos, individualmente, y la puntuación total de cada jugador.

> **Nota:** Recuerda que al imprimir un conjunto debes usar `sorted` para que sea consistente con los casos de prueba.
```plaintext
Game Over! Let's see how both players did:
Both players got these questions right: [1, 3]
Questions only Player 1 got right: [2]
Questions only Player 2 got right: [4]
Player 1's score: 2 out of 4
Player 2's score: 2 out of 4
```

---

## Problema 8: Gurú de la lista de invitados

¡Limpia, verifica y coordina!

### 🎯 Descripción general

Estás trabajando para una empresa boutique de planificación de eventos y te han asignado la tarea de preparar una gala privada exclusiva. El equipo necesita tu ayuda para procesar datos desordenados de invitados, confirmar RSVPs y asignar mesas para la cena. A lo largo de este laboratorio, usarás:

- **Métodos de strings** para limpiar nombres de invitados
- **Métodos de conjuntos** para gestionar datos de RSVP
- **Tuplas** para asignar asientos en las mesas

Cada parte se basa en la anterior, así que trabájalas en orden.

---

### 🧪 Parte 1: Primeros pasos — Recopilar datos de invitados y RSVP

Se te proporciona código que recopila lo siguiente:
- Nombres de invitados sin procesar (ingresados por un usuario)
- Nombres de personas que confirmaron "Sí"
- Nombres de personas que confirmaron "No"

Hay un problema: hay errores y bugs en el código proporcionado. Tu tarea es depurar el código y agregar tres declaraciones print:
1. La primera declaración print debe imprimir `raw_guest_list`.
2. La segunda declaración print debe imprimir `rsvp_yes_list`.
3. La tercera declaración print debe imprimir `rsvp_no_list`.

#### ✏️ Funcionalidad esperada del código

1. Solicita al usuario que ingrese nombres de invitados. Deben ingresar un nombre por línea y escribir `"done"` cuando terminen. La entrada debe ser **insensible a mayúsculas/minúsculas** para la entrada `"done"`. Cada nombre ingresado se agrega a una lista.
2. Repite esto para:
   - Invitados que confirmaron **sí**
   - Invitados que confirmaron **no**
3. Imprime cada lista.

#### ✅ Código inicial

También proporcionado en `main.py`:
```python
# Guest List Guru — Part 1 (with bugs)

# Collect raw guest entries
raw_guest_list = []
print("Enter guest names (type 'done' when finished'):")

while True:
    name = input(> )
    if name == "Done":
        break
    raw_guest_list.append(name)

# Input RSVP yes
rsvp_yes_list = []
print("\nEnter names of guests who RSVP'd YES (type 'done' when finished):")
while True
    name = input("> ")
    if name == 'DONE':
        break
    rsvp_yes_list + name

# Input RSVP no
rsvp_no_list = []
print("\nEnter names of guests who RSVP'd NO (type 'done' when finished):")
while True:
    name = input("> ")
    if name.lower() == 'done':
        break
    rsvp_no_list.append(name
```

#### ✅ Entrada de ejemplo

**🧍 Nombres de invitados:**
```plaintext
alice smith
Bob Jones
CHARLIE DAVIS
alice smith  
Charlie davis
done
```

**✅ RSVP "Sí":**
```plaintext
Alice smith
CHARLIE DAVIS
done
```

**❌ RSVP "No":**
```plaintext
BOB JONES
done
```

#### ✅ Salida esperada
```plaintext
Enter guest names (type 'done' when finished):
>  
> 
> 
> 
> 
> 
Enter names of guests who RSVP'd YES (type 'done' when finished):
> 
> 
> 
Enter names of guests who RSVP'd NO (type 'done' when finished):
> 
> 
['alice smith', '  Bob Jones', 'CHARLIE DAVIS', 'alice smith  ', 'Charlie davis']
['Alice smith', 'CHARLIE DAVIS']
['BOB JONES']
```

---

### 🔤 Parte 2: Limpiar la lista de invitados (Métodos de strings + Conjuntos)

¡La lista de invitados está desordenada! Necesitas limpiarla antes de continuar.

> ℹ️ **Sobre tu código de la Parte 1**
>
> **Debes** tener el código de la Parte 1 funcionando para hacer esta parte. Comenta las tres declaraciones print al final del código de la Parte 1.

#### ✏️ Instrucciones

1. Usa métodos de strings para limpiar cada nombre en `raw_guest_list`:
   - **Elimina** los espacios en blanco al inicio y final.
   - Estandariza la capitalización a formato **título** (title case).
2. Agrega los nombres limpios a un **conjunto** para eliminar duplicados.
3. Muestra el conjunto limpio de nombres de invitados de `raw_guest_list` en el siguiente formato:
```plaintext
   Cleaned Guest List:
   <cleaned_guest_list>
```

> 🧠 ¿Por qué un conjunto? ¡Elimina automáticamente cualquier entrada repetida!

> ⚠️ **Nota importante sobre los conjuntos**
>
> Los conjuntos son **desordenados**. Esto significa que **el orden no está garantizado** en tiempo de ejecución. Por esto, debes convertir tu conjunto en una **lista ordenada** o usar algún otro método de ordenación alfabética antes de imprimir.

#### ✅ Entrada de ejemplo

**🧍 Nombres de invitados:**
```plaintext
alice smith
Bob Jones
CHARLIE DAVIS
alice smith  
Charlie davis
done
```

**✅ RSVP "Sí":**
```plaintext
Alice smith
CHARLIE DAVIS
done
```

**❌ RSVP "No":**
```plaintext
BOB JONES
done
```

#### ✅ Salida esperada
```plaintext
Enter guest names (type 'done' when finished):
> 
> 
> 
> 
> 
> 
Enter names of guests who RSVP'd YES (type 'done' when finished):
> 
> 
> 
Enter names of guests who RSVP'd NO (type 'done' when finished):
> 
> 
Cleaned Guest List:
['Alice Smith', 'Bob Jones', 'Charlie Davis']
```

---

### 📬 Parte 3: Reconciliación de RSVPs (Operaciones de conjuntos)

Ahora que tienes una lista de invitados limpia y las respuestas de RSVP, es hora de determinar quién realmente vendrá a la gala.

#### ✏️ Instrucciones

1. Limpia `rsvp_yes_list` y `rsvp_no_list` de la misma forma que limpiaste la lista de invitados.
2. Convierte las listas de RSVP limpias en conjuntos.
3. Usa operaciones de conjuntos para determinar:
   - ✅ Invitados que vendrán (`coming`)
   - ❌ Invitados que declinaron (`declined`)
   - ❓ Invitados que no han respondido (`no_response`)
   - 🧐 Cualquier RSVP (ya sea "sí" o "no") de personas que no están en la lista original de invitados (`unexpected`)
4. Imprime cada grupo claramente, incluso los que estén vacíos, en el siguiente formato:
```plaintext
   Coming: <coming>
   Declined: <declined>
   No Response: <no_response>
   Unexpected RSVPs: <unexpected>
```
5. Mantén la salida de la Parte 1.

#### ✅ Entrada de ejemplo

Aquí hay una **entrada de ejemplo** que producirá salidas no vacías para **las cuatro categorías**:

- ✅ Invitados que vendrán
- ❌ Invitados que declinaron
- ❓ Invitados que no han respondido
- ⚠️ RSVPs inesperados (no están en la lista de invitados)

**🧍 Nombres de invitados:**
```plaintext
amy pond
rory williams
River Song
the doctor
clara oswald
done
```

**✅ RSVP "Sí":**
```plaintext
The Doctor
rose tyler
amy pond
done
```

**❌ RSVP "No":**
```plaintext
Rory Williams
captain jack
done
```

#### ✅ Salida esperada
```plaintext
Enter guest names (type 'done' when finished):
> 
> 
> 
> 
> 
> 
Enter names of guests who RSVP'd YES (type 'done' when finished):
> 
> 
> 
> 
Enter names of guests who RSVP'd NO (type 'done' when finished):
> 
> 
> 
Cleaned Guest List:
['Amy Pond', 'Clara Oswald', 'River Song', 'Rory Williams', 'The Doctor']
Coming: ['Amy Pond', 'The Doctor']
Declined: ['Rory Williams']
No Response: ['Clara Oswald', 'River Song']
Unexpected RSVPs: ['Captain Jack', 'Rose Tyler']
```

---

### 🍽️ Parte 4: Asignación de mesas (¡Tuplas!)

Es hora de asignar a los invitados a las mesas para la cena. Usarás tuplas para organizar el plan de asientos.

#### ✏️ Instrucciones

1. Ordena la lista de invitados que confirmaron "sí" (este es el conjunto `coming` de la parte anterior).
2. Agrupa los invitados ordenados en parejas en orden alfabético usando un bucle.
3. Para cada pareja, crea una **tupla** en el formato:
```python
   (invitado1, invitado2)
```
4. Agrega cada tupla a una **lista**.
5. Si hay un número impar de invitados, la última mesa debe tener tres invitados.
6. Imprime las asignaciones de mesas en el siguiente formato:
```plaintext
   Table Assignments:
   Table 1: <pareja_de_invitados>
   Table 2: <pareja_de_invitados>
   ...
   Table <n>: <pareja_de_invitados>
```
7. Comienza los números de mesa en 1 e incrementa.
8. Mantén las salidas de las Partes 1 y 2.

#### ✅ Conjunto de entrada 1: Emparejamiento perfecto (4 invitados)

**🧍 Nombres de invitados:**
```plaintext
amy pond
rory williams
River Song
the doctor
done
```

**✅ RSVP "Sí":**
```plaintext
amy pond
the doctor
River Song
rory williams
done
```

**❌ RSVP "No":**
```plaintext
done
```

**🧾 Conjunto `coming` esperado:**
```python
{'Amy Pond', 'The Doctor', 'River Song', 'Rory Williams'}
```

**🎯 Salida:**
```plaintext
Table Assignments:
Table 1: (Amy Pond, River Song)
Table 2: (Rory Williams, The Doctor)
```

#### ✅ Conjunto de entrada 2: Número impar (5 invitados)

**🧍 Nombres de invitados:**
```plaintext
mickey smith
rose tyler
jack harkness
martha jones
donna noble
done
```

**✅ RSVP "Sí":**
```plaintext
rose tyler
martha jones
donna noble
mickey smith
jack harkness
done
```

**❌ RSVP "No":**
```plaintext
done
```

**🧾 Conjunto `coming` esperado:**
```python
{'Mickey Smith', 'Rose Tyler', 'Jack Harkness', 'Martha Jones', 'Donna Noble'}
```

**🎯 Salida:**
```plaintext
Table Assignments:
Table 1: (Donna Noble, Jack Harkness)
Table 2: (Martha Jones, Mickey Smith, Rose Tyler)
```

#### ✅ Conjunto de entrada 3: Caso mínimo (2 invitados)

**🧍 Nombres de invitados:**
```plaintext
leela
k9
done
```

**✅ RSVP "Sí":**
```plaintext
leela
k9
done
```

**❌ RSVP "No":**
```plaintext
done
```

**🧾 Conjunto `coming` esperado:**
```python
{'Leela', 'K9'}
```

**🎯 Salida:**
```plaintext
Table Assignments:
Table 1: (K9, Leela)
```