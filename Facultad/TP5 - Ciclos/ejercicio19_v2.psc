Algoritmo ejercicio19
	Definir Numero, Contador Como Entero;
	
	Contador <- 0;
	
	Escribir "Ingrese un numero: ";
	Leer Numero;
	Mientras (Numero <> 0) Hacer
		Si (Numero < 0) Entonces
			Contador <- Contador + 1;
		FinSi
		Escribir "Ingrese un numero: ";
		Leer Numero;
	FinMientras
	
	Escribir "Se contaron ", Contador , " numeros negativos.";
FinAlgoritmo
