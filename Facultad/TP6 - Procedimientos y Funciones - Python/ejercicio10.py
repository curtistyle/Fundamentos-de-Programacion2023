""" Escribir una función que tenga un parámetro de tipo entero y que devuelva la letra P si el 
Nº es positivo y N si es negativo o cero. """

def polaridad(numero):
    if numero >= 0:
        return 'P'
    else:
        return 'N'
    
numero = int(input("Ingrese un numero entero: "))

print(f"El numero que ingreso es: {polaridad(numero)}")

