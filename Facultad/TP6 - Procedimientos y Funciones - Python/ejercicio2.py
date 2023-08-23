from math import pow

def perimetro(alto,ancho):
    return (alto*2) + (ancho*2)

alto = float(input("Ingrese el alto: "))
ancho = float(input("Ingrese el ancho: "))

print(f"El perimetro del rectangulo es: {perimetro(alto, ancho):.2f}")

