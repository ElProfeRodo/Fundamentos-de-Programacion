from random import randint

lista_productos = []

def agregar_producto(lista_productos:list):
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock de el producto: "))
    categoria = input("Ingrese la categoria del producto: ")

    diccionario = {
        "codigo": randint(100, 999),
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "categoria": categoria
    } 

    lista_productos.append(diccionario)

def editar_producto(lista_productos:list):
    consulta_producto = input("Editar Producto: ")
    indice = buscar_producto(lista_productos, consulta_producto)
    
    if indice != None:
        nombre = input("Nombre: ")
        precio = int(input("Precio: "))
        stock = int(input("Stock: "))
        categoria = input("Categoria: ")
        
        lista_productos[indice]['nombre'] = nombre
        lista_productos[indice]['precio'] = precio
        lista_productos[indice]['stock'] = stock
        lista_productos[indice]['categoria'] = categoria
    else:
        print("El producto no existe")

def ver_producto(lista_productos:list):
    producto = input("Producto: ")
    indice = buscar_producto(lista_productos, producto)
    
    if indice != None:
        print(f"Código: {lista_productos[indice]['codigo']}")
        print(f"Nombre: {lista_productos[indice]['nombre']}")
        print(f"Precio: {lista_productos[indice]['precio']}")
        print(f"Stock: {lista_productos[indice]['stock']}")
        print(f"Categoria: {lista_productos[indice]['categoria']}")
    else:
        print("El producto no existe")

def listar_productos(lista_productos:list, categoria:str):
    if len(lista_productos) != 0:
        for i in range(len(lista_productos)):
            if categoria == "todos":
                print(f"Código: {lista_productos[i]['codigo']}")
                print(f"Nombre: {lista_productos[i]['nombre']}")
                print(f"Precio: {lista_productos[i]['precio']}")
                print(f"Stock: {lista_productos[i]['stock']}")
            elif categoria == lista_productos[i]['categoria']:
                print(f"Código: {lista_productos[i]['codigo']}")
                print(f"Nombre: {lista_productos[i]['nombre']}")
                print(f"Precio: {lista_productos[i]['precio']}")
                print(f"Stock: {lista_productos[i]['stock']}")
        print()
    else:
        print("No hay productos para mostrar")

def buscar_producto(lista_productos:list, busqueda:str):
    for i in range(len(lista_productos)):
        if lista_productos[i]['nombre'] == busqueda:
            return i
    return None

while True:
    print("1. Realizar pedido")
    print("2. Agregar producto")
    print("3. Editar producto")
    print("4. Ver producto")
    print("5. Listar productos")
    print("6. Mostrar carrito")
    print("7. Salir")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        pass
    elif opcion == "2":
        agregar_producto(lista_productos)
    elif opcion == "3":
        editar_producto(lista_productos)
    elif opcion == "4":
        ver_producto(lista_productos)
    elif opcion == "5":
        categoria = input("Categoria: ")
        listar_productos(lista_productos, categoria)
    elif opcion == "6":
        pass
    elif opcion == "7":
        break
    else:
        print("La opción es incorrecta")
