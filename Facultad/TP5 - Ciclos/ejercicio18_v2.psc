Algoritmo ejercicio18
    Definir Letra, Ocurrencia Como Cadena;
    Definir Contador Como Entero;
	
    Contador <- 0;
    
    Escribir "Ingrese el caracter que desea que se cuente: ";
    Leer Ocurrencia;
	
	Escribir "Ingrese una letra: ";
	Leer Letra;
	
    Mientras (Letra <> '.') Hacer
        Si (Letra = Ocurrencia) Entonces
            Contador <- Contador + 1;
        FinSi
		Escribir "Ingrese una letra: ";
        Leer Letra;
    FinMientras
	
	Escribir "El caracter ", Ocurrencia , " se repitio ", Contador ," veces.";
FinAlgoritmo