""" Se lee un vector de Números enteros y se desea saber si entre dichos números se encuentra
    un valor leído previamente. En caso afirmativo, visualizar su posición en la lista. Resolver el
    problema por:
        a- Búsqueda secuencial.
        b- Búsqueda binaria.
 """

def cargar_lista_dinamica(hasta):
    vector = []
    valor = int(input("Ingrese un valor: "))
    while valor != hasta:
        print(vector)
        vector = vector + [valor]
        valor = int(input("Ingrese un valor: "))
    return vector, len(vector)

def busqueda_secuencia(buscado, vector : list, tamanio : int, inicio=0):
    pos = -1
    for indice in range(inicio, tamanio):
        if (buscado == vector[indice]):
             pos = indice
             break
    return pos
