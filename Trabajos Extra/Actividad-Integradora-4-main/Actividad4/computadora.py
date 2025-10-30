from componenteCPU import ComponenteCPU
class Computadora:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.listaComponentesCPU = []

    def agregarComponentes(self,componente,marca,cantidad,precio):
        comp = ComponenteCPU(componente,marca,cantidad,precio)
        self.listaComponentesCPU.append(comp)

    def mostrarComponentes(self,comp):
        subTotal = comp.precio * comp.cantidad
        print(f"{comp.componente}   {comp.marca}    {comp.cantidad}     {comp.precio}       {subTotal}")
        return subTotal
        
        