"""
Crear una función que reciba como parámetro un número decimal 
y retorne el mismo número redondeado a 2 decimales.
"""

def redondear(numero):
    return round(numero, 2)

numero = redondear(1.25356465465465465465)
print(numero)