""" Se dispone de un conjunto de tarjetas rojas y azules, las cuales están numeradas en forma 
correlativa. El lote de tarjetas termina con una tarjeta blanca. El problema es determinar 
de  las  tarjetas  del  lote:  cuántas  son  azules  y  con  número  par;  cuántas  son  rojas  y  con 
número impar, y cuántas son las restantes (excepto la blanca) 
Algoritmo ejercicio24
    Definir Indice, Par, Impar Como Entero;
    Definir Tarjeta Como Cadena;
	
    Indice <- 0;
    Par <- 0;
    Impar <- 0;
	
	Escribir "Ingrese el lote de Cartas Rojas y Azules, (Blanca para terminar el ciclo).";
	Indice <- Indice + 1;
	Escribir "(", Indice ,") Ingresar el color de la tarjeta (roja/azul): ";
	Leer Tarjeta;
    Mientras No ((Tarjeta = 'Blanca') o (Tarjeta = 'blanca')) Hacer
        Si (Tarjeta = 'Roja') o (Tarjeta = 'roja') Entonces
            Si ((Indice mod 2) = 0) Entonces
                Par <- Par + 1;
            FinSi
        SiNo
            Si (Tarjeta = 'Azul') o (Tarjeta = 'azul') Entonces
				Si ((Indice mod 2) <> 0) Entonces
					Impar <- Impar + 1;
				FinSi
			SiNo
				Escribir "Dato invalido.";
				Indice <- Indice + 1;
			FinSi
		FinSi
		
		Indice <- Indice + 1;
        Escribir "(", Indice ,") Ingresar el color de la tarjeta (roja/azul): ";
        Leer Tarjeta;
	FinMientras
	Indice <- Indice - 1;
	
    Escribir "El N� de Tarjetas Rojas y Pares: ", Par;
    Escribir "El N� de Tarjetas Azules e Impares: ", Impar;
    Escribir "El resto de tarjetas: ", (Indice - (Par + Impar));
FinAlgoritmo

"""

# incicializar variables
indice = 1
par = 0
impar = 0

print("Ingrese el lote de cartas Rojas y Azules (Blanca para terminar).")

tarjeta = input(f"({indice}) Ingrese el color de la tarjeta: ")

while not ((tarjeta == 'blanca') or  (tarjeta == 'Blanca')):
    if (tarjeta == 'roja') or (tarjeta == 'Roja'):
        if ((indice % 2) == 0):
            par += 1
    elif (tarjeta == 'azul') or (tarjeta == 'Azul'):
        if ((indice % 2) != 0):
            impar += 1   
    else:
        print("Dato Invalido !.")
        indice -= 1
    tarjeta = input(f"({indice}) Ingrese el color de la tarjeta: ")
    indice += 1
    
print(f"Tarjetas Rojas Pares: {par}.")
print(f"Tarjetas Azules Impares: {impar}.") 
print(f"Resto de Tarjetas: {(indice - 1) - (par + impar)}")


    

        



