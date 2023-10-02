""" Dada  una  matriz  rectangular  realizar  un  programa  que  devuelva  el  mayor  de  los  elementos 
contenidos en ella, considerando solamente aquellos en los cuales la suma de sus subíndices es 
par. Es decir [1,1], [1,3], [1,5] [2,2], etc. """

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


def mostrar_matriz(matriz : list, filas : int, columnas : int):
    """Muestra la matriz en forma de bloque."""
    from colorama import Fore, Style
    for fila in range(0, filas):
        print(f"Fila {fila + 1}:",end="  ")
        for columna in range(0, columnas):
            print(f"{Fore.RED}{matriz[fila][columna]}{Style.RESET_ALL}",end="  ")
        print()
        
def subindeice_par(fila, columna):
    """Retorna `True` si el modulo de los subindice es par, de lo contrario retorna `False`"""
    suma = fila + columna
    if ((suma % 2) == 0):
        return True
    else:
        return False

def determinar_mayor(matriz : list, filas : int, columnas : int):
    """Retorna el elemento `mayor` de los subindices pares de la `matriz`"""
    mayor = [matriz[0][0],[0,0]]
    for fila in range(0, filas):
        for columna in range(0, columnas):
            if ((subindeice_par(fila,columna) == True) and (matriz[fila][columna] > mayor[0])):
                mayor[0] = matriz[fila][columna]
                mayor[1] = [fila,columna]
    return mayor
    

if __name__=="__main__":
    filas = 3
    columnas = 3
    
    matriz = crear_matriz(filas, columnas)
    
    cargar_matriz(matriz, filas, columnas)
    
    mostrar_matriz(matriz, filas, columnas)

    mayor = determinar_mayor(matriz, filas, columnas)

    print(mayor)
    print(f"El elemento mayor es: {mayor[0]}")
    
    
    
