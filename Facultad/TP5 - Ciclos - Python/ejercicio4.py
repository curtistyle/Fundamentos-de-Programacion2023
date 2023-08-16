""" Ingresar un Nº y un carácter y mostrar dicho carácter repetido tantas veces como indica el 
Nº. """

numero = int(input("Ingrese un numero: "))
caracter = input("Ingrese una letra: ")

for index in range(1,numero + 1):
    print(f"#{index}: ", caracter)
    
