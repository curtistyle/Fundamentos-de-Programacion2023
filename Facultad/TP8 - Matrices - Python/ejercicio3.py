""" Dada una matriz de 5 filas y 10 columnas: 
        A- Escribir el algoritmo necesario para cargar la matriz 
           con valores. 
        B- Determinar la sumatoria de c/u de las columnas. 
        C- Mostrar el mayor valor de c/u 
           de sus columnas. 
        D- Mostrar la posición (F,C) del menor valor de la matriz. """

def crear_matriz(filas, columnas, valor=None):
    """Crea una matriz de 'n' `filas` y 'n' `columnas` e inicializa la matriz con x `valor`"""
    if ((filas > 0) and (columnas > 0)):
        matriz = []
        for fila in range(filas):
            matriz = matriz + [[]]
            for columna in range(columnas):
                matriz[fila] = matriz[fila] + [valor]
        return matriz
    else:
        return None
    
def cargar_matriz(matriz, filas, columnas):
    """Carga una matriz recorriendola por `fila`"""
    for fila in range(filas):
        print(f"Ingrese las valores de la fila {fila + 1}: ")
        for columna in range(columnas):
            matriz[fila][columna] = int(input(f"Columna {columna + 1}: "))
        print()


def mostrar_matriz(matriz : list, filas, columnas):
    """Muestra la matriz en forma de bloque"""
    for fila in range(0, filas):
        concatenar_fila = f"Fila {fila + 1}: "
        for columna in range(0, columnas):
            concatenar_fila += str(matriz[fila][columna]) + "  "
        print(concatenar_fila)


def sumatoria_columnas(matriz : list, filas : int, columnas : int):
    """Retorna una `lista` con la sumatoria de cada una de las columnas"""
    lista = [0] * columnas
    for columna in range(0, columnas):
        print()
        for fila in range(0, filas):
            lista[columna] +=  matriz[fila][columna]
    return lista
            
    
if __name__=='__main__':

    filas = 3
    columnas = 3

    lista_2 = crear_matriz(3,3,0)

    lista = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    m  = crear_matriz(3,3,0)
    
    cargar_matriz(m,3,3)
    
    mostrar_matriz(m,3,3)
    
    print(sumatoria_columnas(m,3,3))
    

