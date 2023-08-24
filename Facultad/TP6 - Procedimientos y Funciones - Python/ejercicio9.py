""" Escribir una función par tal que indique si un número es par o impar. """

def paridad(numero):
    return int((numero % 2) == 0)

numero = int(input("Ingrese un numero: "))

print("Es par" if (paridad(numero) == 1) else "Es impar")

