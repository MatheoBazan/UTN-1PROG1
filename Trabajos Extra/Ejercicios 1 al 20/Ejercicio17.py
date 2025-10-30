# 17) Cree una clase FuncionesPrograma y codifique una función estática getFechaString que reciba como parámetro una fecha y retorne la fecha como
# una cadena literal. Ejemplo recibo 15/10/1900, la salida debe ser, Quince de Octubre de mil novecientos. Cree una clase Principal que contenga un
# método main y haga uso de la función getFechaString.

from datetime import datetime

class FuncionesPrograma:

    @staticmethod
    def getFechaString(fecha):

        dias_literal = {
            1: "Uno", 2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco",
            6: "Seis", 7: "Siete", 8: "Ocho", 9: "Nueve", 10: "Diez",
            11: "Once", 12: "Doce", 13: "Trece", 14: "Catorce", 15: "Quince",
            16: "Dieciséis", 17: "Diecisiete", 18: "Dieciocho", 19: "Diecinueve",
            20: "Veinte", 21: "Veintiuno", 22: "Veintidós", 23: "Veintitrés",
            24: "Veinticuatro", 25: "Veinticinco", 26: "Veintiséis",
            27: "Veintisiete", 28: "Veintiocho", 29: "Veintinueve",
            30: "Treinta", 31: "Treinta y uno"
        }

        meses_literal = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo",
            6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre",
            11: "Noviembre", 12: "Diciembre"
        }

        # Convertimos la fecha a objeto datetime
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        dia = fecha_dt.day
        mes = fecha_dt.month
        anio = fecha_dt.year

        # Convertimos el año a texto simple (para simplificar)
        anio_literal = FuncionesPrograma.numero_a_texto(anio)

        return f"{dias_literal[dia]} de {meses_literal[mes]} de {anio_literal}"

    @staticmethod
    def numero_a_texto(numero):
        
        # Convierte un número entero a texto (simplificado, hasta 1999 por ejemplo)
        
        unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
        decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
        centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos",
                    "seiscientos", "setecientos", "ochocientos", "novecientos"]

        if numero == 1000:
            return "mil"
        if numero < 1000:
            c = numero // 100
            d = (numero % 100) // 10
            u = numero % 10
            texto = ""
            if c > 0:
                texto += centenas[c] + " "
            if d > 0:
                texto += decenas[d] + " "
            if u > 0:
                texto += unidades[u]
            return texto.strip()
        return str(numero)  # fallback

# Clase Principal que hace uso de la función
class Principal:

    @staticmethod
    def main():
        fecha = input("Ingrese una fecha (dd/mm/yyyy): ")
        fecha_literal = FuncionesPrograma.getFechaString(fecha)
        print("Fecha en texto:", fecha_literal)

# Ejecutamos el main
if __name__ == "__main__":
    Principal.main()