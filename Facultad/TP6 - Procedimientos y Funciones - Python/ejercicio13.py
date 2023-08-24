""" Escribir una función lógica vocal que determine si un carácter es una vocal. """

# Estructura del match

# match asunto:
#     case <patron_1>:
#         <accion_1>
#     case <patron_2>:
#         <accion_2>
#     case <patron_3>
#         <accion_3>
#     case _:
#         <accion_comodín>
    
        


# def vocal(caracter):
#     if (caracter in ('a','e','i','o','u')):
#         return True
#     else:
#         return False

def vocal(x):
    if ((x == 'a') or (x == 'e') or (x == 'i') or (x == 'o') or (x == 'u')):
        return True
    else: 
        return False

# def vocal(caracter):
#     if (caracter == 'a'):
#         return True
#     elif (caracter == 'e'):
#         return True
#     elif (caracter == 'i'):
#         return True
#     elif (caracter == 'o'):
#         return True
#     elif (caracter == 'u'):
#         return True
#     else:
#         return False
        

# def vocal(caracter):
#     match caracter:
#         case 'a':
#             return True
#         case 'e':
#             return True
#         case 'i':
#             return True
#         case 'o':
#             return True
#         case 'u':
#             return True
#         case _:
#             return False

# def vocal(caracter):
#     match caracter:
#         case 'a' | 'e' | 'i' | 'o' | 'u':
#             return True
#         case _:
#             return False


while True:
    caracter = input("Ingrese un caracter: ")   
    if (vocal(caracter) == True):
        print(f"El caracter '{caracter}' es una vocal.")
    else:
        print(f"El caracter '{caracter}' No es una vocal.")
    