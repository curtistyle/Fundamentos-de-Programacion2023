Algoritmo ejercicio6
	Definir Numero1, Numero2, Auxiliar Como Real;
	
	Escribir "Ingrese el primer numero: ";
    Leer Numero2;
	Escribir "Ingrese el segundo numero: ";
	Leer Numero2;
    
	Si ((Numero1 mod Numero2) = 0) Entonces
        Auxiliar <- Numero1;
        Numero1 <- Numero2;
        Numero2 <- Auxiliar;
        
        Escribir "Se intercambambiaron los numeros, Numero1: ", Numero1 ," y Numero2: ", Numero2;
    FinSi
FinAlgoritmo
