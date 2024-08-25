"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1): 
        """se basa en una propiedad matemática de los números primos: 
           si un número n es divisible por algún número distinto de 1 y
           de sí mismo, entonces al menos uno de esos divisores será menor
           o igual a la raíz cuadrada de n."""
        if num%i == 0:
            return False
        
    return True

def primos_entre(lim_inf, lim_sup):
    primos=[]

    for num in range(lim_inf, lim_sup + 1):
        if es_primo(num):
            primos.append(num)
    return primos

primos = primos_entre(1,100)

for primo in primos:
    print(primo)
