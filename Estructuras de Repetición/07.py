"""
Solicitar por pantalla el ingreso de una contraseña por el teclado,
si el valor ingresado coincide con el valor definido en el programa, 
mostrar por pantalla “Sus credenciales son correctas”. Sino, 
volver a solicitarla hasta que coincida. El usuario tendrá tres 
intentos para introducir la contraseña correcta, después de superar los
intentos, el programa debe dejar de solicitar la contraseña y 
mostrar el mensaje “Su cuenta ha sido bloqueada”.
"""

contraseña_correcta = "hola"
intentos = 3

while True:
    if intentos > 0:
        contraseña_ingresada = input("Contraseña: ")
        if contraseña_ingresada == contraseña_correcta:
            print("Sus credenciales son correctas")
            break
        else:
            intentos -= 1
    else:
        print("Su cuenta ha sido bloqueada")
        break

