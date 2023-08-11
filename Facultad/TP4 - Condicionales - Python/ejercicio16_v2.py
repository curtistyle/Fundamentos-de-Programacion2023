""" Escribir un algoritmo en el que se introduzca el número de un mes (1 a 12) y visualice el 
Nº de días de ese mes. (no considerar año bisiesto) """

mes = int(input("Ingrese el numero de mes: "))

if mes in [4,6,8,11]:
    print("El mes ", mes, " tiene 30 dias.")
elif mes == 2:
    print("El mes ", mes, " tiene 28 dias.")
else:
    print("El mes ", mes, " tiene 31 dias.")