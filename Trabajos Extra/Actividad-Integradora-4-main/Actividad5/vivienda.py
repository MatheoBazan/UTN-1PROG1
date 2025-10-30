from habitacion import Habitacion
class Vivienda:
    def __init__(self,calle,numero,manzana,nroCasa,superficieTerreno,):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitacion = []
    
    def agregarHabitacion(self,nombre,metrosCuadrados):
        cuarto = Habitacion(nombre,metrosCuadrados)
        self.habitacion.append(cuarto)


    def getMetrosCuadradosCubiertos(self):
        total = 0
        if not self.habitacion:
            print("No hay datos registrados aun")
            return
        else:
            for metros in self.habitacion:
                total += metros.metrosCuadrados
            if total > self.superficieTerreno:
                print("La superficie cubierta no puede ser mayor a la superficie del terreno")
                return
            else:
                return total