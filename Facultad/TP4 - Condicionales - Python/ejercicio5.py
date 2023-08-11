"""Ingresar un par de valores, emitirlos, y si ambos son positivos, emitir también su promedio."""

print("Ingrese dos numeros.")

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

print("Primer numero: ", numero1)
print("Segundo numero: ", numero2)

if (numero1 > 0) and (numero2 > 0):
    print("su promedio es {2:.f}".format((numero1 + numero2) / 2))


