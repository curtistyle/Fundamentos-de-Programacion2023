from msvcrt import getwch

vector = []

indice = 0
numero = int(input('ingrese un numero: '))
while (str(numero) != '0'):
    vector[indice] = numero
    indice + 1
    
