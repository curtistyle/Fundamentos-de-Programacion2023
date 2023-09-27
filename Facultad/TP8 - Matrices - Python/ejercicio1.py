""" Calcular la media de una lista de 25 estudiantes de una clase de informática con notas en cuatro 
materias. """





# for i in range(len(matriz)):
#     print(f"Fila ({i+1}): ")
#     for j in range(len(matriz[0])):
#         print(f"Columna ({j+1}): ")
#         matriz[i][j] = int(input('ingrese el elemento: '))
# print(matriz)


def cargar_matriz(matriz : list, filas, columnas):
    for i in range(0, filas):
        print(f"Ingrese las notas de la materia {i+1}: ")
        for j in range(0, columnas):
            matriz[i][j] = int(input(f"Alumno {j+1}: "))

def determinar_promedio(matriz : list, filas : int, columnas : int):
    total_alumnos = filas * columnas
    acomulador = 0
    for fila in range(0, filas):
        for columna in range(0, columnas):
            acomulador = acomulador + matriz[fila][columna]
    return acomulador / total_alumnos


def mostrar_matriz(matriz : list, filas, columnas):
    for fila in range(0, filas):
        fila_print = f"Materia {fila + 1}: "
        for columna in range(0, columnas):
            fila_print += str(matriz[fila][columna]) + "  "
        print(fila_print)


if __name__=='__main__':
    # matriz=[[0,0,0],[0,0,0,]]
    # len(matriz) devuelve la cantidad de filas
    # len(matriz[0]) devuelve la cantidad de columnas

    # lista = [
    #     [0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0],
    # ]


    materia1 = [0,0,0,0,0]
    materia2 = [0,0,0,0,0]
    materia3 = [0,0,0,0,0]
    materia4 = [0,0,0,0,0]

    lista = [materia1, materia2, materia3, materia4]
    
    filas = len(lista)
    columnas = len(lista[0])

    cargar_matriz(lista, filas, columnas)

    mostrar_matriz(lista, filas, columnas)

    promedio = determinar_promedio(lista, filas, columnas)

    print(f"El promedio total de todos los alumnos en las cuatros materias es: {promedio:2}")