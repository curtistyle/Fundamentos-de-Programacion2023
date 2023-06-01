SubProceso Perimetro <- Obtener_Perimetro( Radio )
	Definir Perimetro Como Real;
	Perimetro <- 2 * PI * Radio;
FinSubProceso



Algoritmo ejercicio2
	Definir Radio, Resultado Como Real;
	
	Escribir "Ingrese el Radio de la circunferencia para obtener el perimetro: ";
	Leer Radio;
	
	Resultado <- Obtener_Perimetro(Radio);
	Escribir "El perimetro de la circunferencia es: ", Resultado;
FinAlgoritmo
