# import json


# with open( "Facultad\TP - Archivos\main.txt", "r", encoding="utf-8" ) as item:
#     for texto in item.readlines():
#         print(texto, end="")
    
# archivo = None
# with open( "Facultad\TP - Archivos\main.txt", "a", encoding="utf-8" ) as item:
#     item.writelines()
#     archivo = item
    
# # print(end="\n\n")

# f = open( "Facultad\TP - Archivos\main.txt", "r", encoding="utf-8" )
# # print( type(f) )


# with open( "Facultad\TP - Archivos\main.txt", "r", encoding="utf-8" ) as fichero:
#     print(fichero)
#     print( f"{'#':<5} {'Nombre':>10} {'Edad':>10}" )
#     for linea in fichero:
#         numero, nombre, edad = linea.split()
#         print( f"{numero:<5} {nombre:>10} {edad:>10}" )
#     fichero.close()

# with open( "Facultad\TP - Archivos\main.txt", "r", encoding="utf-8" ) as fichero:
#     fichero.seek(0,0)
#     print(fichero.read())

# !seek
# with open( "Facultad\TP - Archivos\cuentas.txt", "r", encoding="utf-8" ) as fichero:
#     linea1=fichero.readline()
#     print( linea1 )
#     fichero.seek( len(linea1) + 1, 0 )
#     linea2=fichero.readline()
#     print( linea2 )


# with open( "cuentas.txt", "r", encoding="utf-8" ) as fichero:
#     texto = fichero.read()                       
#     lineas = texto.split( '\n' )  
#     print( f"{'ID':>5} {'Nombre':>10} {'Apellido':>10} {'Email':>20} {'Edad':>5}" )                 
#     for indice in range( 0, len( lineas ) ):
#         linea = lineas[indice]
#         datos = linea.split()
#         print( f"{datos[0]:>5} {datos[1]:>10} {datos[2]:>10} {datos[3]:>20} {datos[4]:>5}" ) 
    
with open( "Facultad\TP - Archivos\cuentas.txt", "r", encoding="utf-8" ) as fichero:
    lineas = fichero.readlines()                        
    print( f"{'ID':>5} {'Nombre':>10} {'Apellido':>10} {'Email':>20} {'Edad':>5}" )                 
    for indice in range( 0, len( lineas ) ):
        linea = lineas[indice]
        datos = linea.split()
        print( f"{datos[0]:>5} {datos[1]:>10} {datos[2]:>10} {datos[3]:>20} {datos[4]:>5}" ) 