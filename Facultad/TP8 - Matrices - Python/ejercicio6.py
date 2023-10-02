"""  
Se tiene un listado con los siguientes datos: Número de alumno ( 1 a n ) , número de materia ( 1 a m ),
 nota ( 0 a 10 ). 
    o El mismo número de alumno y de materia puede aparecer más de una vez. 
    o El listado no está ordenado, ni necesariamente completo. Esto último quiere decir que puede 
      ser que un alumno no haya cursado una o más materias, y por lo tanto no existan los datos 
      correspondientes en el listado. 
Se pide:  
 
    a- Crear una estructura bidimensional que almacene el promedio por materia de cada 
       alumno e informarla asignándole en la impresión un guión en caso de faltar datos. 
    b- Informar el porcentaje de alumnos que cursó cada materia y el promedio general por 
       materia considerando los alumnos que la cursaron. 
    c- Informar la cantidad de materias que cursó cada alumno y el promedio que obtuvo 
       considerando las materias que cursó.
"""
from msvcrt import getwch


def crear_lista(tamanio : int):
    vector = [None] * tamanio
    return vector, tamanio

def cargar_lista(vector : list, tamanio : int):
    for indice in range(0, tamanio):
        vector[indice] = indice + 1

def busqueda_binaria(lista, tamanio, buscado, posicion=-1):
    primero = 0
    ultimo  = tamanio - 1
    while (posicion == -1) and (primero <= ultimo):
        medio = (primero + ultimo) // 2
        if (lista[medio] == buscado):
            posicion = medio
        elif (lista[medio] >= buscado):
            ultimo   = medio - 1
        else:
            primero  = medio + 1   
    return posicion

if __name__=="__main__":
    
    
    tamanio = int(input("Ingrese la cantidad de alumnos: "))
    alumnos = crear_lista(tamanio)

    tamanio = int(input("Ingrese la cantidad de materias: "))
    materias = crear_lista(tamanio)

    # tamanio = int(input("Ingrese la cantidad de materias: "))
    # notas = crear_lista(tamanio)


    for alumno in range(0, len(alumnos)):
        
        numero = int(input("Ingrese el numero de alumno: "))
        alumnos[alumno] = 
        for materia in range(0, len(materias)):
            print(f"Ingrese la nota de la materia '{materia + 1}' (s/n)")
            if (getwch() == 's'):
                materias[materia] = float(input("Nota: "))
            else:
                materias[materia] = None
            