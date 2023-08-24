""" Escribir un procedimiento digito, que determine si un carácter es uno de los dígitos de o a 
9.  """

def rango(caracter):
    return caracter.isdigit()

# def rango2(caracter):
#     if (caracter >= '0') and (caracter <= '9'):
#         return True
#     else:
#         return False


caracter = input("Ingrese un caracter: ")

if (rango(caracter) == True):
    print(f"El caracter '{caracter}' es un digito 0 .. 9.")
else:
    print(f"El caracter '{caracter}' No es un digito 0 .. 9")
    
