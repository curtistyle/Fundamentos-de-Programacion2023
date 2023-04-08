Algoritmo ejercicio2
    Definir Indice, Suma Como Entero;
	Definir Producto Como Real;
	
    Indice <- 19;
    Producto <- 1;
    Suma <- 0;
	
    Repetir
        Indice <- Indice + 1;
		Si ((Indice mod 2) = 0) Entonces
            Suma <- Suma + Indice;
            Producto <- Producto * Indice;
        FinSi
    Hasta Que Indice = 500;
	
    Escribir "Suma: ", Suma ," Producto: ", Producto;
FinAlgoritmo