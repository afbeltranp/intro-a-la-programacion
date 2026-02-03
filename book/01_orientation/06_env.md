# Tu primer programa en Python 3 en Microsoft Windows

Esta página explica cómo configurar un entorno de programación en **Python** para tu computadora con **Microsoft Windows** y ofrece una guía paso a paso para escribir y ejecutar un programa sencillo de **“Hola, mundo”**. Todo el software mencionado es gratuito y está disponible en Internet. Estas instrucciones están pensadas para **Windows 10**, pero para otras versiones recientes de Windows el proceso es muy similar.

---

## Descripción general

El entorno de programación que necesitas consiste en:

- **Python**, es decir, el intérprete de Python.
- **Visual Studio Code (VS Code)** como editor/IDE.

---

## Descargar e instalar Python 

> **Nota:** El Explorador de Windows usa la palabra *carpeta* (*folder*). En este documento usaremos el término *directorio*, equivalente.

Sigue estos pasos para descargar e instalar Python:

1. Abre tu navegador y busca: **“Python download Windows”**.
2. Entra al sitio oficial de Python y descarga el instalador para Windows (normalmente **“Windows standalone installer (64-bit)”**).
3. Ejecuta el instalador.
4. **Muy importante:** marca la casilla  
   ✅ **“Add Python to PATH”** (Agregar Python al PATH)  
   y luego instala con las opciones por defecto.

*(Opcional)* Puedes borrar el archivo instalador cuando termine.

---

## Instalar VS Code y la extensión de Python

### 1) Descargar e instalar VS Code

1. Busca: **“Visual Studio Code download”**.
2. Descarga VS Code desde el sitio oficial de Microsoft.
3. Ejecuta el instalador y sigue los pasos.  

### 2) Instalar la extensión de Python en VS Code

1. Abre **VS Code**.
2. Ve a **Extensiones** (icono de cuadritos a la izquierda) o presiona:  
   - `Ctrl + Shift + X`
3. Busca: **Python**
4. Instala **Python (Microsoft)**.

---

## Probar la instalación (Python)

1. Desde la **terminal integrada de VS Code**, escribe:

    ```bash
    python
    ```

   Deberías ver algo parecido a:
  
    ```
    Python 3.x.x
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

2. Sal de Python:

    ```bash
    exit()
    ```

---

## Configurar VS Code para trabajar con Python

Elegir el intérprete de Python

1. En VS Code presiona: `Ctrl + Shift + P` 
    
2. Escribe: _Python: Select Interprete_
    
3. Elige la versión de Python instalada (la recomendada suele decir “Python 3.x.x”).

---

## Escribir tu primer programa

1. Crea un directorio: `C:\Users\tuusuario\hello`
2. Abre VS Code y abre esa carpeta:

    **File → Open Folder...**

    Selecciona `C:\Users\tuusuario\hello`

3. Crea un archivo nuevo llamado: `helloworld.py` (todo en minúsculas).

4. Escribe este programa exactamente:

    ```python 
    # Escribe 'Hello, World' en la salida estándar.
    print("Hello, World")
    ```

5. Guarda el archivo (`Ctrl + S`).

---

## Ejecutar tu primer programa
  Desde la terminal integrada de VS Code (recomendado):

  1. Abre la terminal en VS Code: **Terminal → New Terminal**

  2. Verifica que estás en la carpeta `hello` (si abriste la carpeta correcta, ya debería estar).

  3. Ejecuta:

      ```bash
      python helloworld.py
      ```
  4. Si ves:

      ```
      Hello, World
      ```

      ¡Funcionó correctamente!

---

## Consejos si aparece un error

* Revisa que el archivo se llame exactamente `helloworld.py` (minúsculas).
* Si el comando `python` no se reconoce, intenta `python3`.
  Si tampoco funciona, es casi seguro que faltó marcar Add Python to PATH al instalar.

¡Listo! Ya instalaste y configuraste un entorno razonable de Python en Windows y ejecutaste tu primer programa en Python.


# Tu primer programa en Python 3 en macOS

Esta página explica cómo configurar un entorno de programación en **Python** para tu computadora con **macOS** y ofrece una guía paso a paso para escribir y ejecutar un programa sencillo de **"Hola, mundo"**. Todo el software mencionado es gratuito y está disponible en Internet. Estas instrucciones funcionan para versiones recientes de macOS (Big Sur, Monterey, Ventura, Sonoma y posteriores).

---

## Descripción general

El entorno de programación que necesitas consiste en:

- **Python**, es decir, el intérprete de Python.
- **Visual Studio Code (VS Code)** como editor/IDE.

---

## Descargar e instalar Python

> **Nota:** macOS viene con Python preinstalado, pero suele ser una versión antigua (Python 2.7). Te recomendamos instalar la versión más reciente de Python 3.

Sigue estos pasos para descargar e instalar Python:

1. Abre tu navegador y busca: **"Python download macOS"**.
2. Entra al sitio oficial de Python (python.org) y descarga el instalador para macOS (normalmente **"macOS 64-bit installer"**).
3. Abre el archivo `.pkg` descargado y sigue el asistente de instalación.
4. Acepta los términos y completa la instalación con las opciones por defecto.

*(Opcional)* Puedes mover el archivo instalador a la papelera cuando termine.

---

## Instalar VS Code y la extensión de Python

### 1) Descargar e instalar VS Code

1. Busca: **"Visual Studio Code download"**.
2. Descarga VS Code desde el sitio oficial de Microsoft.
3. Descarga el archivo `.zip` para macOS.
4. Descomprime el archivo y arrastra **Visual Studio Code** a tu carpeta **Aplicaciones**.

### 2) Instalar la extensión de Python en VS Code

1. Abre **VS Code** desde la carpeta Aplicaciones.
2. Ve a **Extensiones** (icono de cuadritos a la izquierda) o presiona:  
   - `⌘ + Shift + X`
3. Busca: **Python**
4. Instala **Python (Microsoft)**.

---

## Probar la instalación (Python)

1. Abre la aplicación **Terminal** (puedes buscarla con Spotlight presionando `⌘ + Espacio` y escribiendo "Terminal").

2. Escribe:
```bash
    python3 --version
