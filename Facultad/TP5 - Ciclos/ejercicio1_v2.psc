Algoritmo ejercicio1
	Definir Numero1, Numero2, Promedio Como Real;
	Definir Indice Como Entero;
	
	Indice <- 1;
	
	Mientras  Indice <= 5 Hacer
		Escribir "Ingrese el par (", Indice ,"): ";
		Escribir "Numero 1: ";
		Leer Numero1;
		Escribir "Numero 2: ";
		Leer Numero2;
		Escribir "Par [", Indice, "]: ", Numero1," y ", Numero2,".";
		
		Si (Numero1 > 0) y (Numero2 > 0) Entonces
			Promedio <- (Numero1 + Numero2) / 2;
			Escribir "Como el par [", Indice ,"] es positivo, su promedio es:  ", Promedio;
		FinSi
		Indice <- Indice + 1;
	FinMientras
FinAlgoritmo
	