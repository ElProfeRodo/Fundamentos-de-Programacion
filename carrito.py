import random

lista_productos = []

def crear_producto(lista_productos:list):
    # Se genera un numero de tres digitos
    codigo = random.randint(100, 999)

    while True:
        nombre = input("Nombre: ")
        # Se valida que el largo ser mayor o igual a 3
        if len(nombre) >= 3: 
            break
        else:
            print("El nombre debe tener por lo menos 3 caracteres")

    precio = input("Precio: ")
    # Validamos que el precio sean digitos mayores que cero
    while not precio.isdigit() or int(precio) <= 0:
        precio = input("Precio: ")

    stock = input("Stock: ")
    # Validamos que el stock sean digitos mayores que cero
    while not stock.isdigit() or int(stock) <= 0:
        stock = input("Stock: ")

    dicc_producto = {
        'codigo': codigo,
        'nombre': nombre,
        'precio': int(precio),
        'stock': int(stock)
    }

    lista_productos.append(dicc_producto)

def editar_producto(lista_productos:list, codigo):
    indice = buscar_producto(lista_productos, codigo)
    if indice != None:
        nombre = input("Nombre: ")
        precio = int(input("Precio: "))
        stock = int(input("Stock: "))
        lista_productos[indice]['nombre'] = nombre
        lista_productos[indice]['precio'] = precio
        lista_productos[indice]['stock'] = stock

def buscar_producto(lista_productos:list, codigo):
    for i in range(len(lista_productos)):
        if lista_productos[i]['codigo'] == codigo:
            return i
    return None

def listar_productos(lista_productos:list):
    print("Nombre \t Precio \t Stock")
    print("--------------------------------")
    for producto in lista_productos:
        print(f"{producto['nombre']} \t {producto['precio']} \t\t {producto['stock']}")

while True:
    # Menú
    print("1. Crear producto")
    print("6. Listar productos")
    opcion = input("Opción: ")

    if opcion == "1":
        crear_producto(lista_productos)
    elif opcion == "6":
        listar_productos(lista_productos)
    else:
        print("La opción no existe")
