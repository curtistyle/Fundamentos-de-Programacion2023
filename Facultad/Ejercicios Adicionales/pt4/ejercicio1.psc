//  Se tiene el monto disponible para abonar los sueldos de los empleados 
//	de una empresa, la propuesta es que el/la estudiante plantee el ejercicio
//	para abonar los sueldos hasta que no se disponga más de fondos. Incluya 
//  las modificaciones que crea necesarias para mostrar la cantidad de 
//	sueldos abonados. Determine además en el caso que posea fondos 
//	determinados por cada una de las tres sucursales de una empresa, ¿cómo
//	diseñaría el algoritmo para que cumpla con el objetivo?

Algoritmo ejercicio1
	Definir Fondos, Monto Como Real;
	Definir Indice Como Entero;
	
	Indice <- Indice = 0;
	
	Escribir "Ingrese el monto total de la empresa: ";
	Leer Fondos;
	
	
	Repetir 
		Si (Fondos > 0) Entonces
			
			Escribir "Ingrese el sueldo del Empleado Nº",Indice,'.:';
			Leer Monto;
			Si (Monto < Fondos) Entonces
				Fondos <- Fondos - Monto;
				Indice <- Indice + 1;
				Escribir "Se le abono al empleado $", Trunc(Monto),'.';
			SiNo
				Escribir "Fondos insuficientes."
			FinSi
		FinSi
		
		Escribir "Fondos disponibles: ", Fondos;
	Hasta Que (Fondos = 0) 
FinAlgoritmo
