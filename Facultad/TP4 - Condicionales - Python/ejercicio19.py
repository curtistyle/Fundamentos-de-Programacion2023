"""  Leer un número, si dicho número está comprendido entre 23 y 54, decir si es múltiplo de 3 
o de 5.  """

numero = int(input("Ingrese un numero: "))

if (numero >= 23) and (numero <= 54):
    if ((numero % 3) == 0):
        print("El numero ", numero, " es multiplo de 3.")
    if ((numero % 5) == 0):
        print("El numero ", numero, " es multiplo de 5.")


