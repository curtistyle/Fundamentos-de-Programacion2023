""" Escribir  un  programa  que,  utilizando  procedimientos  con  parámetros,  lea  desde  el 
teclado  las  unidades  y  el  precio  que  quiere  comprar,  y  en  función  de  las  unidades 
introducidas le haga un descuento o no. """

def descuento(monto, desc):
    pass


opcion = input("Quiere ingresar productos (s/n): ")

while(opcion == 's'):
    cantidad = int(input("Ingrese la cantidad de productos: "))
    monto = float(input("Ingrese el monto (por unidad) del produco: $"))

    monto = monto * cantidad

    desc = 0
    opcion = input("Quiere hacer un descuento (s/n): ")
    if (opcion == 's') and (opcion == 'S'):
        desc = float(input("Ingrese el porcentaje del descuento: %"))
        total = descuento(monto, desc)
    
    if (desc != 0):
        print(f"Usted compro {cantidad} productos por ${monto} pero recibe un descuento del %{desc:.2f} por lo tanto usted paga ${total:.2f}.")
    else:
        print(f"Usted compro {cantidad} productos por ${monto} pero no recibe un descuento.")




