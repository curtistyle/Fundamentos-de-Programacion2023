# lista = ["a", "b", "c", "d"]


# nueva_lista = lista + [""]

# pos = 1

# print(lista)

# for i in range( pos, len(lista) ):
#     nueva_lista[i + 1] = lista[i] 

# nueva_lista[pos] = "asd"

# print(nueva_lista)

import  archivos
data = archivos.listado()

print(data)

for item in data:
    print(item)
# txt = "Hello, welcome to my world."

# if ' ' in txt:
#     print('existe')
# else:
#     print('no existe!')