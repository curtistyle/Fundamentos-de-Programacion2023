"""Dados tres números enteros positivos, determinar cuál es el mayor."""

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

if (numero1 > numero2) and (numero1 > numero3):
    print("El numero ", numero1, " es el mayor.")
elif (numero2 > numero1) and (numero2 > numero3):
    print("El numero ", numero2, " es el mayor.")
else:
    print("El numero ", numero3, " es el mayor.")
    
