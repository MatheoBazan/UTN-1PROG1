# ============================================
# EJERCICIO 7: PIRÁMIDE DE BLOQUES
# ============================================

def contar_bloques(n):
    """Devuelve el total de bloques necesarios para construir la pirámide."""
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print("EJERCICIO 7: PIRÁMIDE DE BLOQUES")
nivel = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(nivel)}")

print("\n--------------------------------------------\n")