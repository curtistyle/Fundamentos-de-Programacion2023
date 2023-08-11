""" Se ingresa el nombre, edad y dirección de dos socios, se pide mostrar los datos de socio 
más joven.  """

print("Primer socio.")
nombre1 = input("Ingrese el nombre: ")
edad1 = int(input("Ingrese la edad: "))
direccion1 = input("Ingrese la direccion: ")

print("Segundo socio.")
nombre2 = input("Ingrese el nombre: ")
edad2 = int(input("Ingrese la edad: "))
direccion2 = input("Ingrese la direccion: ")

print("El socio mas joven es: ")
if(edad1 < edad2):
    print("Nombre: ", nombre1, " - Edad: ", edad1, " - Direccion: ", direccion1)
else:
    print("Nombre: ", nombre2, " - Edad: ", edad2, " - Direccion: ", direccion2)
    

