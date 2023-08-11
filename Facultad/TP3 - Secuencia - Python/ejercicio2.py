"""Dadas las longitudes de los dos catetos de un triángulo rectángulo, hallar la longitud de la hipotenusa."""

from math import sqrt, pow

cateto1 = float(input("Ingrese la longitud del primer cateto: "))
cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

print("La longitud de la hipotenusa es: ", sqrt(pow(cateto1,2) + pow(cateto2,2)))

# ! resultado = sqrt(pow(cateto1,2) + pow(cateto2,2))
# ! print("La longitud es: {: .2f}".format(resultado))
