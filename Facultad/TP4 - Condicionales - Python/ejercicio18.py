""" Leer dos números. Decir si el primero es divisible por el segundo, si esto se cumple decir 
si es un número par o impar."""

print("Ingrese dos numero.")

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if ((numero1 % numero2) == 0):
    if ((numero1 % 2) == 0):
        print("El ", numero1, " es Par.")
    else:
        print("El ", numero1, " es Impar.")
    if ((numero2 % 2) == 0):
        print("El ", numero2, " es Par.")
    else:
        print("El ", numero2, " es Impar.")
else:
    print("El ", numero1, " no es divisible por ", numero2)
    
    
        
        
