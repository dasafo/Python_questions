"""
Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url d://rae ejemplo:
 *   https://dasafodata.com/wp-content/uploads/2021/09/icono_dasafodata.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
"""

import requests
from PIL import Image
from io import BytesIO

def obtener_aspect_ratio(url):
    # Descargar la imagen desde la URL
    response = requests.get(url)
    if response.status_code == 200:
        img_data = response.content
        # Abrir la imagen
        img = Image.open(BytesIO(img_data))
        # Obtener las dimensiones
        width, height = img.size
        # Calcular el aspect ratio
        gcd = gcd_recursive(width, height)
        ratio = f"{width // gcd}:{height // gcd}"
        return ratio
    else:
        return "No se pudo obtener la imagen."

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

# URL de ejemplo
url = "https://dasafodata.com/wp-content/uploads/2021/09/icono_dasafodata.png"
print(obtener_aspect_ratio(url))