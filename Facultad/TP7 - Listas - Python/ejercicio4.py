"""Generar y emitir el vector A = (1,0,1,0,1,0, ...) de N elementos."""

def crear_lista(tamanio : int):
    """Crea una `lista` de n elementos"""
    vector = [None] * tamanio
    return vector, tamanio

def cargar_lista(tamanio : int, vector : list):
    """Carga una `lista` asignandole a cada posicion de la misma un valor"""
    for indice in range(0, tamanio):
        vector[indice] = int(input(f"Ingrese un elemento en la posicion #{indice+1}: "))

def recorrer_lista(tamanio : int, vector : list):
    """Recorre la lista y muetra sus elementos"""
    print("Elementos de la lista: ")
    for indice in range(0, tamanio):
        print(f"{indice=} valor={vector[indice]}")
        
def mostrar_lista(vector : list):
    print(vector)

def generar_lista1(tamanio : int, vector : list):
    for indice in range(0, tamanio):
       vector[indice] = 1 if indice % 2 == 0 else 0

def generar_lista2(tamanio : int, vector : list):
    for indice in range(0, tamanio):
        vector[indice] = indice % 2
        
        
tamanio = int(input("Ingrese el tamaño de la lista: "))

lista_numeros1,tamanio = crear_lista(tamanio)

generar_lista1(tamanio,lista_numeros1)

print("Lista 1:")
mostrar_lista(lista_numeros1)

# recorrer_lista(tamanio,lista_numeros1)

lista_numeros2,tamanio = crear_lista(tamanio)

generar_lista2(tamanio,lista_numeros2)

print("Lista 2:")
mostrar_lista(lista_numeros2)

# recorrer_lista(tamanio,lista_numeros2)