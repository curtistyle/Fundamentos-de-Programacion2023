""" Sumar los elementos que están en la diagonal principal de una matriz dada. """

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
        
def cargar_matriz(matriz : list, filas : int, columnas : int):
    """Carga una matriz recorriendola por `fila`."""
    for fila in range(filas):
        print(f"Fila {fila + 1}. ")
        for columna in range(columnas):
            matriz[fila][columna] = int(input(f" - Columna {columna + 1}: "))
        print()

def suma_diagonal_principal(matriz : list, filas : int, columnas : int):
    """Retorna la suma de los elementos de la diagonal principal de una `matriz`"""
    sumatoria = 0
    if columnas < filas:
        print("A")
        for columna in range(0, columnas):
            sumatoria += matriz[columna][columna]
    else:
        print("B")
        for fila in range(0, filas):
            sumatoria += matriz[fila][fila]
    return sumatoria

if __name__=="__main__":
    
    FILAS = 3
    COLUMNAS = 4
    
    matriz = crear_matriz(FILAS, COLUMNAS)
    
    cargar_matriz(matriz, FILAS, COLUMNAS)
    
    mostrar_matriz(matriz, FILAS, COLUMNAS)
    
    resultado = suma_diagonal_principal(matriz, FILAS, COLUMNAS)
    
    print(f"La suma de los elementos de la diagonal principal da como resultado: {resultado}")
    
    