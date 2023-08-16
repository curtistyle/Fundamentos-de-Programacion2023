""" Se  efectúa  una  encuesta  entre  1200  usuarios  de  sistemas  operativos.  Las  respuestas 
están  codificadas  como  1,  2  ó  3  según  sea  el  elegido.  Preparar  un  algoritmo  para 
ingresarle las 120 respuestas, y muestre por pantalla el número del sistema preferido.  """

contador1 = 0
contador2 = 0
contador3 = 0

for index in range(1,2):
    respuesta = int(input("Ingrese una opcion (1:windows,2:linux,3:OS): "))
    if (respuesta == 1):
        contador1 += 1
    elif (respuesta == 2):
        contador2 += 1
    elif (respuesta == 3):
        contador3 += 1

contador1 = 4
contador2 = 2 
contador3 = 1

if (contador1 > contador2) and (contador1 > contador3):
    print("1: Windows es el sistema operativo favorito.")
elif (contador2 > contador1) and (contador2 > contador3):
    print("2: Linux es el sistema operativo favorito.")
else:
    print("3: OS es el sistema operativo favorito.")

