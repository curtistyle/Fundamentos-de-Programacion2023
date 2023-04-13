Algoritmo ejercicio6
	Definir Contador1, Contador2, Indice Como Entero;
	Definir Letra Como Caracter;
	
	Contador1 <- 0;
	Contador2 <- 0;

	Para Indice <- 1 Hasta 8 Hacer
		Escribir  "Ingrese una letra: ";
		Leer Letra;
		Segun Letra Hacer
			"a" : Contador1 <- Contador1 + 1; 
			"*" : Contador2 <- Contador2 + 1;
		FinSegun
	FinPara
	
	Escribir "Contador de (a):", Contador1;
	Escribir "Contador de (b):", Contador2;
FinAlgoritmo
