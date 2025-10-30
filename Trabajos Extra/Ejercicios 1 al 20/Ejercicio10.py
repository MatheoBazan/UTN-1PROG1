#10- Convertir una cadena a mayúsculas o minúsculas, daremos opción a que el usuario pida que se desea hacer 
#(convertir a mayúsculas o convertir a minúsculas) y mostrar el resultado por pantalla.
texto = input("Ingresa una cadena: ")
opcion = input("¿Quieres convertir a (M)ayúsculas o (m)inúsculas?: ")

if opcion.lower() == "m":
    print("En minúsculas:", texto.lower())
else:
    print("En mayúsculas:", texto.upper())
