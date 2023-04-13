Algoritmo ejercicio13
    Definir Empleado, Seccion, Total, Edad Como Entero;
    Definir Promedio Como Real;
    Definir Seccion1, Seccion2, Seccion3, Seccion4, Seccion5 Como Entero;
    Definir Edad1, Edad2, Edad3, Edad4, Edad5 Como Entero;
	
    Seccion1 <- 0;
    Seccion2 <- 0;
    Seccion3 <- 0;
    Seccion4 <- 0;
    Seccion5 <- 0;
    Edad1 <- 0;
    Edad2 <- 0;
    Edad3 <- 0;
    Edad4 <- 0;
    Edad5 <- 0;
    Total <- 15;
	
    Para Empleado <- 1 Hasta Total Hacer
        Escribir "Ingrese la seccion (1/2/3/4/5) a la que pertenece el obrero(",Empleado,"): ";
        Leer Seccion
        Segun Seccion Hacer
            1 : 
                Seccion1 <- Seccion1 + 1;
                Escribir "Ingrese la edad del empleado: ";
				Leer Edad;
                Edad1 <- Edad1 + Edad;
            2 : 
                Seccion2 <- Seccion2 + 1;
                Escribir "Ingrese la edad del empleado: ";
                Edad2 <- Edad2 + Edad;
				Leer Edad;
            3 : 
                Seccion3 <- Seccion3 + 1;
                Escribir "Ingrese la edad del empleado: ";
                Edad3 <- Edad3 + Edad;
				Leer Edad;
            4 : 
                Seccion4 <- Seccion4 + 1;
                Escribir "Ingrese la edad del empleado: ";
                Edad4 <- Edad4 + Edad;
				Leer Edad;
            5 : 
                Seccion5 <- Seccion5 + 1;
                Escribir "Ingrese la edad del empleado: ";
                Edad5 <- Edad5 + Edad;
				Leer Edad;
			De Otro Modo:
				Escribir "Seccion incorrecta.";
		FinSegun
    FinPara
    
    Promedio <- Edad1 / Seccion1;
    Escribir "En la seccion 1 hay ", Seccion1 ," obreros y su promedio de edad es de : ", Promedio ," Años.";
	
    Promedio <- Edad2 / Seccion2;
    Escribir "En la seccion 2 hay ", Seccion2 ," obreros y su promedio de edad es de : ", Promedio ," Años.";
	
    Promedio <- Edad3 / Seccion3;
    Escribir "En la seccion 3 hay ", Seccion3 ," obreros y su promedio de edad es de : ", Promedio ," Años.";
	
    Promedio <- Edad4 / Seccion4;
    Escribir "En la seccion 4 hay ", Seccion4 ," obreros y su promedio de edad es de : ", Promedio ," Años.";
	
    Promedio <- Edad5 / Seccion5;
    Escribir "En la seccion 5 hay ", Seccion5 ," obreros y su promedio de edad es de : ", Promedio ," Años.";
FinAlgoritmo
