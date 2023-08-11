""" Calcular el descuento considerando que para un monto mayor de $  1000.- el descuento 
es del 10%, caso contrario es del 2%. Se pide mostrar monto con descuento incluido. """

monto = float(input("Ingrese el monto: "))

if (monto > 1000):
    print(f"Usted recibira un descuento del 10%: ${(monto - ((monto * 10)/100)):.2f}.")
else:
    print(f"Usted recibira un descuento del 5%: ${(monto - ((monto * 10)/100)):.2f}.")