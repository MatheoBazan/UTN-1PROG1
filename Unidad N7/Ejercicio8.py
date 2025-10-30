#Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.
productos = {}
while True:
    print("Opciones:")
    print("1. Consultar stock")
    print("2. Agregar unidades")
    print("3. Agregar producto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        stock = productos.get(producto, 0)
        print(f"Stock de {producto}: {stock}")
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
        productos[producto] = productos.get(producto, 0) + unidades
        print(f"Stock actualizado de {producto}: {productos[producto]}")
    elif opcion == "3":
        producto = input("Ingrese el nombre del producto: ")
        if producto not in productos:
            stock = int(input("Ingrese el stock inicial: "))
            productos[producto] = stock
            print(f"Producto {producto} agregado con stock {stock}.")
        else:
            print(f"El producto {producto} ya existe.")
    elif opcion == "4":
        break
    else:
        print("Opción inválida.")