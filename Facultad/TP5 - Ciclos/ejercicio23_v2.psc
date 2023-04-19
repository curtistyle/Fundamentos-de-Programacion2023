Algoritmo ejercicio23
    Definir Numero, Indice, Maximo, Contador, Factorial Como Entero;
	
    Factorial <- 1;
    Contador <- 0;
	Numero <- 1;
	
    Mientras (Numero <> 0) Hacer
		Escribir "Ingrese un numero: ";
        Leer Numero;
		
        Si (Numero > 0) Entonces
            Si Numero > 1000 Entonces
                Contador <- Contador + 1;
				Factorial <- Factorial * Contador;
			FinSi
		FinSi
	FinMientras
	
	
	Escribir "Hay ", Contador ," valores mayores a 1000.";
	Si (Contador < 20) Entonces
		Escribir "El factorial de ", Contador , "! es ", Factorial ,".";
	FinSi
FinAlgoritmo