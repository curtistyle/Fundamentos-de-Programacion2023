Algoritmo ejercicio1
	Definir Numero1, Numero2, Promedio Como Real;
	Definir Indice Como Entero;
	
	Indice <- 0;
	
	Repetir
		Indice <- Indice + 1;
		Escribir " >>Ingrese el par (", Indice ,")<< ";
		Escribir "Numero 1: ";
		Leer Numero1;
		Escribir "Numero 2: ";
		Leer Numero2;
		Escribir "Par [", Indice, "]: ", Numero1," y ", Numero2,".";
		
		Si (Numero1 > 0) y (Numero2 > 0) Entonces
			Promedio <- (Numero1 + Numero2) / 2;
			Escribir "Como el par [", Indice ,"] es positivo, su promedio es:  ", Promedio;
		FinSi
	Hasta Que Indice = 5;
FinAlgoritmo