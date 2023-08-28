""" Leer un vector de 100 Números reales, un componente por vez. Emitir la sumatoria 
de sus componentes. """

import random

lista_de_numero = []
tamanio = 5

# cargar lista
# for indice in range(0,100):
#     numero = random.randint(1,10)
#     #numero = float(input(f"({indice+1}) Ingrese un numero: "))
#     lista_de_numero.append(numero)

lista_de_numero = [None] * tamanio

for indice in range(0,5):
    numero = random.randint(100,20000)
    #numero = float(input(f"({indice+1}) Ingrese un numero: "))
    lista_de_numero[indice] = numero

# mostrar lista

print(f'{"Indice":<15} {"Valor":<15}')
for indice in range(0,len(lista_de_numero)):
    print(f"{(indice+1):>6} {lista_de_numero[indice]:>14}")
