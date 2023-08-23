""" Escribir un procedimiento Geometría tal que dado el alto y ancho de un rectángulo calcule 
el área. """

def geometria(alto,ancho):
    return alto * ancho

alto = float(input("Ingrese el alto del rectangulo: "))
ancho = float(input("Ingrese el ancho del rectangulo: "))

print(f"El area del rectangulo es {(alto * ancho):.2f}.")

