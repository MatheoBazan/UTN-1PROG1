#Ingresás 3 alumnos, cada uno con una tupla de 3 notas, y mostrás su promedio.
alumnos = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese la nota {j+1} de {nombre}: ")) for j in range(3))
    if any(nota > 10 or nota < 0 for nota in notas):
        print("Error: Las notas deben estar entre 0 y 10.")
    else:
        alumnos[nombre] = notas

print("Promedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

print("No te enteraste de la ultima actualizacion :D")
