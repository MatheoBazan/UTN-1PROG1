listaVocales = ["a","e","i","o","u","á","é","í","ó","ú"]

def vocales (frase):
    suma = 0
    for caracter in frase:
        if caracter in listaVocales:
            suma += 1
    return suma

cadena = input("Ingrese un frase o palabra caulquiera ")
tamanoCadena = len(cadena)
total = vocales(cadena.lower())
print(f"La frase {cadena} tiene {tamanoCadena} caracteres en total y {total} son vocales")