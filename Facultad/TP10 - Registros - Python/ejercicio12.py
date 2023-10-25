"""
1- Se tienen los datos de los afiliados que realizan aportes a obras sociales, de cada
uno se almacena Apellido y nombre, Obra social, Monto de cuota y cantidad de
integrantes del grupo familiar.
Se pide:
    a- Realice un subprograma que cargue los datos hasta que el usuario lo desee.
    b- Listado ordenado por Obra Social y apellido y nombre.
    d- Mostrar total aportado a esta obra social por todos sus afiliados (IOSPER).
    e- Calcular total de familias que poseen más de 6 integrantes en su grupo familiar,
       y de éstos mostrar solo los que aportan más de 10000 pesos.
    f- Mostrar si Pablo Benitez es afiliado, de ser asi mostrar la cantidad de integrantes
       del grupo familiar y la obra social
"""
import tableprint as tp
from msvcrt import getwch
import os

def limpiar():
    os.system("cls") 

def insertar():
    afiliado = { 'nombre' : str, 'apellido' : str, 'obra_social' : str, 'cuota' : float, 'integrantes' : int }
    afiliado['nombre'] = input( "Ingrese el nombre: " )
    afiliado['apelldio'] = input( "Ingrese el apellido: " )
    afiliado['obra_social'] = input( "Ingrese la obra social: " )
    afiliado['cuota'] = float( input( "Ingrese la cuota de la obra social: " ) )
    afiliado['integrantes'] = int( input("Ingrese la cantidad de integrantes del grupo familiar: ") )
    return afiliado

def cargar(lista : list, tamanio : int, ultimo : int):
    indice = 0
    if ultimo > 0:
        indice = ultimo
    
    print( " - ¿Quiere ingresar un afiliado? (s/n): ", end="" )
    opc = getwch()
    limpiar()
    while (( opc.upper() == 'S' ) or (len(lista) < tamanio)):
        print(f" # Afiliado {indice + 1}")
        afiliado = insertar()  
        lista[indice] = afiliado
        limpiar()
        print( " - ¿Quiere ingresar un afiliado? (s/n): ", end="" )
        opc = getwch()
        limpiar()
        indice += 1
        print()
    if (indice > 0):
        return (indice)
    else:
        return -1

def contar( lista : list, ultimo : int, campo : str, ocurrencia ):
    contador = 0
    posicion = [-1] * ultimo
    for indice in range ( 0, ultimo ):
        if lista[indice][campo] > ocurrencia:
            contador += 1
            posicion[indice] = indice
    return contador, posicion

def contar_( lista : list, ultimo : int, campo : str, ocurrencia ):
    contador = 0
    registros = [ -1 ] * ultimo
    for indice in range( 0, ultimo ):
        if lista[ indice ][ campo ] > ocurrencia:
            registros[ contador ] = lista[ indice ]
            contador += 1
    return contador, registros

def total( lista : list, ultimo : int, campo : str, valor : str ):
    acumulador = 0
    for elemento in range( 0, ultimo ):
        if lista[elemento][campo] == valor:
            acumulador += lista[elemento]['cuota']
    return acumulador

def burbuja(lista : list, clave : str) -> None:
    """Metodo de ordenamiento burbuja"""
    for i in range(0,(len(lista)-1)):
        for j in range(0,(len(lista)-1)-i):
            if lista[j][clave] > lista[j+1][clave]:
                aux               = lista[j][clave]
                lista[j][clave]   = lista[j+1][clave]
                lista[j+1][clave] = aux
    
def busqueda_binaria(lista : list, tamanio : int, buscado, clave ) -> int:
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

def busqueda_nombre_apellido( lista : list, tamanio : int, buscado : list ):
    primero  = 0
    ultimo   = tamanio - 1
    posicion = None
    while (posicion == None) and (primero <= ultimo):
        medio = (primero + ultimo) // 2
        if (lista[medio]['nombre'] == buscado[0]) and (lista[medio]['apellido'] >= buscado[1]):
            posicion = medio
        elif (lista[medio]['nombre'] == buscado[0]) and (lista[medio]['apellido'] >= buscado[1]):
            ultimo   = medio - 1
        else:
            primero  = medio + 1   
    return posicion 

def quitar( lista : list, ultimo : list ):
    limpiar()
    print("Ingrese el nombre y apelldo del afiliado que quiera quitar: ")
    nombre = input(" - Nombre: ")
    apellido = input(" - Apellido: ")
    burbuja( lista, 'nombre' )
    limpiar()
    if busqueda_binaria( lista, ultimo, nombre, 'nombre' ) != None:
        burbuja( lista, 'apellido' )
        posicion = busqueda_binaria( lista, ultimo, apellido, 'apellido' )
        if posicion != None:
            lista[posicion] = 0
            if posicion < ultimo:
                for indice in range(posicion, ultimo):
                    lista[indice] = lista[indice + 1]
                    if lista[indice + 1] == 0:
                        posicion = indice + 1
                        print( f"Se quito {nombre} {apellido} correctamente." )
        else:
            print( f"El apellido \'{apellido}\' no existe! o es incorrecto" )
    else: 
        print( f"El nombre \'{nombre}\' no existe! o es incorrecto" )
    return posicion
  
