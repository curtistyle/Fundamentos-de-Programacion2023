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


def divisor (x,y):
    assert y != 0, "El divisor no puede ser cero"
    return x / y

x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))

print(f"Resultado: {divisor(x,y)}")