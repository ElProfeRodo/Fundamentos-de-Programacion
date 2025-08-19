"""
Pedir el ingreso de un teléfono y verificar que la cantidad de números sea igual que nueve. Mostrar el resultado por pantalla.
"""

telefono = input("Telefono: ")

if len(telefono) == 9:
    print("El telefono es valido")
else:
    print("El telefono no es valido")