def burbuja_modificado( lista : list, ultimo : int ):
    for i in range(ultimo - 1):
        for j in range(ultimo - 1 - i):
            elemento_actual = lista[j]['obra_social'] + lista[j]['nombre'] + lista[j]['apellido']
            elemnto_siguiente = lista[j + 1]['obra_social'] + lista[j + 1]['nombre'] + lista[j]['apellido']
            if elemento_actual > elemnto_siguiente:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

def burbuja_personalizado( lista : list, ultimo : int, parametros : list ):
    for i in range(ultimo - 1):
        for j in range(ultimo - 1 - i):
            elemento_actual = ''
            elemento_siguiente = ''
            for campo in range( 0, parametros ): 
                elemento_actual += lista[ j ][ campo ]
            for campo in range( 0, parametros ): 
                elemento_siguiente += lista[ j + 1 ][ campo ]
            if elemento_actual > elemento_siguiente:
                aux = lista[ j ]
                lista[ j ] = lista[ j + 1 ]
                lista[ j + 1 ] = aux

def crear_matriz(filas : int, columnas : int, valor=None):
    """Crea una matriz de 'n' `filas` y 'n' `columnas` e inicializa la matriz con x `valor`."""
    matriz = []
    for fila in range(filas):
        matriz = matriz + [[]]
        for columna in range(columnas):
            matriz[fila] = matriz[fila] + [valor]
    return matriz


def registro_a_matriz( lista : list, tamanio : int):
    matriz = crear_matriz( tamanio, 5 )
    for fila in range(0, tamanio):
        matriz[fila][0] = lista[fila]['nombre']
        matriz[fila][1] = lista[fila]['apellido']
        matriz[fila][2] = lista[fila]['obra_social']
        matriz[fila][3] = lista[fila]['cuota']
        matriz[fila][4] = lista[fila]['integrantes']

    return matriz


def ordenar( lista : list, opc : str, ultimo : int ):
    if opc.upper() == 'A':
        burbuja_modificado( lista, ultimo )
        matriz = registro_a_matriz( lista, ultimo )

        headers = ['Nombre', 'Apellido', 'Obra Social', 'Cuota', 'Integrantes']
        tp.table(matriz, headers) 
    if opc.upper() == 'B':
        limpiar()
        print( " - Parametros: \'nombre\', \'apelldio\', \'obra_social\', \'cuota\', \'integrantes\'." )
        print( " - Ej: nombre>apellido", end="\n\n" )
        parametros=input( "Ingrese el orden de ordenamiento. " )
        parametros = parametros.split('>') 
        limpiar()
        burbuja_personalizado( lista, ultimo, parametros )
        matriz = registro_a_matriz( lista, ultimo )
        headers = ['Nombre', 'Apellido', 'Obra Social', 'Cuota', 'Integrantes']
        tp.table(matriz, headers) 

def menu( afiliados=0 ):
    afiliados = str(afiliados)
    if len(afiliados) == 1:
        afiliados = '0' + afiliados
    while True:
        print(
         "#################################################\n"
         "#                                               #\n"
        f"#   · (A) Agregar afilieados \'{ afiliados }\'.              #\n"
        f"#   · (B) Quitar un afiliado.                   #\n"
        f"#   · (C) Listado ordenado.                     #\n"
        f"#   · (D) Listado aporte total por obra social. #\n"
        f"#   · (E) Buscar afiliado.                      #\n"
        f"#   · (F) Otros datos.                          #\n"
        f"#   · (Z) Salir                                 #\n"
         "#                                               #\n"
         "#################################################"    
        )
        opc = getwch()
        if opc.upper() in ['A', 'B', 'C', 'D', 'E', 'F', 'Z']:
            limpiar()
            return opc
    
def menu_ordenamiento():
    while True:
        limpiar()   
        print(
            " *** MOSTRAR LISTADO ORDENADO POR: *** \n\n"
            "  (A) Obra Social > Apellido > Nombre \n"
            "  (B) Personalizado. \n"
        )
        opc = getwch()
        if ( ( opc.upper() == 'A' ) or ( opc.upper() == 'B' ) ):
            return opc

