"""
Calcular la edad de un usuario. El usuario debe ingresar su nombre y año de nacimiento. Por pantalla se debe mostrar: 
Hola [USUARIO], tienes [EDAD] años.
"""

nombre = input("Ingresa tu nombre: ")
año_nacimiento = int(input("Ingresa año nacimiento: "))

edad = 2025 - año_nacimiento

print(f"Hola {nombre}, tienes {edad} años")
