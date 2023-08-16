""" Calcular la suma y el producto de los números pares comprendidos entre 20 y 500. """

from decimal import Decimal

suma = 0
producto = 1
for index in range(20,500):
    if ((index % 2) == 0):
        suma = suma + index
        producto = producto * index


print(f"La suma de los numeros pares comprendidos de 20 a 500 es: {suma} y el producto es: ")
print("{:.3e}".format(Decimal(producto)))
print(f"{Decimal(producto):.3e}")