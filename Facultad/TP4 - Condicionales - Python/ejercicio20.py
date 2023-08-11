""" Dadas las 4 notas obtenidas por un alumno, calcular e informar su promedio e informar 
una leyenda que indique si está aprobado o no. La condición de aprobación es obtener un 
promedio mayor o igual que 4. """

print("Ingrese las cuatros notas.")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercer nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

if (promedio >= 4):
    print(f"El alumno esta aprobado. Nota promedio: {promedio:.1f}")
else:
    print(f"El alumno esta desaprobado. Nota promedio: {promedio:.1f}")
    
