"""Dado el número matemático PI, se solicita al usuario que ingrese el valor del radio de una 
circunferencia  y  calcule  y  muestre  por  pantalla  el  área  y  perímetro.  (área  =  PI  *  radio2 
perímetro = 2 * PI * radio. """

from math import pi, pow

radio = float(input("Ingrese el radio de la circunferencia: "))

area = pi * pow(radio,2)
perimetro = 2 * pi * radio

print(f"El area de la circunferencia es: {area:.2f}.")
print(f"El perimetro de la circunferencia es: {perimetro:.2f}.")


