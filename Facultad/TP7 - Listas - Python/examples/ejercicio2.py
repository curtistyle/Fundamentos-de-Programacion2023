""" Sea un lote de Números enteros positivos que finaliza con un cero que no debe ser 
procesado. Generar un vector con dichos valores y calcular la productoria de sus 
componentes. """

# definir lista
lista_de_numeros = []

def cargar_lista(lista):
    numero = int(input("Ingrese un numero: "))
    while (numero != 0):
        lista.append(numero)
        numero = int(input("Ingrese un numero: "))

def productoria(lista):
    resultado = 1
    for indice in range(0,len(lista)):
        resultado = resultado * lista[indice]
    return resultado

cargar_lista(lista_de_numeros)

print(f"El producto de todos los elementos de la lista da como resultado: {productoria(lista_de_numeros)}")