Algoritmo ejercicio20
    Definir Nota1, Nota2, Nota3, Nota4, Promedio Como Real;
	
	Escribir "Ingrese la primera nota: ";
    Leer Nota1;
	Escribir "Ingrese la segunda nota: ";
	Leer Nota2;
	Escribir "Ingrese la tercera nota: ";
	Leer Nota3;
	Escribir "Ingrese la cuarta nota: ";
	Leer Nota4;
	
    Promedio <- (Nota1 + Nota2 + Nota3 + Nota4) / 4;
	
    Si (Promedio >= 4) Entonces
        Escribir "Su promedio es: ", Promedio ,", usted esta aprobado.";
    SiNo
        Escribir "Su promedio es: ", Promedio ,", usted esta desaprobado.";
    FinSi
FinAlgoritmo