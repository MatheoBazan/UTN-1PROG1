#Escribe un programa que pida al usuario una lista de números y cuente cuántos de
#ellos son pares y cuántos son impares.
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
pares = [i for i in lista if i % 2 == 0]
impares = [i for i in lista if i % 2 != 0]
print(f"Esta es la lista completa: {lista}")
print(f"Este es el numero total de numeros pares: {len(pares)} y la lista de estos {pares}")
print(f"Este es el numero total de numeros impares: {len(impares)} y la lista de estos {impares}")