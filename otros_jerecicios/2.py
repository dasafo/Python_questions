"""
Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""
def anagram(a, b):
    if a.lower()==b.lower():
        return False
    return sorted(a.lower()) == sorted(b.lower())

print(anagram("amor", "Roma"))  # Debería devolver True
print(anagram("amor", "amor"))  # Debería devolver False
print(anagram("amor", "roma"))  # Debería devolver True
print(anagram("hola", "adiós")) # Debería devolver False