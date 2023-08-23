""" Escribir  un  algoritmo  que  permita  leer  una  serie  de  enteros.  Contar  el  Nº  de  valores 
introducidos y su suma. """

# incializar variables
acumulador = 0
contador = 0

numero = int(input("Ingrese un numero (0 para terminar): "))

while(numero != 0):
    contador += 1
    acumulador = acumulador + numero
    numero = int(input("Ingrese un numero: (0 para terminar)"))
    
print(f"Se ingresaron {contador} y la suma de ellos da {acumulador}")


