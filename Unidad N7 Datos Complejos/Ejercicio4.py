#Ejercicio N4: El programa debe permitir cargar 5 contactos (clave = nombre, valor = número) y luego consultar uno.
contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero
# Fin de carga
print("Contactos cargados:")
for nombre, numero in contactos.items():
    print(f"{nombre}: {numero}")
# Consulta de contactos
consulta = input("Ingrese el nombre del contacto a consultar: ")
salir=0
if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")
    while salir==0:
        opcion=input("Desea consultar otro contacto? (s/n): ")
        if opcion.lower()=='s':
            consulta = input("Ingrese el nombre del contacto a consultar: ")
            if consulta in contactos:
                print(f"El número de {consulta} es {contactos[consulta]}")
            else:
                print("Contacto no encontrado.")
        elif opcion.lower()=='n':
            salir=1
        else:
            print("Opción no válida. Por favor ingrese 's' o 'n'.")
else:
    print("Contacto no encontrado.")
