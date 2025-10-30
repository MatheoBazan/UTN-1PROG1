# 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800
print(precios_frutas)
frutas = list(precios_frutas.keys())
print(frutas)

#El programa debe permitir cargar 5 contactos (clave = nombre, valor = número) y luego consultar uno.
contactos = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero

print("Contactos cargados:")
for nombre, numero in contactos.items():
    print(f"{nombre}: {numero}")

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