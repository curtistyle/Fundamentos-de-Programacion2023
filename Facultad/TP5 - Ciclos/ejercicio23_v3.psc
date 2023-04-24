Algoritmo ejercicio23
    Definir Numero, Indice, Maximo, Contador, Factorial Como Entero;
	
    Factorial <- 1;
    Contador <- 1;
	
	Escribir "Ingrese un numero: ";
	Leer Numero;
	
    Mientras (Numero <> 0) Hacer		
        Si (Numero > 0) Entonces
            Si Numero > 1000 Entonces
                Contador <- Contador + 1;
			FinSi
		FinSi
		
		Escribir "Ingrese un numero: ";
        Leer Numero;
	FinMientras
	
	Si (Contador < 20) y (Contador > 1) Entonces
		Para Indice <- 1 Hasta Contador Hacer
			Factorial <- Factorial * Indice;         
		FinPara    
	SiNo
		Factorial <- 1;
	FinSi
	
	Escribir "Hay ", Contador ," valores mayores a 1000.";
	Si (Contador < 20) Entonces
		Escribir "El factorial de ", Contador , " es ", Factorial ,".";
	FinSi
FinAlgoritmo