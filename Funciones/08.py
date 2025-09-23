"""
Crear una función que solicite una contraseña por teclado y verifique 
si tiene al menos 8 caracteres. La función debe retornar True si cumple
la condición y False en caso contrario.
"""

def password():
    contraseña = input("Contraseña: ")
    return len(contraseña) >= 8

if password():
    print("La contraseña es valida")
else:
    print("La contraseña no es valida")