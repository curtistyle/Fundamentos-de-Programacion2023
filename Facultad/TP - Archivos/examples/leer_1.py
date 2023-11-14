with open( "cuentas.txt", "r", encoding="utf-8" ) as fichero:
    texto = fichero.read()                       
    lineas = texto.split( '\n' )  
    print( f"{'ID':>5} {'Nombre':>10} {'Apellido':>10} {'Email':>20} {'Edad':>5}" )                 
    for indice in range( 0, len( lineas ) ):
        linea = lineas[indice]
        datos = linea.split()
        print( f"{datos[0]:>5} {datos[1]:>10} {datos[2]:>10} {datos[3]:>20} {datos[4]:>5}" ) 