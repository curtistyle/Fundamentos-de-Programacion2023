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

def media_par(tamanio : int, vector : list):
    acumulador = 0
    for indice in range(0, tamanio, 2):
        acumulador += vector[indice]
    return acumulador


if __name__=="__main__":
    lista_numero = [4,3,1,4,5]
    
    print(len(lista_numero)//2)

