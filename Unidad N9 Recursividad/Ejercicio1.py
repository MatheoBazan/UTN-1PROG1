# ============================================
# EJERCICIO 1: FACTORIAL DE UN NÚMERO
# ============================================

def factorial(n):
    """Función recursiva que calcula el factorial de un número."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("EJERCICIO 1: FACTORIAL DE UN NÚMERO")
numero = int(input("Ingrese un número entero positivo: "))

for i in range(1, numero + 1):
    print(f"Factorial de {i} = {factorial(i)}")

print("\n--------------------------------------------\n")