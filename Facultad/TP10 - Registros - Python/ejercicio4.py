""" Escribir un programa que lea los valores de c/campo de un registro de stock de un almacén. Los 
    campos son: 
    - Cod_art: integer; 
    - Descripción: string [30]; 
    - Cantidad: word; (0 ..65535) 
    - Precio_unitario: real;  
 
Se pide además: 
    a-  Cargar datos hasta que el cod_art = 0. 
    b-  Mostrar del artículo más caro, cantidad en existencia.  
    c-  Dado un cod_articulo ver si existe. 
    d-  Mostrar si este almacén vende queso “Don Bautista”.  
    e-  Mostrar el artículo con menor existencia. 
    f-  Mostrar cual es el artículo más barato. """
    
def insertar():
    stock = { 'cod_art' : int, 'descripcion' : str, 'cantidad' : int, 'precio_unitario' : float }
    sentinela = int(input("Ingrese el codigo del articulo: "))
    if sentinela != 0:
        stock['cod_art'] = sentinela
        stock['descripcion'] = input("Ingrese la descipcion del articulo: ")
        stock['cantidad'] = int(input("Ingrese la cantidad de articulos: "))
        stock['precio_unitario'] = float(input("Ingrese el precio unitario: "))
    return stock, sentinela

def cargar(lyst : list, tamanio : int):
    indice = 0
    print(f" # Stock {indice + 1}")
    stock, sentinela = insertar()
    print()
    while ((sentinela != 0) or (len(lyst) < tamanio)):
        lyst[indice] = stock
        indice += 1
        print(f" # Stock {indice + 1}")
        stock, sentinela = insertar() 
        print()
    return indice
   
def mostrar_todo(lista : list, ultimo : int):
    for stock in range(0, ultimo):
        print(f"Articulo {stock + 1}.")
        print(f"Codigo Articulo = {lista[stock]['cod_art']}") 
        print(f"Descripcion     = {lista[stock]['descripcion']}") 
        print(f"Cantidad        = {lista[stock]['cantidad']}") 
        print(f"Precio Unitario = {lista[stock]['precio_unitario']}") 
        print()

def mostrar(lista : list, posicion : int, campos : list):
    for indice in range(0, len(campos)):
        print(f"{campos[indice]}={lista[posicion][campos[indice]]}")
        

def mayor(lista : list, tamanio : int, campo : str):
    mayor = lista[0][campo]
    for stock in range(0, tamanio):
        if lista[stock][campo] > mayor:
            mayor = lista[stock][campo]
            posicion = stock
    return posicion

def menor(lista : list, tamanio : int, campo : str):
    menor = lista[0][campo]
    for stock in range(0, tamanio):
        if lista[stock][campo] < menor:
            menor = lista[stock][campo]
            posicion = stock
    return posicion

def burbuja(lista : list, clave : str):
    for i in range(0,(ultimo-1)):
        for j in range(0,(ultimo-1)-i):
            if lista[j][clave] > lista[j+1][clave]:
                aux               = lista[j][clave]
                lista[j][clave]   = lista[j+1][clave]
                lista[j+1][clave] = aux

def busqueda_binaria(lista : list, tamanio : int, buscado, clave, posicion=None) -> int:
    primero = 0
    ultimo  = tamanio - 1
    while (posicion == None) and (primero <= ultimo):
        medio = (primero + ultimo) // 2
        if (lista[medio][clave] == buscado):
            posicion = medio
        elif (lista[medio][clave] >= buscado):
            ultimo   = medio - 1
        else:
            primero  = medio + 1   
    return posicion



lyst = [0,0,0,0]

lyst = [
    { 'cod_art' : 2, 'descripcion' : "Papa", 'cantidad' : 12, 'precio_unitario' : 100 },
    { 'cod_art' : 3, 'descripcion' : "Tomate", 'cantidad' : 30, 'precio_unitario' : 120 },
    { 'cod_art' : 4, 'descripcion' : "Queso Don Bautista", 'cantidad' : 8, 'precio_unitario' : 200 },
    { 'cod_art' : 5, 'descripcion' : "Cebolla", 'cantidad' : 10, 'precio_unitario' : 80 },
    0,
    0
    ]

TAMANIO = len(lyst)

# ultimo = cargar(lyst, TAMANIO)
# print("ultimo=",ultimo)
# print(lyst)
ultimo = 4
for item in lyst:
    print(item)

# TODO: b - Mostrar del artículo más caro, cantidad en existencia.

posicion = mayor(lyst, ultimo, 'precio_unitario')
print(f"El articulo mas caro es '{lyst[posicion]['descripcion']}', cantidad: {lyst[posicion]['cantidad']} ")

# TODO: c - Dado un cod_articulo ver si existe. 

buscado = int(input("Ingrese un codigo de articulo: "))
posicion = busqueda_binaria(lyst, ultimo, buscado, 'cod_art')
if posicion != None:
    print(f"El articulo existe. ({posicion})")
else:
    print("El articulo no existe.")

# TODO: d - Mostrar si este almacén vende queso “Don Bautista”. 

burbuja(lyst, 'descripcion')
mostrar_todo(lyst, ultimo)

posicion = busqueda_binaria(lyst, ultimo, 'Queso Don Bautista', 'descripcion')
if posicion != None:
    print(f" 'Queso Don Bautista' EXISTE en el almacen.")
else:
    print(f" 'Queso Don Bautista' NO EXISTE en el almacen.")

# TODO: e - Mostrar el artículo con menor existencia. 

posicion = menor(lyst, ultimo, 'cantidad')
print(f"El articulo con menor existencia es '{lyst[posicion]['descripcion']}'.")

# TODO: f - Mostrar cual es el artículo más barato.

posicion = menor(lyst, ultimo, 'precio_unitario')
print(f"El articulo mas barato es '{lyst[posicion]['descripcion']}'")


