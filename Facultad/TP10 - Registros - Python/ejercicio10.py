"""
Se tiene una agenda telefónica con los siguientes datos: Nombre, dirección, Nº teléfono (puede o 
no tener), se pide: 
    a- Listado de personas con Nº telefónico. 
    b- Listado de personas sin Nº telefónico, con sus respectivas direcciones. 
    c- Dada una persona mostrar su dirección y Nº de teléfono si tiene.
"""

tipo_persona = [ {'nombre' : str, 'direccion' : str, 'telefono' : str } ]

def insertar():
    persona = tipo_persona
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
                print(f" - Telfono : {lista[persona]['telefono']}")
        else:
            print(f"Perosona {persona + 1}.")
            print(f" - Nombre : {lista[persona]['nombre']}")
            print(f" - Direccion : {lista[persona]['direccion']}")
            print(f" - Telfono : {lista[persona]['telefono']}")


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

