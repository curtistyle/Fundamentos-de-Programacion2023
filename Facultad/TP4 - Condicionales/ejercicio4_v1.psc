Algoritmo ejercicio4
	Definir Numero1, Numero2, Resultado Como Entero;
	
	Escribir "Ingrese el primer numero: ";
    Leer Numero1;
	Escribir "Ingrese el segundo numero: ";
	Leer Numero2;
	
    Resultado <- Numero1 mod Numero2;
	
    Si (Resultado = 0) Entonces
        Escribir Numero1 ," es divisible por ", Numero2;
    FinSi
FinAlgoritmo
