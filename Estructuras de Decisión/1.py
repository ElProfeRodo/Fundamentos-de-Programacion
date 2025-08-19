"""
Solicitar un número por el teclado y verificar si es positivo (mayor que cero). Mostrar el resultado de la comprobación por pantalla.
"""

numero = int(input("Ingresa un numero: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
