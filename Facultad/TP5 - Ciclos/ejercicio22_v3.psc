// Dada una lista de valores numéricos, hallar su rango, es decir la diferencia entre su valor 
// máximo y su valor mínimo

Algoritmo ejercicio22
    Definir Numero, Maximo, Minimo, Indice Como Entero;
	
    Indice <- 0;
	Escribir "Ingrese un numero: ";
	Leer Numero;
	Minimo <- Numero;
	Maximo <- Numero;
	
    Mientras (Numero <> 0) Hacer
        Si (Numero > Maximo) y (Numero <> 0) Entonces
            Maximo <- Numero;
        SiNo
            Si (Numero < Minimo) y (Numero <> 0) Entonces
				Minimo <- Numero;
			FinSi
        FinSi
		Escribir "Ingrese un numero: ";
		Leer Numero;
    FinMientras
	
    
    Escribir "Maximo: ", Maximo ," Minimo: ", Minimo;
	Escribir "Su rango es: ", Maximo - Minimo;
FinAlgoritmo
