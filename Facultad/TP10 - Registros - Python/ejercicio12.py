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
    print()
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

def quitar( lista : list, ultimo : list, posicion : int ):
    

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
        

lista = [0, 0, 0, 0, 0]

TAMANIO = len( lista )

limpiar()

opc = ''
ultimo = 0

while opc.upper() != 'Z':
    opc = menu( ultimo )
    if opc.upper() == 'A':
        limpiar()
        ultimo = cargar( lista, TAMANIO, ultimo )
    elif opc.upper() == 'B':
        posicion = busqueda_binaria( lista, ultimo, buscado, '' )



