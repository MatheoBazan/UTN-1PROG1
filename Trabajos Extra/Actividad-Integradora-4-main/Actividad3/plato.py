from ingredientes import Ingredientes
class Plato:
    def __init__(self,nombreCompleto,precio,esBebida):
        self.nombreCompleto = nombreCompleto
        self.precio = precio
        self.esBebida = esBebida
        self.ingredientes = []
    
    def agregarIngredientes(self,nombre,cantidad,unidadMedida):
        ingred = Ingredientes(nombre,cantidad,unidadMedida)
        self.ingredientes.append(ingred)

    def mostrarIngredientes(self,ingre):
        print("Nombre       Cantidad        Unidad")
        print(f"{ingre.nombre}     {ingre.cantidad}     {ingre.unidadMedida}")


        