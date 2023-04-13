Algoritmo ejercicio11
    Definir Indice, Numero1, Numero2, Contador1, Contador2 Como Entero;
	
    Para Indice <- 1 Hasta 50 Hacer
        Escribir "Ingrese un par de numero: ";
		Escribir "X: ";
		Leer Numero1;
		Escribir "Y: ";
		Leer Numero2;
		
        Si (Numero1 > Numero2) Entonces
            Contador1 <- Contador1 + 1;
        SiNo
            Si (Numero1 < Numero2) Entonces
                Contador2 <- Contador2 + 1;
            SiNo
                Escribir "El par de numero no puede ser igual."
            FinSi
        FinSi
    FinPara
    
    Escribir "Hay ", Contador1 ," pares donde X > Y.";
    Escribir "Hay ", Contador2 ," pares donde X < Y.";
FinAlgoritmo