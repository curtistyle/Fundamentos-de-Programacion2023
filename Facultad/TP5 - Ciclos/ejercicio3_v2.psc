Algoritmo ejercicio3
	Definir Numero, Maximo, Indice, Orden Como Entero;
	
	Maximo <- 0;
	Indice <- 1;
	Mientras Indice <= 10 Hacer
		Leer Numero;
		
		Si (Numero > Maximo) Entonces
			Maximo <- Numero;
			Orden <- Indice;
		FinSi
		Indice <- Indice + 1;
	FinMientras
	
	Escribir "Valor maximo del lote es: ", Maximo ,", en el orden: ", Orden ,".";
FinAlgoritmo