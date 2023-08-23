""" Dada  una  lista  de  precios  de  productos,  la  cual  termina  con  un  precio  igual  a  cero.  Se 
desea saber el monto total a pagar y la cantidad de artículos comprados. 

Algoritmo ejercicio25
    Definir Indice Como Entero;
    Definir Monto, MontoTotal Como Real;
	
    Indice <- 0;
	MontoTotal <- 0;
	
    Escribir "Ingrese la lista de precios.";
	
	Repetir
		Indice <- Indice + 1;
		Escribir "Monto del poducto (", Indice ,"): ";
		Leer Monto;
		MontoTotal <- MontoTotal + Monto;
	Hasta Que (Monto = 0)

	Escribir "Cantidad de productos: ", Indice ,".";
	Escribir "Monto Total a pagar: $", MontoTotal ,".";
FinAlgoritmo
"""

indice = 0

print("Ingrese la lista de precios.")

monto = int(input("Ingrese un monto: "))

while (monto != 0):
    
    monto = int(input("Ingrese un monto: "))
    indice += 1
