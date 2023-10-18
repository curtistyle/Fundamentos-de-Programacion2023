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
    
tipo_stock = {
    'cod_art' : int,
    'descripcion' : str,
    'cantidad' : int,
    'precio_unitario' : float
}

def insertar():
    stock = tipo_stock
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
    
    if (indice > 0):
        return (indice + 1)
    else:
        return 0
   
def mostrar_todo(lista : list, ultimo : int):
    for stock in range(0, ultimo):
        print(lista[stock]['cod_art']) 
        print(lista[stock]['descripcion']) 
        print(lista[stock]['cantidad']) 
        print(lista[stock]['precio_unitario']) 

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

ultimo = cargar(lyst, TAMANIO)
print("ultimo=",ultimo)
print(lyst)
# mostrar(lyst, ultimo)



