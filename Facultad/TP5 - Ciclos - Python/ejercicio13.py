""" En una fábrica hay 4.000 obreros distribuidos en cinco secciones. Se requiere determinar 
cuántos obreros hay y el promedio de edad de los mismos por cada sección. Asumir que 
se tiene como entrada los siguientes datos para cada obrero: Nº de empleado, sección a 
la que pertenece y edad. """

from msvcrt import getwch

# Seccion 1
contador1 = 0
acumulador1 = 0
# Seccion 2
contador2 = 0
acumulador2 = 0
# Seccion 3
contador3 = 0
acumulador3 = 0
# Seccion 4
contador4 = 0
acumulador4 = 0
# Seccion 5
contador5 = 0
acumulador5 = 0

for index in range(1,10):
    opcion = int(input(f"#{index} Ingrese la seccion a la que pertene el empleado (1,2,3,4,5): "))
    edad = int(input("Ingrese la edad: "))
    
    if (opcion == 1):
        contador1 += 1
        acumulador1 = acumulador1 + edad
    elif (opcion == 2):
        contador2 += 1
        acumulador2 = acumulador2 + edad
    elif (opcion == 3):
        contador3 += 1
        acumulador3 = acumulador3 + edad
    elif (opcion == 4):
        contador4 += 1
        acumulador4 = acumulador4 + edad
    elif (opcion == 5):
        contador5 += 1
        acumulador5 = acumulador5 + edad
    else:
        print("Opcion incorrecta.")
        
print(f"La seccion 1 tiene {contador1} empleados y su promedio de edad es {acumulador1/contador1:.1f} "
        f"\n La Seccion 2 tiene {contador2} empleados y su promedio de edad es {acumulador2/contador2:.1f}"
        f"\n La Seccion 3 tiene {contador3} empleados y su promedio de edad es {acumulador3/contador3:.1f}"
        f"\n La Seccion 4 tiene {contador4} empleados y su promedio de edad es {acumulador4/contador4:.1f}"
        f"\n La Seccion 5 tiene {contador5} empleados y su promedio de edad es {acumulador5/contador5:.1f}")

    
    
            
    

