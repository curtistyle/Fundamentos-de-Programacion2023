# Modulo para la manipulacion de archivos.
import os

def existe( nombre, ruta="" ):
    """Retorna `True` si existe el `nombre` del fichero donde se ejecuto el script. Tambien podemos pasarle otra `ruta`."""
    if os.path.exists(ruta + nombre + '.txt'):
        return True
    else:
        return False

def crear( nombre, ruta="" ):
    """Crea un archivo de texto mediante un `nombre`. La `ruta` es opcional"""
    with open( f"{ruta + nombre + '.txt'}", "w", encoding="utf-8" ) as fichero:
        ...
    
def leer( nombre, ruta="" ):
    """Lee un archivo de texto mediante un `nombre`. La `ruta` es opcional"""
    with open( f"{ruta + nombre + '.txt'}", "r", encoding="utf-8" ) as fichero:
        return fichero.readlines()

def escribir( datos, nombre, ruta="" ):
    """Escribe en un archivo de texto mediante un `nombre`. La `ruta` es opcional"""
    with open( f"{ruta + nombre + '.txt'}", "w", encoding="utf-8" ) as fichero:
        fichero.writelines( datos )

def eliminar( nombre, ruta="" ):
    """Elimina un archivo de texto mediante un `nombre`. La `ruta` es opcional"""
    os.remove(ruta + nombre + '.txt')

def renombrar( nombre_actual, nombre_nuevo , ruta="" ):
    """Renombra un archivo de texto mediante un `nombre_actual` y lo remplaza por un `nombre_nuevo`. La `ruta` es opcional"""
    os.rename( ruta + nombre_actual + '.txt', ruta + nombre_nuevo + '.txt' )

def listado():
    """Listado de archivos del directorio donde se ejecuta el script"""
    directorio = os.scandir()
    lista = []
    i = 1
    for archivo in directorio:
        if "." in  archivo.name:
            nombre, extension = archivo.name.rsplit('.',1)
            if extension == "txt" or extension == 'py':
                lista.append({'id' : str(i), 'nombre' : nombre, 'extension' : "."+extension, 'tamanio' : archivo.stat().st_size})
                i += 1
    return lista

def nombre_por_id( nombre : str, lista : list ):
    """Retorna el nombre del archivo del directoria mediante un id o nombre."""
    if nombre.isalnum():
        for indice in range( 0, len( lista ) ):
            if lista[ indice ]['id'] == nombre:
                return lista[ indice ][ 'nombre' ]
        return nombre
    else:
        return nombre