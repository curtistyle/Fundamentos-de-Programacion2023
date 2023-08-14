"""  De una prueba de nivel realizada a un alumno se conoce la cantidad total de preguntas 
realizadas y la cantidad de respuestas correctas. Informar el nivel registrado de acuerdo 
a la siguiente escala: 

    Muy Bueno si el porcentaje es mayor o igual a 90% 
        ▪ Bueno entre 70% y 90% 
        ▪ Regular entre 50% y 70% 
        ▪ Malo si el porcentaje es menor que 50%
"""

total_preguntas = int(input("Ingrese la cantidad total de preguntas realizadas: "))
total_respuestas_correctas = int(input("Ingrese la cantidad total de respuestas correcta: "))

porcentaje = (total_respuestas_correctas * 100) / total_preguntas

print("Nivel de respuestas correctas: ")
if (porcentaje < 50):
    print("Malo.")
elif (porcentaje >= 50) and (porcentaje < 70):
    print("Regular.")
elif (porcentaje >= 70) and (porcentaje < 90):
    print("Bueno.")
else:
    print("Muy Bueno.")


