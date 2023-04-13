Algoritmo ejercicio16
	Definir Letra Como Caracter;
	Definir Contador Como Entero;
	
	Contador <- 0;
	
	Repetir
		Escribir " > Ingrese un catacter: ";
		Leer Letra;
		Si (Letra > '0') y (Letra < '9') Entonces
			Contador <- Contador + 1;
		FinSi
	Hasta Que (Letra = '#')
	
	Escribir "Los caracteres comprendidos entre 0..9 aparecen: ", Contador ," veces.";
FinAlgoritmo