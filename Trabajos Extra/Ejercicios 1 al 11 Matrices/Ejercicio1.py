def crear_matriz(filas, columnas):
    matriz = []
    valor = 1
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(valor)
            valor += 1
        matriz.append(fila)
    return matriz

# Ejemplo de uso
filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

resultado = crear_matriz(filas, columnas)

print("Matriz generada:")
for fila in resultado:
    print(fila)
