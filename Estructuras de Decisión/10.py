"""
Generar un programa para asignar una letra según el rango de una calificación,
solicitando la nota por el teclado, y devolviendo la letra por pantalla a partir de la
siguiente tabla:
Nota      | Letra
---------------------
6.0 a 7.0 | A
5.1 a 5.9 | B
4.0 a 5.0 | C
1.0 a 3.9 | D
"""

nota = float(input("Ingresa nota: "))

if nota >= 6.0 and nota <= 7.0:
    print("A")

elif nota >= 5.1 and nota <= 5.9:
    print("B")

elif nota >= 4.0 and nota <= 5.0:
    print("C")

elif nota >= 1.0 and nota <= 3.9:
    print("D")
