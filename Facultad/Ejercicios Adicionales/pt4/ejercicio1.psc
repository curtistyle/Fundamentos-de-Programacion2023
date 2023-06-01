//  Se tiene el monto disponible para abonar los sueldos de los empleados 
//	de una empresa, la propuesta es que el/la estudiante plantee el ejercicio
//	para abonar los sueldos hasta que no se disponga más de fondos. Incluya 
//  las modificaciones que crea necesarias para mostrar la cantidad de 
//	sueldos abonados. Determine además en el caso que posea fondos 
//	determinados por cada una de las tres sucursales de una empresa, ¿cómo
//	diseñaría el algoritmo para que cumpla con el objetivo?

Algoritmo ejercicio1
	Definir Fondos, Sueldo Como Real;
	Definir Empleado, Empresa Como Entero;
	
	Para Empresa <- 1 Hasta 3 Hacer
		Escribir "Ingrese el monto total de la empresa ",Empresa,": ";
		Leer Fondos;
		
		// - Designa los sueldos a los empledos hasta que el ultimo monto 
		//   que se asigna es mayor a los fondos de la empresa.
		Escribir "Ingrese el sueldo del Empleado Nº ",Empleado,'.:';
		Leer Sueldo;
		Mientras ((Fondos > Sueldo) y (Fondos > 0))  Hacer
				Fondos <- Fondos - Sueldo;
				Empleado <- Empleado + 1;
				Escribir "Se le abono al empleado $",Sueldo,'.';	
				Escribir "Fondos disponibles: $", Fondos,'.';
				Escribir "Ingrese el sueldo del Empleado Nº ",Empleado,'.:';
				Leer Sueldo;
		FinMientras
		Escribir "Fondos insuficientes";
		
		Escribir "La empresa ",Empresa," abono ", Empleado, " sueldos";
	FinPara
FinAlgoritmo
