#Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999)
#y por medio del uso de las operaciones matemáticas módulo 10 y división por 10
#efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo
#14. Plantee el algoritmo planteando métodos para su resolución

import math

def sumaDigitos(num):
    resultado = 0
    digito = 0
    while num > 0:
        digito = num % 10
        num = math.trunc(num/10)
        resultado = resultado + digito
    return resultado
while True:
    try:
        numero = int(input("Ingrese un numero de 3 digitos "))
        if numero >= 100 and numero <=999:
            suma = sumaDigitos(numero)
            print(f"La suma de todos los digitos del numero {numero} es {suma}")
            break
        else:
            print("El numero debe de ser de tres digitos no mas y no menos")
    except:
        print("Error, no ingreso un numero. Vuelva a intentar")