#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Ejemplo:
agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "14:00"): "Clase de Python"
}
dia = input("Día: ")
hora = input("Hora: ")
if (dia, hora) in agenda:
    print("Actividad:", agenda[(dia, hora)])
else:
    print("No hay actividad registrada.")
