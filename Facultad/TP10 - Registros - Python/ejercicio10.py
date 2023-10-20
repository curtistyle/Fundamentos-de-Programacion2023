"""
Se tiene una agenda telefónica con los siguientes datos: Nombre, dirección, Nº teléfono (puede o 
no tener), se pide: 
    a- Listado de personas con Nº telefónico. 
    b- Listado de personas sin Nº telefónico, con sus respectivas direcciones. 
    c- Dada una persona mostrar su dirección y Nº de teléfono si tiene.
"""


def insertar():
    persona = {'nombre' : str, 'direccion' : str, 'telefono' : str }
    persona['nombre'] = input("Ingrese el nombre del persona: ")
    persona['direccion'] = input("Ingrese la direccion de la persona: ")
    persona['telefono'] = input("Ingrese el telefono de la persona: ")
    return persona

def cargar(lista : list, tamanio : int):
    indice = 0
    print()
    opc = input(" - ¿Quiere ingresar un persona? (s/n): ")
    while (( opc.upper() == 'S' ) or (len(lista) < tamanio)):
        print(f" # Libro {indice + 1}")
        persona = insertar()  
        lista[indice] = persona
        opc = input(" - ¿Quiere ingresar un persona? (s/n): ")
        indice += 1
        print()
    if (indice > 0):
        return (indice + 1)
    else:
        return 0

def mayor(lista : list, tamanio : int, campo : str):
    mayor = lista[0][campo]
    for stock in range(0, tamanio):
        if lista[stock][campo] > mayor:
            mayor = lista[stock][campo]
            posicion = stock
    return posicion

def mostrar(lista : list, tamanio : int, telefono : bool):
    for persona in range(0, tamanio):
        if telefono == True:
            # TODO: Listado de persona con telefono
            if lista[persona]['telefono'] != '':
                print(f"Perosona {persona + 1}.")
                print(f" - Nombre : {lista[persona]['nombre']}")
                print(f" - Direccion : {lista[persona]['direccion']}")
                print(f" - Telfono : {lista[persona]['telefono']}", end="\n\n")
        else:
            if lista[persona]['telefono'] == '':
                print(f"Perosona {persona + 1}.")
                print(f" - Nombre : {lista[persona]['nombre']}")
                print(f" - Direccion : {lista[persona]['direccion']}")
                print(f" - Telfono : {lista[persona]['telefono']}", end="\n\n")


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

def burbuja(lista : list, clave : str) -> None:
    """Metodo de ordenamiento burbuja"""
    for i in range(0,(len(lista)-1)):
        for j in range(0,(len(lista)-1)-i):
            if lista[j][clave] > lista[j+1][clave]:
                aux               = lista[j][clave]
                lista[j][clave]   = lista[j+1][clave]
                lista[j+1][clave] = aux


personas = [
    { 'nombre' : "Ana Sánchez", 'direccion' : 'Boulevard Alvear 5051', 'telefono' : 344212312 },
    { 'nombre' : "David González", 'direccion' : 'Avenida España 5253', 'telefono' : 344265432 },
    { 'nombre' : "Laura Fernández", 'direccion' : 'Calle Moreno 5455', 'telefono' : '' },
    { 'nombre' : "Juan Martínez", 'direccion' : 'Paseo Rivadavia 5657', 'telefono' : 344257324 },
    { 'nombre' : "Marta Díaz", 'direccion' : 'Boulevard 25 de Mayo 5859', 'telefono' : '' },
    { 'nombre' : "Antonio Pérez", 'direccion' : 'Avenida San Luis 6061', 'telefono' : '' },
    { 'nombre' : "Sandra Rodríguez", 'direccion' : 'Calle Santiago 6263', 'telefono' : 344277452 },
    { 'nombre' : "Francisco Sánchez", 'direccion' : 'Paseo Entre Ríos 6465', 'telefono' : 344242132 }
]

ultimo = len( personas )


    
# TODO: a- Listado de personas con Nº telefónico. 

print( " · Personas con numero de telefono: ", end="\n\n" )
mostrar( personas, ultimo, True )

# TODO: b- Listado de personas sin Nº telefónico, con sus respectivas direcciones. 

print( " · Personas sin numero de tefono: ", end="\n\n" )
mostrar( personas, ultimo, False )

# TODO: c- Dada una persona mostrar su dirección y Nº de teléfono si tiene.

burbuja( personas, 'nombre' )
buscado = input( "Ingrese el nombre de una persona: " )
posicion = busqueda_binaria( personas, ultimo, buscado, 'nombre' )
print()
if posicion != -1:
    print( f" - Nombre : { personas[posicion]['nombre'] }" )
    print( f" - Direccion : { personas[posicion]['direccion'] }" )
    print( f" - Telfono : { personas[posicion]['telefono'] }", end="\n\n" )
else:
    print( f"La personas { buscado } no existe!." )
