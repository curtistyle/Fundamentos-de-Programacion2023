# from msvcrt import getwch, getch
# from colorama import Fore


# tecla_presionada = 'a'
# while (tecla_presionada != 0):
#     print("Presiona una tecla: ")
#     tecla_presionada = getch()
#     print(Fore.RED + f"Presionaste la tecla: {tecla_presionada.decode('utf-8')}")


# ! -----------------------------

# persons = [
#     {"name" : "L. Messi", "year" : 36, "dorsal" : 10},
#     {"name" : "A. Di Maria", "year" : 35, "dorsal" : 11},
#     {"name" : "A. Varela", "year" : 22, "dorsal" : 22},
#     {"name" : "C. Medina", "year" : 21, "dorsal" : 36}
# ]

# print(f'{"Nombre":<15}{"Edad":<14}{"Dorsal":<10}')
# for person in persons:
#     print(f"{person['name']:<15}{person['year']:<14}{person['dorsal']:<10}")

# ! ------------------------------------

# def divisor (x,y):
#     assert y != 0, "El divisor no puede ser cero"
#     return x / y

# x = int(input("Ingrese el valor de x: "))
# y = int(input("Ingrese el valor de y: "))

# print(f"Resultado: {divisor(x,y)}")

# ! -------------------------------------------

# # Función de filtrado para números pares
# def es_par(numero):
#     return numero % 2 == 0

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Filtrar los números pares de la lista
# numeros_pares = filter(es_par, numeros)

# # Convertir el resultado a una lista
# numeros_pares_lista = list(numeros_pares)

# print(numeros_pares_lista)  # Imprime [2, 4, 6, 8, 10]


# numero = int(input("Ingrese un numero: "))

# print("Es par" if ((numero % 2) == 0) else "Es impar")


lyst = ["rojo", "verde", "amarillo"]

for item, index in enumerate(lyst):
    print(f"{item=}, {index=}")
