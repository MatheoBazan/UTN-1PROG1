# 19) Cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un atributo de nombre operación.
# Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente:

# sumarNumeros()
# restarNumeros()
# multiplicarNumeros()
# dividirNumeros()

#El quinto método será el siguiente:
#aplicarOperacion(operacion){
#…………………..}

# Cree una clase Calculo que contenga un método main, donde cree una instancia de la
# clase OperacionMatematica, asigne 2 valores para las variables de la instancia y
# ejecute la función aplicarOperacion, pasando como parámetro primero “+”, después “-
# ”, a continuación “*” y finalmente “/”. Muestre por pantalla el resultado de las operaciones. 

class OperacionMatematica:
    def __init__(self, valor1=0, valor2=0):
        self.valor1 = valor1
        self.valor2 = valor2
        self.operacion = ""  # atributo para almacenar la operación actual

    # Métodos básicos
    def sumarNumeros(self):
        return self.valor1 + self.valor2

    def restarNumeros(self):
        return self.valor1 - self.valor2

    def multiplicarNumeros(self):
        return self.valor1 * self.valor2

    def dividirNumeros(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: División por cero"

    # Método para aplicar la operación indicada
    def aplicarOperacion(self, operacion):
        self.operacion = operacion
        if operacion == "+":
            return self.sumarNumeros()
        elif operacion == "-":
            return self.restarNumeros()
        elif operacion == "*":
            return self.multiplicarNumeros()
        elif operacion == "/":
            return self.dividirNumeros()
        else:
            return "Operación no válida"

# ---------------- Clase principal ----------------
class Calculo:
    @staticmethod
    def main():
        # Crear instancia
        op = OperacionMatematica()

        # Asignar valores
        op.valor1 = float(input("Ingrese el primer valor: "))
        op.valor2 = float(input("Ingrese el segundo valor: "))

        # Aplicar varias operaciones
        print("Suma:", op.aplicarOperacion("+"))
        print("Resta:", op.aplicarOperacion("-"))
        print("Multiplicación:", op.aplicarOperacion("*"))
        print("División:", op.aplicarOperacion("/"))

# Ejecutar el main
if __name__ == "__main__":
    Calculo.main()