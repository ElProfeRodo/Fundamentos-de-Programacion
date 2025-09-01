"""
Solicitar la cantidad de números que el usuario desea introducir,
luego solicitar esos números y devolver por pantalla el menor y el mayor de ellos.
"""

cantidad = int(input("Cantidad: "))
numero = int(input("Numero: "))
mayor = numero
menor = numero
contador = 0

while contador < cantidad - 1:
    contador += 1
    numero = int(input("Numero: "))
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print(f"El mayor es {mayor}")
print(f"El menor es {menor}")
