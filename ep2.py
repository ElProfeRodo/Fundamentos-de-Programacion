def validar_numero(numero):
    if numero > 0:
        return True
    else:
        return False

def generar_boleta(monto):
    if monto >= 10000:
        descuento = monto * 0.05
    else:
        descuento = 0
        
    subtotal = monto - descuento
    iva = subtotal * 0.19
    total_pagar = subtotal + iva
    
    print("Boleta electronica")
    print("------------------")
    print(f"Monto \t\t {monto}")
    print(f"Descuento \t {descuento}")
    print(f"Subtotal \t {subtotal}")
    print(f"IVA \t\t {iva}")
    print(f"Total pagar \t {total_pagar}")

def mostrar_tarifas():
    print("Rango edades       | Tarifa")
    print("---------------------------")
    print("Menores de 18 años | 2.000")
    print("Entre 18 y 59 años | 3.000")
    print("Desde los 60 años  | 1.500")

def vender_entradas():
    total = 0

    cantidad = int(input("Cantidad: "))
    while validar_numero(cantidad) == False:
        cantidad = int(input("Cantidad: "))

    for i in range(cantidad):
        while True:
            edad = int(input("Edad: "))
            if validar_numero(edad):
                break
        
        if edad < 18:
            total += 2000
        elif edad >= 18 and edad <= 59:
            total += 3000
        elif edad >= 60:
            total += 1500
    
    return total
        

while True:
    print("1. Vender entradas")
    print("2. Mostrar tarifas")
    print("3. SALIR")

    opcion = input("Opcion: ")

    if opcion == "1":
        total_venta = vender_entradas()
        generar_boleta(total_venta)

    elif opcion == "2":
        mostrar_tarifas()

    elif opcion == "3":
        break

    else:
        print("La opcion es incorrecta")