#Desarrolle un programa que ayude a una cajera a determinar el número de billetes y
#monedas que se necesitan de cada una de las siguientes denominaciones 200, 100, 50,
#20, 10, 5, 2 y 1, y monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de
#dinero dada. Ejemplo si la cantidad es 1390,55 se necesitan 6 billetes de 200, 1 billete
#de 100, 1 billete de 50, 2 billetes de 20, 1 moneda de 0.50 y una moneda de 0.05
#centavos. Plantee el algoritmo planteando métodos para su resolución.

import math

def billetes200(dinero):
    if dinero >= 200:
        billetes = math.trunc(dinero / 200)
        dinero = dinero % 200
        print(f"{billetes} billetes de 200")
    billetes100(dinero)

def billetes100(dinero):
    if dinero >= 100:
        billetes = math.trunc(dinero / 100)
        dinero = dinero % 100
        print(f"{billetes} billetes de 100")
    billetes50(dinero)

def billetes50(dinero):
    if dinero >= 50:
        billetes = math.trunc(dinero / 50)
        dinero = dinero % 50
        print(f"{billetes} billetes de 50")
    billetes20(dinero)

def billetes20(dinero):
    if dinero >= 20:
        billetes = math.trunc(dinero / 20)
        dinero = dinero % 20
        print(f"{billetes} billetes de 20")
    billetes10(dinero)

def billetes10(dinero):
    if dinero >= 10:
        billetes = math.trunc(dinero / 10)
        dinero = dinero % 10
        print(f"{billetes} billetes de 10")
    billetes5(dinero)

def billetes5(dinero):
    if dinero >= 5:
        billetes = math.trunc(dinero / 5)
        dinero = dinero % 5
        print(f"{billetes} billetes de 5")
    billetes2(dinero)

def billetes2(dinero):
    if dinero >= 2:
        billetes = math.trunc(dinero / 2)
        dinero = dinero % 2
        print(f"{billetes} billetes de 2")
    billetes1(dinero)

def billetes1(dinero):
    if dinero >= 1:
        billetes = math.trunc(dinero / 1)
        dinero = dinero % 1
        print(f"{billetes} billetes de 1")
    monedas050(dinero)

def monedas050(dinero):
    if dinero >= 0.50:
        monedas = math.trunc(dinero / 0.50)
        dinero = dinero % 0.50
        print(f"{monedas} monedas de 0.50 centavos")
    monedas025(dinero)

def monedas025(dinero):
    if dinero >= 0.25:
        monedas = math.trunc(dinero / 0.25)
        dinero = dinero % 0.25
        print(f"{monedas} monedas de 0.25 centavos")
    monedas010(dinero)

def monedas010(dinero):
    if dinero >= 0.10:
        monedas = math.trunc(dinero / 0.10)
        dinero = dinero % 0.10
        print(f"{monedas} monedas de 0.10 centavos")
    monedas005(dinero)

def monedas005(dinero):
    if dinero >= 0.05:
        monedas = math.trunc(dinero / 0.05)
        dinero = dinero % 0.05
        print(f"{monedas} monedas de 0.05 centavos")

while True:
    try:
        dinero = float(input("Ingrese el dinero "))
        break
    except:
        print("Error, no ingreso un valor. Vuelva a intentar")
print("Se necesitan: ")
billetes200(dinero)
