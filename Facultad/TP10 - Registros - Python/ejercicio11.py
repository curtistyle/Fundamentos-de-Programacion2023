"""
Se tiene una lista de precios con código de artículo, descripción, precio. Se pide: 
    a- lista de precios completa. 
    b- Listado de todos los artículos que empiezan con b. 
    c- Consulta de un precio según el cod. de artículo. 
    d- Cual es el artículo más caro. 
"""

tipo_articulo = { 'codigo' : int, 'descripcion' : str, 'precio' : float }

def insertar():
    articulo = tipo_articulo
    articulo['nombre'] = input("Ingrese el nombre del articulo: ")
    articulo['direccion'] = input("Ingrese la direccion de la articulo: ")
    articulo['telefono'] = input("Ingrese el telefono de la articulo: ")
    return articulo

def cargar(lista : list, tamanio : int):
    indice = 0
    print()
    opc = input(" - ¿Quiere ingresar un articulo? (s/n): ")
    while (( opc.upper() == 'S' ) or (len(lista) < tamanio)):
        print(f" # Libro {indice + 1}")
        articulo = insertar()  
        lista[indice] = articulo
        opc = input(" - ¿Quiere ingresar un articulo? (s/n): ")
        indice += 1
        print()
    if (indice > 0):
        return (indice + 1)
    else:
        return 0