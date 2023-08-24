""" Escribir una función que dados 2 números, calcule el porcentaje que el primero representa 
respecto del segundo. """

def porcentaje(a,b):
    return (a/b)*100

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

if (numero2 != 0):
    print(f"El porcentaje que el primer numero {numero1} representa sobre el segundo numero {numero2} es: {porcentaje(numero1,numero2):.1f}%.")
else:
    print("El segundo numero tiene que ser distindo de cero.")
    
    
