"""
Crear una función que reciba como parámetro una palabra 
y un número entero n, y retorne la palabra repetida n 
veces por pantalla.
"""

def repetir_palabra(palabra, n):
    return palabra * n

def repetir_palabra(palabra, n):
    cont = 0
    palabras = ""
    while cont < n:
        cont += 1
        palabras += palabra
    return palabras

resultado = repetir_palabra("Hola", 3)
print(resultado)