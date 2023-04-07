Algoritmo ejercicio19
    Definir Numero Como Real;
	
	Escribir "Ingrese un numero: ";
    Leer Numero;
	
    Si (Numero >= 23) y (Numero <= 54) Entonces
        Si ((Numero mod 5) = 0) Entonces
            Escribir Numero, " es multiplo de 5";
        SiNo
            Escribir Numero, " NO es multiplo de 5";
        FinSi
    Sino
        Escribir "El ", Numero , " no esta en el rango definido.";
    FinSi 
FinAlgoritmo  