#La librería NumPy se utiliza principalmente para trabajar con arreglos (arrays) 
# multidimensionales y para realizar operaciones matemáticas de manera rápida y eficiente.
#Los arrays de NumPy son más eficientes en memoria y mucho más rápidos para operaciones numéricas.
#Suma, resta, multiplicación, división, potencias, etc., se pueden hacer elemento por elemento sin necesidad de bucles.
#Puede realizar raíces cuadradas, trigonometría, logaritmos, estadísticas, álgebra lineal.
#Está optimizada en C, lo que hace que sea muchísimo más rápida que las listas de Python.

import numpy as np

# Crear un array
a = np.array([2, 4, 6, 8])
print(a * 2)
print(a + 5) 
print(a / 2)
print(a ** 2)