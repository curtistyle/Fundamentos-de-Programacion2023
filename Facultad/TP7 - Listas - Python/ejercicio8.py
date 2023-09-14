""" Leer un vector de N elementos. Emitir el valor mínimo y la cantidad de veces que se repitió 
ese valor.  """

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

def minimo(tamanio : int, vector : list):
    """Determina el minimo elemento de la lista."""
    aux = vector[0]
    for indice in range(1, tamanio):
        if vector[indice] < aux:
            aux = vector[indice]
    # aux = valor minimo
    return aux

def ocurrencias(tamanio : int, vector : list, minimo : int):
    """Determina las ocurrencias de un valor dado (`minimo`) en una lista"""
    contador = 0
    for indice in range(0, tamanio):
        if (minimo == vector[indice]):
            contador += 1
    return contador

if __name__=="__main__":
    lista_numeros, tamanio = crear_lista(5)
    cargar_lista(lista_numeros)
    print(lista_numeros)

    print(f"El valor minimo de la lista de numeros es: {minimo(tamanio, lista_numeros)}.")
    print(f"El valor minimo se repitio {ocurrencias(tamanio, lista_numeros, minimo)} veces.")



