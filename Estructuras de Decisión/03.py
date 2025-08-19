"""
Ingresar dos números por el teclado y determinar cuál es el mayor de ellos. Mostrar el resultado por pantalla
"""

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

if num1 > num2:
    print("Num1 es mayor que Num2")
elif num1 < num2:
    print("Num1 es menor que Num2")
else:
    print("Los numeros son iguales")
