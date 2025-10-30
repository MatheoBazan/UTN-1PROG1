from alumno import Alumno
class CargarNotas:
    def __init__(self):
        self.alumnos = []

    def validarLegajo(self,nombre,numero):
        for num in self.alumnos:
            if num.legajo == numero:
                print("Este legajo ya existe ingrese, revise el legajo")
                return True
        alumno = Alumno(nombre,numero)
        return alumno
            
    def agregarAlumno(self,alumno):
        self.alumnos.append(alumno)

def cargarAlumno():
    cargar = CargarNotas()
    while True:
        nombre = input("Ingrese el nombre completo del alumno: ")
        if not nombre.replace(" ","").isalpha():
            print("Error, ingrese el nombre completo no caracteres o numeros")
        else:
            break
    while True:
        try:
            numero = int(input("Ingrese el numero de legajo del alumno: "))
            if numero < 0:
                print("El legajo no puede ser negativo, ingrese lo nuevamente")
            elif len(str(numero).replace(" ","")) == 5:
                alumno = cargar.validarLegajo(nombre,numero)
                if alumno == True:
                    continue
                else:
                    cargarNota(alumno,cargar)
                    break
            else:
                print("Error, el legajo debe de ser de 5 numeros")
        except:
            print("Error, el legajo debe de estar compuesto por numeros no por letras")
    
def cargarNota(alumno,cargar):
    while True:
        while True:
            materia = input("Ingrese el nombre de la catedra: ")
            if not materia.replace(" ","").isalpha():
                print("Error, ingrese el nombre de la catedra sin caracteres o numeros")
            else:
                break
        while True:
            try:
                nota = float(input("Ingrese la nota de la catedra: "))
                if nota <= 0 or nota > 10:
                    print("Error, ingrese la nota entre 1 y 10")
                else:
                    alumno.agregarNota(materia,nota)
                    break
            except:
                print("Error, ingrese numeros no letras o caracteres")
        opcion = input("Si no desea seguir cargando notas ingrese s sino ingrese cualquier otra cosa").lower()
        if opcion != "s":
            break
    cargar.agregarAlumno(alumno)

if __name__ == "__main__":
    cargarAlumno()