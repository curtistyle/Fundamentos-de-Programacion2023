Algoritmo ejercicio2
    Definir Indice, Suma Como Entero;
	Definir Producto Como Real; 
	
    Producto <- 1;
    Suma <- 0;
	
    Para Indice <- 20 Hasta 500 Con Paso 2 Hacer
		Suma <- Suma + Indice;
		Producto <- Producto * Indice;
    FinPara
	
    Escribir "Suma: ", Suma ," Producto: ", Producto;
FinAlgoritmo