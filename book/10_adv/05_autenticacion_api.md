# Autenticación de APIs

## Autenticación de APIs para Principiantes

### Objetivos de Aprendizaje

Al finalizar este módulo, deberías poder:

- Entender por qué es necesaria la autenticación en las APIs
- Identificar tipos comunes de métodos de autenticación en APIs
- Usar una clave de API en una solicitud de Python
- Almacenar credenciales de autenticación de forma segura
- Hacer una solicitud autenticada a una API usando Python

---

## Por Qué Se Necesita la Autenticación

La autenticación en las APIs ayuda a:

- Verificar quién está haciendo la solicitud
- Prevenir el acceso no autorizado
- Proteger datos sensibles
- Limitar el abuso o mal uso de los servicios
- Rastrear el uso de una API

La autenticación garantiza que solo los usuarios o aplicaciones aprobados puedan acceder a los recursos protegidos.

---

## Claves de API

Una **clave de API** es una cadena de texto única proporcionada por un servicio para identificar tu aplicación.

Ejemplo:

```python
clave_api = "123456abcdef"
```

Al hacer una solicitud, la clave se envía junto con ella para que el servidor sepa quién eres.

---

## Ejemplo: Hacer una Solicitud Autenticada a una API en Python

A continuación se muestra un ejemplo simple usando la biblioteca `requests`:

```python
import requests

url = "https://api.example.com/data"

headers = {
    "Authorization": "Bearer TU_TOKEN_DE_API"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())
```

---

## Prácticas Importantes de Seguridad

**Nunca:**

- Compartas tus claves de API públicamente
- Escribas claves directamente en programas que otros verán

En su lugar:

- Almacena las claves en **variables de entorno** escribiéndolas en un archivo `.env`.
- Usa archivos de configuración que no se suban al control de versiones.

Ejemplo:

```python
import os

clave_api = os.getenv("API_KEY")
```

Si `clave_api` está en `.env`, este código carga el valor de `clave_api`.

---

## Resumen

La autenticación de APIs:

- Confirma la identidad
- Controla el acceso
- Protege los datos
- Permite la comunicación segura entre sistemas

Entender la autenticación es un paso importante para trabajar con APIs del mundo real.

---



## ❓ Práctica con la API de la NASA

Tienes un script de Python que obtiene la **Foto Astronómica del Día** usando la API
gratuita de la NASA, pero el script lee la clave de API desde `.env` por razones de
seguridad. En `.env` edita el marcador de posición etiquetado como
(`<TU_CLAVE_NASA_AQUÍ>`).

Tu tarea es:

1. **Obtener tu propia clave de API de la NASA.**
2. **Insertarla en el archivo de entorno** para que la solicitud se autentique correctamente.

---

### Instrucciones

1. **Obtén tu clave de API**
   - Ve a [https://api.nasa.gov](https://api.nasa.gov).
   - Llena el formulario con tu nombre y correo electrónico y haz clic en "Signup".
   - Recibirás tu clave de API por correo electrónico en pocos segundos.

2. **Edita el archivo `.env`**
   - Encuentra la línea que contiene `<TU_CLAVE_NASA_AQUÍ>`.
   - Reemplaza el marcador de posición completamente con tu clave.

3. **Ejecuta el script**
   - El script debería imprimir el título y la descripción de la foto astronómica
     del día, sin generar un error de autenticación.

4. **Entrega** – Una vez que el script se ejecute exitosamente, corre el caso de
   prueba de abajo.

**Después de completar estos pasos, experimenta cambiando la fecha del parámetro
`date` en el script para explorar fotos de otros días:**

```python
params = {
    "api_key": api_key,
    "date": "2024-07-04"  # Prueba con otras fechas en formato AAAA-MM-DD
}
```

**Pista: Si encuentras el error ModuleNotFoundError, ¿qué te enseñó la sección
de Introducción a las Bibliotecas?**

---

### Contexto y Recursos

- Registro y documentación de la API de la NASA: [https://api.nasa.gov](https://api.nasa.gov)
- Endpoint utilizado: **APOD** (Astronomy Picture of the Day)
- El script de ejemplo ya está proporcionado en el espacio de trabajo (`nasa_api.py`).

---

**¡Buena suerte y disfruta explorando el universo con código!**

```python
import requests
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NASA_API_KEY")

if not api_key:
    raise ValueError("Clave de API faltante. Revisa tu archivo .env")

url = "https://api.nasa.gov/planetary/apod"
params = {
    "api_key": api_key,
    "date": "2026-05-03"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Título:", data["title"])
    print("Fecha:", data["date"])
    print("Descripción:", data["explanation"][:300], "...")

    if data["media_type"] == "image":
        image_response = requests.get(data["url"])
        img = mpimg.imread(BytesIO(image_response.content), format="jpg")

        plt.figure(figsize=(10, 7))
        plt.imshow(img)
        plt.axis("off")
        plt.title(data["title"], fontsize=14, pad=12)
        plt.tight_layout()
        plt.show()
    else:
        print("La entrada de hoy es un video:", data["url"])
else:
    print("Error:", response.status_code)
```

