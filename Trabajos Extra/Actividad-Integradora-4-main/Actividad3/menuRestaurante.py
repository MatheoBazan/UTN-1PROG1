from plato import Plato
class MenuRestaurante:
    def __init__(self):
        self.platosMenu = []

    def mostrarPlato(self,pedido,plato):
        if pedido.esBebida == True:
            print(pedido.nombreCompleto)
            print(f"Precio: $ {pedido.precio}")
        else:
            print(pedido.nombreCompleto)
            print(f"Precio: $ {pedido.precio}")
            print("Ingredientes: ")
            for ingrediente in plato.ingredientes:
                plato.mostrarIngredientes(ingrediente)


def pedido():
    menu = MenuRestaurante()
    while True:
        print("Bienvenido")
        nombre = pedirNombre()
        precio = pedirPrecio()
        bebida = esBebida()
        plato = Plato(nombre,precio,bebida)
        if bebida == False:
            pedirIngredientes(plato)
            menu.platosMenu.append(plato)
            opcion = input("¿Continuar cargando platos? (Ingrese n si no desea continuar/ Ingrese cualquier cosa para continuar): ").lower()
            if opcion == "n":
                break
    print("-----------Menu-----------")
    for pedido in menu.platosMenu:
        menu.mostrarPlato(pedido,plato)
    
def pedirNombre():
    while True:
        nombre = input("¿Que desea pedir?: ")
        if not nombre.replace(" ","").isalpha():
            print("Ingrese el nombre del producto sin numeros o caracteres")
        else:
            return nombre      

def pedirPrecio():
    while True:
        try:
            precio = float(input("¿Cuanto cuesto el producto?: "))
            if precio <= 0:
                print("El valor del producto no puede ser menor a 0, vuelva a ingresar el precio")
            else:
                return precio
        except:
            print("Error, debe de ingresra el precio del producto en numeros no letras")

def esBebida():
    while True:
        opcion = input("¿Su producto es una bebida? (Ingrese s si es una bebida/ Ingrese n si no es una bebida): ").lower()
        if opcion == "s":
            return True
        elif opcion == "n":
            return False
        else:
            print("Error, ingrese s o n segun si su pedido es o no una bebida")

def pedirIngredientes(plato):
    listaNombresIngredientes = []
    while True:
        while True:
            nombreIngrediente = input("Ingrese el nombre del ingrediente a agregar: ")
            if not nombreIngrediente.replace(" ","").isalpha():
                print("Error, ingrese el nombre del ingrediente sin numero o caracteres")
            else:
                if not listaNombresIngredientes:
                    listaNombresIngredientes.append(nombreIngrediente.lower())
                    break
                else:
                    for nombre in listaNombresIngredientes:
                        if nombre == nombreIngrediente.lower():
                            print(f"Error, ya existe un ingrediente con el nombre {nombre} en la lista")
                            break
                    else:
                        break

        while True: 
            try:
                cantidad = int(input(f"Ingrese la cantidad de {nombreIngrediente} que se va a utilizar: "))
                if cantidad <= 0:
                    print("Error, no puede ingresar un cantidad menor a 10. Vuelva a ingresar")
                else:
                    break
            except ValueError:
                print("Error, ingrese la cantidad en numeros")

        while True:
            unidadesMedidas = ["gramo", "kilogramo", "miligramo", "mililitro", "litro", "taza", "unidad", "pizca"]
            print("Ahora ingrese la unidad de medida, estas son las opciones disponibles: ")
            for i in unidadesMedidas:
                print(i)
            unidad = input("Ingrese la unidad de medidad sin espacios: ").lower()
            for i in unidadesMedidas:
                if i == unidad:
                    plato.agregarIngredientes(nombreIngrediente,cantidad,unidad)
                    break
            else:
                print(f"No esta disponible la unidad {unidad}, vuelva a ingresar la unidad de medida")
            break
        opcion = input("¿Desea seguir cargando ingredientes? (Ingrese n si no desea continuar/ Ingrese cualquier cosa para continuar): ").lower()
        if opcion == "n":
            return
    

if __name__ == "__main__":
    pedido()