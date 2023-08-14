"""  Dados 3 números, informarlos en orden creciente. """

print("Ingrese tres numeros.")

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

if (numero1 > numero2 > numero3):
    print("(A)Ordenados de forma creciente: ", numero3, " - ", numero2, " - ", numero1, ".")
elif (numero1 > numero3 > numero2):
    print("(B)Ordenados de forma creciete: ", numero2, " - ", numero3, " - ", numero1, ".")   
elif (numero2 > numero1 > numero3):
    print("(C)Ordenados de forma creciete: ", numero3, " - ", numero1, " - ", numero2, ".")
elif (numero2 > numero3 > numero1):
    print("(D)Ordenados de forma creciete: ", numero1, " - ", numero3, " - ", numero2, ".")
elif (numero3 > numero1 > numero2):
    print("(E)Ordenados de forma creciete: ", numero2, " - ", numero1, " - ", numero3, ".")
else:
    print("(F)Ordenados de forma creciete: ", numero1, " - ", numero2, " - ", numero3, ".")
