"""
En una empresa se guardan los códigos de empleados, edades, los sueldos y la antigüedad en años  (Nº  entero).  Se  pide  calcular:  
    a- Sueldo del empleado más antiguo y edad.
    b- Sueldo del empleado más nuevo y edad.
    c- Promedio de sueldos. 
    d- Promedio de edades.
"""

def insertar():
    empleado = { 'codigo' : int, 'edad' : int, 'sueldo' : float, 'antiguedad' : int }
    empleado['codigo'] = int(input("Ingrese el codigo del empleado: "))
    empleado['edad'] = int(input("Ingrese la edad del empleado: "))
    empleado['sueldo'] = float(input("Ingrese sueldo del empleado: "))
    empleado['antiguedad'] = int(input("Ingrese los años de antiguedad del empleado: "))
    return empleado

def cargar(lista : list, tamanio : int):
    indice = 0
    print()
    opc = input(" - ¿Quiere ingresar un alquilino? (s/n): ")
    while (( opc.upper() == 'S' ) or (len(lista) < tamanio)):
        print(f" # Libro {indice + 1}")
        empleado = insertar()  
        lista[indice] = empleado
        opc = input(" - ¿Quiere ingresar un alquilino? (s/n): ")
        indice += 1
        print()
    if (indice > 0):
        return (indice + 1)
    else:
        return 0
    
def mayor(lista : list, tamanio : int, campo : str):
    mayor = lista[0][campo]
    for empleado in range(0, tamanio):
        if lista[empleado][campo] >= mayor:
            mayor = lista[empleado][campo]
            posicion = empleado
    return posicion

def mayor_segun(lista : int, tamanio : int, campo : str, segun : list):
    mayor = lista[segun[0]][campo]
    posicion = segun[0]
    for indice in range(0, tamanio):
        if segun[indice] != -1:
            if lista[segun[indice]][campo] > mayor:
                mayor = lista[segun[indice]][campo]
                posicion = segun[indice]
    return posicion 

def menor_segun(lista : int, tamanio : int, campo : str, segun : list):
    menor = lista[segun[0]][campo]
    posicion = segun[0]
    for indice in range(0, tamanio):
        if segun[indice] != -1:
            if lista[segun[indice]][campo] < menor:
                menor = lista[segun[indice]][campo]
                posicion = segun[indice]
    return posicion 

def menor(lista : list, tamanio : int, campo : str):
    menor = lista[0][campo]
    for empleado in range(0, tamanio):
        if lista[empleado][campo] <= menor:
            menor = lista[empleado][campo]
            posicion = empleado
    return posicion

def ocurrencias(lista : list, tamanio : int, campo : str, apuntar):
    """Retorna una `lista` con la posicion de las ocurrencias encontradas"""
    resultado = [-1] * tamanio
    i = 0
    for indice in range(0, tamanio):
        if lista[indice][campo] == lista[apuntar][campo]:
            resultado[i] = indice
            i += 1
    return resultado


def promedio(lista : list, tamanio : int, campo : str):
    acumulador = 0
    for empleado in range(0, tamanio):
        acumulador += lista[empleado][campo]
    return acumulador / tamanio

empresa = [
    { 'codigo' : 1, 'edad' : 30, 'sueldo' : 4000, 'antiguedad' : 5 },
    { 'codigo' : 2, 'edad' : 25, 'sueldo' : 4200, 'antiguedad' : 3 }, 
    { 'codigo' : 3, 'edad' : 38, 'sueldo' : 4350, 'antiguedad' : 5 },
    { 'codigo' : 4, 'edad' : 20, 'sueldo' : 4010, 'antiguedad' : 1 }, #
    { 'codigo' : 5, 'edad' : 49, 'sueldo' : 3990, 'antiguedad' : 4 },
    { 'codigo' : 6, 'edad' : 50, 'sueldo' : 4440, 'antiguedad' : 1 }, #
    { 'codigo' : 7, 'edad' : 23, 'sueldo' : 4100, 'antiguedad' : 5 },
    { 'codigo' : 8, 'edad' : 33, 'sueldo' : 4220, 'antiguedad' : 5 },
    0,
    0
    ]

ultimo = 8

# TODO: a - Sueldo del empleado más antiguo y edad.

apuntar = mayor(empresa, ultimo, 'antiguedad')
mayor_antiguedad = ocurrencias(empresa, ultimo, 'antiguedad', apuntar)
posicion = mayor_segun(empresa, ultimo, 'edad', mayor_antiguedad)
print("Empleado mas antiguo y edad: \n",
    f" - Codigo = {empresa[posicion]['codigo']}\n", 
    f" - Edad = {empresa[posicion]['edad']}\n",
    f" - Sueldo = $ {empresa[posicion]['sueldo']}\n",
    f" - Antiguedad = {empresa[posicion]['antiguedad']}\n" )

# TODO: b- Sueldo del empleado más nuevo y edad.

apuntar = menor(empresa, ultimo, 'antiguedad')
menor_antiguedad = ocurrencias(empresa, ultimo, 'antiguedad', apuntar)
posicion = menor_segun(empresa, ultimo, 'edad', menor_antiguedad)
print("Empleado mas nuevo y edad: \n",
    f" - Codigo = {empresa[posicion]['codigo']}\n", 
    f" - Edad = {empresa[posicion]['edad']}\n",
    f" - Sueldo = $ {empresa[posicion]['sueldo']}\n",
    f" - Antiguedad = {empresa[posicion]['antiguedad']}\n" )

# TODO: c- Promedio de sueldos. 

resultado = promedio( empresa, ultimo, 'sueldo' )
print( f"El promedio de sueldos es: $ {resultado:.2f}.", end="\n\n" )

# TODO: d- Promedio de edades.

resultado = promedio( empresa, ultimo, 'edad' )
print( f"El promedio de sueldos es: {resultado:.2f}" )



