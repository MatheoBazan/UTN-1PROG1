#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
print("Ejercicio N1")
for i in range(101):
    print(i)
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
print("Ejercicio N2")
n = int(input("Ingresa un número entero: "))
if n == 0:
    cantidad = 1
else:
    n_abs = abs(n)
    cantidad = 0
    while n_abs > 0:
        n_abs //= 10
        cantidad += 1
print("Cantidad de dígitos:", cantidad)
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.
print("Ejercicio N3")
a = int(input("Ingresa el primer entero: "))
b = int(input("Ingresa el segundo entero: "))

inicio = min(a, b) + 1
fin = max(a, b)
total = 0
for x in range(inicio, fin):
    total += x
print("Suma entre", a, "y", b, "(excluyendo extremos):", total)
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
print("Ejercicio N4")
total = 0
while True:
    n = int(input("Ingresa un entero (0 para terminar): "))
    if n == 0:
        break
    total += n
print("Total acumulado:", total)
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
print("Ejercicio N5")
import random

secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (0 a 9): "))
    intentos += 1
    if intento == secreto:
        print("¡Correcto! El número era", secreto)
        print("Intentos necesarios:", intentos)
        break
    else:
        print("No es. Intenta de nuevo.")
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente
print("Ejercicio N6")
for i in range(100, -1, -2):
    print(i)
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
print("Ejercicio N7")
n = int(input("Ingresa un entero positivo N: "))
while n < 0:
    n = int(input("N debe ser no negativo. Ingresa nuevamente: "))
total = 0
for i in range(n + 1):
    total += i
print("Suma de 0 a", n, "=", total)
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).
N = 100  # cambia este valor para probar con menos
print("Ejercicio N8")
pares = impares = negativos = positivos = 0

for _ in range(N):
    n = int(input("Ingresa un entero: "))

    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print(f"Pares: {pares}, Impares: {impares}, Negativos: {negativos}, Positivos: {positivos}")
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
print("Ejercicio N9")
N = 100
total = 0
for _ in range(N):
    n = int(input("Ingresa un entero: "))
    total += n
media = total / N
print("Media:", media)
print("Ejercicio N10")
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
n = int(input("Ingresa un entero: "))
signo = -1 if n < 0 else 1
n_abs = abs(n)
invertido = 0

if n_abs == 0:
    invertido = 0
else:
    while n_abs > 0:
        ultimo = n_abs % 10
        invertido = invertido * 10 + ultimo
        n_abs //= 10

print("Invertido:", signo * invertido)