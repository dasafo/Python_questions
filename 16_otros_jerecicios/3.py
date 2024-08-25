"""
Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibo(n):
    fib_sequence = [0,1]

    while len(fib_sequence) <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


for i, num in enumerate(fibo(50)):
    print(f"{i+1}: {num}")

