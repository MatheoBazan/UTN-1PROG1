# Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # solo hasta la raíz cuadrada
        if n % i == 0:
            return False
    return True

# Ingreso de lista por teclado
numeros = list(map(int, input("Ingresa números separados por espacio: ").split()))

# Filtrar los primos usando list comprehension
primos = [n for n in numeros if es_primo(n)]

print("Números primos encontrados:", primos)
