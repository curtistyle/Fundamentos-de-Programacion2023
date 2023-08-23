""" Dada una lista de valores enteros positivos, hallar cuántos valores mayores que 1.000 hay. 
Si la cantidad es menor que 20 calcular su factorial. """

# inicializar variables
contador = 0
factorial = 1
numero = int(input("Ingrese un numero: "))

while (numero != 0):
    if (numero > 1000):
        contador += 1
    numero = int(input("Ingrese un numero: "))

print(f"Se contaron {contador} numeros mayores a 1000.")

if (contador < 20):
    for n in range(1, contador + 1):
        factorial = factorial * n

print(f"El factorial de {contador} es {factorial}.")