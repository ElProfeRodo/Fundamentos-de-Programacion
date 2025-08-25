"""
Crear un programa que permita imprimir una boleta con el detalle de una compra. El
programa debe solicitar tres productos y sus cantidades. Los precios de los
productos deben ser definidos en el programa. El programa debe aplicar un
descuento del 10% si la compra es igual o superior a $20.000, el detalle de la boleta
se muestra por pantalla:
2 x Tallarines    $1.960
3 x Tomates       $2.985
2 x Huevos        $15.990
Subtotal          $20.935
Descuento         $2.093
Total pagar       $18.842
"""
precio1 = 980
precio2 = 995
precio3 = 7995

producto1 = input("Ingresa producto 1: ")
cantidad1 = int(input("Ingresa cantidad 1: "))

producto2 = input("Ingresa producto 2: ")
cantidad2 = int(input("Ingresa cantidad 2: "))

producto3 = input("Ingresa producto 3: ")
cantidad3 = int(input("Ingresa cantidad 3: "))

subtotal1 = cantidad1*precio1
subtotal2 = cantidad2*precio2
subtotal3 = cantidad3*precio3

subtotal = subtotal1 + subtotal2 + subtotal3

if subtotal >= 20000:
    descuento = subtotal * 0.10
else:
    descuento = 0

total = subtotal - descuento

print(f"{cantidad1} x {producto1} \t ${subtotal1}")
print(f"{cantidad2} x {producto2} \t ${subtotal2}")
print(f"{cantidad3} x {producto3} \t ${subtotal3}")
print(f"Subtotal \t ${subtotal}")
print(f"Descuento \t ${descuento:.0f}")
print(f"Total \t\t ${total:.0f}")
