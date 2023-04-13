Algoritmo ejercicio10
    Definir Indice, N  Como Entero;
	Definir Serie Como Real;
	
    Serie <- 0;
	
	Escribir "Calculadora de la serie h(n)=1 + ½ + 1/3 + ... + 1/n."
	Escribir "Ingrese el valor de N: ";
    Leer N;
	
    Si (N > 0) Entonces
        Para Indice <- 1 Hasta N Hacer
            Serie <- Serie + 1/Indice;
        FinPara
    SiNo
        Escribir "N debe ser mayor que 0.";
    FinSi
	
    Escribir "El resultado de la serie es: ", Serie;
FinAlgoritmo