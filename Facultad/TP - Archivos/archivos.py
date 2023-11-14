# Modulo para la manipulacion de archivos.
import os

def existe( nombre, ruta="" ):
    if os.path.exists(ruta + nombre + '.txt'):
        return True
    else:
        return False

def crear( nombre, ruta="" ):
    with open( f"{ruta + nombre + '.txt'}", "w", encoding="utf-8" ) as fichero:
        ...
    
def leer( nombre, ruta="" ):
    with open( f"{ruta + nombre + '.txt'}", "r", encoding="utf-8" ) as fichero:
        return fichero.readlines()

def escribir( datos, nombre, ruta="" ):
    with open( f"{ruta + nombre + '.txt'}", "w", encoding="utf-8" ) as fichero:
        fichero.writelines( datos )

def eliminar( nombre, ruta="" ):
    os.remove(ruta + nombre + '.txt')

def renombrar( nombre_actual, nombre_nuevo , ruta="" ):
    os.rename( ruta + nombre_actual + '.txt', ruta + nombre_nuevo + '.txt' )

def listado():
    directorio = os.scandir()
    lista = []
    for archivo in directorio:
        if "." in  archivo.name:
            nombre, extension = archivo.name.rsplit('.',1)
            if extension == "txt" or extension == 'py':
                lista.append({'nombre' : nombre, 'extension' : "."+extension, 'tamanio' : archivo.stat().st_size})
    return lista