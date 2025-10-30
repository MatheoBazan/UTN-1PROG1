# Escribe un programa que permita al usuario ingresar una lista de números y elimine los elementos duplicados.

numeros = list(map(int, input("Ingresa varios numeros para hacer una lista: ").split()))

sin_duplicados = list(set(numeros))

print("Lista sin duplicados:", sin_duplicados)