#CASTEO: Codifique un programa que solicite el ingreso de un número decimal y 
# asigne el mismo a una variable valorDecimal, aplique las operaciones de CASTING 
# para convertir la variable en otro tipo de dato. Investigue las diferentes formas 
# de lograr la conversión. Muestre por pantalla el resultado de las conversiones. 

def numeroEntero (numero):
    entero = int(numero)
    print(f"Asi se es el numero {numero} entero: {entero}")

def numeroBooleano (numero):
    booleano = bool(numero)
    print(f"Asi se es el numero {numero} en booleano: {booleano}")

def cadenaNumero (numero):
    cadena = str(numero)
    print(f"Asi se es el numero {numero} como cadena: {cadena}")
    listaNumero(cadena)

def listaNumero(num):
    lista = list(num)
    print(f"Asi se es el numero {num} como lista: {lista}")
    tumplaNumero(lista,num)
    conjuntoNumeros(num)

def tumplaNumero(lis,n):
    tupla = tuple(lis)
    print(f"Asi se es el numero {n} como tupla: {tupla}")

def conjuntoNumeros(n):
    conjunto = set(n)
    print(f"Asi se es el numero {n} como conjunto: {conjunto}")

while True:
    try:
        valorDecimal = float(input("Ingrese un numero decimal "))
        break
    except:
        print("Error, no ingreso un numero decimal. Vuelva a intentar")
print(f"Asi se es el numero {valorDecimal} como decimal: {valorDecimal}")
numeroEntero(valorDecimal)
numeroBooleano(valorDecimal)
cadenaNumero(valorDecimal)

    