"""
Se tiene una lista de los inscriptos a un concurso de canto. De cada uno se 
tiene: apellido y nombre, edad, canción que interpretará y autor de la 
misma.
Se pide:
    A – Definir la estructura necesaria para representar el problema y cargarla 
        con los datos de cada concursante.
    B - Calcular promedio de edad de los concursantes.
    C - Crear una lista con los concursantes menores de 18 años.
    D - Listado ordenado por apellido y nombre de todos los concursantes.
    E – Determinar si existe al menos una canción cuya autora es Adele.
    F - Listado ordenado por autores de las canciones que se interpretarán.
    G - Determinar porcentaje de menores a 18 años sobre el total
"""



from msvcrt import getwch
from colorama import Fore, Style
from os import system

limpiar = system

def insertar():
    inscriptos = { 'nombre' : str, 'apellido' : str, 'edad' : int, 'cancion' : str, 'autor' : str }
    inscriptos['nombre'] = input( "Ingrese el nombre: " )
    inscriptos['apelldio'] = input( "Ingrese el apellido: " )
    inscriptos['edad'] = int( input( "Ingrese la edad: " ) )
    inscriptos['cancion'] = input( "Ingrese la cancion que interpretara: " )
    inscriptos['autor'] = input("Ingrese el autor de la cancion que interpreta: ") 
    return inscriptos

def cargar(lista : list, tamanio : int, ultimo : int):
    indice = 0
    if ultimo > 0:
        indice = ultimo
    
    print( " - ¿Quiere ingresar un participante? (s/n): " )
    opc = getwch()
    limpiar("cls")
    while (( opc.upper() == 'S' ) or (len(lista) < tamanio)):
        print(f" # inscriptos {indice + 1}")
        inscriptos = insertar()  
        lista[indice] = inscriptos
        limpiar("cls")
        print( " - ¿Quiere ingresar un participante? (s/n): " )
        opc = getwch()
        limpiar("cls")
        indice += 1
        print()
    if (indice > 0):
        return (indice)
    else:
        return -1
    
def mostrar( lista : list, ultimo : int ):
    for persona in range( 0, ultimo ):
        print( 
            f" - Nombre: {lista[persona]['nombre']}\n"
            f" - Apellido: {lista[persona]['apellido']}\n"
            f" - Edad: {lista[persona]['edad']}\n"
            f" - Cancion: {lista[persona]['cancion']}\n"
            f" - Autor: {lista[persona]['autor']}\n\n")
    input()
    
    limpiar("cls")

def promedio( lista : list, tamanio : int, campo : str ):
    acumulador = 0
    for item in range(0, tamanio):
        acumulador += lista[ item ][ campo ]
    return acumulador / tamanio

def determinar_menores( lista1 : list, lista2 : list, ultimo : int ):
    menores = 0
    for participante in range( 0, ultimo ):
        if lista1[participante]['edad'] < 18:
            lista2[ menores ] = lista1[ participante ]
            menores += 1
    return menores

def burbuja_personalizado( lista : list, ultimo : int, parametros : list ):
    for i in range(ultimo - 1):
        for j in range(ultimo - 1 - i):
            elemento_actual = ''
            elemento_siguiente = ''
            for campo in range( 0, len( parametros ) ): 
                elemento_actual += lista[ j ][ parametros[ campo ] ]
            for campo in range( 0, len( parametros ) ): 
                elemento_siguiente += lista[ j + 1 ][ parametros[ campo ]  ]
            if elemento_actual > elemento_siguiente:
                aux = lista[ j ]
                lista[ j ] = lista[ j + 1 ]
                lista[ j + 1 ] = aux

def busqueda_binaria(lista : list, tamanio : int, buscado, clave ):
    primero  = 0
    ultimo   = tamanio - 1
    posicion = None
    while (posicion == None) and (primero <= ultimo):
        medio = (primero + ultimo) // 2
        if (lista[medio][clave] == buscado):
            posicion = medio
        elif (lista[medio][clave] >= buscado):
            ultimo   = medio - 1
        else:
            primero  = medio + 1   
    return posicion    

def contar( lista : int, ultimo : int, campo : str, ocurrencia ):
    contador = 0
    for indice in range( 0, ultimo ):
        if lista[ indice ][ campo ] < ocurrencia:
            contador += 1
    return contador    

def porcentaje( total, cantidad ):
    return ( ( cantidad * 100 ) / total )

