# ! Trabajo Practico Archivos Sebastian Maldonado

import archivos
import texto
import menus
from os import system
from msvcrt import getwch

opc = "0"

while (opc != '9'):
    opc = menus.principal()
    
    # ? Menu Principal -> Crear archivo
    if (opc == "1"):
        system("cls")
        print()
        centinela = False
 
        while True:
            nombre = input( f" ~ Ingrese el nombre del arhivo de texto: ")
   
            if (archivos.existe(nombre)) == False:
                archivos.crear(nombre)
                print( f" ~ El archivo se creo correctamente con el nombre \'{nombre}.txt\'" )
                input()
                system("cls")
                break
            else:    
                print( f" ! El archivo con el nombre \'{nombre}\' ya existe. ", end="\n\n" )
                print( f"   ? (1) Probar con otro nombre." )
                print( f"   ? (2) Eliminarlo." )
    
                opc_crear = input()
    
                system("cls")
 
                if opc_crear == "2":
                    archivos.eliminar(nombre)
                    print( f" ~ El archivo \'{nombre}.txt\' fue eliminado." )
                    break
                elif opc_crear == "1":
                    ...
    # ? Menu Principal -> Directorio
    elif (opc == "2"):
  
        while (True):
            system("cls")
            print( f" ~ Archivos en el directorio: ", end="\n\n" )
            
            print( f"{'ID':<3} | {'NOMBRE':<30} | {'EXTENSION':<10} | {'TAMANIO':<5}" )
            print( "------------------------------------------------------------" )
            fichero = archivos.listado()
            for indice in range( 0, len( fichero ) ):
                print( f"{indice+1:<3} | {fichero[indice]['nombre']:<30} | {fichero[indice]['extension']:<10} | {fichero[indice]['tamanio']:<5}" )
            print( "------------------------------------------------------------" )
            print( "[1 Abrir]-[2 Eliminar]-[3 Renombrar]      [9 Menu Principal]", end="\n\n" )
            
            opc_directorio = getwch()
            
            # ? Directorio -> Abrir
            if (opc_directorio == "1"):
                nombre = input( "[1 Abrir] ~ Ingrese el NOMBRE del archivo o el ID: " )
                nombre = archivos.nombre_por_id( nombre, fichero )

                if archivos.existe( nombre ):
                    system("cls")
                    
                    datos = archivos.leer( nombre )
                    texto.mostrar( datos )
                    
                    print()
                    print( "---------------------------------------------------------------" )
                    print( "Fila: [1 Agregar]-[2 Quitar]-[3 Reemplazar]||[9 Directorios]", end="\n\n" )
                    
                    opc_abrir = getwch()
                    
                    # ? Abrir -> Agregar
                    if (opc_abrir == "1"):
                        while True:
                            posicion = int( input( " ~ Ingrese la posicion en la que quieres agregar la fila: " ) )
                            print()
                            cadena = input( " ~ Ingrese la cadena: " )
                            
                            datos = texto.añadir( datos, cadena, posicion )
                            if datos is not None:
                                archivos.escribir( datos, nombre )
                            
                            print()
                            print( " ? Quieres ingresar una nueva fila: (s/n)" )
                            
                            opc_anadir = getwch()
                            system('cls')
                            if opc_anadir.upper() != 'S':
                                break
                            
                    # ? Abrir -> Quitar
                    elif (opc_abrir == "2"):
                        while True:
                      
                            posicion = int( input( " ~ Ingrese la posicion de la fila a quitar: " ) )
                            print()

                            datos = texto.quitar( datos, posicion )
                            if datos is not None:
                                archivos.escribir( datos, nombre )
                            
                            print()
                            print( " ? Quieres quitar una fila: (s/n)" )
                            
                            opc_quitar = getwch()
                            system('cls')
                            
                            if opc_quitar.upper() != 'S':
                                break
                    # ? Abrir -> Reemplazar
                    elif (opc_abrir == "3"):
                        while True:
                     
                            posicion = int( input( " ~ Ingrese la posicion de la fila que quieres reemplazar: " ) )
                            print()
                            linea = input( " ~ Ingrese la cadena: " )
                            
                            datos = texto.reemplazar( datos, linea, posicion )
                            if datos is not None:
                                archivos.escribir( datos, nombre )
                            
                            print()
                            print( " ? Quieres reemplazar una fila: (s/n)" )
                            
                            opc_reemplazar = getwch()
                            system('cls')
                            if opc_reemplazar.upper() != 'S':
                                break
                    
                    # ? Abrir -> Directorio
                    elif (opc_abrir == "9"):
                        system("cls") 
                        
            # ? Directorio -> Eliminar
            elif (opc_directorio == "2"):
                
                nombre = input( "[2 Eliminar] ~ Ingrese el NOMBRE del archivo o el ID: " )            
                nombre = archivos.nombre_por_id( nombre, fichero )
                
                if archivos.existe( nombre ):
                    archivos.eliminar( nombre )
                    print( end="\n" )
                    print( f" ~ El archivo {nombre} fue eliminado.", end="\n\n" )
                else:
                    print( f" ~ El archivo {nombre} no existe.", end="\n\n" )    
                
                input()
                system("cls")
            
            # ? Directorio -> Renombrar
            elif (opc_directorio == "3"):     
                nombre = input( "[2 Renombrar] ~ Ingrese el NOMBRE del archivo o el ID: " )
                nombre = archivos.nombre_por_id( nombre, fichero )
                print( end="\n" )
   
                if archivos.existe( nombre ):  
        
                    nuevo_nombre = input( f" ~ Ingrese el nuevo nombre: " ) 
                    archivos.renombrar( nombre, nuevo_nombre )
                    print( end="\n" )
                    print( f"Archivo reenombrado \'{nombre}\' --> \'{nuevo_nombre}\'." )    
    
                else:
    
                    print( f" ~ El archivo {nombre} no existe.", end="\n\n" )
   
                print( end="\n" )
                input()

                system("cls")
                
            # ? Directorio -> Menu Principal
            elif (opc_directorio == "9"):
                opc = 0
                system("cls")
                break
            
