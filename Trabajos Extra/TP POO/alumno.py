from nota import Nota
class Alumno:
    def __init__(self,nombreCompleto,legajo,):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def agregarNota(self,catedra,notaExamen):
        nota = Nota()
        self.notas.append(nota(catedra,notaExamen))

    def calcularPromedio(self):
        promedio = 0
        for nota in self.notaExamen:
            promedio += nota
        return promedio