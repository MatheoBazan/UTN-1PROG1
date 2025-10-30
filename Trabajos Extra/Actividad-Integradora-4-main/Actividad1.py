class Celdas:
    def __init__(self,fila,columna,valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        

class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def agregarCelda(self,fila,columna,valor):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                print(f"Error, ya existe un valor en la posicion fila:{fila} y celda {columna}")
                return
        self.celdasMatriz.append(Celdas(fila,columna,valor))
    
    def mostrarDatos(self):
        if not self.celdasMatriz:
            print("No hay datos cargados aun")
        else:
            for celdas in self.celdasMatriz:
                print(f"Fila: {celdas.fila} | Columna: {celdas.columna} | Valor: {celdas.valor}")
    
    def buscarValorMatriz(self,fila,columna):
        for celdas in self.celdasMatriz:
            if celdas.fila == fila and celdas.columna == columna:
                print(f"El valor de la posicion Fila {fila} y Columna {columna} es: {celdas.valor}")
                break
        else:
            print(f"No se encuentra nignun valor en la posicion Fila {fila} y Columna {columna}")

def menu():
    matriz = Matriz()
    while True:
        try:
            opcion = int(input("Bienvenido, que desea realizar:\n1) Cargar Datos\n2) Ver valores Cargados\n3) Buscar un Valor\n4) Salir\n"))
            if opcion == 1:
                cargarDatos(matriz)
            elif opcion == 2:
                matriz.mostrarDatos()
            elif opcion == 3:
                buscarValor(matriz)
            elif opcion == 4:
                print("Hasta Luego")
                break
            else:
                print("Error, ingrese una opcion valida")
        except:
            print("Error, ingrese un numero de la opciones")

def cargarDatos(matriz):
    while True:
        valor = input("Primero ingrese un valor cualquiera y si desea salir ingrese FIN: ")
        if valor == "FIN":
            break
        else:
            print("Ahora ingrese el numero de la fila")
            fila = validarNumero()
            print("Ahora ingrese el numero de la columna")
            columna = validarNumero()
            matriz.agregarCelda(fila, columna,valor)

def validarNumero():
    while True:
        try:
            numero = int(input("Ingrese el numero: "))
            if numero < 0:
                print("Error, ingrese un numero positivo")
            else:
                return numero
        except:
            print("Error, ingrese un numero no letras o caracteres")

def buscarValor(matriz):
    print("Primero ingrese el numero de la fila del valor que busca")
    fila = validarNumero()
    print("Ahora ingrese el valor de la columna del valor que busca")
    columna = validarNumero()
    matriz.buscarValorMatriz(fila,columna)

if __name__ == "__main__":
    menu()