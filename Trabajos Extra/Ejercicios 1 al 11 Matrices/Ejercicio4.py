import numpy as np

def tamanoMatriz():
    while True:
        try:
            tam = int(input())
            if tam > 0:
                return tam
            else:
                print("No puede ingresar valores nulos o negativos")
        except ValueError:
            print("Error, no ingreso un número")

def crearMatriz(fila, columna):
    while True:
        try:
            opcion = int(input("Elija una opcion: \n1- Llenar la matriz manualmente \n2- Llenar la matriz de manera aleatoria \n"))
            if opcion == 1:
                matriz = np.zeros((fila, columna), dtype=int)
                for i in range(fila):
                    for j in range(columna):
                        matriz[i][j] = int(input(f"Ingrese un número para la posición [{i},{j}]: "))
                break
            elif opcion == 2:
                matriz = np.random.randint(1, 101, size=(fila, columna))
                break
            else:
                print("Opción no disponible, vuelva a intentar")
        except ValueError:
            print("No se ingresó un número")
    
    print(f"\nMatriz original:\n{matriz}")
    
    # 🔹 Calcular la transpuesta 
    #Opcion 1
    transpuesta = matriz.T
    print(f"\nMatriz transpuesta:\n{transpuesta}")

    #Opcion 2
    traspuesta2 = []
    for j in range(columna):
        nuevaFila = []
        for i in range(fila):
            nuevaFila.append(int(matriz[i][j]))
        traspuesta2.append(nuevaFila)
    print("Traspuesta: ")
    for i in traspuesta2:
        print(i)


print("Ingrese el tamaño de las filas")
filas = tamanoMatriz()
print("Ingrese el tamaño de las columnas")
columnas = tamanoMatriz()
crearMatriz(filas, columnas)
