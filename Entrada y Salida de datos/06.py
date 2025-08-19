"""
Crear un programa que solicite el nombre y precio de un producto, junto con el porcentaje de descuento que se le va a aplicar. El valor del precio puede ser un número real y el valor del descuento debe ser un número entero.
Mostrar el nombre, el precio original y el precio con descuento por pantalla.
"""

producto = input("Ingresa el producto: ")
precio = int(input("Ingresa el precio: "))
descuento = int(input("Ingresa el descuento: "))

precio_final = precio - (precio * (descuento)/100)

print(f"El producto {producto} costaba {precio}, con {descuento}% vale {precio_final}")
