"""
En una distribuidora se lleva mensualmente, la siguiente información: código de producto, cantidad 
vendida,  costo  de  fabricación  del  producto  (por  unidad),  precio  unitario  de  venta  al  público.  Se 
desea  calcular:  
    a - Cual fue el producto más vendido.  
    b - Cual fue la ganancia que se obtuvo al vender dicho producto (en x cantidad). 
    c - Cual es el costo unitario del producto más caro.
"""

tipo_producto = { 'codigo' : int, 'cantidad' : int, 'costo_fabricacion' : float, 'precio_venta' : float }


def insertar():
    producto = tipo_producto
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

#    Ganancia = (PrecioVenta - PrecioCompra) * CantidadVendida
def ganancia(producto : dict):
    ganancia = (producto['monto'] - producto['costo_fabricacion']) * producto[['cantidad']]
    return ganancia

distribuidora = [
    { 'codigo' : 1, 'cantidad' : 50, 'costo_fabricacion' : 100, 'precio_venta' : 1200 },
    { 'codigo' : 2, 'cantidad' : 100, 'costo_fabricacion' : 50, 'precio_venta' : 200 },
    { 'codigo' : 3, 'cantidad' : 40, 'costo_fabricacion' : 200, 'precio_venta' : 2200 },
    { 'codigo' : 4, 'cantidad' : 200, 'costo_fabricacion' : 30, 'precio_venta' : 100 },
    { 'codigo' : 5, 'cantidad' : 300, 'costo_fabricacion' : 20, 'precio_venta' : 50 },
    0,
    0,
]

