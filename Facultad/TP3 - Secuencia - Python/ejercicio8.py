""" Escriba un programa que permita el ingreso de un número de tres dígitos y determine si 
es un número Armstrong (ej. 153, 371). Como el número que se ingresa posee 3 dígitos, 
la suma de cada uno de sus dígitos elevado a 3 debe ser igual al número. """

from math import pow

numero = int(input("Ingrese un numero de 3 digitos: "))

digito1 = numero // 100
digito2 = (numero - (digito1 * 100)) // 10
digito3 = (numero - ((digito1 * 100) + (digito2 * 10)))

suma = pow(digito1,3) + pow(digito2,3) + pow(digito3,3)

# print("digito1: ", digito1)
# print("digito2: ", digito2)
# print("digito3: ", digito3)
print("Numero: ", suma)

