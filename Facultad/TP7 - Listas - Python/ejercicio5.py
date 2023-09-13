""" Leer un vector de 10 elementos reales y emitir las siguientes leyendas según, 
corresponda:  “El  vector  tiene  todas  sus  componentes  positivas”,  “El  vector  tiene 
componentes negativas”, “El vector tiene algún cero”. """


def crear_lista(tamanio : int):
    vector = [None] * tamanio
    return vector, tamanio

def cargar_lista(tamanio : int, vector : list):
    for indice in range(0, tamanio):
        vector[indice] = float(input(f"Ingrese un elemento en la posicion #{indice+1}: "))

def recorrer_lista(tamanio : int, vector : list):
    print("Elementos de la lista: ")
    for indice in range(0, tamanio):
        print(f"{indice=} valor={vector[indice]}")
        
def contar_ocurrencias(tamanio : int, vector : list):
    ocurrencias = [0, 0, 0]
    for indice in range(0, tamanio):
        if vector[indice] > 0:
            ocurrencias[0] += 1
        elif vector[indice] < 0:        
            ocurrencias[1] += 1
        else:
            ocurrencias[2] += 1
    return ocurrencias            
            

#lista_numeros, tamanio = crear_lista(10)

#cargar_lista(tamanio, lista_numeros)

tamanio = 10
lista_numeros = [10,0,-21,45,86,65,32,33,11,44]

lista_ocurrencias = contar_ocurrencias(tamanio, lista_numeros)

print(lista_ocurrencias)

if lista_ocurrencias[0] == tamanio:
    """Si en la `lista_ocurrencias` en la posicion 0 tiene el mismo 
    valor que el tamanio de la lista de numeros, entonces todas sus 
    componentes son positivas."""
    print("El vector tiene todas sus compenentes positivas.")
if lista_ocurrencias[1] > 0:
    """Si en la `lista_ocurrencias` en la posicion 1 el valor es mayor que 0, 
    entonces tiene al menos alguna componente negativa."""
    print("El vector tiene componentes negativas.")
if lista_ocurrencias[2] > 0:
    """Si en la `lista_ocurrencias` en la posicion 3 el valor es mayor que 0,
    entonces tiene al menos un valor en alguna de sus componentes igual a cero."""
    print("El vector Tiene algun cero.")


