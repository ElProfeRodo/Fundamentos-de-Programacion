precio = 8000

while True:
    cliente = input("Cliente: ")
    if len(cliente) >= 3:
        break
    else:
        print("El nombre del cliente debe tener por lo menos 3 caracteres")

# cliente = input("Cliente: ")
# while len(cliente) < 3:
#     print("El nombre debe tener al menos 3 caracteres")
#     cliente = input("Cliente: ")

while True:
    cantidad = int(input("Cantidad: "))
    if cantidad > 0:
        break
    else:
        print("La cantidad debe ser positiva")

pedido = cantidad * precio
iva = pedido * 0.19
total = pedido + iva

print(f"Total a pagar: {total}")

while True:
    efectivo = int(input("Efectivo: "))
    if efectivo >= total:
        break
    else:
        print("El efectivo no es suficiente")

vuelto = efectivo - total

print("------------------------")
print("    RESUMEN")
print("------------------------")
print(f"Cliente {cliente}")
print(f"Pizzas {cantidad}")
print(f"Precio c/u {precio}")
print(f"Pedido {pedido}")
print(f"IVA {iva}")
print(f"Total {total}")
print(f"Efectivo {efectivo}")
print(f"Vuelto {vuelto}")