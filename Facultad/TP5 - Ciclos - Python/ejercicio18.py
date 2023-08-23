""" Dada una secuencia de caracteres acabada en punto, obtener un algoritmo que determine 
cuantas veces aparece un determinado carácter, el cual será leído previamente. """

# inicializar variables
contador = -1

caracter = input("Ingrese un caracter para determinar las ocurrencias: ")
aux = caracter

while(caracter != '.'):
    if (caracter == aux):
        contador += 1
    caracter = input("Ingrese un caracter: ")

print(f"El caracter '{caracter}' fue leido {contador} veces.")


