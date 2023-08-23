""" Dada una lista de valores numéricos, hallar su rango, es decir la diferencia entre su valor 
máximo y su valor mínimo """

# inicializar variables
maximo = 0
minimo = 0

numero = int(input("Ingrese un numero: "))
minimo = numero

while (numero != 0):
    if (numero > maximo):
        maximo = numero
    if (numero < minimo):
        minimo = numero
    numero = int(input("Ingrese un numero: "))

print(f"El maximo numero ingresado es {maximo}, el minimo {minimo} y su diferencia es {maximo - minimo}.")