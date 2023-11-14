valor_anterior = input("Ingrese el valor que desea reemplar: ")
valor_nuevo = input("Ingrese el nuevo valor: ")

with open("info_departamentos.txt", "+r", encoding="utf-8" ) as fichero:
    lineas = fichero.readlines()
    
    for i in range( 0, len( lineas ) ):
        datos = lineas[i].split()
        for j in range( 0, len( datos ) ):
            if datos[j] == valor_anterior:
                datos[j] = valor_nuevo
                lineas[i] = " ".join( datos ) + "\n"

    fichero.seek(0)
    fichero.writelines( lineas )