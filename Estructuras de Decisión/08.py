"""Solicitar tres números por el teclado, y determinar cuál es el mayor de ellos."""

num1 = int(input("Ingresa numero 1: "))
num2 = int(input("Ingresa numero 2: "))
num3 = int(input("Ingresa numero 3: "))

if num1 > num2 and num1 > num3:
    print(f"El mayor es {num1}")

elif num2 > num1 and num2 > num3:
    print(f"El mayor es {num2}")

elif num3 > num1 and num3 > num2:
    print(f"El mayor es {num3}")

else:
    print("Los numeros son iguales")
