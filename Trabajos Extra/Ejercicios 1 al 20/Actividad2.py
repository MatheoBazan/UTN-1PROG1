#Si se asigna un valor a una variable fuera de rango (mayor de lo establecido) ¿Qué
#ocurre? ¿Existe alguna forma de resolverlo? Ejemplifique. 

#En Python a diferencia de otros lenjuages las variables no tienen un rango fijo predeterminado. El tipo int puede crecer 
#practicamente sin limites, lo unico que puede frenar es la memoria disponible en la PC.
#Ejemplo:

numero = 9999999999999999999999999999
print (numero)

#Pasa exactamente lo mismo con los decimales
numeroDecimal = 1.7e308
print(numeroDecimal)

#Y esto pasa si nos pasamos del rango del decimal o flotante
numeroDecimal = 1.8e308
print(numeroDecimal)

#Si ahora hablamos no sobre la limitacion de Python sino sobre el propio codigo limitando el ingreso de variables, si es posible
# y existen algunas formas de resolverlo

#Obligrar al usuario a que ingrese un numero con n cantidad de cifras

while True:
    numero = int(input("Ingrese un numero de hasta 5 cifras"))
    if numero >= -99999 and numero <= 99999:
        break
    else:
        print("Numero fuera de rango. Vuelva a intentar")
    print(f"Numero aceptado {numero}")

#Esto obliga a que usuario ingrese infinitamente numeros hasta que ingrese un numero de 5 cifras o menos
#Tambien se puede con cadenas

while True:
    palabra = input("Ingrese una palabra")
    if len(palabra) > 5:
        print("Mas de 5 letras, vuelva a intentar")
    else:
        print(f"Palabras aceptada {palabra}")
        break

#Otra forma es truncando el numero que ingrese el usuario hasta que tengamos el numero con la cantidad de cifras que necesitemos

numero = int(input("Ingrese cualquier numero"))
#Convertimos el numero a cadena, usamos el abs para evitar problemas con el signo y lo limitamos a 5 cifras en caso de ser mas y lo transfromamos a numero
numeroTruncado = int(str(abs(numero))[:5])
#En caso de ser negativo poner de nuevo el signo
if numero < 0:
    numeroTruncado = -numeroTruncado
print(f"Numero original: {numero}")
print(f"Numero truncado: {numeroTruncado}")

#Otra forma es dividiendo el numero por 10 hasta que de la cantidad de cifras buscadas

numero = int(input("Ingrese un numero"))
numeroTruncado = numero
while abs(numeroTruncado) > 99999:
    numeroTruncado = numeroTruncado / 10
if numero < 0:
    numeroTruncado = -numeroTruncado
print(f"Numero original: {numero}")
print(f"Numero truncado: {numeroTruncado}")

#En conclusion no hay ningun problema con variables muy grandes en Python solamente estan limitados a la memoria de la PC.
#En cuanto a que el propio codigo oblige a limitar las variables tampoco hay problema ya que este es capaz de limitarlo ya se 
#obligando al usuario a ingresar un numero con n cantidad de cifras o cortandolo automaticamente sin tenes que obligar al usuario a ingresar otro numero.  