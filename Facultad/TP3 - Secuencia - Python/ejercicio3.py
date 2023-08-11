"""Dadas  las  horas  trabajadas  por  un  operario  y  el  valor  de  las  mismas,  determinar  
que sueldo percibe dicho operario. Se solicita indicar cuanto cobraría si se aplican descuentos 
del 20% """

horas_trabajas = int(input("Ingrese las horas trabajadas del operario: "))
valor_hora = float(input("Ingrese el valor de las horas trabajadas: "))

sueldo = horas_trabajas * valor_hora

print("El sueldo del operario es: ${:.2f}".format(sueldo))

descuento = sueldo * 0.2

print(f"El sueldo con un %20 de duescuento ${sueldo - descuento:.2f}")

