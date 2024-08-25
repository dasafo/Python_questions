"""
* Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
"""

def contar_palabras(texto):
    # Definir los caracteres de puntuación a eliminar
    signos_puntuacion = ".,;:!?()[]{}\"'"

    # Convertir el texto a minúsculas
    texto = texto.lower()
    
    # Eliminar los signos de puntuación
    texto_limpio = ""
    for caracter in texto:
        if caracter not in signos_puntuacion:
            texto_limpio += caracter
    
    # Dividir el texto en palabras
    palabras = []
    palabra_actual = ""
    for caracter in texto_limpio:
        if caracter.isspace():
            if palabra_actual:
                palabras.append(palabra_actual)
                palabra_actual = ""
        else:
            palabra_actual += caracter
    if palabra_actual:
        palabras.append(palabra_actual)
    
    # Contar las palabras
    conteo_palabras = {}
    for palabra in palabras:
        if palabra in conteo_palabras:
            conteo_palabras[palabra] += 1
        else:
            conteo_palabras[palabra] = 1
    
    # Mostrar el recuento final
    for palabra, conteo in conteo_palabras.items():
        print(f"{palabra}: {conteo}")

# Ejemplo de uso
texto = "Hola, mundo! Hola a todos. El mundo es grande, pero el universo es aún más grande."
contar_palabras(texto)
