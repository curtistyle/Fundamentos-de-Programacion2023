""" Imprimir la media de los elementos que se encuentran en las posiciones pares y la media 
de los elementos que se encuentran en las posiciones impares de un vector numérico.  """

def crear_lista(tamanio : int):
    vector = [None] * tamanio
    return vector, tamanio

def cargar_lista(tamanio : int, vector : list):
    for indice in range(0, tamanio):
        vector[indice] = int(input(f"Ingrese un elemento en la posicion #{indice+1}: "))

def recorrer_lista(tamanio : int, vector : list):
    print("Elementos de la lista: ")
    for indice in range(0, tamanio):
        print(f"{indice=} valor={vector[indice]}")

def paridad(tamanio : str):
    if (tamanio%2) == 0:
        par = tamanio // 2
        impar = par
    else:
        impar = tamanio // 2
        par = impar + 1
    return par, impar


def media_par(tamanio : int, vector : list):
    acumulador = 0
    for indice in range(0, tamanio, 2):
        acumulador += vector[indice]
    a, b = paridad(tamanio)   
    return acumulador / a


if __name__=="__main__":
    lista_numero = [4,3,4,4,4,3]
    # par: 0, 2 impar: 1, 3
    # print((len(lista_numero)//2))

    # if (len(lista_numero)%2) == 0:
    #     par = len(lista_numero)//2
    #     impar = par
    #     print(f"{par=} {impar=}")
    # else:
    #     impar = len(lista_numero)//2
    #     par = impar + 1
        
    #     print(f"{par=} {impar=}")

    print(media_par(6,lista_numero))