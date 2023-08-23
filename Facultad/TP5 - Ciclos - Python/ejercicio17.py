""" Construir  un  algoritmo  que,  dada  una  secuencia  de  enteros  acabada  con  el  valor  cero, 
devuelva el mayor de ellos. Determinar cuántos números negativos han aparecido. """

# inicializar variables
mayor = 0
contador = 0

numero = int(input("Ingrese un numero: "))

while (numero != 0):
    if (numero > mayor):
        mayor = numero
    if (numero < 0):
        contador += 1
    numero = int(input("Ingrese un numero: "))
    
print(f"Cantidad de numeros negaticos '{contador}' y el mayor numero que se ingreso '{mayor}'")

