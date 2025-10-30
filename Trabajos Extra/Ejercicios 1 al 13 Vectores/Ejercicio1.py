# Pedimos al usuario una lista de números
numeros = list(map(int, input("Ingresa números separados por espacio: ").split()))

#Calculamos la suma con iterador
suma = 0
for i in numeros:
    suma += i
print(f"Esta es la suma de todos los numeros del vector: {suma}")

# Calculamos la suma usando la función sum()
suma_total = sum(numeros)

print("La suma de todos los elementos es:", suma_total)
