""" Diseñe un algoritmo que determine el porcentaje de: Alumnos promocionados, Alumnos 
regularizados, Alumnos desaprobados y Alumnos libres, teniendo como datos cantidad de 
alumnos que cumplen con cada condición.  """

alumnos_promociondos = int(input("Ingrese la cantidad de alumnos promocionados: "))
alumnos_regularizados = int(input("Ingrese la cantidad de alumnos regularizados: "))
alumnos_desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
alumnos_libres = int(input("Ingrese la cantidad de alumnos libres: "))

total_alumnos = alumnos_promociondos + alumnos_regularizados + alumnos_desaprobados + alumnos_libres

print(f"Porcentaje de alumnos promocionados: {((alumnos_promociondos * 100)/total_alumnos):.2f} %.")
print(f"Porcentaje de alumnos regularizados: {((alumnos_regularizados * 100)/total_alumnos):.2f} %.")
print(f"Porcentaje de alumnos desaprobados: {((alumnos_desaprobados * 100)/total_alumnos):.2f} %.")
print(f"Porcentaje de alumnos libres: {((alumnos_libres * 100)/total_alumnos):.2f} %.")

