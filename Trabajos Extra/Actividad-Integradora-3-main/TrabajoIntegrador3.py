def comprobar_existencia():
    try:
        with open("alumnos.txt","r") as alumnos:
            print("Archivo alumnos.txt encontrado, Iniciando Programa")
            for linea in alumnos:
                lista = linea.strip().split(";")
                diccionario = {lista[2]:[lista[0],lista[1],lista[3]]}
            return diccionario
    except FileNotFoundError:
            print("Archivo alumnos.txt no encontrado, creando archivo")
            alumnos = open("alumnos.txt","w")
            alumnos.close()
            print("Archivo creado, Iniciando Programa")
            diccionario = {}
            return diccionario

def menu(diccionario_alumnos):
    while True:
        print("Bienvenido, que desea realizar (ingrese el numero segun lo que desea realizar)")
        try:
            opcion = int(input("1.Ver Alumnos\n2.Agregar Alumno\n3.Generar y mostrar archivo de aprobados\n4.Salir\n"))
            if opcion == 1:
                leer_alumnos() 
            elif opcion == 2:
                agregar_alumno(diccionario_alumnos)
            elif opcion == 3:
                guardar_aprobados()
            elif opcion == 4:
                print("Hasta luego")
                break
            else:
                print(f"Error, no existe ninguna opcion {opcion}, vuelva a intentar")
        except:
            print("Error, ingrese un numero valido")

def leer_alumnos():
    with open("alumnos.txt","r") as alumnos:
        for linea in alumnos:
            lista = linea.strip().split(";")
            if not lista:
                print("No hay alumnos disponibles")
                break
            else:
                print(f"Legajo: {lista[2]} | Nombre: {lista[0]} | Apellido: {lista[1]} | Nota promedio: {lista[3]}")

def agregar_alumno(diccionario):
    while True:
        nombre = input("Ingrese el nombre del alumno ")
        if nombre.isalpha():
            break
        else:
            print("Error, ingrese solo el nombre sin espacios, numeros o caracteres")
    while True:
        apellido = input("Ingrese el apellido del alumno ")
        if apellido.isalpha():
            break
        else:
            print("Error, ingrese solo el apellido sin espacios, numeros o caracteres")
    legajo = validar_existe_alumno(diccionario)
    if legajo is None:
        return
    while True:
        try:
            nota = int(input("Ingrese el promedio del alumno "))
            if 1 <= nota <=10:
                break
            else:
                print("El valor de la nota debe de ser entre 1 y 10")
        except:
            print("Error, debe de ingresar un numero no letras")
    with open("alumnos.txt","a") as alumnos:
        alumnos.write(f"{nombre};{apellido};{legajo};{nota}\n")
    diccionario[legajo] = [nombre,apellido,nota]

def validar_existe_alumno(diccionario):
    while True:
        try:
            opcion = input("Ingrese el numero de legajo del alumno, debe de ser de 5 cifras, o si desea salir ingrese s o salir ").lower()
            if opcion == "s" or opcion == "salir":
                return
            elif len(str(int(opcion))) == 5:
                if not diccionario:
                    return opcion
                else:
                    for i in diccionario.keys():
                        if opcion == i:
                            print(f"El legajo {opcion} ya existe en el archivo alumnos.txt, no se permite su escritura")
                            break
                    else:
                        return opcion
            else:
                print("Error, el legajo debe de ser de 5 digitos")
        except ValueError:
            print("Error, solo ingrese numeros no letras")

def guardar_aprobados():
    alumnos_aprobados = []
    with open("alumnos.txt","r") as alumnos:
        for linea in alumnos:
            lista = linea.strip().split(";")
            if int(lista[3]) >= 6:
                alumnos_aprobados.append(lista)
    if not alumnos_aprobados:
                print("No hay alumnos aprobados")
                return
    with open("aprobados.txt","w") as aprobados:
            for linea in alumnos_aprobados:
                aprobados.write(f"{linea[0]};{linea[1]};{linea[2]};{linea[3]}\n")
    with open("aprobados.txt","r") as aprobados:
        print("Lista de los alumnos aprobados")
        for linea in aprobados:
            lista = linea.strip().split(";")
            print(f"Legajo: {lista[2]} | Nombre: {lista[0]} | Apellido: {lista[1]} | Nota promedio: {lista[3]}")

diccionario_alumnos = comprobar_existencia()
menu(diccionario_alumnos)