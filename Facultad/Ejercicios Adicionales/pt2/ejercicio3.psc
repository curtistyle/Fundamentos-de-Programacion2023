// 3. Se tiene el listado de personas inscriptas para ser donantes de órganos. Las
// mismas se registran en 3 lugares: Facultad de Ciencia y Tecnología de
// UADER, Plaza Ramírez y Sede de Dono por vos. Por cada donante se lee:
//	apellido y nombre, edad, enfermedad preexistente y si se ha realizado algún
//	trasplante. Se pide:
//		a) Promedio de edad por lugar de adhesión.
//		b) Persona más joven por sede (considerar que es único).
//		c) Listado de donantes menores de 18 años. En cada caso ingresar datos
//		del tutor.
// 		d) Porcentaje de trasplantados donantes sobre el total.
//      e) Indicar la cantidad de donantes con enfermedad preexistentes e indicar
//         además la cantidad que han padecido cáncer.

Algoritmo ejercicio3
	
	Definir Premedio Como Real;
	Definir Sede, Indice, Edad, Aux_Edad, Contador Como Entero;
	Definir Opcion Como Caracter;
	Definir Nombre, Apellido, Enfermedad_Preexistente Como Cadena;
	Definir Translante Como Logico;
	// (varaibles) Persona mas joven por Sede
	Definir Persona_MJ_UADER, Persona_MJ_Plaza, Persona_MJ_Dono Como Cadena;
	// (variables) Promedio de edad por lugar de ashesion
	Definir Cede_UADER, Cede_Plaza, Cede_Dono Como Entero;
	Definir Edad_UADER, Edad_Plaza, Edad_Dono Como Entero;
	
	Cede_UADER <- 0;
	Edad_UADER <- 0;
	Cede_Plaza <- 0;
	Edad_Plaza <- 0;
	Cede_Dono <- 0;
	Edad_Dono <- 0;
	Indice <- 1;
	Contador <- 0;
	
	Para Sede <- 1 Hasta 3 Hacer
		Segun Sede Hacer
			1 : Escribir "Facultad de Ciencias y Tecnologias UADER.";
			2 : Escribir "Plaza Ramirez.";
			3 : Escribir "Dono por vos.";
		FinSegun
		Aux_Edad <- 200;
		Escribir "Quiere agregar un donante (s/n): ";
		Mientras (Opcion = 's') Hacer
			Escribir " > Nombre: ";
			Leer Nombre;
			Escribir " > Apellido: ";
			Leer Apellido;
			Escribir " > Edad: ";
			Leer Edad;
			Escribir " > Enfermedad Preexistente: ";
			Leer Enfermedad_Preexistente;
			
			
			Si (Sede = 1) Entonces
				// Contador y acumulador de edad Sede UADER
				Cede_UADER <- Cede_UADER + 1;
				Edad_UADER <- Edad_UADER + Edad;
				// Persona mas Joven de UADER
				Si (Edad < Aux_Edad) Entonces
					Aux_Edad <- Edad;
					Persona_MJ_UADER <- Nombre + ' ' + Apellido;
				FinSi
			SiNo
				Si (Sede = 2) Entonces
					// Contador y acumulador de Plaza Ramirez
					Cede_Plaza <- Cede_Plaza + 1;
					Edad_Plaza <- Edad_Plaza + Edad;
					// Persona mas Joven de Plaza Ramirez
					Si (Edad < Aux_Edad) Entonces
						Aux_Edad <- Edad;
						Persona_MJ_Plaza <- Nombre + ' ' + Apellido;
					FinSi
				SiNo
					Si (Sede = 3) Entonces
						// Contador y acumulador de Sede Dono por vos
						Cede_Dono <- Cede_Dono + 1;
						Edad_Dono <- Edad_Dono + Edad;
						// Persona mas Joven de Sede Dono por vos
						Si (Edad < Aux_Edad) Entonces
							Aux_Edad <- Edad;
							Persona_MJ_Dono <- Nombre + ' ' + Apellido;
						FinSi
					FinSi
				FinSi
			FinSi
		Indice <- Indice + 1;
		FinMientras
	FinPara
FinAlgoritmo
