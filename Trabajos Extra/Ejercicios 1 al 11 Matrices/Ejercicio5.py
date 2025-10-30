#Escribe un programa que encuentre el valor más grande en una lista bidimensional.
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
            opcion = int(input("Elija una opcion: \n1-Llenar la matriz manualmente \n2-Llenar la matriz de manera aleatoria \n"))
            if opcion == 1:
                matriz = np.zeros((fila, columna), dtype=int)
                for i in range(fila):
                    for j in range(columna):
                        matriz[i][j] = int(input("Ingrese un numero para la matriz "))
                break
            elif opcion == 2:
                matriz = np.random.randint(1,101,size=(fila, columna))
                break
            else:
                print("Opcion no disponible, vuelva a intentar")
        except:
            print("No se ingreso un numero")
    print(f"Esta es la matriz resultantes: \n {matriz}")
    #Opcion 1
    print(f"Este es el numero mas grande de la matriz: {matriz.max()}")
    #Opcion 2
    mayor = matriz[0][0]
    for i in range(fila):
        for j in range(columna):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
    print(f"Numero mayor de la matriz {mayor}")

print("Ingrese el tamaño de las filas")
filas = tamanoMatriz()
print("Ingrese el tamaño de las columnas")
columnas = tamanoMatriz()
crearMatriz(filas, columnas)