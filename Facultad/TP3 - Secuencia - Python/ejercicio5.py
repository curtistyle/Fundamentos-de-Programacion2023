"""Dadas las calificaciones de 4 exámenes finales de un estudiante determinar el promedio. """

nota1 = float(input("Ingrese la nota del primer examen: "))
nota2 = float(input("Ingrese la nota del segundo examen: "))
nota3 = float(input("Ingrese la nota del tercer examen: "))
nota4 = float(input("Ingrese la nota del cuarto examen: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

print(f"El promedio de las cuatros notas es: {promedio:.2f}")

