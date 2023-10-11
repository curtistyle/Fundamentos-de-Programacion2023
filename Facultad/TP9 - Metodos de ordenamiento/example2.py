def burbuja(lista, tamanio):
    for i in range(0,(tamanio-1)):
        for j in range(0,(tamanio-1)-i):
            if lista[j]>lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
                
            
                
def ordenar(lista, tamanio):
    """ Burbuja mejorado """
    for i in range(0, tamanio - 1):
        for j in range(i + 1, tamanio):
            if (lista[i] > lista[j]):
                aux      = lista[i] 
                lista[i] = lista[j]
                lista[j] = aux  
                

lista = [8, 10, 3, 2, 5, 7]
tamanio = len(lista)

print("Lista: ", lista)
print("Tamanio: ", tamanio)

burbuja(lista, tamanio)
print()
lista = [8, 10, 3, 2, 5, 7]
print()
ordenar(lista, tamanio)

print()
print(lista)