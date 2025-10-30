# ===============================================================
# EJERCICIO 1 - CREAR ARCHIVO INICIAL CON PRODUCTOS
# ===============================================================

print("=== TRABAJO PRÁCTICO: ARCHIVOS EN PYTHON ===\n")
print("Creando archivo 'productos.txt' con datos iniciales...\n")

with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,850.0,15\n")
    archivo.write("Goma,50.0,40\n")

print("Archivo creado correctamente con tres productos.\n")

# ===============================================================
# EJERCICIO 2 - LEER Y MOSTRAR PRODUCTOS
# ===============================================================

print("=== MOSTRAR PRODUCTOS DEL ARCHIVO ===")

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

print("\nLectura finalizada.\n")

# ===============================================================
# EJERCICIO 3 - AGREGAR NUEVO PRODUCTO DESDE TECLADO
# ===============================================================

print("=== AGREGAR NUEVO PRODUCTO ===")
nuevo = input("Ingrese un nuevo producto (nombre,precio,cantidad): ")

# Validar que el formato sea correcto
if "," in nuevo and len(nuevo.split(",")) == 3:
    with open("productos.txt", "a") as archivo:
        archivo.write("\n" + nuevo.strip())
    print("Producto agregado correctamente.\n")
else:
    print("Formato incorrecto. Ejemplo válido: Regla,100.0,20\n")

# ===============================================================
# EJERCICIO 4 - CARGAR PRODUCTOS EN UNA LISTA DE DICCIONARIOS
# ===============================================================

print("=== CARGANDO PRODUCTOS EN LISTA DE DICCIONARIOS ===")

productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

print("Productos cargados correctamente.\n")

for p in productos:
    print(f"{p['nombre']} - ${p['precio']} - Stock: {p['cantidad']}")

# ===============================================================
# EJERCICIO 5 - BUSCAR PRODUCTO POR NOMBRE
# ===============================================================

print("\n=== BUSCAR PRODUCTO POR NOMBRE ===")
nombre_buscar = input("Ingrese el nombre del producto a buscar: ").capitalize()
encontrado = False

for p in productos:
    if p["nombre"].capitalize() == nombre_buscar:
        print(f"Producto encontrado: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.\n")

# ===============================================================
# EJERCICIO 6 - GUARDAR PRODUCTOS ACTUALIZADOS EN EL ARCHIVO
# ===============================================================

print("\n=== GUARDAR PRODUCTOS ACTUALIZADOS ===")

with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("Archivo 'productos.txt' actualizado correctamente.\n")

print("=== FIN DEL PROGRAMA ===")
