"""
Crear una función que reciba como parámetros el precio de un producto
y el porcentaje de descuento. La función debe retornar el precio final 
con el descuento aplicado
"""

def calcular_precio(precio, descuento):
    return precio - (precio * descuento / 100)

precio_final = calcular_precio(1000, 50)
print(f"El precio final es {precio_final}")