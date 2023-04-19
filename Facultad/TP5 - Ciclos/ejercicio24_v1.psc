Algoritmo ejercicio24
    Definir Indice, Par, Impar, Contador Como Entero;
    Definir Tarjeta Como Cadena;
	
    Contador <- 0;
    Indice <- 0;
    Par <- 0;
    Impar <- 0;
	
	Escribir "Ingrese el lote de Cartas Rojas y Azules, (Blanca para terminar el ciclo).";
    Repetir
        Indice <- Indice + 1;
        Escribir "(", Indice ,") Ingresar el color de la tarjeta (roja/azul): ";
        Leer Tarjeta;
		
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
				Si (Tarjeta = 'Blanca') o (Tarjeta = 'blanca') Entonces
					Indice <- Indice - 1;
				SiNo
					Escribir "Dato Invalido";
					Indice <- Indice - 1;
				FinSi
			FinSi
		FinSi
	Hasta Que ((Tarjeta = 'Blanca') o (Tarjeta = 'blanca'))
		
	Escribir "El Nº de Tarjetas Rojas y Pares: ", Par;
	Escribir "El Nº de Tarjetas Azules e Impares: ", Impar;
	Escribir "El resto de tarjetas: ", (Indice - (Par + Impar));
FinAlgoritmo