"""Leer el nombre y sueldo de una persona mostrar si este gana más de 30.000 pesos."""

nombre = input("Ingrese el nombre: ")
sueldo = float(input("Ingrese el sueldo: "))

if (sueldo > 30000):
    print(nombre, "gana ", sueldo)
    