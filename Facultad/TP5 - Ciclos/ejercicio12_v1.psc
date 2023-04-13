Algoritmo ejercicio12
    Definir Indice, Contador1, Contador2, Contador3, Numero Como Entero;
	
    Contador1 <- 0;
    Contador2 <- 0;
    Contador3 <- 0;
	
    Para Indice <- 1 Hasta 10 Hacer
        Escribir "Ingrese el nivel (1/2/3) de comportamiento del alumno (",Indice,"): ";
        Leer Numero;
        
        Segun Numero Hacer
            1 : Contador1 <- Contador1 + 1;
            2 : Contador2 <- Contador2 + 1;
            3 : Contador3 <- Contador3 + 1;
        FinSegun
    FinPara
	
	
    Escribir Contador1 ," alumnos obtuvieron la calificacion 1.";
    Escribir Contador2 ," alumnos obtuvieron la calificacion 2.";
    Escribir Contador3 ," alumnos obtuvieron la calificacion 3.";
FinAlgoritmo