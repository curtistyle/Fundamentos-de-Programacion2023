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

def mostrar(lista : str, tamanio : int):
    for indice in range(0, tamanio):
        for key, item in lista[indice].items():
            print(f"{key} = {item}")
        print()

def burbuja(lista : list, clave : str) -> None:
    """Metodo de ordenamiento burbuja"""
    for i in range(0,(len(lista)-1)):
        for j in range(0,(len(lista)-1)-i):
            if lista[j][clave] > lista[j+1][clave]:
                aux               = lista[j][clave]
                lista[j][clave]   = lista[j+1][clave]
                lista[j+1][clave] = aux

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

alumnos = [
    {'numero' : 1, 'nombre' : 'Pablo López', 'nota': 8},
    {'numero' : 2, 'nombre' : 'Ana María Sánchez', 'nota': 9},
    {'numero' : 3, 'nombre' : 'Julia García', 'nota': 4},
    {'numero' : 4, 'nombre' : 'Nuria Sánchez', 'nota': 5},
    {'numero' : 5, 'nombre' : 'Daniel Martínez', 'nota': 7.50},
]

print("# Sin ordenar")
mostrar(alumnos, len(alumnos))

burbuja(alumnos,'nombre')

print("# Ordenado")
mostrar(alumnos, len(alumnos))

buscado = input("Ingrese un nombre: ")
pos = busqueda_binaria(alumnos, len(alumnos), buscado, "nombre")

if pos is not None:
    print(f"{buscado} existe en la lista, posicion: {pos + 1}")
else:
    print(f"{buscado} no existe. {pos + 1}")




