""" Escribir un programa que lea los valores de c/campo de un registro de stock de un  almacén. Los 
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

# consistencia de datos
def codigo_articulo(dato, error):
    if dato < 0:
        return f"error, dato fuera de rango {dato}"
    else:
        return None

def descipcion(dato, error):
    
    ...
def insertar(error):
    stock = tipo_stock
    
    stock = input("Ingrese el codigo de aticulo: ")...