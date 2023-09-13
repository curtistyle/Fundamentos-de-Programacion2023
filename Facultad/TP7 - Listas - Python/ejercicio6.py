""" Leer un arreglo de 20 elementos de tipo carácter. Generar y emitir otro vector B tal que 
B[i] = A[i]. """

def crear_lista(tamanio : int):
    vector = [None] * tamanio
    return vector, tamanio

def cargar_lista(tamanio : int, vector : list):
    for indice in range(0, tamanio):
        vector[indice] = str(input(f"Ingrese un elemento en la posicion #{indice+1}: "))

def recorrer_lista(tamanio : int, vector : list):
    print("Elementos de la lista: ")
    for indice in range(0, tamanio):
        print(f"{indice=} valor={vector[indice]}")
        
def duplicar_lista(tamanio : int, A : list):
    B, tamanio = crear_lista(tamanio)
    for indice in range(0, tamanio):
        B[indice] = A[indice]
    return B

A, tamanio = crear_lista(20)

cargar_lista(tamanio, A)

B = duplicar_lista(tamanio, A)

print("Lista A: ")
recorrer_lista(A, tamanio)

print("Lista B: ")
recorrer_lista(B, tamanio)

