Algoritmo ejercicio21
    Definir Numero, AuxNumero, Indice Como Entero;
    Definir Palo, AuxPalo Como Cadena;
	
    Indice <- 0;
	
    Repetir 
        Escribir "Ingrese una carta. ";
        Escribir "Numero: ";
        Leer Numero;
        Escribir "Palo: ";
        Leer Palo;
		
        Si (Indice = 0) Entonces
			Escribir "Se separo del mazo el ", Numero ," de ", Palo ,".";
            AuxPalo <- Palo;
            AuxNumero <- Numero + 1;
        FinSi
		Indice <- Indice + 1;
    Hasta Que ((AuxPalo = Palo) y (AuxNumero = Numero))
	
    Escribir "Fueron necesario sacar ", Indice - 1," cartas del mazo.";
FinAlgoritmo