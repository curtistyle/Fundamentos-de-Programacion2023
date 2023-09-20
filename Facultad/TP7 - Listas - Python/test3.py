def burbuja(lista : list):
    for i in range(0, (len(lista) - 1) - 1):
        for j in range(0,len(lista) - 1 - i):
            if lista[j]>lista[j + 1]:
                aux=lista[j]
                lista[j]=lista[j + 1]
                lista[j + 1]=aux

lista_numeros = [5,3,4,1,2,9,8,7]

burbuja(lista_numeros)

print(lista_numeros)