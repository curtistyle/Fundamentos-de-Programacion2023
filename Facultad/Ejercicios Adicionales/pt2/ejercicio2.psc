//. Se tienen las pel�culas candidatas al Oscar durante el per�odo 2020-2022.
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
	Definir Origen_Argentina, Origen_Brasil, Duracion, Duracion_Maxima Como Entero;
	Definir Candidata_Protagonista1, Candidata_Genero1, Candidata_Protagonista2, Candidata_Genero2, Titulo_Maxima_Duracion Como Cadena;
	
	Duracion_Maxima <- 0;
	Candidata_Protagonista1 <- '';
	Candidata_Genero1 <- '';
	Candidata_Protagonista2 <- ''; 
	Candidata_Genero2 <- '';
	
	
	Escribir "Quiere ingresar una pelicula(s/n): ";
	Leer Opcion;
	Mientras (Opcion = 's') Hacer
		Escribir "Ingrese el titulo: ";
		Leer Titulo;
		
		Escribir "Ingrese el Genero: ";
		Leer Genero;
		
		Escribir "Ingrese el Protagonista: ";
		Leer Protagonista;
		
		Escribir "Ingrese el Origen: ";
		Leer Origen;
		
		Escribir "Ingrese la duracion: ";
		Leer Duracion;
		
		Escribir "Quiere ingresar una pelicula(s/n): ";
		Leer Opcion;		
		
		Si ((Origen = 'argentina') o (Origen = 'Argentina')) Entonces
			Origen_Argentina <- Origen_Argentina + 1;
		FinSi
		
		Si ((Origen = 'Brazil') o (Origen = 'brazil')) Entonces
			Origen_Brasil <- Origen_Brasil + 1;
		FinSi
		
		//"La teor�a del todo" y "El c�digo enigma"
		Si (Titulo = 'La teoria del todo') Entonces
			Candidata_Genero1 <- Genero;
			Candidata_Protagonista1 <- Protagonista;
		SiNo
			Si (Titulo = 'El codigo enigma') Entonces
				Candidata_Genero2 <- Genero;
				Candidata_Protagonista2 <- Protagonista;
			FinSi
		FinSi
		
		Si (Duracion > Duracion_Maxima) Entonces
			Duracion_Maxima <- Duracion;
			Titulo_Maxima_Duracion <- Titulo;
		FinSi
		
	FinMientras
	
FinAlgoritmo
