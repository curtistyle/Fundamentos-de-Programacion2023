# tipo_persona = { 'nombre' : str, 'apellido' : str, 'edad' : int }

def insertar():
    persona = { 'nombre' : str, 'apellido' : str, 'edad' : int }
    persona['nombre'] = input( "Ingrese el nombre: " )
    persona['apellido'] = input( "Ingrese el apellido: " )
    persona['edad'] = input( "Ingrese la edad: " )
    return persona

def cargar( lista : list, tamanio : int ):
    indice = 0
    opc = input( "¿Quiere ingresar una nueva persona? (s/n): " )
    while( ( opc.upper() == 'S' ) and ( indice < tamanio ) ):
        persona = insertar()
        lista[indice] = persona
        indice += 1;
        print( lista, end="\n\n" )
        opc = input( "¿Quiere ingresar una nueva persona? (s/n): " )
    return indice + 1


lista = [ 0, 0, 0, 0, ]

TAMANIO = len(lista)

cargar( lista, TAMANIO )


