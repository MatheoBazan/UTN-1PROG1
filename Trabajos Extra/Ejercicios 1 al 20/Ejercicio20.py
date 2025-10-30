# Cree una clase Fracción con dos atributos, numerador y denominador. Agregue a la clase los siguientes 4 métodos e implemente los mismos:

# sumarFracciones(Fraccion f1, Fraccion f2)
# restarFracciones(Fraccion f1, Fraccion f2)
# multiplicarFracciones(Fraccion f1, Fraccion f2)
# dividirFracciones(Fraccion f1, Fraccion f2)

# Todos los métodos deben retornar la fracción resultante de la operación.
# Cree una clase OperacionesFraccion que contenga un método main donde se solicite
# al usuario el ingreso de 4 valores numéricos enteros con los cuales se crearan 2 objetos
# Fracción y finalizada la creación de los mismos se ejecutaran los 4 métodos
# implementados anteriormente asignando el resultado a una nueva variable de tipo
# Fracción y mostrando por pantalla el resultado de las operaciones realizadas. 

# Clase Fracción
class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    # Sumar fracciones (método de instancia)
    def sumarFracciones(self, f2):
        numerador = self.numerador * f2.denominador + f2.numerador * self.denominador
        denominador = self.denominador * f2.denominador
        return Fraccion(numerador, denominador)

    # Restar fracciones
    def restarFracciones(self, f2):
        numerador = self.numerador * f2.denominador - f2.numerador * self.denominador
        denominador = self.denominador * f2.denominador
        return Fraccion(numerador, denominador)

    # Multiplicar fracciones
    def multiplicarFracciones(self, f2):
        numerador = self.numerador * f2.numerador
        denominador = self.denominador * f2.denominador
        return Fraccion(numerador, denominador)

    # Dividir fracciones
    def dividirFracciones(self, f2):
        if f2.numerador == 0:
            raise ValueError("No se puede dividir por una fracción con numerador 0")
        numerador = self.numerador * f2.denominador
        denominador = self.denominador * f2.numerador
        return Fraccion(numerador, denominador)


# ---------------- Clase principal ----------------
class OperacionesFraccion:
    @staticmethod
    def main():
        print("Ingrese los valores para la primera fracción:")
        num1 = int(input("Numerador: "))
        den1 = int(input("Denominador: "))
        f1 = Fraccion(num1, den1)

        print("\nIngrese los valores para la segunda fracción:")
        num2 = int(input("Numerador: "))
        den2 = int(input("Denominador: "))
        f2 = Fraccion(num2, den2)

        suma = f1.sumarFracciones(f2)
        resta = f1.restarFracciones(f2)
        multiplicacion = f1.multiplicarFracciones(f2)
        division = f1.dividirFracciones(f2)

        print("\nResultados:")
        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        print(f"División: {division}")


if __name__ == "__main__":
    OperacionesFraccion.main()
