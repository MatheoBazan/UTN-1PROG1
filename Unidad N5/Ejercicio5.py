#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#numeros = [8, 15, 3, 22, 7]
#Lo primero que vemos es que se crea una lista con cinco números

#numeros.remove(max(numeros))
#Luego utiliza la función max() que devuelve el valor máximo dentro de esa lista
#adentro de un numeros.remove() que lo que hace es eliminar ese número de la lista.

#Luego utiliza un print(numeros) que imprime la nueva lista
#en este caso imprime [8, 15, 3, 7]