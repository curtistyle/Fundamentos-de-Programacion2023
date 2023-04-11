Algoritmo ejercicio4
    Definir Numero, Indice Como Entero;
    Definir Letra Como Caracter;
	
	Escribir "Ingrese un numero: ";
    Leer Numero;
	Escribir "Ingrese una letra: ";
	Leer Letra;
	Escribir "Susecion: ";
	
    Indice <- 0;
	
    Repetir
		Indice <- Indice + 1;
        Escribir "[", Indice ,"]: ", Letra;
    Hasta Que Indice = Numero;
FinAlgoritmo