// Escribir  un  algoritmo  que  permita  leer  una  serie  de  enteros.  Contar  el  Nº  de  valores introducidos y su suma. 

Algoritmo ejercicio20
	Definir Numero, Contador, Acumulador Como Entero;
	
	Acomulador <- 0;
	Contador <- 0;
	Numero <- 1;
	
	Mientras (Numero <> 0) Hacer
		Escribir "Ingrese un numero: ";
		Leer Numero;
		Contador <- Contador + 1;
		Acomulador <- Acomulador + Numero;
	FinMientras
FinAlgoritmo
