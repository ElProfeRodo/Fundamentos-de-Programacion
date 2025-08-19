"""
Pedir el ingreso de un username y verificar que la cantidad de caracteres sea mayor o igual a diez. Mostrar el resultado por pantalla.
"""
username = input("Username: ")

if len(username) >= 10:
    print("OK")
else:
    print("Username no valido")
