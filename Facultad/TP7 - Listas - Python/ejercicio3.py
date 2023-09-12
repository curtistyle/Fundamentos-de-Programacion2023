""" Leer un vector de N  elementos, de a uno por vez. Generar y emitir la sumatoria de sus 
componentes de posición par.  """

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

def sumatoria_par(tamanio : int, vector : list):
    """Devuelve la `sumatoria` de los numeros con `indice` par de la `lista`"""
    sumatoria = 0
    for indice in range(0,tamanio):
        if ((indice % 2) == 0):
            sumatoria = sumatoria + vector[indice]
    return sumatoria


tamanio = int(input("Ingrese el tamaño de la lista: "))

lista_numero, tamanio = crear_lista(tamanio)

cargar_lista(tamanio,lista_numero)

print("La sumatoria de los numeron con indice par de la lista es: ", sumatoria_par(tamanio, lista_numero))