def menu_obra_social():
    while True:
        limpiar()
        print(
            " *** MOSTRAR EL TOTAL APORTADO POR OBRA SOCIAL: *** \n\n"
            "  (A) IOSPER. \n"
            "  (B) Otros"
        )
        opc = getwch()
        if ( ( opc.upper() == 'A' ) or ( opc.upper() == 'B' ) ):
            return opc


lista = [
    { 'nombre' : "Ana", 'apellido' : "Sánchez", 'obra_social' : "IOSPER", 'cuota' : 1200, 'integrantes' : 3 },
    { 'nombre' : "Marta", 'apellido' : "Díaz", 'obra_social' : "OSME", 'cuota' : 1330, 'integrantes' : 8 },
    { 'nombre' : "Alejandro", 'apellido' : "Pérez", 'obra_social' : "IOSPER", 'cuota' : 1100, 'integrantes' : 6 },
    { 'nombre' : "Raúl", 'apellido' : "González", 'obra_social' : "OSPRESA", 'cuota' : 1200, 'integrantes' : 3 },
    { 'nombre' : "Julia", 'apellido' : "García", 'obra_social' : "OSSEG", 'cuota' : 900, 'integrantes' : 5 },
    { 'nombre' : "Nuria", 'apellido' : "López", 'obra_social' : "OSME", 'cuota' : 14000, 'integrantes' : 7 },
    { 'nombre' : "Sandra", 'apellido' : "Martínez", 'obra_social' : "OSPRESA", 'cuota' : 1100, 'integrantes' : 5 },
    { 'nombre' : "Jesús", 'apellido' : "García", 'obra_social' : "OSME", 'cuota' : 12000, 'integrantes' : 9 },
    { 'nombre' : "Pablo", 'apellido' : "Benitez", 'obra_social' : "OSSEG", 'cuota' : 800, 'integrantes' : 8 },
    0,
    0,
    0,
    0,
    0,
    0
]

TAMANIO = len( lista )

opc = ''
# ultimo = TAMANIO
ultimo = 9

while opc.upper() != 'Z':
    limpiar()
    opc = menu( ultimo )
    if opc.upper() == 'A':
        ultimo = cargar( lista, TAMANIO, ultimo )
    elif opc.upper() == 'B':
        
        ultimo = quitar( lista, ultimo )
    elif opc.upper() == 'C':
        
        opc = menu_ordenamiento()
        ordenar( lista, opc, ultimo )
        input()
    elif opc.upper() == 'D':
        
        opc = menu_obra_social()
        if ( opc.upper() == 'A' ):
            print( f"El total aportado de todos los afiliados a IOSPER es: $ {total( lista, ultimo, 'obra_social', 'IOSPER' ):.2f}" )
            input()
        elif ( opc.upper() == 'B' ):
            buscado = input( "Ingrese el nombre de la obra social: " )
            print(end="\n\n")
            burbuja( lista, 'obra_social' )
            posicion = busqueda_binaria( lista, ultimo, buscado, 'obra_social' )
            if posicion is not None:
                print( f"El total aportado de todos los afiliados a {buscado} es: $ {total( lista, ultimo, 'obra_social', buscado ):.2f}" )
            else:
                print( f"La obra social {buscado} no existe!." )
            input()
    elif opc.upper() == 'F':
        
        contador, registros = contar_( lista, ultimo, 'integrantes', 6 )
        print( f"{contador=} - {registros}" )
        print( f"Cantidad de Familias que possen mas de 6 integrantes en su grupo familiar: {contador}", end="\n\n" )
        contador, registros = contar_( registros, contador, 'cuota', float(10000) )
        print( f"{contador=} - {registros}" )
        for persona in range( 0, contador ):
            print(
                f" + Nombre: {registros[persona]['nombre']}.\n"
                f" + Apellido: {registros[persona]['apellido']}.\n"
                f" + Obra Social: {registros[persona]['obra_social']}.\n"
                f" + Cuota: {registros[persona]['cuota']}.\n"
                f" + Integrantes: {registros[persona]['integrantes']}.\n\n"
            )         
        input()
    elif opc.upper() == 'E':
        
        print( " *** BUSCAR AFILIADO **** ", end="\n\n" )
        nombre = input( " - Nombre: " )
        apellido = input( " - Apellido: " )
        print()
        buscado = [nombre, apellido]
        burbuja_personalizado( lista, ultimo, ['nombre', 'apellido'] )
        posicion = busqueda_nombre_apellido( lista, ultimo, buscado )
        if ( posicion ) is not None:
            print( f"{nombre} {apellido} esta afiliado a la obra social \'{lista[posicion]['obra_social']}\'.", end="\n\n" )
            print( f"Y su grupo familiar esta integrado por {lista[posicion]['integrantes']} personas." )
            input()
        else: 
            print( f"{nombre} {apellido} no existe!" )
            input()
