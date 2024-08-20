"""
Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invert_string(sentence):
    sentence_list = list(sentence)
    ini = 0
    end = len(sentence_list) - 1

    while ini < end:
        temp = sentence_list[ini]
        sentence_list[ini] = sentence_list[end]
        sentence_list[end] = temp

        ini += 1
        end -= 1
    return ''.join(sentence_list)

print(invert_string("Hola Mundo"))
        