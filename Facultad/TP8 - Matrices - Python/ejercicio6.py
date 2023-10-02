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
import tableprint as tp

def crear_lista(tamanio : int):
    vector = [None] * tamanio
    return vector, tamanio

def cargar_lista(vector : list, tamanio : int):
    for indice in range(0, tamanio):
        vector[indice] = indice + 1

def busqueda_binaria(lista, tamanio, buscado):
    primero  = 0
    ultimo   = tamanio - 1
    posicion = None
    while (posicion == -1) and (primero <= ultimo):
        medio = (primero + ultimo) // 2
        if (lista[medio] == buscado):
            posicion = medio
        elif (lista[medio] >= buscado):
            ultimo   = medio - 1
        else:
            primero  = medio + 1   
    return posicion

def burbuja(lista : list):
    for i in range(0, (len(lista) - 1) - 1):
        for j in range(0, len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                aux          = lista[j]
                lista[j]     = lista[j + 1]
                lista[j + 1] = aux

def crear_matriz(filas : int, columnas : int, valor=None):
    """Crea una matriz de 'n' `filas` y 'n' `columnas` e inicializa la matriz con x `valor`."""
    if ((filas > 0) and (columnas > 0)):
        matriz = []
        for fila in range(filas):
            matriz = matriz + [[]]
            for columna in range(columnas):
                matriz[fila] = matriz[fila] + [valor]
        return matriz
    else:
        return None
    
def mostrar_matriz(matriz : list, filas : int, columnas : int):
    """Muestra la matriz en forma de bloque."""
    from colorama import Fore, Style
    for fila in range(0, filas):
        print(f"Materia {fila + 1}:",end="  ")
        for columna in range(0, columnas):
            print(f"{Fore.RED}{matriz[fila][columna]}{Style.RESET_ALL}",end="  ")
        print()
        
        
def promedio_fila(matriz : list, filas : int, columnas : int):
    """retorna una `lista` con los promedio de cada una de las `fila` de una `matriz`"""
    promedios = [0] * filas
    for fila in range(0, filas):
        contador = 0
        for columna in range(0, columnas):
            if (matriz[fila][columna] != '-'):
                promedios[fila] += matriz[fila][columna]
                contador += 1
        promedios[fila] = round((promedios[fila] / contador), 2)
    return promedios
                
def porcentaje_fila(matriz : list, filas : int, columnas : int):
    """Retorna una `lista` con los `porcentajes` de `elementos` que existen en cada `fila`"""
    porcentaje = [0] * filas
    for fila in range(0, filas):
        contador = 0    
        for columna in range(0, columnas):
            if (matriz[fila][columna] != '-'):
                contador += 1
        porcentaje[fila] = round(((contador * 100) / filas),2)
    return porcentaje     
   
def items_columna(matriz : list, filas : int, columnas : int):
    """Retorna una `lista` con la `cantidad` de `item` que existen en c/u de las `columnas` de un `matriz`"""
    items = [0] * columnas
    for columna in range(0, columnas):
        contador = 0
        for fila in range(0, filas):
            if (matriz[fila][columna] != '-'):
                contador += 1
        items[columna] = contador
    return items

def promedio_columna(matriz : list, filas : int, columnas :int):
    promedios = [0] * columnas
    for columna in range(0, columnas):  
        contador = 0
        for fila in range(0, filas):
            if (matriz[fila][columna] != '-'):
                contador += 1
                promedios[columna] += matriz[fila][columna]
        promedios[columna] = round((promedios[columna] / contador), 2)
    return promedios

def invertir_matriz(matriz : list, filas : int, columnas : int):
    nueva_matriz = crear_matriz(columnas, filas)
    for fila in range(0, filas):
        for columna in range(0, columnas):
            nueva_matriz[columna][fila] = matriz[fila][columna]
    return nueva_matriz

if __name__=="__main__":

    # (1, Matematica ; 2, Historia ; 3, Ciencias Politicas ; 4, Programación ; 5, Ingles)

    # [[numero_alumno,numero_materia,nota], [numero_alumno,numero_materia,nota]]

    lista = [
        [3,4,7],
        [2,1,8],
        [5,2,9],
        [1,3,4],
        [2,2,5],
        [4,5,10],
        [3,5,3],
        [1,1,3],
        [3,2,4],
        [4,3,8],
        [5,3,7],
        [5,4,3],
        [5,1,5],
        [2,4,7],
        [4,2,6]
    ]
    
    filas = 5 # alumnos
    columnas = 5 # materias
    
    matriz = crear_matriz(filas, columnas, "-")

    for indice in range(0, len(lista)):
        alumno = lista[indice][0] - 1
        materia = lista[indice][1] - 1
        matriz[materia][alumno] = lista[indice][2]
   
    # * TABLA 1
    headers = ['Alumno 1', 'Alumno 2', 'Alumno 3', 'Alumno 4', 'Alumno 5']
    tp.table(matriz, headers)
    
    
    
    # (b) calcula el porcentaje de alumos que curso cada materia
    porcentaje_alumnos = porcentaje_fila(matriz,filas,columnas)
    
    # (b) calcula el promedio por materia teniendo en cuenta la cantidad de alumnos que la cursaron
    promedio_materia = promedio_fila(matriz, filas ,columnas)
    
    """     c- Informar la cantidad de materias que cursó cada alumno y el promedio que obtuvo 
       considerando las materias que cursó. """
       
    # (c) determina la cantidad de materias que curso cada alumno
    cantidad_materias_alumno = items_columna(matriz, filas, columnas)
    
    # (c) determina el promedio que obtubo cada alumno teniendo en cuenta la cantidad de materias que curso.
    promedio_materias_alumno = promedio_columna(matriz, filas, columnas)
    
    
    # * TABLA 2: 
    headers = ["Nº Materia","% Alumnos", "Σ Alumnos"]
    datos = [
        [i+1 for i in range(0,len(porcentaje_alumnos))],
        porcentaje_alumnos,
        promedio_materia
    ]
    datos = invertir_matriz(datos, len(datos), len(datos[0]))
    tp.table(datos, headers)
    print("% Alumnos: Porcentaje de Alumnos, Σ Alumnos: Promedio Alumnos")
    
    
    # * TABLA 3: 
    headers = ["Nº Alumno","± Materias", "Σ Materias"]
    datos = [
        [i+1 for i in range(0,len(cantidad_materias_alumno))],
        cantidad_materias_alumno,
        promedio_materias_alumno
    ]
    datos = invertir_matriz(datos, len(datos), len(datos[0]))
    tp.table(datos, headers)
    print("± Materia: Cantidad de Materias cursadas, Σ Materias: Promedio Materias")