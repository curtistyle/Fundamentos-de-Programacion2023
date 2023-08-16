""" Hacer un programa que lea 100 Números, indique cuáles son múltiplos de 2 y contarlos. """

contador = 0
for index in range(1,5):
    numero = int(input(f"({index}) Ingrese un numero: "))
    
    if ((numero % 2) == 0):
        contador += 1

print("Se contaron ", contador, " numeros multiplos de 2.")