"""
Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
"""

def area(poligono):
    tipo = poligono['tipo']
    if tipo == "triangulo":
        base = poligono['base']
        altura = poligono['altura']
        return base * altura / 2
    elif tipo == 'cuadrado':
        lado = poligono['lado']
        return lado ** 2
    elif tipo == 'rectangulo':
        base = poligono['base']
        altura = poligono['altura']
        return base * altura
    else:
        raise ValueError("Tipo de poligono no soportado")
    
# Ejemplos de uso
triangulo = {'tipo': 'triangulo', 'base': 10, 'altura': 5}
cuadrado = {'tipo': 'cuadrado', 'lado': 4}
rectangulo = {'tipo': 'rectangulo', 'base': 8, 'altura': 3}

print("Área del triángulo:", area(triangulo))  # Debería devolver 25.0
print("Área del cuadrado:", area(cuadrado))    # Debería devolver 16
print("Área del rectángulo:", area(rectangulo))# Debería devolver 24