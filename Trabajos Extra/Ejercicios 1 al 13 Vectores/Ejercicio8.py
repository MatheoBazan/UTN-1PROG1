# Escribe un programa que identifique y muestre los elementos que se repiten en una lista.

from collections import Counter

numeros = list(map(int, input("Ingresa números separados por espacio: ").split()))

#Con iteraciones
numerosRepetidos = []
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[j] == numeros[i]:
            if numeros[j] not in numerosRepetidos:
                numerosRepetidos.append(numeros[j])
print(f"Lista de numeros repetidos: {numerosRepetidos}")

#Con libreria
conteo = Counter(numeros)
duplicados = [n for n, count in conteo.items() if count > 1]

print("Elementos repetidos:", duplicados)
