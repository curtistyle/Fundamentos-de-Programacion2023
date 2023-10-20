"""
Se tiene una lista de precios con código de artículo, descripción, precio. Se pide: 
    a- lista de precios completa. 
    b- Listado de todos los artículos que empiezan con b. 
    c- Consulta de un precio según el cod. de artículo. 
    d- Cual es el artículo más caro. 
"""



def insertar():
    articulo = { 'codigo' : int, 'descripcion' : str, 'precio' : float }
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
    
def mostrar( lista : list, tamanio : int ):
    for articulo in range( 0, tamanio ):
        print( f" - Codigo = { lista[articulo]['codigo'] }" )
        print( f" - Descripcion = { lista[articulo]['descripcion'] }" )
        print( f" - Precio = { lista[articulo]['precio'] }", end="\n\n" )    

def mostrar_ocurrencia( lista : list, tamanio : int, campo : int, ocurrencia : str ):
    for articulo in range( 0, tamanio ):
        if lista[articulo][campo][0].upper() == ocurrencia.upper():
            print( f" - Codigo = { lista[articulo]['codigo'] }" )
            print( f" - Descripcion = { lista[articulo]['descripcion'] }" )
            print( f" - Precio = { lista[articulo]['precio'] }", end="\n\n" ) 

def busqueda_binaria(lista : list, tamanio : int, buscado, clave, posicion=None) -> int:
    primero = 0
    ultimo  = tamanio - 1
    while (posicion == None) and (primero <= ultimo):
        medio = (primero + ultimo) // 2
        if (lista[medio][clave] == buscado):
            posicion = medio
        elif (lista[medio][clave] >= buscado):
            ultimo   = medio - 1
        else:
            primero  = medio + 1   
    return posicion

def mayor(lista : list, tamanio : int, campo : str):
    mayor = lista[0][campo]
    for stock in range(0, tamanio):
        if lista[stock][campo] > mayor:
            mayor = lista[stock][campo]
            posicion = stock
    return posicion

def burbuja(lista : list, clave : str) -> None:
    """Metodo de ordenamiento burbuja"""
    for i in range(0,(len(lista)-1)):
        for j in range(0,(len(lista)-1)-i):
            if lista[j][clave] > lista[j+1][clave]:
                aux               = lista[j][clave]
                lista[j][clave]   = lista[j+1][clave]
                lista[j+1][clave] = aux


gondola = [
    { 'codigo' : 1, 'descripcion' : "Papa", 'precio' : 800 },
    { 'codigo' : 2, 'descripcion' : "Tomate", 'precio' : 720 },
    { 'codigo' : 3, 'descripcion' : "Zanahoria", 'precio' : 550 },
    { 'codigo' : 4, 'descripcion' : "Banana", 'precio' : 640 },
    { 'codigo' : 5, 'descripcion' : "Fideos", 'precio' : 300 },
    { 'codigo' : 6, 'descripcion' : "Dulce de Leche", 'precio' : 750 },
    { 'codigo' : 7, 'descripcion' : "Batana", 'precio' : 690 },
    { 'codigo' : 8, 'descripcion' : "Pan", 'precio' : 940 },
    { 'codigo' : 9, 'descripcion' : "Barras de Cereal", 'precio' : 340 },
    ]

ultimo = len( gondola )

    # a- lista de precios completa. 
    # b- Listado de todos los artículos que empiezan con b. 
    # c- Consulta de un precio según el cod. de artículo. 
    # d- Cual es el artículo más caro. 
    
# TODO: a - Lista de precios completa

print( " ***LISTA COMPLETA DE ARTICULOS***" )
mostrar( gondola, ultimo )

# TODO: b- Listado de todos los artículos que empiezan con b. 
print( "***LISTA DE TODOS LOS ARTICULOS QUE EMPIEZAN CON 'B'***" )
mostrar_ocurrencia( gondola, ultimo, 'descripcion', 'b' )

# TODO: c- Consulta de un precio según el cod. de artículo. 

burbuja( gondola, 'codigo' )
buscado = int(input( "Ingrese el cidigo de un articulo: " ))
posicion = busqueda_binaria( gondola, ultimo, buscado, 'codigo' )
print("POS: ", posicion)
print()
if posicion != None:
    print( " # Articulo buscado: " )
    print( f"  Codigo = { gondola[posicion]['codigo'] }.\n"
           f"  Descripcion = { gondola[posicion]['descripcion'] }.\n"
           f"  Precio = { gondola[posicion]['precio'] }.\n" 
         )
else:
    print( f" ¡El articulo buscado cod:{buscado}, no existe! " )
    
# TODO: d- Cual es el artículo más caro.

posicion = mayor( gondola, ultimo, 'precio' )
print( f" # El articulo mas caro es: {gondola[posicion]['descripcion']} - $ {gondola[posicion]['precio']}." )
