from vivienda import Vivienda

class Barrio:
    def __init__(self, nombre, empresaConstructora):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.vivienda = []  # lista de objetos Vivienda

    def getSuperficieTotalTerreno(self):
        if not self.vivienda:
            return 0
        total = sum(v.superficieTerreno for v in self.vivienda)
        return total

    def getSuperficieTotalTerrenoXManzana(self, manzana):
        if not self.vivienda:
            return 0
        total = sum(v.superficieTerreno for v in self.vivienda if v.manzana == manzana)
        return total

    def obtenerNumeroCasa(self, numero):
        for casa in self.vivienda:
            if casa.nroCasa == numero:
                return casa.getMetrosCuadradosCubiertos()
        return None

    def getSuperficieTotalCubierta(self):
        if not self.vivienda:
            return 0
        total = 0
        for casa in self.vivienda:
            superficie = casa.getMetrosCuadradosCubiertos()
            if superficie:
                total += superficie
        return total
