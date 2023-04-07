Algoritmo ejercicio5
	Definir Numero1, Numero2, Promedio Como Real;
	
	Escribir "Ingrese el primer numero: ";
    Leer Numero1;
	Escribir "Ingrese el segundo numero: ";
	Leer Numero2;
	
    Escribir Numero1, Numero2;
	
    Si (Numero1 > 0) y (Numero2 > 0) Entonces
        Promedio <- (Numero1 + Numero2) / 2;
		Escribir "El promedio de ", Numero1 ," y ", Numero2 ," es : ", Promedio;
    FinSi
FinAlgoritmo
