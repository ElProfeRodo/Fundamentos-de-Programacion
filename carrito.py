from os import system
from random import randint
import random
system('cls')


productos = []
añadidos=0
excludes = []

def agregar_producto(productos:list, excludes):
    codigo = random.randint(100, 999)
    while codigo in excludes:
        codigo = random.randint(100, 999)
    
    nombre = input("Nombre: ")
    while not nombre.isalpha() or len(nombre) < 4:
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
    
def buscar_producto(productos, codigo):
    indice = None

    if not productos:
        print("\nNo hay productos registrados.\n")
        return None

    for i in range(len(productos)):
        if productos[i]['codigo'] == codigo:
            indice = i
            break

    return indice

def listar_producto():
    intentos=0
    while añadidos>intentos:
        print(f"Codigo: {productos[intentos]['codigo']}  Nombre: {productos[intentos]['nombre']}  Stock: {productos[intentos]['stock']}  Precio: {productos[intentos]['precio']}")
        intentos+=1

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
        agregar_producto(productos, excludes)
        excludes.append({productos[añadidos]['codigo']})
        añadidos+=1
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


