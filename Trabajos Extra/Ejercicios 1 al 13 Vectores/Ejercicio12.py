# Ingresar dos listas de igual longitud
lista1 = list(map(int, input("Ingresa la primera lista (números separados por espacio): ").split()))
lista2 = list(map(int, input("Ingresa la segunda lista (números separados por espacio): ").split()))

# Verificamos que tengan la misma longitud
if len(lista1) != len(lista2):
    print("Error: Las listas deben tener la misma longitud")
else:
    # Suma elemento por elemento
    suma = [lista1[i] + lista2[i] for i in range(len(lista1))]
    print("Resultado de la suma elemento por elemento:", suma)
