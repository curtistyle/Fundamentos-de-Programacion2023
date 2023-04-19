Algoritmo ejercicio22
    Definir Numero, Maximo, Minimo, Indice Como Entero;
    Definir Control Como Logico;
	
    Control <- Falso;
    Indice <- 0;
    Maximo <- 0;
    Minimo <- 0;
	Numero <- 1;
	
    Mientras (Numero <> 0) Hacer
        Leer Numero;
		
        Si (Control = Falso) Entonces
            Minimo <- Numero;
			Maximo <- Numero;
            Control <- Verdadero;
        FinSi
		
        Si (Numero >= Maximo) y (Numero <> 0) Entonces
            Maximo <- Numero;
        SiNo
            Si (Numero <= Minimo) y (Numero <> 0) Entonces
				Minimo <- Numero;
			FinSi
        FinSi
    FinMientras
	
    Escribir "Minimo: ", Minimo, ", Maximo: ", Maximo;
	Escribir "El rango del maximo y minimo es: ", Maximo - Minimo;
FinAlgoritmo