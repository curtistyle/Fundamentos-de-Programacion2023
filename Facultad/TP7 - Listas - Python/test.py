
# tamanio = 5
# lista = [None] * tamanio

# def inicializar_lista(lista):
#     for indice in range(0,len(lista)):
#         lista[indice] = 0
#     return lista
        
# print(lista)

# persons = [
#     {"name" : "L. Messi", "year" : 36, "dorsal" : 10},
#     {"name" : "A. Di Maria", "year" : 35, "dorsal" : 11},
#     {"name" : "A. Varela", "year" : 22, "dorsal" : 22},
#     {"name" : "C. Medina", "year" : 21, "dorsal" : 36}
# ]

# print(f'{"Nombre":<15}{"Edad":<14}{"Dorsal":<10}')
# for person in persons:
#     print(f"{person['name']:<15}{person['year']:<14}{person['dorsal']:<10}")


# tipo_persona = {
#     "nombre"   : str(),
#     "apellido" : str(),
#     "edad"     : int(),
#     "DNI"      : int()
# }

# lista_personas = [tipo_persona] * 5

# for persona in lista_personas:
#     persona['nombre'] = input("Nombre: ")
#     persona['apellido'] = input("Apellido: ")
#     persona['edad'] = input("Edad: ")
#     persona['DNI'] = input("DNI: ")


def cargar_vector(vector, indice=0):
    num = int(input(f"({indice})Ingrese un numero: "))

    while ((num != 0) and (indice < len(vector))):
        vector[indice] = num
        indice += 1
        num = int(input(f"({indice})Ingrese un numero: "))
    return indice

lista = [None,None,None,None,None,None,None,None,None]

"""Primera carga"""
limite = cargar_vector(lista)

print('Limte: ', limite)
print(lista)

"""Segunda carga"""
limite = cargar_vector(lista,limite)

print('Limte: ', limite)
print(lista)

"""Recorrer vector"""
def mostrar_vector(vector, limite):
    for indice in range(0, limite):
        print(f"({indice}) valor: {vector[indice]}")

mostrar_vector(lista, limite)