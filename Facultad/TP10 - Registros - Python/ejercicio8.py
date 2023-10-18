"""
De cada alumno de una materia ‘x’ se registra Nº de alumno, nota y sexo. Se desea saber: 
    a - Cuantos varones aprobaron (nota>=4).
    b - que % de mujeres sacó 10.
    c - % de desaprobados. 
"""

tipo_alumno = { 'numero' : int, 'nota' : float, 'sexo' : str }

def insertar():
    alumno = tipo_alumno
    alumno['numero'] = int(input("Ingrese el numero del alumno: "))
    alumno['nota'] = float(input("Ingrese la nota del alumno: "))
    alumno['sexo'] = str(input("Ingrese el sexo del alumno: "))
    alumno['antiguedad'] = int(input("Ingrese los años de antiguedad del alumno: "))
    return alumno

def cargar(lista : list, tamanio : int):
    indice = 0
    print()
    opc = input(" - ¿Quiere ingresar un alquilino? (s/n): ")
    while (( opc.upper() == 'S' ) or (len(lista) < tamanio)):
        print(f" # Libro {indice + 1}")
        alumno = insertar()  
        lista[indice] = alumno
        opc = input(" - ¿Quiere ingresar un alquilino? (s/n): ")
        indice += 1
        print()
    if (indice > 0):
        return (indice + 1)
    else:
        return 0
    
def contar_ocurrencia(lista : list, tamanio : int, campo : str):
    contador = 0
    for stock in range(0, tamanio): 
        if lista[stock][campo] >= 4:
            contador += 1    
    return contador

def aprobado_mujeres(lista : list, tamanio : int, campo : str):
    contador = 0
    for alumno in range(0, tamanio):
        if lista[alumno]['sexo'] == 'femenino':
            if lista[alumno]['edad'] == 10:
                contador += 1        
    return contador       
        
def desaprobados(lista : list, tamanio : int):
    contador = 0
    for alumno in range(0, tamanio):
        if lista[alumno]['nota'] < 4:
            contador += 1
    return contador

def porcentaje(cantidad : int, total : int):
    if cantidad > 0:
        return (cantidad * 100) / total
    else:
        return 0
    
