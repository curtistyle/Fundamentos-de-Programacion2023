""" 
Se tienen los trabajos presentados para cada una de las cuatro líneas de
un congreso de docentes binacional. De cada una se tienen temática,
moderador y cantidad de trabajos. Se pide procesar cada uno de los
trabajos presentados teniendo en cuenta que de cada uno se lee: título,
autores y línea en la cual se presenta (docencia en la pospandemia,
educación superior como derecho, investigación y extensión).
Se pide:
    a. Total de trabajos por línea y en total.
    b. Determinar de cual línea se presentaron mas trabajos y el
       porcentaje que representa este número en el total.
    c. Determinar si una autora determinada presentó trabajó y si es así
       mostrar los datos del trabajo.
"""

from msvcrt import getwch

# Inicializar variables
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0

for index in range(1,4):
    tematica = input("Ingrese la Tematica: ")
    moderador = input("Ingrese el Moderador: ")
    cantidadTrabajos = int(input("Ingrese la cantidad de trabajos: "))
    
    for indice in range(1,cantidadTrabajos + 1):
        print(f"Trabajo N{indice}.")
        titulo = input("Ingrese el Titulo: ")
        autor = input("Ingrese el Autor: ")
        while True: 
            print("Ingrese la linea en la cual se presenta: ")
            print(" * (1) Docencia en la pospandemia.")
            print(" * (2) Educacion superior como derecho.")
            print(" * (3) Investigacion: ")
            print(" * (4) Extension.")
            estado = int(getwch())
            if ((estado >= 1) and (estado <= 4)):
                break
            
            match estado:
                case 1:
                    contador1 += 1
                case 2: 
                    contador2 += 1
                case 3: 
                    contador3 += 1
                case 4: 
                    contador4 += 1
                case _:
                    pass
                
    
    print(f"En la tematica '{tematica}', bajo la supervicion de '{moderador}' \n "
          f"Se presentaron {cantidadTrabajos} de los cuales en cada linea de trabajo hubo: \n\n")
    
    print(f" * Docencia en la pandemia: {contador1:<38}")
    print(f" * Educacion superior como derecho: {contador2:<38}")
    print(f" * Investigacion: {contador3:<38}")
    print(f" * Extension:  {contador4:<38}")

    if ((contador1 > contador2) and (contador1 > contador3) and (contador1 > contador4)):
        print("Predomino la linea de trabajo 'Docencia en la pandemia'.")
        print(f"Con un porcentaje con respecto al resto: {((contador1*100)/cantidadTrabajos):.1f}%")
    elif((contador2 > contador1) and (contador2 > contador3) and (contador2 > contador4)):
        print("Predomino la linea de trabajo 'Educacion superior como derecho.'")
        print(f"Con un porcentaje con respecto al resto: {((contador2*100)/cantidadTrabajos):.1f}%")
    elif((contador3 > contador1) and (contador3 > contador2) and (contador3 > contador4)):
        print("Predomino la linea de trabajo 'Investigacion.'")
        print(f"Con un porcentaje con respecto al resto: {((contador3*100)/cantidadTrabajos):.1f}%")
    elif((contador4 > contador1) and (contador4 > contador2) and (contador4 > contador3)):
        print("Predomino la linea de trabajo 'Extencion'")
        print(f"Con un porcentaje con respecto al resto: {((contador4*100)/cantidadTrabajos):.1f}%")
    
    