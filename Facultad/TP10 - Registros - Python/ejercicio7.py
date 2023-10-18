"""
En una empresa se guardan los códigos de empleados, edades, los sueldos y la antigüedad en años  (Nº  entero).  Se  pide  calcular:  
    a- Sueldo del empleado más antiguo y edad.
    b- Sueldo del empleado más nuevo y edad.
    c- Promedio de sueldos. 
    d- Promedio de edades.
"""

tipo_empleado = { 'codigo' : int, 'edad' : int, 'sueldo' : float, 'antiguedad' : int }

def insertar():
    empleado = tipo_empleado
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
        if lista[empleado][campo] > mayor:
            mayor = lista[empleado][campo]
            posicion = empleado
    return posicion

def menor(lista : list, tamanio : int, campo : str):
    menor = lista[0][campo]
    for empleado in range(0, tamanio):
        if lista[empleado][campo] < menor:
            menor = lista[empleado][campo]
            posicion = empleado
    return posicion

def promedio(lista : list, tamanio : int, campo : str):
    acumulador = 0
    for empleado in range(0, tamanio):
        acumulador += lista[empleado][campo]
    return acumulador / tamanio

empresa = [
    { 'codigo' : 1, 'edad' : 30, 'sueldo' : 4000, 'antiguedad' : int },
    { 'codigo' : 2, 'edad' : 25, 'sueldo' : 4200, 'antiguedad' : int },
    { 'codigo' : 3, 'edad' : 38, 'sueldo' : 4350, 'antiguedad' : int },
    { 'codigo' : 4, 'edad' : 20, 'sueldo' : 4010, 'antiguedad' : int },
    { 'codigo' : 5, 'edad' : 49, 'sueldo' : 4800, 'antiguedad' : int },
    0,
    0
    ]



