from random import randint

for index in range(0, 5):
    numero = randint(0,100)
    print(numero)

def crear_matriz(filas : int, columnas : int, valor=None):
    """Crea una matriz de 'n' `filas` y 'n' `columnas` e inicializa la matriz con x `valor`."""
    if ((filas > 0) and (columnas > 0)):
        matriz = []
        for fila in range(filas):
            matriz = matriz + [[]]
            for columna in range(columnas):
                matriz[fila] = matriz[fila] + [valor]
        return matriz
    else:
        return None
    
def mostrar_matriz(matriz : list, filas : int, columnas : int):
    """Muestra la matriz en forma de bloque."""
    from colorama import Fore, Style
    for fila in range(0, filas):
        print(f"Fila {fila + 1}:",end="  ")
        for columna in range(0, columnas):
            print(f"{Fore.RED}{matriz[fila][columna]}{Style.RESET_ALL}",end="  ")
        print()


def cargar_matriz_random(matriz : list, filas : int, columnas : int):
    for fila in range(0, filas): 
        for columna in range(0, columnas):
            matriz[fila][columna] = randint(0, 100)

def burbuja(lista):
    for i in range(0,(len(lista)-1)):
        for j in range(0,(len(lista)-1)-i):
            if lista[j]>lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux

def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

def burbuja_matriz(matriz : list, filas : int, columnas : int):
    for fila in range(0, filas):
        burbuja(matriz[fila])



if __name__=="__main__":

    FILAS = 3
    COLUMNAS = 4

    matriz = crear_matriz(FILAS, COLUMNAS)

    cargar_matriz_random(matriz, FILAS, COLUMNAS)

    print("Desordenado: ")
    mostrar_matriz(matriz, FILAS, COLUMNAS)

    print()

    burbuja_matriz(matriz, FILAS, COLUMNAS)

    print("Ordenado: ")
    mostrar_matriz(matriz, FILAS, COLUMNAS)