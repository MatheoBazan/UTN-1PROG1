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

    # 🔹 Pedir escalar al usuario
    escalar = int(input("\nIngrese un valor escalar para multiplicar la matriz: "))

    # 🔹 Multiplicar la matriz por el escalar
    resultado = matriz * escalar
    
    print(f"\nMatriz resultante al multiplicar por {escalar}:\n{resultado}")

    #Opcion 2:
    resultado2 = matriz
    for i in range(fila):
        for j in range(columna):
            resultado2[i][j] *= escalar
    print("Resultado")
    for i in resultado2:
        print(i)
        
print("Ingrese el tamaño de las filas")
filas = tamanoMatriz()
print("Ingrese el tamaño de las columnas")
columnas = tamanoMatriz()
crearMatriz(filas, columnas)
