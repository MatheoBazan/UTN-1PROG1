#Escribe un programa que multiplique cada elemento de una lista de números por un
#valor ingresado por el usuario.
lista = []
while True:
    dato = input("Ingrese un numero cualquiera, si desea terminar ingrese salir ")
    if dato.lower() == "salir":
        break
    try:
        numero = float(dato)
        lista.append(numero)
    except ValueError:
        print("No ah ingresado un numero, vuelva a intentar")
while True:
    try:
        multiplicador = float(input("Ingrese un numero que multiplicara a todos los numeros de la lista "))
        break
    except ValueError:
        print("No ah ingresado un numero, vuelva a intentar")
print(f"Esta es la lista original {lista}")
lista = [i * multiplicador for i in lista]
print(f"Y esta es la lista con los numeros multiplicados por {multiplicador}: {lista}")