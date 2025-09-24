#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
#diferentes clientes: 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"

# c) eliminar "pan" del primer cliente
compras[0].remove("pan")

print(compras)
