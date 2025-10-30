# Escribe un programa que permita al usuario ingresar una lista y un número, y cuente cuántas veces aparece ese número en la lista.

numero = int(input("Ingrese un número que quiere verificar cuántas veces aparece: "))
numeros = list(map(int, input("Ingresa números separados por espacio: ").split()))

contador = 0
#Con iteracion
for i in numeros:
    if i == numero:
        contador += 1
print(f"El numero {numero} se repite {contador} veces")

#Con funcion
veces = numeros.count(numero)

print(f"El número {numero} aparece {veces} veces en la lista.")