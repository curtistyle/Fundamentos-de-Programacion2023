""" Leer un vector de N elementos y emitir la posición que ocupa el mayor de ellos """

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

def determinar_mayor(tamanio : int, vector : list):
    """Retorna la posicion del elemento mayor de la lista"""
    aux = vector[0]
    for indice in range(1, tamanio):
        if vector[indice] > aux:
            maximo = indice
    return maximo

if __name__=="__main__":
    lista_numeros, tamanio = crear_lista(5)
    cargar_lista(tamanio, lista_numeros)
    print(lista_numeros)
    print(f"El  elemento mayor de la lista se encuentra en la posicion {determinar_mayor(tamanio, lista_numeros)}")
    

        
        
