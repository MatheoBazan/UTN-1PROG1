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
            print("Error, no ingreso un numero")

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
    
    print(f"\nMatriz resultante:\n{matriz}")
    print(f"\nSuma de todos los elementos: {np.sum(matriz)}")

    # 🔹 Forma 1: usando un bucle
    print("\nSuma de cada fila (con bucle):")
    for i, fila in enumerate(matriz):
        print(f"Fila {i+1}: {sum(fila)}")

    # 🔹 Forma 2: usando NumPy directamente
    print("\nSuma de cada fila (con NumPy):")
    print(np.sum(matriz, axis=1))

print("Ingrese el tamaño de las filas")
filas = tamanoMatriz()
print("Ingrese el tamaño de las columnas")
columnas = tamanoMatriz()
crearMatriz(filas, columnas)
