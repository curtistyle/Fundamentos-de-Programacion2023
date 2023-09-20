def crear_lista(tamanio : int):
    vector = [None] * tamanio
    return vector, tamanio

def cargar_lista_dinamica():
    i = 0
    vector = [0]
    valor = int(input("Ingrese un valor: "))
    vector[i] = valor
    while valor != 0:
        i += 1
        vector[i] = vector[i] + [valor] 
        valor = int(input("Ingrese un numero: "))
        if valor == -1: break
    return vector

def recorrer_lista(tamanio : int, vector : list):
    print("Elementos de la lista: ")
    for indice in range(0, tamanio):
        print(f"{indice=} valor={vector[indice]}")


def burbuja(lista : list):
    for i in range(0, (len(lista) - 1) - 1):
        for j in range(0,len(lista) - 1 - i):
            if lista[j]>lista[j + 1]:
                aux=lista[j]
                lista[j]=lista[j + 1]
                lista[j + 1]=aux

def busqueda_binaria(lista,lim, buscado):
    pos = 0
    pri=0
    ult=len(lista)-1
    while (pos==0) and (pri<=ult):
        med=(pri+ult)//2
        if lista[med]==buscado:
            pos=med
        elif lista[med]>=buscado:
            ult=med-1
        else:
            pri=med+1   
    return(pos)


if __name__=="__main__":
    lista_numeros = [2,5,6,2,3,4,27]

    #lista_numeros = cargar_lista_dinamica()

    burbuja(lista_numeros)

    tamanio = len(lista_numeros)

    recorrer_lista(tamanio, lista_numeros)

    

    if busqueda_binaria(lista_numeros,tamanio,27) != 0 :
        print('El 27 esta en lista')
    else:
        print('el 27 no esta en la lista')
