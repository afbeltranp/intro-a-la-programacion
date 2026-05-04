# APIs

## Objetivos de Aprendizaje

- Entender qué es una API y qué problema resuelve
- Aprender cómo se comunican los programas usando APIs
- Reconocer usos comunes de las APIs en el mundo real
- Entender las solicitudes HTTP y los códigos de estado

---

## ¿Qué Es una API?

Una API (Interfaz de Programación de Aplicaciones) permite que un programa solicite datos o servicios de otro programa. En lugar de acceder directamente al código interno o base de datos de otro sistema, un programa envía una solicitud a la API y recibe una respuesta.

Las APIs hacen posible que distintos sistemas de software trabajen juntos de manera controlada y segura.

---

## Por Qué Se Usan las APIs

Las APIs se usan porque:

- Permiten el acceso a datos sin exponer sistemas internos
- Estandarizan cómo se manejan las solicitudes y respuestas
- Facilitan la integración de servicios de diferentes proveedores

Sin APIs, los programas necesitarían acceso directo a bases de datos o código interno, lo cual es inseguro e impracticable.

---

## Cómo Funcionan las APIs (Visión General Conceptual)

En términos generales, la mayoría de las APIs siguen este proceso:

- Un programa envía una solicitud de datos o una acción
- La API recibe y procesa la solicitud
- La API envía de vuelta una respuesta, generalmente en un formato estructurado como JSON

No necesitas conocer la implementación interna de una API para usarla.

---

## Solicitudes HTTP

La mayoría de las APIs web usan el protocolo HTTP. Al trabajar con APIs, verás comúnmente distintos tipos de solicitudes:

- **GET** – Recuperar datos del servidor
- **POST** – Enviar datos nuevos al servidor
- **PUT** – Actualizar datos existentes
- **PATCH** – Actualizar parcialmente datos existentes
- **DELETE** – Eliminar datos

Por ejemplo:

- Una aplicación del clima usa una solicitud **GET** para recuperar datos del pronóstico.
- Un formulario de registro de usuario podría usar una solicitud **POST** para enviar los datos del nuevo usuario al servidor.

Una respuesta a una solicitud HTTP generalmente tiene dos partes: un **código de estado** y datos en **JSON**.

---

## ¿Qué Es JSON?

**JSON (Notación de Objetos de JavaScript)** es un formato de datos ligero usado para enviar y recibir datos estructurados, especialmente en solicitudes web y APIs.

En Python, JSON se parece mucho a un **diccionario**.

Ejemplo de JSON:

```json
{
  "nombre": "Alicia",
  "edad": 20,
  "carrera": "Ciencias de la Computación"
}
```

En Python, esto se convierte en:

```python
{
  "nombre": "Alicia",
  "edad": 20,
  "carrera": "Ciencias de la Computación"
}
```

Observa que:

- Los objetos JSON usan **pares clave–valor**
- Las claves son siempre **cadenas de texto**
- La estructura coincide estrechamente con un diccionario de Python

---

### Acceder a Datos JSON en Python

Cuando recibes JSON en una solicitud (por ejemplo, de una API), generalmente se convierte en un diccionario de Python.

Accedes a los valores usando la sintaxis de diccionario:

```python
data = {
    "nombre": "Alicia",
    "edad": 20
}

print(data["nombre"])   # Alicia
print(data["edad"])     # 20
```

---

### JSON y Atributos de Clase

A menudo, los datos JSON se convierten en un objeto (una instancia de una clase).

Por ejemplo:

