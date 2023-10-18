""" 
En una librería se almacenan los datos de x cantidad de libros, por cada libro se tiene la siguiente 
información: código y stock. Realizar un programa que informe cuando se deba reponer stock de 
cada libro, considerando stock mínimo = 3 libros.
"""

tipo_libro = {'codigo' : int, 'stock' : int}

def insertar():
    libro = tipo_libro
    libro['codigo'] = int(input("Ingrese el codigo del libro: "))
    libro['stock'] = int(input("Ingrese el stock: "))
    return libro

def cargar(lista : list, tamanio : int):
    indice = 0
    print()
    opc = input(" - ¿Quiere ingresar un libro? (s/n): ")
    while (( opc.upper() == 'S' ) or (len(lista) < tamanio)):
        print(f" # Libro {indice + 1}")
        stock = insertar()  
        lista[indice] = stock
        opc = input(" - ¿Quiere ingresar un libro? (s/n): ")
        indice += 1
        print()
    
    if (indice > 0):
        return (indice + 1)
    else:
        return 0
 
def contar_ocurrencia(lista : list, tamanio : int, campo : str):
    contador = 0
    for stock in range(0, tamanio): 
        if lista[stock][campo] < 3:
            contador += 1    
    return contador

            
    
biblioteca = [0,0,0,0]

biblioteca = [
    {'codigo' : 1, 'stock' : 6},
    {'codigo' : 2, 'stock' : 4},
    {'codigo' : 3, 'stock' : 2},
    {'codigo' : 4, 'stock' : 3},
    {'codigo' : 5, 'stock' : 9},
    {'codigo' : 6, 'stock' : 10},
    {'codigo' : 7, 'stock' : 5},    
]

TAMANIO = len(biblioteca)

ultimo = cargar(biblioteca, TAMANIO)

print(biblioteca)