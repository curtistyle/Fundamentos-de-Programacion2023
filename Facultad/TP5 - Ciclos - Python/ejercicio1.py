""" Ingresar  5  pares  de  valores,  en  cada  oportunidad  emitir  ambos  valores  y  si  ambos  son 
positivos, emitir también su promedio.  """

for index in range(1,6):
    print(f"Par {index}.")
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese un numero: "))
    print(f" > Par ({index}), Numero 1: {numero1} y Numero 2: {numero2}.")
    if (numero1 > 0) and (numero2 > 0):
        print(f"Su promedio es: {((numero1 + numero2) / 2):.2f}.")
    input()
     
