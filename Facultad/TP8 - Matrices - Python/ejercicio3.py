""" Dada una matriz de 5 filas y 10 columnas: 
        A- Escribir el algoritmo necesario para cargar la matriz 
           con valores. 
        B- Determinar la sumatoria de c/u de las columnas. 
        C- Mostrar el mayor valor de c/u 
           de sus columnas. 
        D- Mostrar la posición (F,C) del menor valor de la matriz. """

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
    
def cargar_matriz(matriz : list, filas : int, columnas : int):
    """Carga una matriz recorriendola por `fila`."""
    for fila in range(filas):
        print(f"Ingrese las valores de la fila {fila + 1}: ")
        for columna in range(columnas):
            matriz[fila][columna] = int(input(f"Columna {columna + 1}: "))
        print()


def mostrar_matriz(matriz : list, filas, columnas):
    """Muestra la matriz en forma de bloque."""
    # ! COLORAMA
    from colorama import Fore, Style
    for fila in range(0, filas):
        print(f"Fila {fila + 1}:",end="  ")
        for columna in range(0, columnas):
            print(f"{Fore.RED}{matriz[fila][columna]}{Style.RESET_ALL}",end="  ")
        print()


def sumatoria_columna(matriz : list, filas : int, columnas : int):
    """Retorna una `lista` con la sumatoria de cada una de las columnas."""
    lista = [0] * columnas
    for columna in range(0, columnas):
        for fila in range(0, filas):
            lista[columna] +=  matriz[fila][columna]
    return lista
            
def mayor_columna(matriz : list, filas : int, columnas : int):
    """Retorna una `lista` con los elementos mayores de cada una de las columnas."""
    lista = [0] * columnas
    lista[0] = matriz[0][0]
    for columna in range(0, columnas):
        for fila in range(0, filas):
            if (matriz[fila][columna] > lista[columna]):
                    lista[columna] = matriz[fila][columna]
    return lista

def menor_matriz(matriz : list, filas : int, columnas : int):
    """Retorna la `posicion` del menor elemento de una `matriz`."""
    pos = [0,0]
    aux = matriz[0][0]
    for fila in range(0, filas):
        for columna in range(0, columnas):
            if (matriz[fila][columna] < aux):
                aux = matriz[fila][columna]
                pos = [fila,columna]
    return pos          
    
if __name__=='__main__':

    filas = 3
    columnas = 3

    lista_2 = crear_matriz(3,3,0)

    lista = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    matriz  = crear_matriz(filas,columnas,0)
    
    cargar_matriz(matriz,3,3)
    
    mostrar_matriz(matriz,3,3)
    
    resultado = sumatoria_columna(matriz, filas, columnas)
    print(f"Sumatoria columna. C1: {resultado[0]}, C2: {resultado[1]}, C3: {resultado[2]}")
    
    resultado = mayor_columna(matriz, filas, columnas)
    print(f"Mayor columna. C1: {resultado[0]}, C2: {resultado[1]}, C3: {resultado[2]}")
    
    resultado = menor_matriz(matriz, filas, columnas)
    print("Posicion menor matriz: ", resultado)
    
    