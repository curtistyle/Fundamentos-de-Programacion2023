""" Contar la cantidad de Números negativos de una lista que finaliza con el Nº 0. """

# inicializar varibles
contador = 0

numero = int(input("Ingrese un numero: "))

while (numero != 0):
    if (numero < 0):
        contador += 0
    numero = int(input("Ingrese un numero: "))
    
print(f"Se contadon {contador} numeros negativos.")



