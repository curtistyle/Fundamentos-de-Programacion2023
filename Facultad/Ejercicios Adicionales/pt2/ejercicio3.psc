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
	Definir Sede, Indice, Edad, Aux_Edad, Contador, Contador_Transplante, Contador_Enfermedad, Contador_Cancer, Edad_Joven Como Entero;
	Definir Opcion Como Caracter;
	Definir Nombre, Apellido, Tutor, Enfermedad_Preexistente Como Cadena;
	Definir Translante Como Logico;
	// (varaibles) Persona mas joven por Sede
	Definir Persona_MJ_UADER, Persona_MJ_Plaza, Persona_MJ_Dono Como Cadena;
	// (variables) Promedio de edad por lugar de ashesion
	Definir Sede_UADER, Sede_Plaza, Sede_Dono Como Entero;
	Definir Edad_UADER, Edad_Plaza, Edad_Dono Como Entero;
	Definir Edad_MJ_UADER, Edad_MJ_Plaza, Edad_MJ_Dono Como Entero;
	
	Sede_UADER <- 0;
	Edad_UADER <- 0;
	Sede_Plaza <- 0;
	Edad_Plaza <- 0;
	Sede_Dono <- 0;
	Edad_Dono <- 0;
	Indice <- 0;
	Contador <- 0;
	Contador_Transplante <- 0;
	Enfermedad_Preexistente <- ' ';
	Contador_Cancer <- 0;
	Edad_Joven <- 0;
	Edad_MJ_UADER <- 0;
	Edad_MJ_Plaza <- 0;
	Edad_MJ_Dono <- 0;
	
	Para Sede <- 1 Hasta 3 Hacer
		Segun Sede Hacer
			1 : Escribir "Facultad de Ciencias y Tecnologias UADER.";
			2 : Escribir "Plaza Ramirez.";
			3 : Escribir "Dono por vos.";
		FinSegun
		Aux_Edad <- 200;
		Escribir "Quiere agregar un donante (s/n): ";
		Leer Opcion;
		Mientras (Opcion = 's') Hacer
			Escribir " > Nombre: ";
			Leer Nombre;
			Escribir " > Apellido: ";
			Leer Apellido;
			Escribir " > Edad: ";
			Leer Edad;
			Si (Edad < 18) Entonces
				Escribir "Ingrese el nombre completo del tutor.";
				Leer Tutor;
			FinSi
			
			Escribir " > Enfermedad Preexistente: ";
			Leer Enfermedad_Preexistente;
			
			Si (Edad < 18) Entonces
				Escribir "*** Datos del donante menor de edad. ***";
				Escribir " > Nombre: ", Nombre;
				Escribir " > Apellido: ", Apellido;
				Escribir " > Edad: ", Edad;
				Escribir " > Tutor: ", Tutor;
			FinSi
			
			// Contador cantidad de donantes que fueron transplantados
			Escribir "El donante fue transplantado (s/n): ";
			Leer Opcion;
			Si (Opcion = 's') Entonces
				Contador_Transplante <- Contador_Transplante + 1;
			FinSi
			
			// Contador de donantes con Enfermedades Preexistente
			Si (Enfermedad_Preexistente <> ' ') Entonces
				Contador_Transplante <- Contador_Transplante + 1;
			FinSi
			// Contador que determina la cantidad de donantes con cancer
			Si (Enfermedad_Preexistente = 'cancer') o (Enfermedad_Preexistente = 'Cancer') Entonces
				Contador_Cancer <- Contador_Cancer + 1;
			FinSi
			Enfermedad_Preexistente <- ' ';
			
			Si (Sede = 1) Entonces
				// Contador y acumulador de edad Sede UADER
				Sede_UADER <- Sede_UADER + 1;
				Edad_UADER <- Edad_UADER + Edad;
				// Persona mas Joven de UADER
				Si (Edad < Aux_Edad) Entonces
					Aux_Edad <- Edad;
					Persona_MJ_UADER <- Nombre + ' ' + Apellido;
					Edad_MJ_UADER <- Edad;
				FinSi
			SiNo
				Si (Sede = 2) Entonces
					// Contador y acumulador de Plaza Ramirez
					Sede_Plaza <- Sede_Plaza + 1;
					Edad_Plaza <- Edad_Plaza + Edad;
					// Persona mas Joven de Plaza Ramirez
					Si (Edad < Aux_Edad) Entonces
						Aux_Edad <- Edad;
						Persona_MJ_Plaza <- Nombre + ' ' + Apellido;
						Edad_MJ_Plaza <- Edad;
					FinSi
				SiNo
					Si (Sede = 3) Entonces
						// Contador y acumulador de Sede Dono por vos
						Sede_Dono <- Sede_Dono + 1;
						Edad_Dono <- Edad_Dono + Edad;
						// Persona mas Joven de Sede Dono por vos
						Si (Edad < Aux_Edad) Entonces
							Aux_Edad <- Edad;
							Persona_MJ_Dono <- Nombre + ' ' + Apellido;
							Edad_MJ_Dono <- 0;
						FinSi
					FinSi
				FinSi
			FinSi
			Escribir "Desea agregar otro donante (s/n): ";
			Leer Opcion;
			Indice <- Indice + 1;
		FinMientras
	FinPara
	
	Escribir "Promedio de edad de los donantes de la Sede *UADER*: ", Edad_UADER/Sede_UADER;
	Escribir "Promedio de edad de los donantes de la Sede *Plaza Ramirez*: ", Edad_Plaza/Sede_Plaza;
	Escribir "Promedio de edad de los donantes de la Sede *Dono por vos:*", Edad_Plaza/Sede_Plaza;
	
	Escribir "Persona mas Joven de la Sede *UADER*";
	Escribir " > Nombre Completo: ", Persona_MJ_UADER;
	Escribir " > Edad: ", Edad_MJ_UADER;
	
	Escribir "Persona mas Joven de la Sede *Plaza Ramirez*";
	Escribir " > Nombre Completo: ", Persona_MJ_Plaza;
	
FinAlgoritmo
