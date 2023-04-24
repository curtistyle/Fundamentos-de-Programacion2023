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
	
    Escribir "El Nº de Tarjetas Rojas y Pares: ", Par;
    Escribir "El Nº de Tarjetas Azules e Impares: ", Impar;
    Escribir "El resto de tarjetas: ", (Indice - (Par + Impar));
FinAlgoritmo