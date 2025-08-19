"""
Calcular la nota de presentación al examen, solicitando el ingreso de 4 calificaciones y la ponderación de cada una de ellas. Las notas pueden ser números reales y las ponderaciones deben ser números enteros. Mostrar el resultado por pantalla.
"""

nota1 = float(input("Ingresa nota 1: "))
pond1 = int(input("Ingresa ponderacion 1: "))

nota2 = float(input("Ingresa nota 2: "))
pond2 = int(input("Ingresa ponderacion 2: "))

nota3 = float(input("Ingresa nota 3: "))
pond3 = int(input("Ingresa ponderacion 3: "))

nota4 = float(input("Ingresa nota 4: "))
pond4 = int(input("Ingresa ponderacion 4: "))

calculo1 = nota1 * (pond1/100)
calculo2 = nota2 * (pond2/100)
calculo3 = nota3 * (pond3/100)
calculo4 = nota4 * (pond4/100)

nota_presentacion = calculo1 + calculo2 + calculo3 + calculo4

print(f"Tu nota de presentacion es {nota_presentacion:.1f}")
