Algoritmo ejercicio2
    Definir Indice, Suma Como Entero;
	Definir Producto Como Real;
	
    Indice <- 20;
    Producto <- 1;
    Suma <- 0;
	
    Mientras Indice <= 500 Hacer
        Si ((Indice mod 2) = 0) Entonces
            Suma <- Suma + Indice;
            Producto <- Producto * Indice;
        FinSi
        Indice <- Indice + 1;
    FinMientras
	
    Escribir "Suma: ", Suma ," Producto: ", Producto;
FinAlgoritmo