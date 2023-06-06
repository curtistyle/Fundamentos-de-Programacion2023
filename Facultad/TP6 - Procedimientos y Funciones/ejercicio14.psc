SubProceso Calcular_Suma(Limite , Resultado Por Referencia)
	Definir Indice Como Entero;
	Resultado <- 0;
	Para Indice <- 1 Hasta Limite Hacer
		Resultado <- Resultado + Indice;
	FinPara
FinSubProceso

Algoritmo ejercicio14
	Definir Limite, Resultado Como Entero;
	Escribir "Ingrese un numero: ";
	Leer Limite;
	
	Calcular_Suma(Limite,Resultado);
	
	Escribir "El resultado de la sumatoria es: ", Resultado;
FinAlgoritmo
