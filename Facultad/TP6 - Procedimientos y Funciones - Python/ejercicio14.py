""" Escribir un procedimiento que permita calcular la suma 1+2+3+ ... + n. """

def acumulador(numero):
    resultado = 1
    for index in range(1,numero + 1):
        resultado = resultado + index

numero = input("Ingrese un numero: ")

print(f"La suma suceciva de los numeros comprendidos de 1 hasta {numero} da como resultado: {acumulador(numero)}.")