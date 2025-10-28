from random import randint

productos = []

def agregar_producto(productos:list):
    codigo = randint(100, 999)

    nombre = input("Nombre: ")
    while not nombre.isalpha() or len(nombre) < 10:
        nombre = input("Nombre: ")
        
    precio = input("Precio: ")
    while not precio.isdigit() or int(precio) < 0:
        precio = input("Precio: ")

    stock = input("Stock: ")
    while not stock.isdigit() or int(stock) < 0:
        stock = input("Stock: ")

    productos.append({'codigo': codigo, 'nombre': nombre, 'precio': precio, 'stock': stock})

def editar_producto(productos: list):
    nombre_buscar = input("Ingrese el nombre del producto que desea editar: ")
    for i in productos:
        if i['nombre'] == nombre_buscar:
            print(f"Producto encontrado: {i['nombre']}")
            
            nuevo_nombre = input("Nuevo nombre (Enter para mantener actual): ")
            if nuevo_nombre != "":
                while not nuevo_nombre.isalpha() or len(nuevo_nombre) < 10:
                    nuevo_nombre = input("Nombre inválido, ingrese nuevamente: ")
                i['nombre'] = nuevo_nombre

            nuevo_precio = input("Nuevo precio (Enter para mantener actual): ")
            if nuevo_precio != "":
                while not nuevo_precio.isdigit() or int(nuevo_precio) < 0:
                    nuevo_precio = input("Precio inválido, ingrese nuevamente: ")
                i['precio'] = nuevo_precio

            nuevo_stock = input("Nuevo stock (Enter para mantener actual): ")
            if nuevo_stock != "":
                while not nuevo_stock.isdigit() or int(nuevo_stock) < 0:
                    nuevo_stock = input("Stock inválido, ingrese nuevamente: ")
                i['stock'] = nuevo_stock

            print("Producto actualizado correctamente.")
            return
    print("No se encontró un producto con ese nombre.")
def buscar_producto(productos):
    if not productos:
        print("\nNo hay productos registrados.\n")
        return

    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    for producto in productos:
        if producto['nombre'] == nombre_buscar:
            print(f"\nProducto encontrado:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Stock: {producto['stock']}\n")
            return

    print(f"\nProducto '{nombre_buscar}' no encontrado.\n")
def listar_producto():
    print(productos)

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
        editar_producto(productos)
    elif opcion == "3":
        print()
    elif opcion == "4":
        print()
    elif opcion == "5":
        print()
    elif opcion == "6":
        listar_producto()
    elif opcion == "7":
        break
    else:
        print("No es una opción valida, intente de nuevo...")

