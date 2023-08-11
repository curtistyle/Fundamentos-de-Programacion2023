""" Dados tres nombres de alumnos, mostrar si Mariana Ríos se encuentra entre ellos, de lo 
contrario emitir un mensaje “No existe”"""

print("Ingrese tres nombres. ")

nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")
nombre3 = input("Ingrese el tercer nombre: ")

if (nombre1 == "Mariana Rios") or (nombre2 == "Mariana Rios") or (nombre3 == "Mariana Rios"):
    print(nombre1, " se encuentra entre los alumnos.")
else:
    print("No existe.")
    
    