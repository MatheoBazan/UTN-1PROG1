# Ejercicio N10: Invertir las claves y valores de un diccionario.
paises = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Perú": "Lima"}
invertido = {capital: pais for pais, capital in paises.items()}
print(invertido)