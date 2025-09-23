"""
Crear una función que reciba como parámetro dos números, 
y retorne la suma, resta, multiplicación y división de ellos. 
Debe considerar que la división por cero no existe.
"""

def calculo(num1, num2):
    suma = num1 + num2
    resta = num1 + num2
    multiplicacion = num1 * num2
    
    # Divisor distinto que cero
    if num2 != 0:
        division = num1 / num2
    else:
        division = None
        
    return suma, resta, multiplicacion, division

suma, resta, mult, div = calculo(15,)