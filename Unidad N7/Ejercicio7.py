#Alumnos que aprobaron ambos parciales, solo uno de los parciales y al menos uno de los parciales
parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}

print("Ambos:", parcial1 & parcial2)
print("Solo uno:", parcial1 ^ parcial2)
print("Al menos uno:", parcial1 | parcial2)
