# Given a string s, find the length of the longest
# substring without repeating characters.
# 
# Example 1:
#       Input: s = "abcabcbb"
#       Output: 3
#       Explanation: The answer is "abc", with the length of 3.
# 
# Example 2:
#       Input: s = "bbbbb"
#       Output: 1
#       Explanation: The answer is "b", with the length of 1.
# 
# Example 3:
#       Input: s = "pwwkew"
#       Output: 3
#       Explanation: The answer is "wke", with the length of 3.
#       Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# Constraints:
#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.


def longitud_subcadena_mas_larga(s: str) -> int:
    indice_caracter = {}  # Diccionario para almacenar el índice más reciente de cada carácter
    inicio = 0  # Índice de inicio de la subcadena actual
    longitud_maxima = 0  # Longitud máxima de la subcadena encontrada sin caracteres repetidos

    for fin in range(len(s)):
        # Si el carácter ya está en el diccionario y su índice es >= inicio
        if s[fin] in indice_caracter and indice_caracter[s[fin]] >= inicio:
            # Mueve inicio a la derecha del mismo carácter encontrado anteriormente
            inicio = indice_caracter[s[fin]] + 1
        
        # Actualiza el índice más reciente del carácter al índice actual
        indice_caracter[s[fin]] = fin

        # Calcula la longitud de la subcadena actual y actualiza longitud_maxima si es necesario
        longitud_maxima = max(longitud_maxima, fin - inicio + 1)

    return longitud_maxima

print(longitud_subcadena_mas_larga("pwwkew"))

