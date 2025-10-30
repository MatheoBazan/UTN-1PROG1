# 16) Codifique un método que reciba como parámetro una cadena y determine si la misma contiene o no números

contraseña = input("Ingresa una contraseña: ")

def contiene_numeros(cadena):
    for caracter in cadena:
        if caracter.isdigit():  # verifica si el caracter es un dígito
            return True
    return False

if contiene_numeros(contraseña):
    print("La contraseña contiene números.")
else:
    print("La contraseña NO contiene números.")