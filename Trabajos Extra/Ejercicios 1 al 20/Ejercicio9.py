#9- Recorre la cadena del ejercicio 6 y transforma cada carácter a su código ASCII.
cadena = input("Ingresa una cadena: ")
for caracter in cadena:
    print(ord(caracter), end=" ")
