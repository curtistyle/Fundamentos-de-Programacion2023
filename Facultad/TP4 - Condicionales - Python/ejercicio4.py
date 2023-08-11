"""Dados dos números si el primero es divisible por el segundo mostrar un mensaje que así 
lo indique."""

print("Ingrese dos numero: ")
numero1 = float(input("Primer numero: "))
numero2 = float(input("Segundo numero: "))

if ((numero1 % numero2) == 0):
    print("El ", numero1, " es divisible por ", numero2,".")

