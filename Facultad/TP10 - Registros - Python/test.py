# class Persona():
#     name = ""
#     last_name = ""
#     year = 0
   
# persona1 = Persona()

# persona1.name = "Carlos"
# persona1.last_name = "Martinez"
# persona1.year = 32

# print(persona1.name)
# print(persona1.last_name)
# print(persona1.year)

# persona2 = Persona()
# persona2.name = "Marta"
# persona2.last_name = "Saint Paul"
# persona2.year = 13

# print(persona2.name)
# print(persona2.last_name)
# print(persona2.year)



# personas = [
#     {'nombre' : 'Cristian', 'ciudad' : 'Concepcion del Uruguay', 'edad' : 12},
#     {'nombre' : 'Franco', 'ciudad' : 'Gualeguaychu', 'edad' : 13}
# ]

# print(personas[0].keys())

    # "María García",
    # "José Pérez",
    # "Laura Martínez",
    # "Carlos López",
    # "Ana Sánchez",
    # "David González",
    # "Laura Fernández",
    # "Juan Martínez",
    # "Marta Díaz",
    # "Antonio Pérez",
    # "Sandra Rodríguez",
    # "Francisco Sánchez",
    # "Elena Martínez",
    # "Pedro López",


# def burbuja(personas, limite):
#     for i in range(limite - 1):
#         for j in range(limite - 1 - i):
#             nombre_apellido_actual = personas[j]['apellido'] + personas[j]['nombre']
#             nombre_apellido_siguiente = personas[j + 1]['apellido'] + personas[j + 1]['nombre']
#             if nombre_apellido_actual > nombre_apellido_siguiente:
#                 aux = personas[j]
#                 personas[j] = personas[j + 1]
#                 personas[j + 1] = aux

# personas = [
#     { 'nombre' : 'María', 'apellido' : 'García', 'edad' : 18 },
#     { 'nombre' : 'José', 'apellido' : 'Pérez', 'edad' : 23},
#     { 'nombre' : 'Laura', 'apellido' : 'Martínez', 'edad' : 21},
#     { 'nombre' : 'Carlos', 'apellido' : 'Gonzalez', 'edad': 17 },
#     { 'nombre' : 'Ana', 'apellido' : 'Sánchez', 'edad': 35 },
#     { 'nombre' : 'David', 'apellido' : 'Gonzalez', 'edad' : 27 }

# ]

# print("SIN ORDENAR: ")
# for indice in range(0, len(personas)):
#     print(personas[indice])


# burbuja(personas, len(personas))

# print("ORDENADO: ")
# for indice in range(0, len(personas)):
#     print(personas[indice])


# # * [3, 3, 5, 1, 4, 3, 5, 5]
# lista = [3, 3, 5, 1, 4, 3, 5, 5]
# tamanio = 8

# resultado = [-1] * tamanio
# mayor = lista[0]
# for indice in range(0, tamanio):
#     if lista[indice] >= mayor:
#         if lista[indice] > mayor:
#             print('cambio',mayor)
#         mayor = lista[indice]
#         print(mayor)
#         input()


# def crear_matriz(filas : int, columnas : int, valor=None):
#     """Crea una matriz de 'n' `filas` y 'n' `columnas` e inicializa la matriz con x `valor`."""
#     matriz = []
#     for fila in range(filas):
#         matriz = matriz + [[]]
#         for columna in range(columnas):
#             matriz[fila] = matriz[fila] + [valor]
#     return matriz

# print(crear_matriz( 2,4 ))


# ! # Definir el tamaño de la matriz
# filas = 3
# columnas = 3

# # Crear una matriz inicializada con ceros
# matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

# # Imprimir la matriz
# for fila in matriz:
#     print(fila)


lista = ['nombre', 'apellido', 'DNI']

# def burbuja_personalizado( lista : list, ultimo : int, parametros : list ):
#     for i in range(ultimo - 1):
#         for j in range(ultimo - 1 - i):
#             elemento_actual = lista[j]['obra_social'] + lista[j]['nombre'] + lista[j]['apellido']
#             elemnto_siguiente = lista[j + 1]['obra_social'] + lista[j + 1]['nombre'] + lista[j]['apellido']
#             if elemento_actual > elemnto_siguiente:
#                 aux = lista[j]
#                 lista[j] = lista[j + 1]
#                 lista[j + 1] = aux

# for item in lista: elemento_actual += item


ordenar = "noombre>apelldio>obra_social"

print(ordenar.split('>'))
