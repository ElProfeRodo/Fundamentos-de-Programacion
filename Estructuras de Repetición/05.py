"""
Solicitar números desde el teclado hasta que el usuario 
ingrese el valor cero. Luego, mostrar por pantalla el promedio 
de los números positivos.
"""

contador = 0
suma = 0

while True:
    numero = int(input("Numero: "))
    if numero != 0:
        if numero > 0:
            contador += 1
            suma += numero
    else:
        break

if contador == 0:
    print("Error")
else:
    promedio = suma / contador
    print("El promedio es", promedio)