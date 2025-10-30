# Escribe un programa que permita al usuario ingresar una lista de números y calcule el promedio de los elementos.

numeros = list(map(int, input("Ingresa varios numeros para hacer una lista: ").split()))

#Con iterador
suma = 0
contador = 0
for i in numeros:
    suma += i
    contador += 1
print(f"El promedio de los numeros es: {suma/contador}")

#Con funciones
promedio = sum(numeros) / len(numeros)

print("Promedio de la lista: ", promedio)