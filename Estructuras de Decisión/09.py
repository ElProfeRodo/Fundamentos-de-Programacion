"""
Simular un control de acceso, solicitando usuario y contraseña, verificando que
ambos datos coinciden para permitir el ingreso al sistema. El usuario y la contraseña
deben ser definidos en el programa.
"""

usuario_correcto = "admin"
password_correcta = 123

usuario = input("Usuario: ")
password = int(input("Password: "))

if usuario == usuario_correcto and password == password_correcta:
    print("Bienvenid@")
else:
    print("Acceso denegado")
