"""  Se  desea  escribir  el  nombre  del  día  de  la  semana  en  función  de  un  número  del  día, 
introducido por teclado, donde 1 es Domingo, 2 es Lunes, y así sucesivamente. """

dia = int(input("Ingrese el numero del dia de la semana: "))

if (dia == 1):
    print("Lunes.")
elif (dia == 2):
    print("Martes.")
elif (dia == 3):
    print("Miercoles.")
elif (dia == 4):
    print("Jueves.")
elif (dia == 5):
    print("Viernes.")
elif (dia == 6):
    print("Sabado.")
elif (dia == 7):
    print("Domingo.")
else:
    print("Dato invalido. ")