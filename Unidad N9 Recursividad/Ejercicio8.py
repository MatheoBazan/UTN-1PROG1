# ============================================
# EJERCICIO 8: CONTAR OCURRENCIAS DE UN DÍGITO
# ============================================

def contar_digito(numero, digito):
    """Cuenta cuántas veces aparece un dígito en un número."""
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

print("EJERCICIO 8: CONTAR DIGITOS EN UN NÚMERO")
numero = int(input("Ingrese un número entero: "))
digito = int(input("Ingrese el dígito que desea contar: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}.")

print("\n===== FIN DEL TRABAJO PRÁCTICO 7 =====")