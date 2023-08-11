"""Dados dos números si el primero es divisible por el segundo intercambiarlos. """

print("Ingrese dos numero.")

numero1 = float(input("(VAR numero1) - Ingrese el primer numero: "))
numero2 = float(input("(VAR numero2) - Ingrese el segundo numero: "))

if ((numero1 % numero2) == 0):
    aux = numero1
    numero1 = numero2
    numero2 = aux

print("VAR numero1: ", numero1)
print("VAR numero2: ", numero2)


    