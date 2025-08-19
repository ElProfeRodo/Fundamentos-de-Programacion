"""
Calcular índice de masa corporal (IMC) según la fórmula: peso en kilogramos dividido por estatura en metros elevada a dos. El peso y la estatura deben ser ingresados por el usuario. Mostrar por pantalla el resultado.
"""

peso = int(input("Ingresa tu peso: "))
estatura = float(input("Ingresa tu estatura: "))

imc = peso / (estatura ** 2)

print(f"Tu IMC es {imc}")
