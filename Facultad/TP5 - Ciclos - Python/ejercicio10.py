""" Obtener un algoritmo que permita calcular la siguiente serie: h(n)=1 + ½ + 1/3 + ... + 1/n """

numero = int(input("Ingrese un numero para daterminar el limite de la serie: "))

acumulador = 1
for index in (1,numero + 1):
    acumulador = acumulador + (1 / index)

print(f"Resultado: {acumulador:.2f}")




