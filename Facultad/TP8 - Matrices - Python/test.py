# # for i in range(0,4):
# #     print("Hola 1",end='  ')
# # print()
# # for i in range(0,4):
# #     print("Hola 1",end='  ')

# # monto = 123

# # print(type(str()) == type(monto))


# head = ["#", "Columna B", "Columna C"]

matriz = [
    [1, 90932, 59403],
    [ 2,  4092,  3498],
    [  3,   235,   985],
    [   4,    12,    55],
    [5, 90932, 59403],
    [ 6,  4092,  3498],
    [  7,   235,   985],
    [   8,    12,    55],
    [9, 90932, 59403],
    [ 10,  4092,  3498],
    [  11,   235,   985],
    [   12,    12,    55],
    [13, 90932, 59403],
    [ 14,  4092,  3498],
    [  15,   235,   985],
    [   16,    12,    55]
]

# # header
# t_head = ""
# separacion = 5
# for element in head:
#     t_head += " | " + (" " * separacion) + element + (" " * separacion)
# t_head += " |"
# head_zise = len(t_head) - 3

# # top_head = (" |" + "=" * head_zise) + "| "
# # print(top_head)
# # print(t_head)
# # print(top_head)

# top_head = " |"
# for element in enumerate(head):
#     top_head += ("=" * (head_zise//3)) + ("+" if element[0] < len(head)-1 else "|")

# print(top_head)
# print(t_head)
# print(top_head)

# filas = 16
# columnas = 3

# tamanio = head_zise//len(head)
# content = ""
# for fila in range(0, filas):
#     for columna in range(0, columnas):
#         content += " | " + f"{matriz[fila][columna]:>{tamanio-2}}"
#     content += " |\n"

# print(content + top_head)


# import tableprint as tp
# import numpy as np
# # pip install numpy
# # pip install tableprint

# data = np.random.randn(10, 3)
# headers = ['Column A', 'Column B', 'Column C']

# tp.table(matriz, headers)