```

   Deberías ver algo parecido a:
```
    Python 3.x.x
```

3. Ahora inicia el intérprete de Python:
```bash
    python3
```

   Verás algo como:
```
    Python 3.x.x
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
```

4. Sal de Python:
```bash
    exit()
```

---

## Configurar VS Code para trabajar con Python

### Elegir el intérprete de Python

1. En VS Code presiona: `⌘ + Shift + P` 
    
2. Escribe: **Python: Select Interpreter**
    
3. Elige la versión de Python instalada (la recomendada suele decir "Python 3.x.x").

---

## Escribir tu primer programa

1. Crea un directorio en tu carpeta de usuario. Abre Terminal y escribe:
```bash
    mkdir ~/hello
```

2. Abre VS Code y abre esa carpeta:

    **File → Open Folder...** (o `⌘ + O`)

    Selecciona la carpeta `hello` que acabas de crear (estará en `/Users/tuusuario/hello`)

3. Crea un archivo nuevo llamado: `helloworld.py` (todo en minúsculas).

4. Escribe este programa exactamente:
```python 
    # Escribe 'Hello, World' en la salida estándar.
    print("Hello, World")
```

5. Guarda el archivo (`⌘ + S`).

---

## Ejecutar tu primer programa

Desde la terminal integrada de VS Code (recomendado):

1. Abre la terminal en VS Code: **Terminal → New Terminal**.

2. Verifica que estás en la carpeta `hello` (si abriste la carpeta correcta, ya debería estar).

3. Ejecuta:
        ```bash
            python3 helloworld.py
        ```

4. Si ves:
        ```
            Hello, World
        ```

    ¡Funcionó correctamente!

---

## Consejos si aparece un error

* Revisa que el archivo se llame exactamente `helloworld.py` (minúsculas).
* En macOS, el comando correcto puede ser `python3` (no solo `python`), ya que `python` puede apuntar a Python 2.7.
* Si `python3` no se reconoce, verifica que completaste correctamente la instalación de Python 3.

---

¡Listo! Ya instalaste y configuraste un entorno razonable de Python en macOS y ejecutaste tu primer programa en Python.
