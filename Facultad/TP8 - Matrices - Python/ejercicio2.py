""" Se  tiene  una  empresa  con  20  sucursales  que  vende  distintos  tipos  de  artículos  (30).  Se  desea 
acumular cantidad de ventas por sucursal y por artículo. """


def cargar_matriz(matriz : list, filas, columnas):
    for i in range(0, filas):
        print(f"Ingrese los articulos de la sucursal {i+1}: ")
        for j in range(0, columnas):
            matriz[i][j] = int(input(f"Articulo {j+1}: "))
        print()

def ventas_sucursal(matriz : list, columnas, sucursal):
    ventas = 0
    for columna in range(0, columnas):
        ventas += matriz[sucursal -1][columna]
    return ventas

def ventas_articulos(matriz : list, filas, articulo):
    ventas = 0
    for fila in range(0, filas):
        ventas += matriz[fila][articulo - 1] 
    return ventas


if __name__=='__main__':
    sucursal1 = [0,0,0]
    sucursal2 = [0,0,0]

    lista = [
        sucursal1,
        sucursal2
    ]

    filas = len(lista)
    columnas = len(lista[0])

    cargar_matriz(lista, filas, columnas)

    print()
    print(f"La Sucursal 1 vendio {ventas_sucursal(lista, columnas, 1)}." )
    print(f"La Sucursal 2 vendio {ventas_sucursal(lista, columnas, 2)}." )
    print()
    print(f"Se vendieron {ventas_articulos(lista, filas, 1)} del Articulo 1.")
    print(f"Se vendieron {ventas_articulos(lista, filas, 2)} del Articulo 2.")
    print(f"Se vendieron {ventas_articulos(lista, filas, 3)} del Articulo 3.")
    
    