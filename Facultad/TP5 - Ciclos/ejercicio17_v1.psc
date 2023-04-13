Algoritmo ejercicio17
    Definir Numero, Maximo, Contador Como Entero;
	
    Maximo <- 0;
	
    Repetir
		Escribir "Ingrese un numero (0 para terminar): ";
        Leer Numero;
		
        Si (Numero > Maximo) Entonces
            Maximo <- Numero;
        FinSi
        Si (Numero < 0) Entonces
            Contador <- Contador + 1;
        FinSi
    Hasta Que (Numero = 0)
	
    Escribir "El maximo de los numeros ingresado es: ", Maximo;
    Escribir "La cantidad de numeros negativos: ", Contador;
FinAlgoritmo