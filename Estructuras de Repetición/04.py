"""
Solicitar números desde el teclado hasta que el usuario ingrese el valor cero. Luego,
mostrar por pantalla la sumatoria de los números introducidos
"""
suma = 0

while True:
    numero = int(input("Numero: "))
    if numero == 0:
        break
    suma += numero

numero = int(input("Numero: "))
while numero != 0:
    suma += numero
    numero = int(input("Numero: "))

print(f"La suma es {suma}")