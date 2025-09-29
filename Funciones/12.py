def exponente(a, b):
    cont = 0
    resultado = 1
    while cont < b:
        resultado *= a
        cont += 1
    return resultado

exp = exponente(2, 3)
print(exp)