Algoritmo ejercicio18
    Definir Numero1, Numero2 Como Real;
	
	Escribir "Ingrese el primer numero: ";
    Leer Numero1;
	Escribir "Ingrese el segundo numero: ";
	Leer Numero2;
	
    Si ((Numero1 mod Numero2) = 0) Entonces
        Si ((Numero1 mod 2) = 0) Entonces
            Escribir "El primer numero es par.";
        SiNo
            Escribir "El primer numero es impar.";
        FinSi
    SiNo
        Escribir "El primer numero no es divisible por el segundo.";
    FinSi
FinAlgoritmo