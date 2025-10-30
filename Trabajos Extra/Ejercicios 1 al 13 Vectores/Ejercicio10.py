#Escribe un programa que permita al usuario ingresar una lista de números y eliminar
#un elemento en un índice especificado.
lista = []
while True:
    dato = input("Ingrese un numero cualquiera, si desea terminar ingrese salir ")
    if dato.lower() == "salir":
        break
    try:
        numero = float(dato)
        lista.append(numero)
    except ValueError:
        print("No ha ingresado un numero, vuelva a intentar")
print(f"Esta es la lista completa: {lista}")
while True:
    try:
        indice = int(input("Ingrese la posicion del numero que desea eliminar de la lista "))
        if indice > 0 and indice <= len(lista):
            del lista[indice-1]
            break
        else:
            print("No se puede borrar un valor que no se encuentra en la lista")
    except ValueError:
        print("Ingrese un valor valido")
print(f"Asi quedaria la lista sin el valor del indice {indice}: {lista}")
