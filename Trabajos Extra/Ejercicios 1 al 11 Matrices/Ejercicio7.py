#Escribe un programa que extraiga los elementos de la diagonal principal de una matriz cuadrada.
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

def crearMatriz(tam):
    while True:
        try:
            opcion = int(input("Elija una opcion: \n1-Llenar la matriz manualmente \n2-Llenar la matriz de manera aleatoria \n"))
            if opcion == 1:
                matriz = np.zeros((tam, tam), dtype=int)
                for i in range(tam):
                    for j in range(tam):
                        matriz[i][j] = int(input("Ingrese un numero para la matriz "))
                break
            elif opcion == 2:
                matriz = np.random.randint(1,101,size=(tam, tam))
                break
            else:
                print("Opcion no disponible, vuelva a intentar")
        except:
            print("No se ingreso un numero")
    print(f"Esta es la matriz resultantes: \n {matriz}")
    #Opcion 1
    print(f"Estos son los valores de la diagonal {np.diag(matriz)}")
    #Opcion 2
    diagonal = []
    for i in range(tam):
        for j in range(tam):
            if i == j:
                diagonal.append(int(matriz[i][j]))
    print(f"Diagonal central {diagonal}")

print("Ingrese el tamaño de la matriz")
tamano = tamanoMatriz()
crearMatriz(tamano)