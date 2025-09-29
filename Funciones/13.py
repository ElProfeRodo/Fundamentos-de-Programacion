def calificacion(nota):
    if nota < 4.0:
        print("Insuficiente")
    elif nota >= 4.0 and nota <= 5.4:
        print("Suficiente")
    elif nota >= 5.5 and nota <= 6.4:
        print("Bueno")
    elif nota >= 6.5:
        print("Muy bueno")