```python
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

Si el JSON se convierte en esta clase, accedes a los valores usando **notación de punto**:

```python
estudiante.nombre
estudiante.edad
```

Entonces:

- JSON en bruto → se accede como un **diccionario** (`data["clave"]`)
- Convertido a una clase → se accede como un **atributo** (`objeto.clave`)

---

### Construir JSON para una Solicitud

Al enviar JSON en una solicitud, generalmente construyes primero un diccionario de Python:

```python
payload = {
    "nombre": "Alicia",
    "edad": 20
}
```

Este diccionario luego es convertido a JSON automáticamente por la mayoría de los marcos de trabajo.

---

### Lo Que Necesitas Recordar

- JSON está estructurado como pares clave–valor (como un diccionario).
- Las claves son cadenas de texto.
- El JSON convertido se comporta como un diccionario de Python.
- Si se convierte a una clase, accede a los valores usando notación de punto.
- Para enviar JSON, construye un diccionario y deja que el marco de trabajo lo convierta.

Eso es todo lo que necesitas para construir y analizar JSON en este curso.

---

## Códigos de Estado HTTP

Cuando una API responde, incluye un **código de estado** que indica si la solicitud fue exitosa.

Los códigos de estado se agrupan por categoría, según el primer número del código.

### ✅ 2xx — Éxito

| Código de Estado y Nombre | Qué Significa | Qué Pudiste Haber Hecho |
|---------------------------|-------------------------------|--------------------------|
| **200 OK** | La solicitud funcionó y se devolvieron datos. | Enviaste una solicitud correcta y la API respondió correctamente. |
| **201 Creado** | Se creó exitosamente un nuevo elemento. | Enviaste una solicitud POST válida para crear algo. |
| **204 Sin Contenido** | La solicitud funcionó, pero no había nada que devolver. | Actualizaste o eliminaste algo exitosamente, pero no hay datos en la respuesta. |

### ❌ 4xx y 5xx — Errores

| Código de Estado y Nombre | Qué Significa | Qué Pudiste Haber Hecho |
|---------------------------|-------------------------------|--------------------------|
| **400 Solicitud Incorrecta** | La solicitud no tenía el formato correcto. | Puede que falten campos, el formato JSON sea incorrecto o los tipos de datos sean inválidos. |
| **401 No Autorizado** | Se requiere autenticación o falló. | Olvidaste incluir una clave de API, token, o tus credenciales son incorrectas. |
| **403 Prohibido** | No tienes permiso para acceder a este recurso. | Probablemente usaste la URL incorrecta. |
| **404 No Encontrado** | El recurso solicitado no existe. | La URL probablemente es incorrecta. |
| **500 Error Interno del Servidor** | Algo salió mal en el servidor. | Tu solicitud puede ser válida, pero la propia API encontró un problema. |
| **503 Servicio No Disponible** | El servidor no está disponible temporalmente. | La API puede estar caída; intenta de nuevo más tarde. |

Los códigos de estado ayudan a los desarrolladores a entender rápidamente qué ocurrió después de hacer una solicitud.

---

## Ejemplos de Uso de APIs

Las APIs se usan comúnmente para:

- Datos meteorológicos
- Datos financieros y del mercado de valores
- Mapas y servicios de ubicación
- Plataformas de redes sociales
- Servicios de IA y aprendizaje automático

Cuando usas una aplicación para revisar el clima u obtener indicaciones, esa aplicación generalmente está llamando a una o más APIs.

---

## APIs en Python

Python puede interactuar con APIs usando bibliotecas como `requests`. En este curso, los ejemplos de APIs se enfocan en entender el concepto en lugar de construir aplicaciones complejas.

Estructura de ejemplo de una solicitud a una API (no ejecutada):

```python
import requests

response = requests.get("https://api.example.com/data")

print(response.status_code)   # Muestra el código de estado HTTP
print(response.json())        # Convierte la respuesta JSON en datos de Python
```

---

## ❓ Pregunta sobre APIs

El archivo **`api.py`** está pensado para obtener el **clima actual del lugar que elijas** usando la **API gratuita de clima Open-Meteo** y mostrar las condiciones meteorológicas.

Sin embargo, el programa actualmente **falla** debido a un error.

Tu tarea es:

- Asignar a `response` el valor devuelto por `requests.get(url)`, que actualmente falta
- Asegurarte de que el programa se ejecute sin fallar
- Confirmar que muestre correctamente las condiciones climáticas actuales de tu ubicación
- Divertirte buscando el clima de lugares interesantes
- Puedes obtener las coordenadas de diferentes lugares buscándolas en Google

**Lista de coordenadas para algunos lugares interesantes**:

- **París**: 48.8575, 2.3514
- **Nueva York**: 40.7128, -74.0060
- **Roma**: 41.8967, 12.4822
- **Washington D.C.**: 38.9073, -77.0369
- **Vancouver**: 49.2827, -123.1207


```python
import requests

# Coordinates to gather weather from
# input your own coordinates and place name, the ones available are from Gainesville, FL
place_name = "Gainesville, FL"
latitude = 29.6518
longitude = -82.3248

# API endpoint (no authentication required)
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

# Make API request
response =

# Convert response to JSON
data = response.json()

# Extract relevant information
current_weather = data["current_weather"]
temperature = current_weather["temperature"]
windspeed = current_weather["windspeed"]
winddirection = current_weather["winddirection"]
weathercode = current_weather["weathercode"]

# Process data
temp_fahrenheit = (temperature * 9/5) + 32

# Output results
print(f"Current Weather Data for {place_name}:")
print("----------------------------------------")
print(f"Temperature (C): {temperature}")
print(f"Temperature (F): {temp_fahrenheit:.2f}")
print(f"Wind Speed (km/h): {windspeed}")
print(f"Wind Direction (degrees): {winddirection}")
print(f"Weather Code: {weathercode}")
```