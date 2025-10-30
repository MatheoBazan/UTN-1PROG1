frase = input("Ingrese una frase: ").lower().split()

palabras_unicas = set(frase)
print("Palabras únicas:", palabras_unicas)

frecuencia = {}
for palabra in frase:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print("Frecuencia de palabras:", frecuencia)
