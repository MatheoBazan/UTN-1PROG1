#1) Solicitar edad y enviar un mensaje de "Es mayor de edad" o "Es menor de edad"
print('Ejercicio N1')
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print('Es mayor de edad')
else:
    print('Es menor de edad')

#2) Pedir una nota y comprobar si el alumno esta "aprobado" o "desaprobado"
print('Ejercicio N2')
nota= int(input("Ingrese su nota: "))
if nota >=6:
    print('Aprobado')
else:
    print('Desaprobado')

#2) Escribir un programa que permita ingresar solo números pares.
print('Ejercicio N3')
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print('Ha ingresado un número par')
else:
    print('Por favor, ingrese un número par')

#4) Escribir un programa que solicite al usuario su edad e imprima si es niño, adolescente, adulto joven o adulto
print('Ejercicio N4')

edad = int(input("Ingresa tu edad: "))
if edad < 0:
    print("Por Favor ingrese una edad valida")
elif edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
print('Ejercicio N5')

contraseña = input("Ingresa una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6)Escribir un programa que de 100 numeros aleatorios, calcule media, moda y mediana y analise su sesgo
print('Ejercicio N6')

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Lista de números:", numeros_aleatorios)
print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)

if media > mediana and mediana > moda:
    print("La distribución tiene sesgo positivo")
elif media < mediana and mediana < moda:
    print("La distribución tiene sesgo negativo")
elif media == mediana == moda:
    print("La distribución no tiene sesgo")
else:
    print("La distribución no cumple exactamente con los criterios de sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#tiene o no una vocal, el programa hara diferentes cosas
print('Ejercicio N7')

texto = input("Ingresa una palabra o frase: ")

longitud = len(texto)

ultima_letra = texto[longitud - 1]

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    texto = texto + "!"

print(texto)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
print('Ejercicio N8')

nombre = input("Ingresa tu nombre: ")

opcion = int(input("Elige una opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto y clasifique la 
#magnitud en escala ritcher
print('Ejercicio N8')

magnitud = float(input("Ingresa la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10) Pedir al usuario su hemisferio, dia y mes y en base a eso calcular en que estacion del año se encuentra
print('Ejercicio N10')

hemisferio = input("¿En qué hemisferio estás? (N/S): ")
if hemisferio == "N" or hemisferio == "n":
    print("Elegiste hemisferio norte")
elif hemisferio == "S" or hemisferio == "s":
    print("Elegiste hemisferio sur")
else:
    print("Opción no válida")

mes = int(input("Ingresa el número del mes (1-12): "))
dia = int(input("Ingresa el día: "))

if hemisferio == "N" or hemisferio == "n":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        print("Otoño")
    else:
        print("Fecha no válida")

elif hemisferio == "S" or hemisferio == "s":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        print("Primavera")
    else:
        print("Fecha no válida")

else:
    print("Hemisferio no válido")