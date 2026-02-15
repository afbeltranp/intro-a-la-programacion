# Demostración general

## Juego de trivia de cultura pop para dos jugadores (`quiz_game.py`)

### Objetivo

El objetivo de este proyecto es crear un juego de trivia interactivo para dos jugadores en Python para evaluar el conocimiento de los jugadores sobre cultura pop a través de una serie de preguntas de verdadero o falso. Los jugadores se turnarán para responder todas las preguntas, y el juego rastreará y comparará sus puntuaciones para determinar su experiencia en cultura pop. Además, nos dirá cuántas preguntas respondió correctamente cada jugador, cuántas respondió correctamente cada uno de forma única, y cuántas preguntas respondieron ambos correctamente.

---

## Instrucciones

### Paso 1: Inicializar el cuestionario

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

### Paso 2: Configurar el seguimiento de jugadores

Inicializa conjuntos para cada jugador para rastrear los índices de las preguntas que respondan correctamente.

### Paso 3: Mensaje de bienvenida

Imprime un mensaje de bienvenida para presentar a los jugadores el juego y explicar que el Jugador 1 responderá todas las preguntas primero, seguido del Jugador 2.
```plaintext
Welcome to the Pop Culture True or False Quiz - Two Player Edition!
Player 1 will answer all questions first, followed by Player 2.
```

### Paso 4: Realizar el cuestionario

#### Turno del Jugador 1

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

#### Turno del Jugador 2

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

### Paso 5: Comparar resultados

Usa operaciones de conjuntos para determinar qué preguntas respondieron correctamente ambos jugadores y cuáles fueron respondidas correctamente de forma única por cada jugador. (**Pista:** usa intersección y diferencia de conjuntos)

### Paso 6: Mostrar resultados finales

Resume y muestra los resultados, indicando cuántas preguntas fueron respondidas correctamente por ambos, individualmente, y la puntuación total de cada jugador. (Recuerda que al imprimir un conjunto debes usar `sorted` para que sea consistente con los casos de prueba)
```plaintext
Game Over! Let's see how both players did:
Both players got these questions right: [1, 3]
Questions only Player 1 got right: [2]
Questions only Player 2 got right: [4]
Player 1's score: 2 out of 4
Player 2's score: 2 out of 4
```