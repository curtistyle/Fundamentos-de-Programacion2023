Algoritmo ejercicio1
	Definir Indice, Personal, TotalPersonal, AuxPersonal Como Entero;
	Definir Costos, TotalCostos, AuxCostos, Porcentaje Como Real;
	Definir NombreCompleto Como Caracter;
	
	TotalCostos <- 0;
	TotalPersonal <- 0;
	AuxCostos <- 0;
	
	Para Indice <- 0 Hasta 5 Hacer
		Escribir "Nombre completo del responsable de la obra: ";
		Leer NombreCompleto;
		Escribir "Ingrese los datos de la obra(",Indice,").";
		Escribir "Costos de la obra: $";
		Leer Costos;
		Escribir "Cantidad de Personal involucrado en la obra: ";
		Leer Personal;
		
		Si (NombreCompleto = "Maria Paez") Entonces
			AuxCostos <- Costos;
			AuxPersonal <- Personal;
		FinSi
		
		TotalCostos <- TotalCostos + Costos;
		TotalPersonal <- TotalPersonal + Personal;
	FinPara
	
	Escribir "Total de fondos de la obra: ", TotalCostos;
	Escribir "Total de personal de las obras: ", TotalPersonal;
	
	Si (AuxCostos <> 0) Entonces
		Escribir "Maria Paez tiene un cargo en la obra.";
		Porcentaje <- (AuxCostos * 100) / TotalCostos;
		Escribir "Su porcentaje de inversion en la obra con respecto a las demas: ", Porcentaje ,"%";
		Escribir "Cantidad de personal a cargo de Maria Paez: ", AuxPersonal;
	FinSi
FinAlgoritmo


