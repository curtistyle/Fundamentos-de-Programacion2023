"""Hallar  el  área  de  un  cuadrado,  cuyos  lados  tienen  la  longitud  de  la  hipotenusa  de  un 
triángulo rectángulo y cuyos catetos son dados."""

from math import sqrt, pow

cateto1 = float(input("Ingrese el cateto menor del triangulo: "))
cateto2 = float(input("Ingrese el cateto mayor del triangulo: "))

hipotenusa = sqrt(pow(cateto1,2)+pow(cateto2,2))

print(f"El area del cuadrado es: {pow(hipotenusa,2):.2f}")

