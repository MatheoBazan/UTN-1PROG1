# ============================================
# EJERCICIO 3: POTENCIA (base^exponente)
# ============================================

def potencia(base, exponente):
    """Calcula la potencia usando recursividad."""
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

print("EJERCICIO 3: POTENCIA")
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

print("\n--------------------------------------------\n")