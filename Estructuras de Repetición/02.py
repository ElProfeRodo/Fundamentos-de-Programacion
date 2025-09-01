"""
Solicitar la cantidad de números que el usuario desea introducir,
luego solicitar esos números y devolver por pantalla el menor y el mayor de ellos.
"""

cantidad = int(input("Cantidad: "))
contador = 0

while contador < cantidad:
    contador += 1
    numero = int(input("Numero: "))
