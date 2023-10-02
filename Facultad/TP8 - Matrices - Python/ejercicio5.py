""" Se tiene una matriz de 150 filas y 12 columnas de celdas reales. Las filas representan 150 clientes 
    y las columnas los 12 meses del año. Cada celda contiene el monto total facturado a cada cliente 
    c/mes. Se pide: 
        A- Mostrar el monto facturado al cliente 142 en el mes de Agosto. 
        B- Mostrar el Nº de cliente que registró el mayor monto de facturación mensual. 
        C- Mostrar en que mes se registró la menor facturación mensual para un cliente. """
        
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
        print(f"Ingrese las valores del cliente {fila + 1}: ")
        for columna in range(columnas):
            matriz[fila][columna] = int(input(f"Mes {columna + 1}: "))
        print()


def mostrar_matriz(matriz : list, filas : int, columnas : int):
    """Muestra la matriz en forma de bloque."""
    from colorama import Fore, Style
    for fila in range(0, filas):
        print(f"Fila {fila + 1}:",end="  ")
        for columna in range(0, columnas):
            print(f"{Fore.RED}{matriz[fila][columna]}{Style.RESET_ALL}",end="  ")
        print()
        

def obtener_elemento(matriz : list, filas : int, columnas : int, indice_x : int, indice_y : int):
    """Retorna el elemento de la matriz"""
    if ((indice_x > 0) and (indice_x <= filas)):
        if ((indice_y > 0) and (indice_y <= columnas)):
            return matriz[indice_x][indice_y]
        else:
            return None
    else:
        return None

def sumatoria_fila(matriz : list, filas : int, columnas : int):
    """Retorna la suma totoal de c/u de las filas."""
    monto_cliente_total = [0] * filas
    for fila in range(0, filas):
        for columna in range(0, columnas):
            monto_cliente_total[fila] += matriz[fila][columna]
    return monto_cliente_total

def mayor_lista_indice(lista : list, filas : int):
    """Retorna la posicion del `elemento` mayor de una `lista`"""
    aux = lista[0]
    posicion = 0
    for indice in range(0, filas):
        if (lista[indice] > aux):
            aux = lista[indice] 
            posicion = indice
    return posicion
            
def mayor_matriz_indice(matriz : list, filas : int, columnas : int):
    """Retorna la `posicion` del mayor elemento de una `matriz`."""
    pos = [0,0]
    aux = matriz[0][0]
    for fila in range(0, filas):
        for columna in range(0, columnas):
            if (matriz[fila][columna] > aux):
                aux = matriz[fila][columna]
                pos = [fila,columna]
    return pos    

def menor_matriz_indice(matriz : list, filas : int, columnas : int):
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
    columnas = 4
    
    # Crea e inicializa la matriz
    matriz = crear_matriz(filas, columnas,0)
    
    # Carga el monto de los cliente
    cargar_matriz(matriz, filas, columnas)
    
    # Muetra la matriz de clientes x mes
    mostrar_matriz(matriz, filas, columnas)
    
    # Muestra el monto de un cliente en un determinado mes.
    # En este caso el Cliente '2' en el Mes '3'.
    cliente = 2
    mes = 3
    monto = obtener_elemento(matriz, cliente, mes)
    
    # Si el cliente y el mes esta dentro del rango de la matriz
    # 'monto' devuelve un resultado (entero, flotante) de lo contrario
    # devuelve un error.
    if (type(str()) != monto):
        print(f"\nEl {cliente} facturo en el mes {mes}: ${monto}.")
    else:
        # ! Muestra el error
        print(monto)
    
    # Calcula el monto total por cliente.
    lista_monto_total = sumatoria_fila(matriz, filas, columnas,)
    
    # ? Determina el numero de cliente (el primero) que vendio mas.
    posicion = mayor_lista_indice(lista_monto_total, filas)
    print(f"\nEl cliente {posicion + 1} facturo mas que los demas.")
    
    # Determina el cliente que factura mas en un mes
    posicion = mayor_matriz_indice(matriz, filas, columnas)
    print(f"\n*** El cliente {posicion[0] + 1} registro la mayor venta. ***")
    # ? Otro dato: 
    print(f"- En el mes: {posicion[1] + 1}. Monto: ${matriz[posicion[0]][posicion[1]]}")
    
    # Determina en que mes se registro la menor facturacion
    posicion = menor_matriz_indice(matriz, filas, columnas)
    print(f"\nEl mes en el que se registro la menor facturacion es: Mes {posicion[1]}")
    
    