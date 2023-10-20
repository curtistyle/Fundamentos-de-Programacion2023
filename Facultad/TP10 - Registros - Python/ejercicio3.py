""" Se tiene una clase de 30 estudiantes, para c/u se almacenan los siguientes datos: 
    - Nro_estudiante 
    - Nombre 
    Nota Se pide: 
        a- Lista de alumnos con sus respectivas notas ordenados alfabéticamente. 
        b- Nro. de estudiante con mayor nota. 
        c- Nombre de estudiante de menor nota. 
        d- Nota que obtuvo la alumna Laura Suárez. """
        
def insertar():
    estudiante = { 'numero' : int, 'nombre' : str, 'nota' : int }
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

# ? mostrar 1
def mostrar(lista : str, tamanio : int):
    for indice in range(0, tamanio):
        for key, item in lista[indice].items():
            print(f"{key} = {item}")
        print()

# ? mostrar 2
def mostrar_(lista : list, tamanio : int, campos : list):
    for indice in range(0, tamanio):
        for campo in range(0, len(campos)):
            print(f"{campos[campo]} = {lista[indice][campos[campo]]}")
        print()

# ? mostrar 3
def mostrar__(lista : list, tamanio : int, campos : list):
    for indice in range(0, tamanio):
        for key, item in lista[indice].items():
            if key in campos:
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
    {'numero' : 6, 'nombre' : 'Laura Suarez', 'nota': 8}
]

TAMANIO = len(alumnos)

burbuja(alumnos,'nombre')

print("# Lista de los alumnos ordenada: ")
print('>>> MOSTRAR 1: ')
mostrar(alumnos, len(alumnos))
print()
print('>>> MOSTRAR 2: ')
mostrar__(alumnos, len(alumnos), ['nombre'])

print("Numero del alumno con la nota mayor: ")
nota_mayor = mayor(alumnos, TAMANIO, 'nota')
print(alumnos[nota_mayor]['nota'])

print("El nombre del estudiante con la menor nota: ")
nota_menor = menor(alumnos, TAMANIO, 'nota')
print(alumnos[nota_menor]['nota'])



buscado = input("Ingrese un nombre: ")
pos = busqueda_binaria(alumnos, len(alumnos), buscado, "nombre")

if pos is not None:
    print(f"{buscado} existe en la lista, posicion: {pos + 1}")
else:
    print(f"{buscado} no existe. {pos + 1}")
