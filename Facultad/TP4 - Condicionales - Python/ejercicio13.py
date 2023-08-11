"""  Desarrollar un algoritmo que una vez leída una Fecha en formato dd/mm/aaaa, indique cual 
será la fecha un día después. """

fecha = input("Ingrese la fecha en el formato dd/mm/aaaa: ")

dia = int(fecha[0] + fecha[1])
mes = int(fecha[3] + fecha[4])
anio = int(fecha[6] + fecha[7] + fecha[8] + fecha[9])

# Inicializar variables
siguienteDia = 0
siguinteMes = 0
siguienteAnio = 0

if (mes == 2):
    if ((anio % 4) == 0) and (((anio % 100) != 0) or ((anio % 400) == 0)):
        if (dia == 29):
            siguienteDia = 1
            siguienteMes = mes + 1
        else:
            siguienteDia = dia + 1
            siguienteMes = mes
    else:
        if (dia == 28):
            siguienteDia = 1
            siguienteMes = mes + 1
        else:
            siguienteDia = dia + 1
            siguienteMes = mes
else:
    if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
        if (dia == 30):
            siguienteDia = 1
            siguienteMes = mes + 1
        else:
            siguienteDia = dia + 1
            siguienteMes = mes
    else:
        if (dia == 31):
            if (mes == 12):
                siguienteDia = 1
                siguienteMes = 1
                siguienteAnio = anio + 1
            else:
                siguienteDia = dia + 1
                siguienteMes = mes
        else:
            siguienteDia = dia + 1
            siguienteMes = mes
        
if (siguienteAnio != 0):
    print("El dia siguiente es: ", siguienteDia, "/", siguienteMes, "/", siguienteAnio)
else:
    print("El dia siguiente es: ", siguienteDia, "/", siguienteMes, "/", anio)
            


