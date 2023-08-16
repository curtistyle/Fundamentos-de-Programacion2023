""" Se leen 50 pares de Números, c/u de los cuales tienen 2 valores: x e y distintos. Se pide 
contar en cuantos pares x>y y en cuantos y>x. """

contadorx = 0
contadory = 0

for index in range(1,5):
    print(f"Par ({index}).")
    x = int(input("Ingrese un numero: "))
    y = int(input("Ingrese otro numero: "))

    if (x > y):
        contadorx += 1
    elif (x < y):
        contadory += 1
    else:
        print("Los numeros del par leido son iguales, ingrese un par distinto.")
        index -= 1
    
print(f"Hay {contadorx} pares x > y. ")
print(f"Hay {contadory} pares y > x. ")

