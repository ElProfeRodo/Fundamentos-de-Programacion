"""
Crear una función que solicite 15 números por el teclado, y muestre por pantalla la
suma de ellos.
"""
def solicitar_numeros():
    contador = 0
    suma = 0

    while contador < 15:
        numero = int(input("Numero: "))
        suma += numero

    print(f"La suma es {suma}")

solicitar_numeros()