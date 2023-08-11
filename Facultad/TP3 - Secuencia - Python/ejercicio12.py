""" De los y las estudiantes de Fundamentos de Programación se desea saber qué porcentaje 
de personas  menores a  20  años  se  encuentran  cursando  la  materia.  El  programa  debe 
solicitar  al  usuario  que  ingrese  la cantidad  total  de  estudiantes  menores  a 20  años  y  el 
total. """

cantidad_menores = int(input("Ingrese la cantidad de estudiantes menores a 20 anios: "))
total = int(input("Ingrese el total de estuantes del curso: "))

porcentaje = (cantidad_menores * 100) / total

print("El porcentaje de estudiantes menores de 20 es: {:.2f}%".format(porcentaje))

