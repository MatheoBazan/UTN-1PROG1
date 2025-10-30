# ============================================
# EJERCICIO 5: PALABRA PALÍNDROMO
# ============================================

def es_palindromo(palabra):
    """Devuelve True si la palabra es un palíndromo."""
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] != palabra[-1]:
            return False
        return es_palindromo(palabra[1:-1])

print("EJERCICIO 5: COMPROBAR PALÍNDROMO")
palabra = input("Ingrese una palabra: ").lower()
if es_palindromo(palabra):
    print("La palabra es un palíndromo ✅")
else:
    print("La palabra no es un palíndromo ❌")

print("\n--------------------------------------------\n")