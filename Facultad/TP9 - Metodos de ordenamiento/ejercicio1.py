""" Hacer un algoritmo que:
        - Lea una lista de números de teclado que culmina con uno negativo.
        - Los ordene en forma creciente y Visualice la lista ordenada.
        - Buscar si existe el Nº 27 en la lista. """

def crear_lista(tamanio : int, valor=None):
    vector = [valor] * tamanio
    return vector, tamanio

def cargar_lista_dinamica(hasta):
    vector = []
    valor = int(input("Ingrese un valor: "))
    while valor != hasta:
        print(vector)
        vector = vector + [valor]
        valor = int(input("Ingrese un valor: "))
    return vector, len(vector)

def cargar_lista(vector, indice=0, hasta=0):
    num = int(input(f"({indice})Ingrese un numero: "))

    while ((num != hasta) and (indice < len(vector))):
        vector[indice] = num
        indice += 1
        num = int(input(f"({indice})Ingrese un numero: "))
    return indice

def recorrer_lista(tamanio : int, vector : list):
    print("Elementos de la lista: ")
    for indice in range(0, tamanio):
        print(f"{indice=:<8} valor={vector[indice]:<8}")


def burbuja(lista : list):
    for i in range(0, (len(lista) - 1) - 1):
        for j in range(0, len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                aux          = lista[j]
                lista[j]     = lista[j + 1]
                lista[j + 1] = aux

def busqueda_binaria(lista, tamanio, buscado, posicion=0):
    primero = 0
    ultimo  = tamanio - 1
    while (posicion == 0) and (primero <= ultimo):
        medio = (primero + ultimo) // 2
        if (lista[medio] == buscado):
            posicion = medio
        elif (lista[medio] >= buscado):
            ultimo   = medio - 1
        else:
            primero  = medio + 1   
    return posicion


if __name__=="__main__":
    lista_numeros = []

    lista_numeros, tamanio = cargar_lista_dinamica(-1)

    burbuja(lista_numeros)

    # tamanio = len(lista_numeros)

    recorrer_lista(tamanio, lista_numeros)

    if busqueda_binaria(lista_numeros, tamanio, 27) != 0 :
        print('El 27 esta en lista')
    else:
        print('El 27 no esta en la lista')
