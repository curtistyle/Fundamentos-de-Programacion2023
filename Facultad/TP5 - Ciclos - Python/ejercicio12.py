"""  En un colegio de 1000 alumnos se ha registrado, para cada uno de ellos hay un código 
señalando  su  comportamiento  académico.  Dicho  código  puede  tomar  valores  1,  2  o  3. 
Indicar  cuántos  alumnos  obtuvieron  cada  una  de  las  calificaciones  tratando  de  a  una 
calificación por vez. """

from msvcrt import getch

contador1 = 0
contador2 = 0
contador3 = 0

index = 1

while (index <= 10):
    print(f"Ingrese el compartamiento academico (1,2,3) del alumno #{index}.")
    
    opcion = getch()
    print("opcion: ", opcion)
    if (opcion == b'1'):
        contador1 += 1
    elif (opcion == b'2'):
        contador2 += 1
    elif (opcion == b'3'):
        contador3 += 1
    else:
        print("La opcion  que ingrese es invalida.")
        index = index - 1
    index += 1


print(f"El comportamiento 1 lo obtuvo {contador1} alumnos.")
print(f"El comportamiento 2 lo obtuvo {contador2} alumnos.")
print(f"El comportamiento 3 lo obtuvo {contador3} alumnos.")

   


