# Escribe un programa que permita al usuario ingresar una lista y la invierta.

numeros = list(map(int, input("Ingresa varios numeros para hacer una lista: ").split()))

#vector invertido con iteracion
vectorInvertido1 = []
for i in range(len(numeros)-1, -1, -1):
    vectorInvertido1.append(numeros[i])
print(f"Vector invertido primera forma {vectorInvertido1}")

#vector invertido con [::-1]
vectorInvertido2 = numeros[::-1]
print(f"Vector invertido segunda forma {vectorInvertido2}")

#vectro invertido con funcion
numeros.reverse()

print("Lista invertida:", numeros)