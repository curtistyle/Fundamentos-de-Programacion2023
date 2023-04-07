Algoritmo ejercicio10
	Definir Letra1, Letra2, Letra3 Como Caracter;
	
	Escribir "Ingrese el primer caracter: ";
	Leer Letra1;
	Escribir "Ingrese el primer caracter: ";
	Leer Letra2;
	Escribir "Ingrese el primer caracter: ";
	Leer Letra3;
	
	Si ((Letra1 < Letra2) & (Letra1 < Letra3)) Entonces
		Escribir "La letra {", Letra1, "} viene Primero.";
	SiNo
		Si ((Letra2 < Letra1) y (Letra2 < Letra3)) Entonces 
			Escribir "La letra {", Letra2 ,"} viene Primero.";
		SiNo
			Escribir "La letra {", Letra3 ,"} viene Primero.";
		FinSi
	FinSi
FinAlgoritmo
