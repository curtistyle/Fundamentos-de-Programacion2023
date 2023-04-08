Algoritmo ejercicio3
    Definir Numero, Maximo, Indice, Orden Como Entero;
	
    Maximo <- 0;
    Para Indice <- 1 Hasta 475 Hacer
        Leer Numero;
		
        Si (Numero > Maximo) Entonces
            Maximo <- Numero;
            Orden <- Indice;
        FinSi
    FinPara
	
    Escribir "Valor maximo del lote es: ", Maximo ,", en el orden: ", Orden ,".";
FinAlgoritmo