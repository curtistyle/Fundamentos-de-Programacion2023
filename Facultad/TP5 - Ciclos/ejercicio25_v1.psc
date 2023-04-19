Algoritmo ejercicio25
    Definir Indice Como Entero;
    Definir Monto, MontoTotal Como Real;
	
    Indice <- 0;
	MontoTotal <- 0;
	
    Escribir "Ingrese la lista de precios.";
	
	Repetir
		Indice <- Indice + 1;
		Escribir "Monto del poducto (", Indice ,"): ";
		Leer Monto;
		MontoTotal <- MontoTotal + Monto;
	Hasta Que (Monto = 0)

	Escribir "Cantidad de productos: ", Indice ,".";
	Escribir "Monto Total a pagar: $", MontoTotal ,".";
FinAlgoritmo