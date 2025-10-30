from barrio import Barrio
from vivienda import Vivienda

# ----------------------------- MENÚ -----------------------------

def menu():
    barrios = []

    while True:
        try:
            print("\n--- MENÚ ---")
            opcion = int(input(
                "1) Cargar Barrio\n"
                "2) Superficie Total del Terreno\n"
                "3) Superficie del Terreno por Manzana\n"
                "4) Superficie cubierta de una vivienda\n"
                "5) Superficie cubierta total del Barrio\n"
                "6) Salir\n"
                "7) Mostrar resumen de barrios\nSeleccione: "
            ))

            if opcion == 1:
                barrio = cargarBarrio()
                barrios.append(barrio)

            elif opcion == 2:
                nombre = input("Ingrese el nombre del barrio: ")
                for i in barrios:
                    if i.nombre.lower() == nombre.lower():
                        total = i.getSuperficieTotalTerreno()
                        print(f"Superficie total del barrio '{i.nombre}': {total}")
                        break
                else:
                    print("Barrio no encontrado.")

            elif opcion == 3:
                nombre = input("Ingrese el nombre del barrio: ")
                manzana = input("Ingrese la manzana: ")
                for i in barrios:
                    if i.nombre.lower() == nombre.lower():
                        total = i.getSuperficieTotalTerrenoXManzana(manzana)
                        print(f"Superficie total de la manzana '{manzana}': {total}")
                        break
                else:
                    print("Barrio no encontrado.")

            elif opcion == 4:
                nombre = input("Ingrese el nombre del barrio: ")
                for i in barrios:
                    if i.nombre.lower() == nombre.lower():
                        numero = int(input("Ingrese el número de la casa: "))
                        superficie = i.obtenerNumeroCasa(numero)
                        if superficie:
                            print(f"La superficie cubierta de la vivienda es: {superficie}")
                        else:
                            print("No existe una casa con ese número.")
                        break
                else:
                    print("Barrio no encontrado.")

            elif opcion == 5:
                nombre = input("Ingrese el nombre del barrio: ")
                for i in barrios:
                    if i.nombre.lower() == nombre.lower():
                        total = i.getSuperficieTotalCubierta()
                        print(f"Superficie total cubierta del barrio '{i.nombre}': {total}")
                        break
                else:
                    print("Barrio no encontrado.")

            elif opcion == 6:
                print("Hasta luego.")
                break

            elif opcion == 7:
                mostrarResumenBarrios(barrios)

            else:
                print("Opción inválida.")

        except ValueError:
            print("Error, ingrese solo números válidos.")

def mostrarResumenBarrios(barrios):
    if not barrios:
        print("\nNo hay barrios registrados aún.\n")
        return

    print("\n--- RESUMEN DE BARRIOS ---")
    for b in barrios:
        print(f"\nBarrio: {b.nombre}")
        print(f"Empresa constructora: {b.empresaConstructora}")
        print(f"Cantidad de viviendas: {len(b.vivienda)}")
        print(f"Superficie total terreno: {b.getSuperficieTotalTerreno()}")
        print(f"Superficie total cubierta: {b.getSuperficieTotalCubierta()}")
    print("------------------------------")

def cargarBarrio():
    nombre = input("Ingrese el nombre del barrio: ")
    empresaConstructora = input("Ingrese la empresa constructora: ")

    barrio = Barrio(nombre, empresaConstructora)
    print("Ahora procederemos a cargar las viviendas del barrio.")
    while True:
        vivienda = cargarVivienda()
        barrio.vivienda.append(vivienda)
        opcion = input("¿Desea seguir cargando viviendas? (s/n): ").lower()
        if opcion == "n":
            break
    return barrio


def cargarVivienda():
    calle = input("Ingrese el nombre de la calle: ")
    numero = validarNumeroEntero("Ingrese el número de la calle: ")
    manzana = input("Ingrese la manzana: ")
    nroCasa = validarNumeroEntero("Ingrese el número de la casa: ")
    superficieTerreno = validarNumeroDecimal("Ingrese la superficie total del terreno: ")

    vivienda = Vivienda(calle, numero, manzana, nroCasa, superficieTerreno)
    cargarHabitacion(vivienda, superficieTerreno)
    return vivienda


def cargarHabitacion(vivienda, superficie):
    print("Cargando habitaciones...")
    total = 0
    while True:
        nombre = input("Ingrese el nombre de la habitación: ")
        metros = validarNumeroDecimal("Ingrese la superficie de la habitación: ")
        total += metros
        if total > superficie:
            print("Error: la suma supera la superficie del terreno.")
            total -= metros
            continue
        vivienda.agregarHabitacion(nombre, metros)
        opcion = input("¿Desea agregar otra habitación? (s/n): ").lower()
        if opcion == "n":
            break


def validarNumeroEntero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("Debe ingresar un número positivo.")
        except ValueError:
            print("Ingrese solo números enteros.")


def validarNumeroDecimal(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("Debe ingresar un número positivo.")
        except ValueError:
            print("Ingrese solo números válidos (decimales o enteros).")


if __name__ == "__main__":
    menu()