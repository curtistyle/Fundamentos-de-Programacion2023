Algoritmo ejercicio20
    Definir Numero, Suma, Contador Como Entero;
	
    Suma <- 0;
    Contador <- 0;
	
    Escribir "Ingrese una serie de numeros (termina el ciclo con -1): ";
	
    Repetir
		Escribir "Ingrese un numero: ";
        Leer Numero;
        Suma <- Suma + Numero;
        Contador <- Contador + 1;
    Hasta Que (Numero = -1)
	
    Escribir "Cantidad de numeros introducidos: ", Contador - 1;
    Escribir "Suma de los numeros introducidos: ", Suma + 1;
FinAlgoritmo