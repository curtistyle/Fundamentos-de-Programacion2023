""" Una empresa de transporte de pasajeros de larga distancia posee micros de 4 categorías y viaja a 
    250 localidades de zonas turísticas del país. No necesariamente todas las temporadas se habilitan 
    las 4 categorías, ni hay viajes a todas las localidades posibles. 
    a- Se dispone de un registro de todos los pasajes vendidos en una temporada consistente en: 
        código de categoría (a, b, c, d y código de destino (1 a 250) y de un listado ordenado por 
        código del nombre de cada localidad de destino. 
        Se pide informar: 
    a- La cantidad de pasajeros por localidad, por categoría.
    b- La cantidad de pasajeros por localidad. 
    c- La cantidad de pasajeros por categoría.  
    d- El nombre de la localidad a la que viajó la mayor cantidad de pasajeros. 
    e- El nombre de la localidad a la que viajó la menor cantidad de pasajeros.  
"""

from msvcrt import getwch
import tableprint as tp

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
        
def agregar_elemento(elemento, x : int, y : int, matriz : list, filas : int, columnas : int):
    opc = ["a","b","c","d"]
    for indice in range(0, len(opc)):
        if y == opc[indice]:
            y = indice

    if ((x >= 0) and (x <= filas)):
        if ((y >= 0) and (y <= columnas)):
            matriz[x][y] = elemento
        else:
            print("Error, `y` fuera de rango.")
    else:
        print("Error, `x` fuera de rango.")

def suma_columnas(matriz : list, filas : int, columnas : int):
    """Retorna una `lista` con la `suma` total de c/u de las columnas de una `matriz`."""
    lista = [0] * columnas
    for columna in range(0, columnas):
        for fila in range(0, filas):  
            lista[columna] += matriz[fila][columna] 
    return lista

def suma_filas(matriz : list, filas : int, columnas):
    """Retorna una `lista` con la `suma` total de c/u de las filas de una `matriz`."""
    lista = [0] * filas
    for fila in range(0, filas):
        for columna in range(0, columnas):
            lista[fila] += matriz[fila][columna]
    return lista

def mayor_matriz(matriz : list, filas : int, columnas : int):
    """Retorna una `lista` con la `posicion` del elemento `mayor` de una `matriz`."""
    mayor = matriz[0][0]
    pos = None
    for fila in range(0, filas):
        for columna in range(0, columnas):
            if (matriz[fila][columna] > mayor):
                mayor = matriz[fila][columna]
                pos = [fila, columna]
    return pos

def menor_matriz(matriz : list, filas : int, columnas : int):
    """Retorna una `lista` con la `posicion` del elemento `menor` de una `matriz`."""
    menor = matriz[0][0]
    pos = None
    for fila in range(0, filas):
        for columna in range(0, columnas):
            if (matriz[fila][columna] < menor):
                menor = matriz[fila][columna]
                pos = [fila, columna]
    return pos

if __name__=="__main__":
        
    opc = ["a","b","c","d","A","B","C","D"]

    FILAS = 10 # cantidad de localidades.
    COLUMNAS = 4 # cantidad de categorias.

    matriz = crear_matriz(FILAS, COLUMNAS, "-")


    while True:
        print("Quiere agregar un nuevo item? (s/n): ")
        item = getwch()
        if ((item == 's') or (item == 'S')):
            print("Ingrese una categoria (a,b,c,d): ")
            categoria = getwch()
            if categoria in opc:
                destino = int(input(f"CAT {categoria.upper()} - Ingrese el codigo de destino: "))
                if ((destino > 0 ) and (destino < FILAS)):
                    elemento = int(input("Ingrese la cantidad de pasajes que se vendieron: "))
                else:
                    print("rango de detino incorrecto")
                    break
            else:
                print("rango de categoria incorrecto")
                break
        else:
            break
        agregar_elemento(elemento, destino -1, categoria, matriz, FILAS, COLUMNAS)
        
    mostrar_matriz(matriz, FILAS, COLUMNAS)
    headers = ['CAT A', 'CAT B', 'CAT C', 'CAT D']
    tp.table(matriz, headers)


        
        