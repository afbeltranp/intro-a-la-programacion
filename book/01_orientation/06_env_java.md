# Hola Mundo en Java (macOS)

Este documento te indica cómo configurar un entorno de programación en Java para tu computadora macOS. También proporciona una guía paso a paso para crear y compilar un programa en Java usando IntelliJ y ejecutarlo desde la línea de comandos.

Necesitarás una Mac con Apple Silicon (por ejemplo, M1–M4) ejecutando macOS Monterey (versión 12) hasta macOS Sequoia (versión 15).

---

## 0. Instalar el Entorno de Programación en Java

El instalador instala y configura un entorno de programación en Java, incluyendo OpenJDK 11 e IntelliJ IDEA, Community Edition 2025.2.

* Inicia sesión en la cuenta de usuario en la que vas a programar. Tu cuenta debe tener privilegios de Administrador. Descarga [`lift-java-arm64.pkg`](https://lift.cs.princeton.edu/java/mac/lift-java-arm64.pkg). (Si tienes una Mac Intel más antigua, descarga en su lugar [`lift-java-x64.pkg`](https://lift.cs.princeton.edu/java/mac/lift-java-x64.pkg).)

* Haz doble clic en `lift-java-arm64.pkg` para instalar el software. Ingresa tu contraseña de macOS cuando se te solicite y usa todas las opciones predeterminadas.

* Elimina `lift-java-arm64.pkg` (si no se elimina automáticamente).

---

## 1. Abrir un Proyecto en IntelliJ

Desarrollarás tus programas en Java en una aplicación llamada IntelliJ IDEA, Community Edition.

IntelliJ organiza los programas de Java en proyectos. En nuestro contexto, cada proyecto corresponde a una tarea de programación. Un proyecto típico contiene programas en Java, archivos de datos asociados y configuraciones específicas del curso (como opciones del compilador, reglas de estilo y bibliotecas del libro de texto).

* Descarga el proyecto para tu tarea de programación en una ubicación conveniente (como el Escritorio).

* Haz doble clic en el archivo zip para descomprimirlo. Esto crea una carpeta de proyecto con el nombre de la tarea de programación correspondiente (como `hello`). Elimina el archivo zip.

* Inicia IntelliJ a través de Finder → Aplicaciones → IntelliJ IDEA CE.app.

* Cuando inicies IntelliJ por primera vez:
   
   * IntelliJ puede mostrar la política de privacidad de JetBrains. Desplázate hacia abajo y haz clic en Aceptar (Accept).

   * IntelliJ puede preguntar si deseas enviar estadísticas de uso anónimas a JetBrains. Elige tu opción preferida.

   * IntelliJ mostrará la pantalla de Bienvenida a IntelliJ IDEA (Welcome to IntelliJ IDEA).

* Para abrir un proyecto desde la pantalla de Bienvenida a IntelliJ IDEA, haz clic en Abrir (Open) y selecciona la carpeta del proyecto.

* Deberías ver un logo de la tarea (en la ventana principal del editor) y una lista de archivos del proyecto (en la barra lateral de Vista de Proyecto a la izquierda). Si no ves la barra lateral de Vista de Proyecto, selecciona LIFT → Proyecto (⌘1) para activarla.

Cuando inicies IntelliJ por primera vez, puede tomar uno o dos minutos indexar tus archivos; algunas funciones no estarán disponibles hasta que este proceso se complete.

**Advertencia:**
**No hagas clic en Nuevo Proyecto (New Project); esta opción está destinada a programadores avanzados. Además, siempre usa Abrir (Open) con una carpeta de proyecto, no con un archivo individual.**

* Cuando termines de trabajar, selecciona la opción de menú IntelliJ IDEA → Salir de IntelliJ IDEA (Quit IntelliJ IDEA) (⌘Q) para cerrar IntelliJ. La próxima vez que inicies IntelliJ, tus proyectos recientes aparecerán en la pantalla de Bienvenida a IntelliJ IDEA para un acceso fácil.

## 2. Crear un Programa en IntelliJ

Ahora estás listo para escribir tu primer programa en Java. IntelliJ cuenta con muchas herramientas de programación especializadas, incluyendo numeración de líneas, resaltado de sintaxis, coincidencia de paréntesis, sangría automática, formato automático, importación automática, renombrado de variables e inspección continua de código.

* Para crear un nuevo programa en Java:
   
   * Vuelve a abrir IntelliJ y el proyecto (si lo cerraste en el paso anterior).

   * Haz clic en el nombre del proyecto en la barra lateral de Vista de Proyecto (a la izquierda), para que quede resaltado. Si no ves la barra lateral de Vista de Proyecto, selecciona LIFT → Proyecto (Project) (⌘1) para activarla.

   * Selecciona la opción de menú LIFT → Nueva Clase Java (New Java Class). Cuando se te solicite, escribe HelloWorld para el Nombre (Name), seguido de Return.

* En la ventana principal del editor, completa el programa en Java `HelloWorld.java` exactamente como aparece a continuación.
```java
public class HelloWorld {
    public static void main(String[] args) {  
        System.out.println("Hello, World");
    }
}
```

Ten en cuenta que IntelliJ genera automáticamente el código base en gris. Si omites incluso un punto y coma, el programa no funcionará.

* Mientras escribes, IntelliJ resalta diferentes elementos sintácticos en diferentes colores. Cuando escribes un paréntesis izquierdo, IntelliJ añade el paréntesis derecho correspondiente. Cuando comienzas una nueva línea, IntelliJ la sangra automáticamente.

* Para guardar el archivo, selecciona la opción de menú Archivo → Guardar Todo (File → Save All) (⌘S). Cuando guardas el archivo, IntelliJ reformatea tu código (si es necesario).

**Consejo:**
IntelliJ está configurado para guardar automáticamente los cambios que haces en tus archivos ante varios eventos (como compilar, ejecutar, cerrar un archivo o proyecto, o salir del IDE). Aún así, recomendamos usar Archivo → Guardar Todo (File → Save All) (⌘S) frecuentemente por su funcionalidad de reformateo de código.

## 3. Compilar y Ejecutar el Programa (desde IntelliJ)

Ahora es momento de ejecutar (o correr) tu programa. Esta es la parte emocionante, donde tu computadora sigue las instrucciones especificadas en tu programa. Antes de hacerlo, debes compilar tu programa en una forma más adecuada para su ejecución en una computadora.

* Selecciona el programa que deseas compilar y ejecutar en la barra lateral de Vista de Proyecto. El programa debería aparecer ahora en la ventana principal del editor.

* Para compilar tu programa, selecciona la opción de menú LIFT → Recompilar 'HelloWorld.java' (Recompile 'HelloWorld.java') (⌘B). Si la compilación es exitosa, recibirás una confirmación en la barra de estado (en la parte inferior).
Si la compilación falla, se abrirá un panel de Recompilación (Recompile) (en la parte inferior), resaltando los errores o advertencias de tiempo de compilación. Revisa tu programa cuidadosamente en busca de errores tipográficos, usando los mensajes de error como guía.

* Para ejecutar tu programa, selecciona la opción de menú LIFT → Ejecutar 'HelloWorld' con Argumentos (Run 'HelloWorld' with Arguments) (⌘E). Dado que este programa no toma argumentos de línea de comandos, haz clic en OK.
Deberías ver la salida del programa (en blanco), junto con un mensaje que indica que el programa terminó normalmente (con código de salida 0).

**Consejo:**
Usa el menú LIFT para compilar y ejecutar tu programa desde IntelliJ. Los menús Build (Compilar) y Run (Ejecutar) ofrecen opciones adicionales para programadores avanzados.
Además, asegúrate de que la ventana principal del editor esté activa antes de usar el menú LIFT (por ejemplo, haciendo clic en el código que deseas compilar o ejecutar).

---

## 4. Compilar y Ejecutar el Programa (desde la línea de comandos)

La línea de comandos es un mecanismo simple y poderoso para controlar tus programas (por ejemplo, argumentos de línea de comandos redirección de archivos y piping). IntelliJ proporciona una terminal integrada para un acceso fácil a la línea de comandos.

* Selecciona la opción de menú LIFT → Terminal (⌘2).

* Esto iniciará una terminal Bash donde escribes comandos. Verás un símbolo del sistema (command prompt) que se ve algo así:
```
~/Desktop/hello>
```

El `~/Desktop/hello` es el directorio de trabajo actual, donde `~` es una abreviatura de tu directorio principal (home).

* Para compilar tu programa, escribe el siguiente comando `javac`. Más específicamente, escribe el texto en amarillo que aparece en la misma línea que el símbolo del sistema.
```
~/Desktop/hello> javac HelloWorld.java
~/Desktop/hello>
```
Asumiendo que el archivo `HelloWorld.java` está en el directorio de trabajo actual, no deberías ver ningún error o advertencia de tiempo de compilación.

* Para ejecutar tu programa, escribe el siguiente comando `java`:
```
~/Desktop/hello> java HelloWorld
Hello, World
```

Deberías ver la salida de tu programa debajo de la línea en la que escribiste el comando.

**Consejo:**
Típicamente, deberías compilar desde IntelliJ (porque IntelliJ resalta las líneas en las que ocurren errores o advertencias de tiempo de compilación) y ejecutar desde la línea de comandos (porque la línea de comandos facilita especificar argumentos de línea de comandos y usar redirección de archivos).


# Hola Mundo en Java (Windows)

Este documento te indica cómo configurar un entorno de programación en Java para tu computadora Windows. También proporciona una guía paso a paso para crear y compilar un programa en Java usando IntelliJ y ejecutarlo desde la línea de comandos.

Necesitarás una versión de 64 bits de Windows 10 u 11 en hardware Intel/AMD x64. (También tenemos un instalador experimental para Windows ARM64.)

---

## 0. Instalar el Entorno de Programación en Java

El instalador instala y configura un entorno de programación en Java, incluyendo OpenJDK 11 e IntelliJ IDEA Community Edition 2025.2.

* Inicia sesión en la cuenta de usuario en la que vas a programar. Tu cuenta debe tener privilegios de Administrador.

* Descarga el instalador de Windows [`lift-java-installer-x64.exe`](https://lift.cs.princeton.edu/java/windows/lift-java-installer-x64.exe). (Si tienes una máquina Windows ARM64, descarga en su lugar [`lift-java-installer-arm64.exe`](https://lift.cs.princeton.edu/java/windows/lift-java-installer-arm64.exe).)

* Haz doble clic en `lift-java-installer-x64.exe` para instalar el software. Ingresa tu contraseña de Windows cuando se te solicite. Usa todas las opciones predeterminadas.

* Elimina `lift-java-installer-x64.exe`.

---

## 1. Abrir un Proyecto en IntelliJ

Desarrollarás tus programas en Java en una aplicación llamada IntelliJ IDEA Community Edition.

IntelliJ organiza los programas de Java en proyectos. En nuestro contexto, cada proyecto corresponde a una tarea de programación. Un proyecto típico contiene programas en Java, archivos de datos asociados y configuraciones específicas del curso (como opciones del compilador, reglas de estilo y bibliotecas del libro de texto).

* Descarga el proyecto para tu tarea de programación en una ubicación conveniente (como el Escritorio).

* Para descomprimir el archivo zip, haz clic derecho sobre él y selecciona Extraer Todo (Extract All). Esto crea una carpeta de proyecto con el nombre de la tarea de programación correspondiente (como `hello`). Elimina el archivo zip.

* Para iniciar IntelliJ, haz clic en el botón Inicio y escribe "IntelliJ IDEA Community Edition 2025.2".

* Cuando inicies IntelliJ por primera vez:
   * IntelliJ puede mostrar la política de privacidad de JetBrains. Desplázate hacia abajo y haz clic en Aceptar (Accept).
   * IntelliJ puede preguntar si deseas enviar estadísticas de uso anónimas a JetBrains. Elige tu opción preferida.
   * IntelliJ mostrará la pantalla de Bienvenida a IntelliJ IDEA (Welcome to IntelliJ IDEA).

* Para abrir un proyecto desde la pantalla de Bienvenida a IntelliJ IDEA, haz clic en Abrir (Open) y selecciona la carpeta del proyecto.

* Deberías ver un logo de la tarea (en la ventana principal del editor) y una lista de archivos del proyecto (en la barra lateral de Vista de Proyecto a la izquierda).
Si no ves la barra lateral de Vista de Proyecto, selecciona LIFT → Proyecto (Project) (Ctrl + 1) para activarla.
Cuando inicies IntelliJ por primera vez, puede tomar uno o dos minutos indexar tus archivos; algunas funciones no estarán disponibles hasta que este proceso se complete.

**Advertencia:**
No hagas clic en Nuevo Proyecto (New Project); esta opción está destinada a programadores avanzados. Además, siempre usa Abrir (Open) con una carpeta de proyecto, no con un archivo individual.

* Cuando termines de trabajar, selecciona la opción de menú Archivo → Salir (File → Exit) para cerrar IntelliJ. La próxima vez que inicies IntelliJ, tus proyectos recientes aparecerán en la pantalla de Bienvenida a IntelliJ IDEA para un acceso fácil.

---

## 2. Crear un Programa en IntelliJ

Ahora estás listo para escribir tu primer programa en Java. IntelliJ cuenta con muchas herramientas de programación especializadas, incluyendo numeración de líneas, resaltado de sintaxis, coincidencia de paréntesis, sangría automática, formato automático, importación automática, renombrado de variables e inspección continua de código.

* Para crear un nuevo programa en Java:
   * Vuelve a abrir IntelliJ y el proyecto (si lo cerraste en el paso anterior).

   * Haz clic en el nombre del proyecto en la barra lateral de Vista de Proyecto (a la izquierda), para que quede resaltado.
Si no ves la barra lateral de Vista de Proyecto, selecciona LIFT → Proyecto (Project) (Ctrl + 1) para activarla.

   * Selecciona la opción de menú LIFT → Nueva Clase Java (New Java Class). Cuando se te solicite, escribe HelloWorld para el Nombre (Name), seguido de Return.

* En la ventana principal del editor, completa el programa en Java `HelloWorld.java` exactamente como aparece a continuación.
```java
public class HelloWorld {
    public static void main(String[] args) {  
        System.out.println("Hello, World");
    }
}
```

Ten en cuenta que IntelliJ genera automáticamente el código base en gris. Si omites incluso un punto y coma, el programa no funcionará.

* Mientras escribes, IntelliJ resalta diferentes elementos sintácticos en diferentes colores. Cuando escribes un paréntesis izquierdo, IntelliJ añade el paréntesis derecho correspondiente. Cuando comienzas una nueva línea, IntelliJ la sangra automáticamente.

* Para guardar el archivo, selecciona la opción de menú Archivo → Guardar Todo (File → Save All) (Ctrl + S). Cuando guardas el archivo, IntelliJ reformatea tu código (si es necesario).

**Consejo:**
IntelliJ está configurado para guardar automáticamente los cambios que haces en tus archivos ante varios eventos (como compilar, ejecutar, cerrar un archivo o proyecto, o salir del IDE). Aún así, recomendamos usar Archivo → Guardar Todo (File → Save All) (Ctrl + S) frecuentemente por su funcionalidad de reformateo de código.

---

## 3. Compilar y Ejecutar el Programa (desde IntelliJ)

Ahora es momento de ejecutar (o correr) tu programa. Esta es la parte emocionante, donde tu computadora sigue las instrucciones especificadas en tu programa. Antes de hacerlo, debes compilar tu programa en una forma más adecuada para su ejecución en una computadora.

* Selecciona el programa que deseas compilar y ejecutar en la barra lateral de Vista de Proyecto. El programa debería aparecer ahora en la ventana principal del editor.

* Para compilar tu programa, selecciona la opción de menú LIFT → Recompilar 'HelloWorld.java' (Recompile 'HelloWorld.java') (Ctrl + B). Si la compilación es exitosa, recibirás una confirmación en la barra de estado (en la parte inferior).

Si la compilación falla, se abrirá un panel de Recompilación (Recompile) (en la parte inferior), resaltando los errores o advertencias de tiempo de compilación. Revisa tu programa cuidadosamente en busca de errores tipográficos, usando los mensajes de error como guía.

* Para ejecutar tu programa, selecciona la opción de menú LIFT → Ejecutar 'HelloWorld' con Argumentos (Run 'HelloWorld' with Arguments) (Ctrl + E). Dado que este programa no toma argumentos de línea de comandos, haz clic en OK.

Deberías ver la salida del programa (en blanco), junto con un mensaje que indica que el programa terminó normalmente (con código de salida 0).

**Consejo:**
Usa el menú LIFT para compilar y ejecutar tu programa desde IntelliJ. Los menús Build (Compilar) y Run (Ejecutar) ofrecen opciones adicionales para programadores avanzados.

Además, asegúrate de que la ventana principal del editor esté activa antes de usar el menú LIFT (por ejemplo, haciendo clic en el código que deseas compilar o ejecutar).

---

## 4. Compilar y Ejecutar el Programa (desde la línea de comandos)

La línea de comandos es un mecanismo simple y poderoso para controlar tus programas (por ejemplo, argumentos de línea de comandos, redirección de archivos y piping). IntelliJ proporciona una terminal integrada para un acceso fácil a la línea de comandos.

* Selecciona la opción de menú LIFT → Terminal (Alt + 2).

* Esto iniciará una terminal Bash donde escribes comandos. Verás un símbolo del sistema (command prompt) que se ve algo así:
```
~> Active code page: 65001
```

El `~/Desktop/hello` es el directorio de trabajo actual, donde `~` es una abreviatura de tu directorio principal (home).

* Para compilar tu programa, escribe el siguiente comando `javac`. Más específicamente, escribe el texto en amarillo que aparece en la misma línea que el símbolo del sistema.
```
~> javac HelloWorld.java
~>
```

Asumiendo que el archivo `HelloWorld.java` está en el directorio de trabajo actual, no deberías ver ningún error o advertencia de tiempo de compilación.

* Para ejecutar tu programa, escribe el siguiente comando `java`:
```
~> java HelloWorld
Hello, World
```

Deberías ver la salida de tu programa debajo de la línea en la que escribiste el comando.

**Consejo:**
Típicamente, deberías compilar desde IntelliJ (porque IntelliJ resalta las líneas en las que ocurren errores o advertencias de tiempo de compilación) y ejecutar desde la línea de comandos (porque la línea de comandos facilita especificar argumentos de línea de comandos y usar redirección de archivos).