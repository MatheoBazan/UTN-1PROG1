# Escribe un programa que pida al usuario una lista de números y encuentre el mayor y el menor de ellos.

numeros = list(map(int, input("Ingresa números separados por espacio: ").split()))

#Calculamos maximo y minimo con un iterador
maximo = numeros[0]
minimmo = numeros[0]
for i in numeros:
    if i > maximo:
        maximo = i
    if i < minimmo:
        minimmo = i
print(f"El numero mayor es: {maximo}")
print(f"El numero menor es: {minimmo}")

#Calculamos maximo y minimo con las funciones max y min
mayor = max(numeros)
menor = min(numeros)

print("Lista ingresada:", numeros)
print("Número mayor:", mayor)
print("Número menor:", menor)