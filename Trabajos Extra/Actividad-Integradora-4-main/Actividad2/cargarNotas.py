from alumno import Alumno
class cargarNotas:
    def __init__(self):
        self.alumnos = []
    
    def validarLegajo(self,legajo):
        for alumno in self.alumnos:
            if alumno.legajo == legajo:
                return True
        else:
            return legajo 
    
    def mostrarAlumno(self,alumno):
        print(f"Nombre completo: {alumno.nombreCompleto}")
        print(f"Legajo: {alumno.legajo}")
        for nota in alumno.notas:
            alumno.mostrarNotas(nota)
        alumno.calcularPromedio()


def main():
    cargar = cargarNotas()
    while True:
        num = 1
        opcion = input("Cargar Datos de Alumnos(ingrese cualquier tecla)\ns-Salir\n").lower()
        if opcion == "s":
            print("Hasta luego")
            break
        else:
            print(f"Ingrese los datos del alumno {num}")
            alumno = cargarDatosAlumno(cargar)
            print("Ahora se cargaran todas las notas del alumno")
            notasAlumno(alumno,cargar)
            num += 1

def cargarDatosAlumno(cargar):
    while True:
        nombre = input("Ingrese el nombre completo del Alumno: ").replace(" ","")
        if not nombre.isalpha():
            print("Ingrese el nombre nuevamente sin caracteres o numeros")
        else:
            while True:
                try:
                    legajo = int(input("Ingrese el legajo del alumno: "))
                    if len(str(legajo)) != 5:
                        print("Error, el legajo debe tener 5 numeros")
                    else:
                        legajo = cargar.validarLegajo(legajo)
                        if legajo == True:
                            print("Error, este legajo ya existe vuelva a ingresar otro legajo")
                        else:
                            alumno = Alumno(nombre,legajo)
                            return alumno
                except:
                    print("Error, ingrese numeros no letras ni caracteres")

def notasAlumno(alumno,cargar):
    while True:
        materia = input("Ingrese el nombre de la Materia: ").replace(" ","")
        if not materia.isalpha():
            print("Ingrese el nombre nuevamente sin caracteres o numeros")
        else:
            while True:
                try:
                    nota = float(input("Ingrese la nota del alumno: "))
                    if 1 <= nota <= 10:
                        alumno.agregarNota(materia,nota)
                        break
                    else:
                        print("Error, la nota debe de ser entre 1 y 10 no mas ni menos")
                except:
                    print("Error, ingrese numeros no letras ni caracteres")
        opcion = input("Si desea salir ingrese s, sino seleccione cualquier tecla: ").lower()
        if opcion == "s":
            cargar.mostrarAlumno(alumno)
            cargar.alumnos.append(alumno)
            break


if __name__ == "__main__":
    main()