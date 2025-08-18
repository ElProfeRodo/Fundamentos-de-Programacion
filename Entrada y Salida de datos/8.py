"""
Calcular la propina (10%) por un pedido en un restaurante. Debe solicitar el nombre de 3 productos, el precio unitario de cada uno y las cantidades solicitadas.
Mostrar por pantalla el siguiente detalle:
2 x completo		$2.000
3 x bebidas		$1.100
1 x postre			$1.500
Total del pedido		$8.800
Total con propina	$9.680
"""

prod1 = input("Ingresa producto 1: ")
prec1 = int(input("Ingresa precio 1: "))
cant1 = int(input("Ingresa cantidad 1: "))

prod2 = input("Ingresa producto 2: ")
prec2 = int(input("Ingresa precio 2: "))
cant2 = int(input("Ingresa cantidad 2: "))

prod3 = input("Ingresa producto 3: ")
prec3 = int(input("Ingresa precio 3: "))
cant3 = int(input("Ingresa cantidad 3: "))

subtotal1 = prec1 * cant1
subtotal2 = prec2 * cant2
subtotal3 = prec3 * cant3

total = subtotal1 + subtotal2 + subtotal3
propina = total * 0.10
total_final = total + propina

print(f"{cant1} x {prod1} \t\t ${prec1}")
print(f"{cant2} x {prod2} \t\t ${prec2}")
print(f"{cant3} x {prod3} \t\t ${prec3}")
print(f"Total pedido \t\t ${total}")
print(f"Total con propina \t ${total_final}")
