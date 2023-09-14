# lista = []
# lista = lista + [0]
# print(">>>",lista)

# lista = lista + [0]
# print(">>>",lista)

def crear_lista(tamanio : int):
    vector = []
    for indice in range(0, tamanio):
        vector = vector + [None]
    return vector

def burbuja(lista,lim):
    for i in range(0,(len(lista)-1)-1):
        for j in range(0,len(lista)-1-i):
            if (lista[j] > lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                

def cargar_lista_dinamica():
    i = 0
    vector = [0]
    valor = int(input("Ingrese un valor: "))
    vector[i] = valor
    while valor != 0:
        i += 1
        vector[i] = vector[i] + [valor] 
        valor = int(input("Ingrese un numero: "))
        if valor == 0: break
    return vector
         
lista = cargar_lista_dinamica()

print(lista)
# lista = crear_lista(5)
# print(lista)
    