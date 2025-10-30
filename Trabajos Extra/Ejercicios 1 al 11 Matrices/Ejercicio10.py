# Una matriz es simétrica si es igual a su transpuesta. Escribe un programa que verifique si una matriz es simétrica.

# Pedir tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

# Crear la matriz
matriz = []
print("Ingrese los elementos fila por fila, separados por espacio:")
for i in range(n):
    fila = list(map(int, input(f"Fila {i+1}: ").split()))
    matriz.append(fila)

# Verificar si es simétrica
simetrica = True
for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break

# Mostrar resultado
if simetrica:
    print("La matriz es simétrica.")
else:
    print("La matriz NO es simétrica.")