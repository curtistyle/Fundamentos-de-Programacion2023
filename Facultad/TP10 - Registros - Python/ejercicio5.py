""" 
En una librería se almacenan los datos de x cantidad de libros, por cada libro se tiene la siguiente 
información: código y stock. Realizar un programa que informe cuando se deba reponer stock de 
cada libro, considerando stock mínimo = 3 libros.
"""


def insertar():
    libro = {'codigo' : int, 'stock' : int}
    libro['codigo'] = int(input("Ingrese el Codigo del libro: "))
    libro['stock'] = int(input("Ingrese el Stock: "))
    return libro

# # ? Cargar 1
# def cargar(lista : list, tamanio : int):
#     ultimo = 0
#     print()
#     opc = input(" - ¿Quiere ingresar un libro? (s/n): ")
#     while (( opc.upper() == 'S' ) or (len(lista) < tamanio)):
#         print(f" # Libro {ultimo + 1}") 
#         lista[ultimo] = insertar()  
#         opc = input(" - ¿Quiere ingresar un libro? (s/n): ")
#         ultimo += 1
#         print()
    
#     if (ultimo > 0):
#         return (ultimo + 1)
#     else:
#         return 0
    
# ? Cargar 2
def cargar(lista : list, tamanio : int):
    ultimo = 0
    opc = input(" - ¿Quiere ingresar un libro? (s/n): ")
    print()
    while (( opc.upper() == 'S' ) and (ultimo < tamanio)):
        print(f" # Libro {ultimo + 1}", end="\n\n")
        lista[ultimo] = insertar() 
        print("A-",lista)
        if (lista[ultimo]['stock'] < 3):
            print(f"¡Cuidado!, El stock del libro cod:{lista[ultimo]['codigo']} se esta agotando.", end="\n\n")
            opc = input("¿Quiere modificar el Stock? (s/n): ")
            print()
            if opc.upper() == 'S':
                lista[ultimo]['stock'] = int(input("Ingrese el Stock: "))
        opc = input(" - ¿Quiere ingresar un libro? (s/n): ")
        ultimo = ultimo + 1
        print()
        print("B-",lista)
    return ultimo
       
def contar_ocurrencia(lista : list, tamanio : int, campo : str):
    contador = 0
    for stock in range(0, tamanio): 
        if lista[stock][campo] < 3:
            contador += 1    
    return contador

def mostrar_todo(lista : list, ultimo : int):
    for stock in range(0, ultimo):
        print(f"Libro {stock + 1}.")
        print(f"Codigo Libro = {lista[stock]['codigo']}") 
        print(f"Stock        = {lista[stock]['stock']}") 
        print()
    
biblioteca = [0,0,0,0]

# biblioteca = [
#     {'codigo' : 1, 'stock' : 6},
#     {'codigo' : 2, 'stock' : 4},
#     {'codigo' : 3, 'stock' : 2},
#     {'codigo' : 4, 'stock' : 3},
#     {'codigo' : 5, 'stock' : 9},
#     {'codigo' : 6, 'stock' : 10},
#     {'codigo' : 7, 'stock' : 5},    
# ]

# TODO: Defino el tamanio de la lista 



ultimo = cargar(biblioteca, len(biblioteca) )

print(ultimo)

# mostrar_todo(biblioteca, ultimo)
# print(biblioteca)