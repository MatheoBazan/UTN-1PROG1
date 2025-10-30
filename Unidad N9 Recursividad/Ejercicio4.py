# ============================================
# EJERCICIO 4: CONVERTIR DECIMAL A BINARIO
# ============================================

def decimal_a_binario(n):
    """Convierte un número decimal a binario usando recursividad."""
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

print("EJERCICIO 4: CONVERSIÓN DECIMAL A BINARIO")
num = int(input("Ingrese un número decimal: "))
print(f"El número {num} en binario es {decimal_a_binario(num)}")

print("\n--------------------------------------------\n")