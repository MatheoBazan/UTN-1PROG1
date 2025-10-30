# Crea un programa que genere una matriz identidad inversa de tamaño n. Una matriz identidad inversa es
# una matriz cuadrada donde los elementos de la diagonal inversa principal son 1 y el resto son 0.

# Pedir tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz: "))

# Crear la matriz identidad inversa
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if j == n - i - 1:  # condición para la diagonal inversa
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

# Mostrar la matriz
print("Matriz identidad inversa:")
for fila in matriz:
    print(fila)