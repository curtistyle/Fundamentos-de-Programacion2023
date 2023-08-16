""" Hacer un programa que lea 8 caracteres e indique que cantidad de ‘*’ y que cantidad de 
letras ‘a’ aparecen. """

contador1 = 0
contador2 = 2

for index in range(1,9):
    caracter = input(f"{index} Ingrese un caracter: ")
    
    if (caracter == '*'):
        contador1 += 1
    if (caracter == 'a'):
        contador2 +=1
    
print(f"Se contaron {contador1} '*' y {contador2} 'a'.")