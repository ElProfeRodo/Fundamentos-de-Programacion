"""
Crear una función que reciba como parámetro el nombre de una mascota, 
retornando el valor booleano verdadero, si la cantidad de caracteres 
del nombre es mayor a seis, en caso contrario debe retornar el valor 
booleano falso.
Adicionalmente, crear otra función que solicite el nombre de la mascota
por el teclado, y llame a la primera función para validar que la cadena
solicitada tenga la cantidad de caracteres deseada.
"""

def nombre_mascota(parametro_nombre):
    if len(parametro_nombre) > 6:
        return True
    else:
        return False

def solicita_nombre():
    variable_nombre = input("Nombre: ")
    if nombre_mascota(variable_nombre):
        print("El nombre es valido")
    else:
        print("Debe tener mas de 6 caracteres")

solicita_nombre()