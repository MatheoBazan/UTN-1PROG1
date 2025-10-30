# 18) En la clase FuncionesPrograma codifique una método getFechaDate estática que reciba como parámetro 3 valores enteros, día, mes, anio y
# retorne la fecha de tipo date correspondiente. En la clase Principal creada en el punto anterior haga uso de la función getFechaDate.


from datetime import datetime, date

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

        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        dia = fecha_dt.day
        mes = fecha_dt.month
        anio = fecha_dt.year

        anio_literal = FuncionesPrograma.numero_a_texto(anio)

        return f"{dias_literal[dia]} de {meses_literal[mes]} de {anio_literal}"

    @staticmethod
    def numero_a_texto(numero):

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
        return str(numero)

 
    @staticmethod
    def getFechaDate(dia, mes, anio):

        try:
            return date(anio, mes, dia)
        except ValueError:
            print("Fecha inválida")
            return None


class Principal:

    @staticmethod
    def main():
        # Ejemplo con getFechaString
        fecha_str = input("Ingrese una fecha (dd/mm/yyyy): ")
        print("Fecha en texto:", FuncionesPrograma.getFechaString(fecha_str))

        # Ejemplo con getFechaDate
        dia = int(input("Ingrese día: "))
        mes = int(input("Ingrese mes: "))
        anio = int(input("Ingrese año: "))
        fecha_obj = FuncionesPrograma.getFechaDate(dia, mes, anio)
        if fecha_obj:
            print("Fecha como objeto date:", fecha_obj)

# Ejecutamos el main
if __name__ == "__main__":
    Principal.main()