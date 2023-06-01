SubAlgoritmo Suma <- Sumar ( Num1, Num2 )
	Suma <- Num1 + Num2;
FinSubAlgoritmo

Funcion s <- perimetro(a,b)
	s <- a+b;
FinFuncion

Algoritmo Test
	Definir Numero1, Numero2, Resultado Como Entero;
	
	Escribir "Ingrese dos numero: ";
	Leer Numero1;
	Leer Numero2;
	
	Resutaldo <- Sumar(Numero1, Numero2);
	
	Escribir  "La suma es: ", Resultado; 
	Escribir "Perimetro: ",perimetro(Numero1,Numero2);
FinAlgoritmo
	