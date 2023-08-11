""" Confeccionar un algoritmo tal que dados dos números enteros devuelva la suma de los 
mismos, si se cumple que el primero es menor que el segundo, en caso contrario devolver 
el producto de los mismos. """

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))



if (numero1 < numero2):
    print("La suma de los numeros da: ", numero1 + numero2)
else:
    print("El producto de los numeros da: ", numero1 * numero2)

