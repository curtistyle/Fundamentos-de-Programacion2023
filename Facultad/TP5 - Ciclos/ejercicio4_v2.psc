Algoritmo ejercicio4
    Definir Numero, Indice Como Entero;
    Definir Letra Como Caracter;
		
	Escribir "Ingrese un numero: ";
    Leer Numero;
	Escribir "Ingrese una letra: ";
	Leer Letra;
	Escribir "Susecion: ";

    Indice <- 1;
	
    Mientras (Indice <= Numero) Hacer
        Escribir "[", Indice ,"]: ", Letra;
        Indice <- Indice + 1;
    FinMientras
FinAlgoritmo