"""
En una distribuidora se lleva mensualmente, la siguiente información: código de producto, cantidad 
vendida,  costo  de  fabricación  del  producto  (por  unidad),  precio  unitario  de  venta  al  público.  Se 
desea  calcular:  
    a - Cual fue el producto más vendido.  
    b - Cual fue la ganancia que se obtuvo al vender dicho producto (en x cantidad). 
    c - Cual es el costo unitario del producto más caro.
"""

def insertar():
    producto = { 'codigo' : int, 'cantidad' : int, 'costo_fabricacion' : float, 'precio_venta' : float }
    producto['codigo'] = int(input("Ingrese el codigo del producto: "))
    producto['cantidad'] = int(input("Ingrese la cantidad del producto: "))
    producto['costo_fabricacion'] = float(input("Ingrese el costo de fabricación del producto: "))
    producto['precio_venta'] = float(input("Ingrese el precio de venta del producto: "))
    return producto

def cargar(lista : list, tamanio : int):
    indice = 0
    print()
    opc = input(" - ¿Quiere ingresar un producto? (s/n): ")
    while (( opc.upper() == 'S' ) or (len(lista) < tamanio)):
        print(f" # Libro {indice + 1}")
        producto = insertar()  
        lista[indice] = producto
        opc = input(" - ¿Quiere ingresar un producto? (s/n): ")
        indice += 1
        print()
    if (indice > 0):
        return (indice + 1)
    else:
        return 0

def mayor(lista : list, tamanio : int, campo : str):
    mayor = lista[0][campo]
    for stock in range(0, tamanio):
        if lista[stock][campo] > mayor:
            mayor = lista[stock][campo]
            posicion = stock
    return posicion

def ganancia(producto : dict):
    ganancia = (producto['precio_venta'] - producto['costo_fabricacion']) * producto['cantidad']
    return ganancia

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

def burbuja(lista : list, clave : str) -> None:
    """Metodo de ordenamiento burbuja"""
    for i in range(0,(len(lista)-1)):
        for j in range(0,(len(lista)-1)-i):
            if lista[j][clave] > lista[j+1][clave]:
                aux               = lista[j][clave]
                lista[j][clave]   = lista[j+1][clave]
                lista[j+1][clave] = aux

distribuidora = [
    { 'codigo' : 3, 'cantidad' : 40, 'costo_fabricacion' : 200, 'precio_venta' : 2200 },
    { 'codigo' : 1, 'cantidad' : 50, 'costo_fabricacion' : 100, 'precio_venta' : 1200 },
    { 'codigo' : 5, 'cantidad' : 300, 'costo_fabricacion' : 20, 'precio_venta' : 50 },
    { 'codigo' : 4, 'cantidad' : 200, 'costo_fabricacion' : 30, 'precio_venta' : 100 },
    { 'codigo' : 2, 'cantidad' : 100, 'costo_fabricacion' : 50, 'precio_venta' : 200 },
    0,
    0,
]

ultimo = 5

# TODO: a - Cual fue el producto más vendido.  

resultado = mayor( distribuidora, ultimo, 'cantidad' )
print(f"El producto más vendido es: \n"
      f" - Codigo: {distribuidora[resultado]['codigo']}.\n"
      f" - Cantidad: {distribuidora[resultado]['cantidad']}.\n"
      f" - Costo de fabricación: {distribuidora[resultado]['costo_fabricacion']}.\n"
      f" - Precio de venda: {distribuidora[resultado]['precio_venta']}.\n"
      )

# TODO: b - Cual fue la ganancia que se obtuvo al vender dicho producto (en x cantidad). 

buscado = int( input( "Ingrese el codigo del producto del que desea saber su ganancia: " ) )
burbuja(distribuidora, 'codigo')
posicion = busqueda_binaria( distribuidora, ultimo, buscado, 'codigo' )
if posicion != -1:
    resultado = ganancia( distribuidora[posicion] )
    print( f" # La ganancia del producto con el codigo {buscado} es: $ {resultado:.2f}." )
else:
    print( f" # El codigo de producto ({buscado}) no existe." )

# TODO: c - Cual es el costo unitario del producto más caro.

posicion = mayor( distribuidora, ultimo, 'precio_venta' )
print( f" # El producto mas caro es cod:{distribuidora[posicion]['codigo']} con un precio unitario: ${distribuidora[posicion]['precio_venta']}" )

