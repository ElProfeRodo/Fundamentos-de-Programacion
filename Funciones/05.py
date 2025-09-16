"""
Crear una función que reciba como parámetro dos números, correspondientes al
valor mínimo y máximo de un rango. La función debe retornar la suma de los
números impares dentro de ese rango.
"""

def sumar_impares(minimo, maximo):
    sumatoria = 0
    while minimo <= maximo:
        if minimo % 2 != 0:
            sumatoria += minimo
        minimo += 1
    return sumatoria

suma = sumar_impares(10, 20)
print(f"La suma es {suma}")