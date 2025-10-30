from computadora import Computadora
class CostoComputadora:
    def __init__(self):
        pass

    def mostrarPedido(self,pc):
        print("--------Computadora--------")
        print(f"Marca: {pc.marca}")
        print(f"Modelo: {pc.modelo}")
        print("Componentes: ")
        precio = 0
        print("Componente       Marca       Cantidad        Precio X Unidad     SubTotal")
        for comp in pc.listaComponentesCPU:
            precio += pc.mostrarComponentes(comp)
        print()
        print(f"Costo total: {precio}")
        if precio > 50000:
            print(f"El precio sugerido de venta es de {precio} + {precio * 0.3} = {precio + precio * 0.3}")
        else:
            print(f"El precio sugerido de venta es de {precio} + {precio * 0.4} = {precio + precio * 0.4}")


def menu():
    while True:
        costo = CostoComputadora()
        print("Bienvenido")
        pc = cargarInformacion()
        cargarComponentes(pc)
        costo.mostrarPedido(pc)
        while True:
            opcion = input("Desea cotizar una nueva computadora s/n").lower()
            if opcion == "s":
                break
            elif opcion == "n":
                print("Hasta luego")
                return
            else:
                print("Esta opcion no esta disponible, vuelva a intentar")
        

def cargarInformacion():
    while True:
        marca = input("Ingrese la marca de la computadora que busca: ")
        if not marca.replace(" ","").isalpha():
            print("Error, solo ingrese el nombre de la marca no numeros o caracteres")
        else:
            modelo = input(f"Ahora ingrese el modelo de la computadora marca {marca}: ")
            compu = Computadora(marca,modelo)
            return compu

def cargarComponentes(pc):
    listaComponentes = []
    while True:
        while True:
            componente = input("Ingrese el nombre del componente que desea agregar: ")
            if not listaComponentes:
                listaComponentes.append(componente.replace(" ","").lower())
                break
            else:
                for comp in listaComponentes:
                    if comp == componente.replace(" ","").lower():
                        print("Error, este componente ya esta cargado ingrese otro componente")
                        break
                else:
                    listaComponentes.append(componente.replace(" ","").lower())
                    break
                    
        marca = input(f"Ingrese el nombre de la marca del componente {componente}: ")

        print(f"Ahora ingrese la cantidad de {componente} que se va a llevar")
        cantidad = validarCantidadPrecio()
        print(f"Por ultimo ingrese el precio del {componente}")
        precio = validarCantidadPrecio()

        pc.agregarComponentes(componente,marca,cantidad,precio)

        opcion = input("¿Desea continuar cargando componentes? (Ingrese n si no desea continuar, en cambio ingrese cualquier tecla si desea continuar)").lower()
        if opcion == "n":
            return 

def validarCantidadPrecio():
    while True:
            try:
                valor = int(input(f"Por favor ingrese el valor correspondiente al componente que se va a llevar: "))
                if valor <= 0:
                    print("El valor no puede ser 0 o menos")
                else:
                    return valor
            except ValueError:
                print("Error, debe de ingresar numeros no letras o caracteres")

if __name__ == "__main__":
    menu()