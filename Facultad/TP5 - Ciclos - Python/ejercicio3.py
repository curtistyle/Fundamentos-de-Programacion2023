""" Leer  un  lote  de  475  valores  de  a  uno  por  vez.  Determinar  y  emitir  el  valor  máximo  del 
conjunto y el orden en que fue leído. Si hay más de un máximo considerar solo el primer 
valor hallado.  """
mayor = 0
pos = 0
for index in range(1,10):
    numero = int(input(f"({index})Ingrese un numero: "))
    if numero > mayor:
        mayor = numero
        pos = index

print(f"El valor mayor leido es {mayor} y fue ingresado en la posicion #{pos}.")