lista = [
    { 'nombre' : "Ana", 'apellido' : "Sánchez", 'edad' : 14, 'cancion' : "She", 'autor' : "Green Day" },
    { 'nombre' : "Marta", 'apellido' : "Díaz", 'edad' : 16, 'cancion' : "Em A Evil?", 'autor' : "Metallica" },
    { 'nombre' : "Alejandro", 'apellido' : "Pérez", 'edad' : 18, 'cancion' : "Peace Sells", 'autor' : "Megadeth" },
    { 'nombre' : "Raúl", 'apellido' : "González", 'edad' : 23, 'cancion' : "Song 2", 'autor' : "Blur" },
    { 'nombre' : "Julia", 'apellido' : "García", 'edad' : 24, 'cancion' : "School", 'autor' : "Nirvana" },
    { 'nombre' : "Nuria", 'apellido' : "López", 'edad' : 19, 'cancion' : "Welcome to Paradice", 'autor' : "Green Day" },
    { 'nombre' : "Sandra", 'apellido' : "García", 'edad' : 12, 'cancion' : "Hello", 'autor' : "Adele" },
    { 'nombre' : "Jesús", 'apellido' : "García", 'edad' : 15, 'cancion' : "Polly", 'autor' : "Nirvana" },
    { 'nombre' : "Pablo", 'apellido' : "Benitez", 'edad' : 22, 'cancion' : "Revolution is my Name", 'autor' : "Pantera" },
    0,
    0,
    0,
    0,
    0,
    0
]

if __name__=="__main__":

    # ? Tamanio/cantidad de inscriptos de la lista `lista`
    TAMANIO = len(lista)
    # ? Lista con los concursantes menores de edad (edad<18)
    menores = [0] * TAMANIO
    # ? posicion del ultimo inscripto que se agrego
    ultimo = 9

    # TODO: A - Definir la estructura necesaria para representar el problema y cargarla con los datos de cada concursante.
    print( f"{Fore.MAGENTA}A - Cargar participantes.{Style.RESET_ALL}" )
    ultimo = cargar( lista, TAMANIO, ultimo )
    limpiar("cls")

    # TODO: B - Calcular promedio de edad de los concursantes.
    resultado =  promedio( lista, ultimo, 'edad' )
    print( f"{Fore.MAGENTA}B - Promedio de edad de los concursantes.{Style.RESET_ALL}", end="\n\n" )
    print( f"PROMEDIO: {Fore.GREEN}{resultado:.2f}{Style.RESET_ALL}." )
    input()
    limpiar("cls")

    # TODO: C - Crear una lista con los concursantes menores de 18 años.
    print( f"{Fore.MAGENTA}C - Lista con los concursantes menores de 18 años.{Style.RESET_ALL}", end="\n\n" )
    ultimo_menores = determinar_menores( lista, menores, ultimo )
    mostrar( menores, ultimo_menores )


    # TODO: D - Listado ordenado por apellido y nombre de todos los concursantes

    print( f"{Fore.MAGENTA}D - Listado ordenado por apellido y nombre de todos los concursantes.{Style.RESET_ALL}", end="\n\n" )
    burbuja_personalizado( lista, ultimo, [ 'apellido', 'nombre' ] )
    mostrar( lista, ultimo )
    
    # TODO: E – Determinar si existe al menos una canción cuya autora es Adele.

    burbuja_personalizado( lista, ultimo, [ 'autor' ] )
    buscado = input( f"{Fore.MAGENTA}E - Ingrese el nombre de un autor: {Style.RESET_ALL}" )
    posicion = busqueda_binaria( lista, ultimo, buscado, 'autor' )
    if posicion is not None:
        print( f"El autor \'{Fore.GREEN}{lista[posicion]['autor']}{Style.RESET_ALL}\' existe!" )
    else:
        print( f"El autor \'{Fore.RED}{buscado}{Style.RESET_ALL}\' NO existe!" )
    input()
    limpiar("cls")

    # TODO: F - Listado ordenado por autores de las canciones que se interpretarán.

    print( f"{Fore.MAGENTA}F - Listado Ordenado por Autores.{Style.RESET_ALL}", end="\n\n" )
    mostrar( lista, ultimo )

    # TODO: G - Determinar porcentaje de menores a 18 años sobre el total

    cantidad_menores = contar( menores, ultimo_menores, 'edad', 18 )

    print( f"{Fore.MAGENTA}G - Porcentaje de menores de 18 años con respecto al total:{Style.RESET_ALL}" )
    print( f"PORCENTAJE: {Fore.GREEN}{porcentaje( ultimo, cantidad_menores ):.2f}%{Style.RESET_ALL}" )
    input()
    limpiar("cls")
