#Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad
#es una matriz cuadrada donde los elementos de la diagonal principal son 1 y el resto
#son 0.
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
    #Opcion 1
    matriz = np.identity(tam, dtype=int)
    print(f"Asi quedaria la matriz identidad de tamaño {tam} \n {matriz}")
    #Opcion 2
    matriz2 = []
    for i in range(tam):
        fila = []
        for j in range(tam):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        matriz2.append(fila)
    print(f"Matriz identidad:")
    for i in matriz2:
        print(i)

print("Ingrese el tamaño de la matriz")
tamano = tamanoMatriz()
crearMatriz(tamano)