//  Se tienen los trabajos presentados para cada una de las cuatro l�neas de
//	un congreso de docentes binacional. De cada una se tienen tem�tica,
//	moderador y cantidad de trabajos. Se pide procesar cada uno de los
//  trabajos presentados teniendo en cuenta que de cada uno se lee: t�tulo,
//	autores y l�nea en la cual se presenta (docencia en la pospandemia,
//	educaci�n superior como derecho, investigaci�n y extensi�n).
//  Se pide:
//	     a. Total de trabajos por l�nea y en total.
//	     b. Determinar de cual l�nea se presentaron mas trabajos y el
//	        porcentaje que representa este n�mero en el total.
//	     c. Determinar si una autora determinada present� trabaj� y si es as�
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
