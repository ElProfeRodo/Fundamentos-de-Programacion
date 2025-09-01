"""
Solicitar un número desde el teclado y validar que sea positivo.
En caso de no serlo, volver a pedir el número hasta que supere la validación
"""

numero = int(input("Numero: "))

# Se valida que el numero sea positivo
while numero < 0:
    print("El numero debe ser positivo")
    numero = int(input("Numero: "))

while True:
    numero = int(input("Numero: "))
    # Si el numer es positivo, salimos del while
    if numero > 0:
        break
    else:
        print("El numero debe ser positivo")