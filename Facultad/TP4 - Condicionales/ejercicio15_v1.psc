Algoritmo ejercicio15
    Definir Descuento, Monto, Total Como Real;
	
	Escribir "Ingrese el monto: ";
    Leer Monto;
	
    Si (Monto > 1000) Entonces
        Descuento <- (10 * Monto) / 100;
        Total <- Monto - Descuento;
        Escribir "Monto mas el descuento del 10%: ", Total; 
    SiNo
        Descuento <- (2 * Monto) / 100;
        Total <- Monto - Descuento;
        Escribir "Monto mas el descuento del 2%: ", Total; 
    FinSi
FinAlgoritmo