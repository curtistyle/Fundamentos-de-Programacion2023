def quitar( texto : list, numero_fila : int ):
    n_filas = len( texto )
    
    if ( ( numero_fila > 0 ) and ( numero_fila <= len( texto ) ) ):
        for fila in range( numero_fila - 1, n_filas -1 ):
            texto[fila] = texto[fila + 1]
        texto.pop(n_filas - 1) # ! cambiar
        return texto
    
def añadir( texto : list , linea : str, posicion=0 ):
    n_filas = len( texto )
    
    if ( ( posicion > 0 ) and (posicion <= (n_filas + 1) ) ):
        aux = texto + [""]
        for fila in range( posicion - 1, n_filas):
            aux[fila + 1] = texto[fila]
        aux[posicion - 1] = linea + "\n"
        return aux
    else:
        print( f"Error!, posicion fuera de rango." )
        return None

def reemplazar( texto : list, linea : str, posicion ):
    n_filas = len( texto )
    
    if ( ( posicion > 0 ) and (posicion <= n_filas ) ):
        texto[posicion - 1] = linea + "\n"
        return texto
    else:
        print( f"Error!, posicion fuera de rango." )
        return None
    
def mostrar( texto : list ):
    for fila in range( 0, len( texto ) ):
        print( f"{(fila+1):<2} | {texto[fila]}", end="" ) 