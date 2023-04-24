Algoritmo ejercicio21
    Definir Numero, AuxNumero, Indice Como Entero;
    Definir Palo, AuxPalo Como Cadena;
	
	Escribir "Ingrese una carta. ";
	Escribir "Numero: ";
	Leer Numero;
	Escribir "Palo: ";
	Leer Palo;
	AuxPalo <- Palo;
	AuxNumero <- Numero + 1;
	Escribir "Se separo del mazo el ", Numero ," de ", Palo ,".";
	Indice <- 0;
	
    Mientras No ((AuxPalo = Palo) y (AuxNumero = Numero)) Hacer
        Escribir "Ingrese una carta. ";
        Escribir "Numero: ";
        Leer Numero;
        Escribir "Palo: ";
        Leer Palo;
		
		Indice <- Indice + 1;
    FinMientras
	
    Escribir "Fueron necesario sacar ", Indice ," cartas del mazo.";
FinAlgoritmo