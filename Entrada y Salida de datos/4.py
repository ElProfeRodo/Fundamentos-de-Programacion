"""
Convertir temperatura de grados Fahrenheit a grados Celsius, considerando la siguiente fórmula: temperatura en grados Fahrenheit menos treinta y dos, luego dividir el resultado anterior por uno punto ocho. La temperatura en grados Fahrenheit debe ser ingresada por el usuario y el resultado debe ser mostrado por pantalla:
[TEMP_FAH]°F equivale a [TEMP_CEL]°C
"""

temp_f = float(input("Ingresa temperatura: "))
temp_c = (temp_f - 32) / 1.8

print(f"{temp_f}°F equivale a {temp_c}°C")
