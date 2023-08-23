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



for index in range(1,4):
    tematica = input("Ingrese la tematica: ")
    moderador = input("Ingrese el moderador: ")
    cantidadTrabajos = int(input("Ingrese la cantidad de trabajos: "))
    
    opcion = input("Quiere presentar un trabajo (s/n): ")
    while (opcion == 's'):
        
        opcion = input("Quiere presentar un trabajo (s/n): ")