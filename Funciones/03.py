"""
Crear una función que reciba como parámetro un nombre y un apellido, genere la
dirección de correo electrónico Gmail con esos datos y muestre por pantalla el
resultado.
rodolfo.fernandez@gmail.com
"""

def crear_correo(nombre, apellido):
    correo = f"{nombre}.{apellido}@gmail.com"
    print(correo)

un_nombre = input("Nombre: ")
un_apellido = input("Apellido: ")

crear_correo(un_nombre, un_apellido)