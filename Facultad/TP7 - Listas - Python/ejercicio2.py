import types



# lista = [None]



# print(lista)
# i = 0

# print("Ingrese un numero: ")
# numero = int(getwch())
# while (numero !=0):
#     lista[i] = numero
#     print("(1)",lista)
#     numero = int(getwch()) 
#     if (numero != 0):
#         i += 1
#         auxlista = lista
#         print("(2)",auxlista)
#         lista = [None] * (len(lista) + 1)
#         print("(3)",lista)
#         for indice in range(0, len(auxlista)):
#             lista[indice] = auxlista[indice]
#         print("(4)",lista)
        

def cargar_lista_dinamica():
    i = 0
    lista = [None]
    valor = int(input(f"Ingrese un numero en posicion #{i+1}: "))
    while (valor != 0):
        lista[i] = valor
        print(f'{len(lista)=} {lista}')
        valor = int(input(f"Ingrese un numero en posicion #{i+2}: "))
        if (valor != 0):
            i += 1
            aux_lista = lista
            lista = [None] * (len(lista) + 1)
            for indice in range(0, len(aux_lista)):
                lista[indice] = aux_lista[indice]        
    return lista, len(lista)

lista_de_numeros, tamanio = cargar_lista_dinamica()

print(lista_de_numeros)