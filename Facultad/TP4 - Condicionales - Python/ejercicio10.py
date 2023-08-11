"""Leer tres letras, encontrar y visualizar cuál viene primero en el alfabeto."""

print("Ingrese tres letras.")

letra1 = input("Ingrese la primera letra: ")
letra2 = input("Ingrese la segunda letra: ")
letra3 = input("Ingrese la tercera letra: ")

if (ord(letra1) < ord(letra2)) and ((ord(letra1) < ord(letra3))):
    print("La letra '", letra1, "' viene primero en el alfabeto.")
elif ((ord(letra2) < ord(letra1)) and (ord(letra2) < ord(letra3))):
    print("La letra '", letra2, "' viene primero en el alfabeto.")
else:
    print("La letra '", letra3,"' viene primero en el alfabeto.")
