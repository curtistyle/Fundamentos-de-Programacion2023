
def crear_lista(tamanio : int):
    vector = [None] * tamanio
    return vector, tamanio

def cargar_lista(tamanio : int, vector : list):
    for indice in range(0, tamanio):
        vector[indice] = int(input(f"Ingrese un elemento en la posicion #{indice+1}: "))

def recorrer_lista(tamanio : int, vector : list):
    print("Elementos de la lista: ")
    for indice in range(0, tamanio):
        print(f"{indice=} valor={vector[indice]}")

def mostrar_lista(vector : list):
    print(vector)

def sumatoria(tamanio : int, vector : list):
    resultado = 0
    for indice in range(0,tamanio):
        resultado += vector[indice]
    return resultado



lista_numeros, limite = crear_lista(5)

cargar_lista(limite, lista_numeros)

print(f'La suma de los elementos de lista da como resultado:', sumatoria(limite,lista_numeros))

recorrer_lista(limite, lista_numeros)

mostrar_lista(lista_numeros)