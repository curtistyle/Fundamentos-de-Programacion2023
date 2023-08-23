""" Diseñar una función que calcule potencias de forma xn y un programa que haga uso de la 
misma, para distintos valores de x y n. """

from math import pow

def potencia(numero,pot):
    return pow(numero,pot)

numero = float(input("Ingrese un numero: "))
pot = int(input("Ingrese la potencia: "))

print(f"La potencia {pot} de {numero} da: {potencia(numero,pot):.2f}.")



