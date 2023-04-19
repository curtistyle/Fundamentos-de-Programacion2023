Algoritmo ejercicio21
    Definir Numero, AuxNumero, Indice Como Entero;
    Definir Palo, AuxPalo Como Cadena;
	
    Indice <- 0;
	AuxNumero <- 999;
	AuxPalo <- "nocard";
	Numero <- 0;
	Palo <- '';
	
    Mientras ((AuxPalo <> Palo) o (AuxNumero <> Numero)) Hacer
        Escribir "Ingrese una carta. ";
        Escribir "Numero: ";
        Leer Numero;
        Escribir "Palo: ";
        Leer Palo;
		
        Si (Indice = 0) Entonces
			Escribir "Se separo del mazo el ", Numero ," de ", Palo ,".";
            AuxPalo <- Palo;
            AuxNumero <- Numero + 1;
			Escribir "AuxPalo: ", AuxPalo, ", AuxNumero: ", AuxNumero;
        FinSi
		Indice <- Indice + 1;
    FinMientras
	
    Escribir "Fueron necesario sacar ", Indice - 1," cartas del mazo.";
FinAlgoritmo