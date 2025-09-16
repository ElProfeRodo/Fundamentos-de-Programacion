"""
Crear una función que solicite la edad por el teclado, y muestre por pantalla si el
usuario es mayor o menor de edad.
"""

def validar_edad():
    edad = int(input("Edad: "))

    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

validar_edad()