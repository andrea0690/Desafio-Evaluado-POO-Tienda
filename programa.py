from tienda import Restaurante, Farmacia, Supermercado

list_tienda = [Restaurante, Farmacia, Supermercado]
ingresar_productos = 1

opcion_ingreso = int(input("¿Qué tienda desea crear?"
"\n(1.) Restaurante \n(2.) Farmacia \n(3.) Supermercado \n:"))

if opcion_ingreso in [1,2,3]:
    
    nombre = input("Ingrese nombre del establecimiento:\n")
    precio = int(input("Ingrese el precio del delivery:\n"))
    tienda = list_tienda[opcion_ingreso-1](nombre, precio)
    
    while ingresar_productos == 1:
        nombre = input("Ingrese nombre del producto:\n")
        precio = int(input("Ingrese el precio del producto:\n"))
        cantidad = int(input("Ingrese la cantidad de productos:\n"))
        
        tienda.ingresar_producto(nombre, precio, cantidad)
        
        ingresar_productos = int(input("\n¿Desea ingresar mas productos?\n"
            "1. Sí\n2. No\n"))
    
    opcion_ingreso = int(input("Seleccione una opcion!"
        "\n(1.) Listar Productos \n(2.) Realizar una venta \n(3.) Salir \n:"))
    
    while opcion_ingreso != 3:
        
        if opcion_ingreso == 1:
            print(tienda.listar_productos())
        elif opcion_ingreso == 2:
            nombre = input("Ingrese nombre del producto a vender:\n")
            cantidad = int(input("Ingrese la cantidad de productos:\n"))
            tienda.realizar_ventas(nombre,cantidad)
            
        opcion_ingreso = int(input("Seleccione una opcion!"
        "\n(1.) Listar Productos \n(2.) Realizar una venta \n(3.) Salir \n:"))
        
print("Fin")