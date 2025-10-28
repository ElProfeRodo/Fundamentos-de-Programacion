productos = []

def agregar_producto(productos:list):
    nombre = input("Nombre: ")
    while not nombre.isalpha() or len(nombre) < 5:
        nombre = input("Nombre: ")
        
    precio = input("Precio: ")
    while not precio.isdigit() or int(precio) < 0:
        precio = input("Precio: ")

    stock = input("Stock: ")
    while not stock.isdigit() or int(stock) < 0:
        stock = input("Stock: ")

    productos.append({'nombre': nombre, 'precio': precio, 'stock': stock})

while True:
    print("1. Agregar producto")
    print("2. Editar producto")
    print("3. Mostrar producto")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("6. Listar productos")
    print("7. Salir del menu")

    opcion = input("Opción: ")
    
    if opcion == "1":
        agregar_producto(productos)
    elif opcion == "2":
        print()
    elif opcion == "3":
        print()
    elif opcion == "4":
        print()
    elif opcion == "5":
        print()
    elif opcion == "6":
        print()
    elif opcion == "7":
        break
    else:
        print("No es una opción valida, intente de nuevo...")

