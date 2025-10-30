from nota import Nota
class Alumno:
    def __init__(self,nombreCompleto,legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def agregarNota(self,catedra,notaExamen):
        nota = Nota(catedra,notaExamen)
        self.notas.append(nota)

    def mostrarNotas(self,nota):
        print(f"Catedra: {nota.catedra}")
        print(f"Nota Examen: {nota.notaExamen}")

    def calcularPromedio(self):
        promdio = 0
        valor = 0
        for nota in self.notas:
            if nota.notaExamen:
                promdio += nota.notaExamen
                valor += 1
        promdio = (promdio/valor)
        print(f"La nota promedio del alumno es {promdio:.2f}")
