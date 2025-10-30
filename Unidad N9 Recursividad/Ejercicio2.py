# ============================================
# EJERCICIO 2: SERIE DE FIBONACCI
# ============================================

def fibonacci(n):
    """Devuelve el valor de Fibonacci en la posición n."""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("EJERCICIO 2: SERIE DE FIBONACCI")
n = int(input("Ingrese cuántos términos quiere mostrar: "))

print("Serie de Fibonacci:")
for i in range(n):
    print(fibonacci(i), end=" ")
print("\n\n--------------------------------------------\n")