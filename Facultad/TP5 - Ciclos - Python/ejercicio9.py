""" Desarrollar un algoritmo que determine en un conjunto de 100 números: 
        a) Cuántos son mayores que 15. 
        b) Cuántos son mayores que 50. 
        c) Cuántos están comprendidos entre 25 y 45. """

contador1 = 0
contador2 = 0
contador3 = 0

for index in range(1,100):
    numero = int(input("Ingrese un numero: "))

    if (numero > 15):
        contador1 += 1
    elif (numero > 50):
        contador2 += 50
    elif (numero  > 25) and (numero < 45):
        contador3 += 1

print(f"Numeros mayores a 15: {contador1}, mayores a 50: {contador2} y comprendidos entre 25 y 45: {contador3}.")

