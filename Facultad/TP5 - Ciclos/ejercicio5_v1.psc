Algoritmo ejercicio5
    Definir Numero Como Real;
    Definir Indice, Contador Como Entero;
	
    Contador <- 0;
    Para Indice <- 1 Hasta 100 Hacer
        Escribir "(",Indice,") Ingrese un numero: ";
		Leer Numero;
        Si ((Numero mod 2) = 0) Entonces
            Escribir "El numero ", Numero ," es multiplo de 2.";
            Contador <- Contador + 1;            
        FinSi
    FinPara
    Escribir "Cantidad de numeros multiplo de 2: ", Contador;
FinAlgoritmo