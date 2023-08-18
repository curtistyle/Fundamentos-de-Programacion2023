""" Dada una secuencia de caracteres acabada en #, mostrar los números (0..9) que en ella 
aparecen. """

caracter = input("Ingrese un caracter: ")

while (caracter != '#'):
    if (caracter >= '0') and (caracter <= '9'):
        print(f"Caracter: {caracter}")
    caracter = input("Ingrese un caracter: ")
