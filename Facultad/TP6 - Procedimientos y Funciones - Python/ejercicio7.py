""" Escribir una función lógica tal que dadas dos cadenas indique si la primera es más larga 
que la segunda. """

def determinarCadena(cadena1, cadena2):
    if (len(cadena1) > len(cadena2)):
        return True
    else:
        return False

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

print(f"La cadena1 es mas grande que la cadena2? : {determinarCadena(cadena1,cadena2)}")



