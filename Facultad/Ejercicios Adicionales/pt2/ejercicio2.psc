//  Se tienen las pel�culas candidatas al Oscar durante el per�odo 2020-2022.
//  De cada una se tiene: t�tulo, g�nero, protagonistas, origen y duraci�n (en
//  segundos). Suponer que se cargan por a�o. Se pide:
//	a) Cantidad de pel�culas argentinas.
//	b) Indicar si las pel�culas "La teor�a del todo" y "El c�digo enigma" fueron
//		candidatas, si es as� mostrar sus protagonistas y el g�nero al que
//			pertenecen.
//			c) Mostrar porcentaje de pel�culas brasileras.
//			d) T�tulo de la pel�cula con mayor duraci�n.
//			e) Indicar el a�o en que m�s pel�culas se propusieron como candidatas.


Algoritmo ejercicio2
	Definir Indice Como Entero;
	Definir Titulo, Genero, Protagonista, Origen, Opcion Como Cadena;
	Definir Origen_Argentina, Origen_Brasil, Duracion, Duracion_Maxima, Anio, Anio_2020, Anio_2021, Anio_2022 Como Entero;
	Definir Candidata_Protagonista1, Candidata_Genero1, Candidata_Protagonista2, Candidata_Genero2, Titulo_Maxima_Duracion Como Cadena;
	Definir Estado Como Logico;
	
	Estado <- Verdadero;
	Indice <- 0;
	Duracion_Maxima <- 0;
	Candidata_Protagonista1 <- '';
	Candidata_Genero1 <- '';
	Candidata_Protagonista2 <- ''; 
	Candidata_Genero2 <- '';
	Anio_2020 <- 0;
	Anio_2021 <- 0;
	Anio_2022 <- 0;
	
	Escribir "Quiere ingresar una pelicula(s/n): ";
	Leer Opcion;
	Mientras (Opcion = 's') Hacer
		Estado <- Verdadero;
		
		Escribir "Ingrese el titulo: ";
		Leer Titulo;
		
		Escribir "Ingrese el anio: ";
		Leer Anio;
		
		Escribir "Ingrese el Genero: ";
		Leer Genero;
		
		Escribir "Ingrese el Protagonista: ";
		Leer Protagonista;
		
		Escribir "Ingrese el Origen: ";
		Leer Origen;
		
		Escribir "Ingrese la duracion: ";
		Leer Duracion;
		
		Si (Anio = 2020) Entonces
			Anio_2020 <- Anio_2020 + 1;
		SiNo
			Si (Anio = 2021) Entonces
				Anio_2021 <- Anio_2021 + 1;
			SiNo
				Si (Anio = 2022) Entonces
					Anio_2022 <- Anio_2022 + 1;
				SiNo
					Escribir "Anio fuera de rango!";
					Estado <- Falso;
					Indice <- Indice - 1;
				FinSi
			FinSi
		FinSi
		
		// Cantidad de peliculas argentinas
		Si (((Origen = 'argentina') o (Origen = 'Argentina')) y (Estado = Verdadero)) Entonces
			Origen_Argentina <- Origen_Argentina + 1;
		FinSi
		
		// Cantidad de peliculas brazileras
		Si (((Origen = 'Brazil') o (Origen = 'brazil')) y (Estado = Verdadero)) Entonces
			Origen_Brasil <- Origen_Brasil + 1;
		FinSi
		
		//"La teor�a del todo" y "El c�digo enigma"
		Si (((Titulo = 'La teoria del todo') o (Titulo = 'la teoria del todo')) y (Estado = Verdadero)) Entonces
			Candidata_Genero1 <- Genero;
			Candidata_Protagonista1 <- Protagonista;
		SiNo
			Si (((Titulo = 'El codigo enigma') o (Titulo = 'el codigo enigma')) y (Estado = Verdadero)) Entonces
				Candidata_Genero2 <- Genero;
				Candidata_Protagonista2 <- Protagonista;
			FinSi
		FinSi
		
		// Pelicula con mayor duraci�n
		Si ((Duracion > Duracion_Maxima) y (Estado = Verdadero)) Entonces
			Duracion_Maxima <- Duracion;
			Titulo_Maxima_Duracion <- Titulo;
		FinSi
		
		Escribir "Quiere ingresar una pelicula(s/n): ";
		Leer Opcion;
		
		Indice <- Indice + 1;
	FinMientras
	
	Escribir "Cantidad de peliculas Argentinas: ", Origen_Argentina;
	Escribir "Porcentaje de peliculas Brazileras: ", (Origen_Brazil * 100) / Indice;
	Escribir "Titulo de la pelicula con mayor duracion: ", Titulo_Maxima_Duracion;
	
	Si (Candidata_Protagonista1 <> '') y (Candidata_Protagonista2 <> '') Entonces
		Escribir "Las peliculas -La Teoria del todo- y -El codigo enigma- fueron candidatas.";
		Escribir "La teoria del todo: ";
		Escribir " > Genero: ", Candidata_Genero1;
		Escribir " > Protagonista: ", Candidata_Protagonista1;
		Escribir "El codigo enigma: ";
		Escribir " > Genero: ", Candidata_Genero2;
		Escribir " > Protagonista: ", Candidata_Protagonista2;
	FinSi
	
	Si (Anio_2020 > Anio_2021) y (Anio_2020 > Anio_2022) Entonces
		Escribir "Se propusieron como candidatas en 2020 la mayor cantidad de peliculas.";
	SiNo
		Si (Anio_2021 > Anio_2020) y (Anio_2021 > Anio_2022) Entonces
			Escribir "Se propusieron como candidatas en 2021 la mayor cantidad de peliculas.";
		SiNo
			Si (Anio_2022 > Anio_2021) y (Anio_2022 > Anio_2020) Entonces
				Escribir "Se propusieron como candidatas en 2022 la mayor cantidad de peliculas.";
			SiNo
				Si (Anio_2020 = Anio_2021) y (Anio_2020 > Anio_2022) Entonces
					Escribir "Se propusieron como candidatas en 2020 y 2021 la mayor cantidad de peliculas.";
				SiNo
					Si (Anio_2020 = Anio_2022) y (Anio_2020 > Anio_2021) Entonces
						Escribir "Se propusieron como candidatas en 2020 y 2022 la mayor cantidad de peliculas.";
					SiNo
						Escribir "Se propusieron como candidatas en 2021 y 2022 la mayor cantidad de peliculas.";
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
