""" Se realiza una encuesta de aceptación de tres productos (se ingresa el porcentaje de cada 
uno) y quiero determinar cuál de ellos es el menos aceptado y el más aceptado. Imprimir 
un mensaje indicando el nombre de los productos y sus porcentajes. """

producto1 = input("Ingrese el nombre del primer producto: ")
porcentaje1 = float(input("Ingrese el porcentaje de aceptacion: "))
producto2 = input("Ingrese el nombre del segundo producto: ")
porcentaje2 = float(input("Ingrese el porcentaje de aceptacion: "))
producto3 = input("Ingrese el nombre del tercer producto: ")
porcentaje3 = float(input("Ingrese el porcentaje de aceptacion: "))

if (porcentaje1 > porcentaje2) and (porcentaje2 > porcentaje3):
    print("El ", producto1, f" es el mas popular con un {porcentaje1:.2f}%.")
    print("El ", producto3, f" es el menos popular con un {porcentaje3:.2f}%.")
elif (porcentaje1 > porcentaje3) and (porcentaje3 > porcentaje2):
    print("El ", producto1, f" es el mas popular con un {porcentaje1:.2f}%.")
    print("El ", producto2, f" es el menos popular con un {porcentaje2:.2f}%.")
elif (porcentaje2 > porcentaje1) and (porcentaje1 > porcentaje3):
    print("El ", producto2, f" es el mas popular con un {porcentaje2:.2f}%.")
    print("El ", producto3, f" es el menos popular con un {porcentaje3:.2f}%.")
elif (porcentaje2 > porcentaje3) and (porcentaje3 > porcentaje1):
    print("El ", producto2, f" es el mas popular con un {porcentaje2:.2f}%.")
    print("El ", producto1, f" es el menos popular con un {porcentaje1:2f}%.")
elif (porcentaje3 > porcentaje1) and (porcentaje1 > porcentaje2):
    print("El ", producto3, f" es el mas popular con un {porcentaje2:.2f}%.")
    print("El ", producto2, f" es el menos popular con un {porcentaje2:.2f}%.")
else:
    print("El ", producto3, f" es el mas popular con un {porcentaje3:.2f}%.")
    print("El ", producto1, f" es el menos popular con un {porcentaje1:.2f}%.")