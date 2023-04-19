Algoritmo ejercicio23
    Definir Numero, Indice, Maximo, Contador, Factorial Como Entero;
	
    Factorial <- 1;
    Contador <- 0;
	
    Repetir
		Escribir "Ingrese un numero: ";
        Leer Numero;
		
        Si (Numero > 0) Entonces
            Si Numero > 1000 Entonces
                Contador <- Contador + 1;
			FinSi
		FinSi
	Hasta Que (Numero = 0)
		
	Si (Contador < 20) Entonces
		Para Indice <- 1 Hasta Contador Hacer
			Factorial <- Factorial * Indice;         
		FinPara    
	FinSi
	
	Escribir "Hay ", Contador ," valores mayores a 1000.";
	Si (Contador < 20) Entonces
		Escribir "El factorial de ", Contador , " es! ", Factorial ,".";
	FinSi
FinAlgoritmo