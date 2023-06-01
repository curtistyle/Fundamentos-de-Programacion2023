//  Se tienen los trabajos presentados para cada una de las cuatro líneas de
//	un congreso de docentes binacional. De cada una se tienen temática,
//	moderador y cantidad de trabajos. Se pide procesar cada uno de los
//  trabajos presentados teniendo en cuenta que de cada uno se lee: título,
//	autores y línea en la cual se presenta (docencia en la pospandemia,
//	educación superior como derecho, investigación y extensión).
//  Se pide:
//	     a. Total de trabajos por línea y en total.
//	     b. Determinar de cual línea se presentaron mas trabajos y el
//	        porcentaje que representa este número en el total.
//	     c. Determinar si una autora determinada presentó trabajó y si es así
//			mostrar los datos del trabajo.

Algoritmo ejercicio3
	Definir Congreso, Cantidad_Trabajos, Trabajos, Linea1, Linea2, Linea3, Linea4 Como Entero;
	Definir Tematica, Moderador, Titulo, Autores, Opcion Como Cadena;
	
	Trabajos <- 0;
	Linea1 <- 0;
	Linea2 <- 0;
	Linea3 <- 0;
	Linea4 <- 0;
	
	Para Congreso <- 1 Hasta 4 Hacer
		Escribir "Ingrese la Tematica: ";
		Leer Tematica;
		Escribir "Ingrese el Moderador: ";
		Leer Moderador;
		Escribir "Ingrese la Cantidad de Trabajos: ";
		Leer Cantidad_Trabajos;
		
		Mientras (Trabajos <= Cantidad_Trabajos) Hacer
			Escribir "Ingrese el titulo: ";
			Leer Titulo;
			Escribir "Ingrese el autor: ";
			Leer Autor;
			Escribir "Ingrese la linea en la cual se presenta: ";
			Escribir "Las opciones son: ";
			Escribir "(1) - Dosencia en la postpandemia.";
			Escribir "(2) - Educacion superior como derecho.";
			Escribir "(3) - Investigacion.";
			Escribir "(4) - Extencion.";
			Leer Opcion;
			
			Segun (Opcion) Hacer
				'1' : Linea1 <- Linea1 + 1;
				'2' : Linea2 <- Linea2 + 1;
				'3' : Linea3 <- Linea3 + 1;
				'4' : Linea4 <- Linea4 + 1;
			FinSegun
			
			Trabajos <- Trabajos + 1;
		FinMientras
		Trabajos <- 0;
	FinPara
FinAlgoritmo
