import archivos
import texto
import menus
from os import system
from msvcrt import getwch



opc = "0"

while (opc != 9):
    opc = menus.principal()
    
    if (opc == "1"):
        system("cls")
        print()
        centinela = False
        while (centinela == False):
            nombre = input( f" ~ Ingrese el nombre del arhivo de texto: ")
            if (archivos.existe(nombre)) == False:
                archivos.crear(nombre)
                print( f" ~ El archivo se creo correctamente con el nombre \'{nombre}.txt\'" )
                input()
                centinela = True
                system("cls")
            else:
                print( f" ! El archivo con el nombre \'{nombre}\' ya existe. ", end="\n\n" )
                print( f"   ? (1) Probar con otro nombre." )
                print( f"   ? (2) Eliminarlo." )
                opc = input()
                system("cls")
                if opc == "2":
                    archivos.eliminar(nombre)
                    print( f" ~ El archivo \'{nombre}.txt\' fue eliminado." )
                    centinela = True
                elif opc == "1":
                    centinela = False
    elif (opc == "2"):
        centinela = False
        while (centinela == False):
            system("cls")
            print( f" ~ Archivos en el directorio: ", end="\n\n" )
            
            print( f"{'ID':<3} | {'NOMBRE':<30} | {'EXTENSION':<10} | {'TAMANIO':<5}" )
            print( "------------------------------------------------------------" )
            fichero = archivos.listado()
            for indice in range( 0, len( fichero ) ):
                print( f"{indice+1:<3} | {fichero[indice]['nombre']:<30} | {fichero[indice]['extension']:<10} | {fichero[indice]['tamanio']:<5}" )
            print( "------------------------------------------------------------" )
            print( "[1 Abrir]-[2 Eliminar]-[3 Renombrar]      [9 Menu Principal]" )
            
            opc = getwch()
            
            if (opc == "1"):
                nombre = input( "Ingrese el nombre del archivo: " )
                if archivos.existe(nombre):
                    system("cls")
                    datos = archivos.leer(nombre)
                    texto.mostrar(datos)
                    input()
                    