Algoritmo ejercicio2
    Definir Indice, Suma Como Entero;
	Definir Producto Como Real;
	
    Producto <- 1;
    Suma <- 0;
	
    Para Indice <- 20 Hasta 500 Hacer
        Si ((Indice mod 2) = 0) Entonces
            Suma <- Suma + Indice;
            Producto <- Producto * Indice;
        FinSi
    FinPara
	
    Escribir "Suma: ", Suma ," Producto: ", Producto;
FinAlgoritmo