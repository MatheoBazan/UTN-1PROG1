# Datos completos de una persona
print ('Ejercicio N1')
Name = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
Edad = input("Ingrese su edad: ")
Ubicacion = input("Ingrese su lugar de residencia: ")
print ("Soy", Name, Apellido, "Tengo ", Edad, "Años y vivo en", Ubicacion)
# Cálculo del área de un rectángulo en Python
print ('Ejercicio N2')
radio = float(input("Ingrese el radio del círculo: "))
pi = 3.14
area = pi * (radio ** 2)
perimetro = 2 * pi * radio
print ("El Area del circulo es,", area, "y el perimetro del circulo es,", perimetro)
# Pedir al usuario una cantidad de segundos e imprimir cuántas horas equivale.
print ('Ejercicio N3')
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(segundos, "Segundos equivalen a", horas, "horas")
# Pedir al usuario un número e imprimir por pantalla la tabla de multiplicar de dicho número.
print ('Ejercicio N4')
numero = int(input("Ingrese un número: "))
print("La tabla de multiplicar del", numero, "es: ")
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
# Pedir dos números enteros al usuario y mostrar division/multiplicacion/suma/resta
print ('Ejercicio N5')
num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print ("La suma es:", suma, "la resta es:", resta, "la multiplicación es:", multiplicacion, "y la división es:", division)
# Pedir datos al usuario y calcular IMC
print ('Ejercicio N6')
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print("Tu indice de masa corporal es: ", imc)
# Pedir temperatura en Celsius y pasarla a Fahrenheit
print ('Ejercicio N7')
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print("La temperatura en Fahrenheit es:", fahrenheit)
# Pedir 3 números al usuario y calcular promedio
print ('Ejercicio N8')
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print("El promedio de los tres números es:", promedio)