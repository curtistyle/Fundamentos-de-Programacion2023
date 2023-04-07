Algoritmo sin_titulo
	Definir Numero1, Numero2, Promedio Como Real;
	
	Escribir "Ingrese el primer numero: ";
    Leer Numero1;
	Escribir "Ingrese el segundo numero: ";
	Leer Numero2;
	
    Si (Numero1 > 0) y (Numero2 > 0) Entonces
        Promedio <- (Numero1 + Numero2) / 2;
        Escribir Numero1 ," y ", Numero2 ," son positivos y su promedio es: ", Promedio;
    SiNo
        Escribir "Los numeros No son positivos.";
    FinSi
FinAlgoritmo
