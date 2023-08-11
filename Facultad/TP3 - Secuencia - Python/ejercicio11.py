""" Solicitar al usuario que ingrese el precio de un producto al inicio del año, y el precio del 
mismo producto transcurrido un determinado tiempo. El usuario debe mostrar cuál fue el 
porcentaje de aumento que tuvo ese producto en el año. """

valor_inicial = float(input("Ingrese el precio inicial del producto: "))
valor_final = float(input("Ingrese el precio inicial del producto: "))

porcentaje = ((valor_final - valor_inicial) / valor_inicial * 100)

print(f"El producto aumento un: {porcentaje:.1f}%")

