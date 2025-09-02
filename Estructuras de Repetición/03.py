"""
Solicitar la cantidad de número que el usuario desea introducir, luego solicitar esos
números y devolver la sumatoria de los números impares
"""
# Consultamos la cantidad al usuario
cantidad = int(input("Cantidad: "))
contador = 0
suma_impar = 0

# Repetimos segun la cantidad
while contador < cantidad:
    contador += 1
    numero = int(input("Numero: "))
    # Si numero es impar
    if numero % 2 != 0:
        suma_impar += numero
print(f"La sumatoria es {suma_impar}")