""" Se tiene una clase de 30 estudiantes, para c/u se almacenan los siguientes datos: 
    - Nro_estudiante 
    - Nombre 
    Nota Se pide: 
        a- Lista de alumnos con sus respectivas notas ordenados alfabéticamente. 
        b- Nro. de estudiante con mayor nota. 
        c- Nombre de estudiante de menor nota. 
        d- Nota que obtuvo la alumna Laura Suárez. """
        
tipo_estudiante = {
    'numero': int,
    'nombre': str,
    'nota': int
}

def insertar():
    estudiante = tipo_estudiante
    
    estudiante['numero'] = int(input("Ingrese el numero de estudiante: "))
    estudiante['nombre'] = input("Ingrese el nombre del estudiante: ")
    estudiante['nota'] = float(input("Ingrese la nota del estudiante: "))
    return estudiante

def cargar_lista(lista : list, tamanio : int):
    ultimo = 0
    opcion = input("Ingrese s para cargar una poliza:  ")
    while (((opcion == 's') or (opcion == 'S')) and (ultimo < tamanio)):
        lista[ultimo] = insertar()
        ultimo += 1
        print()
        if ultimo < tamanio:
            opcion = input("Ingrese 's' para cargar una poliza: ")
    return ultimo

def mayor(lista : list, tamanio : int, campo : str):
    maximo = lista[0][campo]
    for indice in range(0, tamanio):
        if lista[indice][campo] > maximo:
            maximo = lista[indice][campo]
            posicion = indice
    return posicion

def menor(lista : list, tamanio : int, campo : str):
    maximo = lista[0][campo]
    for indice in range(0, tamanio):
        if lista[indice][campo] < maximo:
            maximo = lista[indice][campo]
            posicion = indice
    return posicion

# ! falta busqueda y ordenamiento.

