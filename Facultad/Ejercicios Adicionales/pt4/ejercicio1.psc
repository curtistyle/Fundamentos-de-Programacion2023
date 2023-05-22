//  Se tiene el monto disponible para abonar los sueldos de los empleados 
//	de una empresa, la propuesta es que el/la estudiante plantee el ejercicio
//	para abonar los sueldos hasta que no se disponga más de fondos. Incluya 
//  las modificaciones que crea necesarias para mostrar la cantidad de 
//	sueldos abonados. Determine además en el caso que posea fondos 
//	determinados por cada una de las tres sucursales de una empresa, ¿cómo
//	diseñaría el algoritmo para que cumpla con el objetivo?

Algoritmo ejercicio1
	Definir Fondos, Monto Como Real;
	Definir Empleado Como Entero;
	
	Empleado <- 1;
	Monto <- 0;
	
	Escribir "Ingrese el monto total de la empresa: ";
	Leer Fondos;
	
	// - Designa los sueldos a los empledos hasta que el ultimo monto 
	//   que se asigna es mayor a los fondos de la empresa.
	Escribir "Ingrese el sueldo del Empleado Nº ",Indice,'.:';
	Leer Monto;
	Mientras ((Fondos > Monto) y (Fondos > 0))  Hacer
		Si (Monto < Fondos) Entonces
			Fondos <- Fondos - Monto;
			Escribir "Se le abono al empleado $",Monto,'.';	
			Empleado <- Empleado + 1;
			Escribir "Fondos disponibles: $", Fondos,'.';
			Escribir "Ingrese el sueldo del Empleado Nº ",Indice,'.:';
			Leer Monto;
		SiNo
			Escribir "Fondos insuficientes.";
		FinSi
	FinMientras
	Escribir "Fondos insuficientes";
	
	Escribir "La empresa abono ", Empleado, " sueldos";
FinAlgoritmo
