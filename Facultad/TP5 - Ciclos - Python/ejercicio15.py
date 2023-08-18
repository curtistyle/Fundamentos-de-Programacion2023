""" Construir  un  algoritmo  que  muestre  por  pantalla  las  tablas  de  multiplicar  usuales  para 
valores comprendidos entre a y b. (a<b). """


a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))


if (a < b):
    for x in range(a,b+1):
        for y in range(1,11):
            print(f"{x} x {y} : {a*y}:")
else:
    print("a tiene que ser menor de b.")