Algoritmo ejercicio15
    Definir Descuento, Monto Como Real;
	
	Escribir "Ingrese el monto: ";
    Leer Monto;
	
    Si (Monto > 1000) Entonces
        Descuento <- Monto - (Monto * 0.1);
        Escribir "Monto: $", Monto ," el descuento del 10%: $", Descuento;  
    SiNo
        Descuento <- Monto - (Monto * 0.02);
        Escribir "Monto: $", Monto ," el descuento del 2%: $", Descuento; 
    FinSi
FinAlgoritmo