"""  Escribir una función lógica de dos parámetros enteros que devuelva True si uno divide al 
otro y False en caso contrario. """

def divisibilidad(numero1, numero2):
    if ((numero1 % numero2) == 0):
        return True
    else:
        return False

numero1 = int(input("Ingrese el primer numero: "))

numero2 = int(input("Ingrese el segundo numero: "))
while numero2 == 0 :
    print("No se puede dividir por 0.")
    numero2 = input("Ingrese el segundo numero: ")
    
print(f"El numero {numero1} es divisible por el numero {numero2} ? : {divisibilidad(numero1,numero2)}.")