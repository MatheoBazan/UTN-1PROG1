# ============================================
# EJERCICIO 6: SUMA DE DÍGITOS
# ============================================

def suma_digitos(n):
    """Suma todos los dígitos de un número entero."""
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

print("EJERCICIO 6: SUMA DE LOS DÍGITOS")
n = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos de {n} es: {suma_digitos(n)}")

print("\n--------------------------------------------\n")