def factorial(numero):
    factorial = 1
    for index in range(1,numero+1):
        factorial = factorial * index
    return factorial

numero = int(input("Ingrese un numero entero para determinar el factorial: "))

print(f"El factorial de {numero} es: {factorial(numero)}.")



