//  Se tiene el monto disponible para abonar los sueldos de los empleados 
//	de una empresa, la propuesta es que el/la estudiante plantee el ejercicio
//	para abonar los sueldos hasta que no se disponga m�s de fondos. Incluya 
//  las modificaciones que crea necesarias para mostrar la cantidad de 
//	sueldos abonados. Determine adem�s en el caso que posea fondos 
//	determinados por cada una de las tres sucursales de una empresa, �c�mo
//	dise�ar�a el algoritmo para que cumpla con el objetivo?

Algoritmo ejercicio1
	Definir Fondos, Monto Como Real;
	Definir Empleados Como Entero;
	
	Empleado <- 1;
	
	Escribir "Ingrese los fondos de la empresa: ";
	Leer Fondos;

	Repetir 
		Escribir "Ingrese el monto del empleado N� ", Empleado,".";
		Leer Monto;
		
		Si (Monto <= Fondos) Entonces
			
		FinSi
		
	Hasta Que (Fondos = 0) 
FinAlgoritmo
