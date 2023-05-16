// 3. Se tiene el listado de personas inscriptas para ser donantes de �rganos. Las
// mismas se registran en 3 lugares: Facultad de Ciencia y Tecnolog�a de
// UADER, Plaza Ram�rez y Sede de Dono por vos. Por cada donante se lee:
//	apellido y nombre, edad, enfermedad preexistente y si se ha realizado alg�n
//	trasplante. Se pide:
//		a) Promedio de edad por lugar de adhesi�n.
//		b) Persona m�s joven por sede (considerar que es �nico).
//		c) Listado de donantes menores de 18 a�os. En cada caso ingresar datos
//		del tutor.
// 		d) Porcentaje de trasplantados donantes sobre el total.
//      e) Indicar la cantidad de donantes con enfermedad preexistentes e indicar
//         adem�s la cantidad que han padecido c�ncer.

Algoritmo ejercicio3
	
	Definir Premedio Como Real;
	Definir Sede, Indice, Edad, Aux_Edad, Contador_Transplante, Contador_Enfermedad, Contador_Cancer Como Entero;
	Definir Opcion Como Caracter;
	Definir Nombre, Apellido, Tutor, Enfermedad_Preexistente Como Cadena;
	Definir Translante Como Logico;
	// (varaibles) Persona mas joven por Sede
	Definir Persona_MJ_UADER, Persona_MJ_Plaza, Persona_MJ_Dono Como Cadena;
	Definir Edad_MJ_UADER, Edad_MJ_Plaza, Edad_MJ_Dono Como Entero;
	// (variables) Promedio de edad por lugar de ashesion
	Definir Sede_UADER, Sede_Plaza, Sede_Dono Como Entero;
	Definir Edad_UADER, Edad_Plaza, Edad_Dono Como Entero;
	
	// Contadores
	Sede_UADER <- 0;
	Sede_Plaza <- 0;
	Sede_Dono <- 0;
	// Acumuladores
	Edad_UADER <- 0;
	Edad_Plaza <- 0;
	Edad_Dono <- 0;
	
	Enfermedad_Preexistente <- ' ';   
	
	Indice <- 0;                      // Cantidad Total de Donantes
	Contador_Transplante <- 0;        // Cantidad de Donantes con Transplantes
	Contador_Enfermedad <- 0;         // Cantidad de Donantes con Enfermadades Preexistentes
	Contador_Cancer <- 0;             // Cantidad de Donantes con Enfermedad: Cancer
	Edad_MJ_UADER <- 0;               // Edad Donante mas joven -UADER-
	Edad_MJ_Plaza <- 0;               // Edad Donante mas joven -Plaza ramirez-
	Edad_MJ_Dono <- 0;                // Edad Donante mas joven -Dono por vos-
	
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
			
			// Determina el rango de edad del donante, si es menor ingresamos el tutor
			Si (Edad < 18) Entonces
				Escribir "Ingrese el nombre completo del Tutor.";
				Leer Tutor;
			FinSi
			
			// Cuenta la cantidad de donadores con enfermedades preexistentes
			Escribir "�Tiene alguna enfermedad Preexistente? (s/n)";
			Leer Opcion;
			Si (Opcion = 's') o (Opcion = 'S') Entonces
				Escribir " > Enfermedad Preexistente: ";
				Leer Enfermedad_Preexistente;
				Contador_Enfermedad <- Contador_Enfermedad + 1;
				
				// Cuenta la cantidad de donadores con enfermedad: cancer
				Si (Enfermedad_Preexistente = 'cancer') o (Enfermedad_Preexistente = 'Cancer') Entonces
					Contador_Cancer <- Contador_Cancer + 1;
				FinSi
				Enfermedad_Preexistente <- ' ';
			FinSi
			
			// Muestra los datos de los donantes menores de edad (en cada ciclo -mientras-)
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
			
			
			Si (Sede = 1) Entonces                // Sede -UADER- 
				Sede_UADER <- Sede_UADER + 1;       // Contador de donadores
				Edad_UADER <- Edad_UADER + Edad;    // Acumulador para determinar promedio
				
				// Determina la Persona mas Joven de UADER
				Si (Edad < Aux_Edad) Entonces
					Aux_Edad <- Edad;
					Persona_MJ_UADER <- Nombre + ' ' + Apellido; // Concateno el nombre y el apellido de un donante en la misma variable
					Edad_MJ_UADER <- Edad;
				FinSi
			SiNo
				Si (Sede = 2) Entonces              // Sede -Plaza Ramirez-  
					Sede_Plaza <- Sede_Plaza + 1;     // Contador de donadores
					Edad_Plaza <- Edad_Plaza + Edad;  // Acumuldor para determinar promedio
					
					// Determina la Persona mas Joven de -Plaza Ramirez-
					Si (Edad < Aux_Edad) Entonces
						Aux_Edad <- Edad;
						Persona_MJ_Plaza <- Nombre + ' ' + Apellido; // Concateno nombre y apellido
						Edad_MJ_Plaza <- Edad;
					FinSi
				SiNo
					Si (Sede = 3) Entonces            // Sede -Dono por vos-
						Sede_Dono <- Sede_Dono + 1;     // Contador de donadores
						Edad_Dono <- Edad_Dono + Edad;  // Acumulador para determinar promedio
						
						// Determina la Persona mas Joven de Sede -Dono por vos-
						Si (Edad < Aux_Edad) Entonces
							Aux_Edad <- Edad;
							Persona_MJ_Dono <- Nombre + ' ' + Apellido; // Concateno nombre y apellido
							Edad_MJ_Dono <- Edad;
						FinSi
					FinSi
				FinSi
			FinSi
			Escribir "Desea agregar otro donante (s/n): ";
			Leer Opcion;
			Indice <- Indice + 1;         // Contador de todos los donantes de todas las sedes
		FinMientras
	FinPara
	
	Escribir "Promedio de edad de los donantes de la Sede *UADER*: ", Edad_UADER / Sede_UADER;
	Escribir "Promedio de edad de los donantes de la Sede *Plaza Ramirez*: ", Edad_Plaza / Sede_Plaza;
	Escribir "Promedio de edad de los donantes de la Sede *Dono por vos:*", Edad_Plaza / Sede_Plaza;
	
	Escribir "Persona mas Joven de la Sede *UADER*";
	Escribir " > Nombre Completo: ", Persona_MJ_UADER;
	Escribir " > Edad: ", Edad_MJ_UADER;
	
	Escribir "Persona mas Joven de la Sede *Plaza Ramirez*";
	Escribir " > Nombre Completo: ", Persona_MJ_Plaza;
	Escribir " > Edad: ", Edad_MJ_Plaza;
	
	Escribir "Persona mas Joven de la Sede *Dono por vos*";
	Escribir " > Nombre Completo: ", Persona_MJ_Dono;
	Escribir " > Edad: ", Edad_MJ_Dono;
	
	Escribir "Porcentaje del total de donadores transplandos: ", (Contador_Transplante * 100) / Indice,"%"; 
	Escribir "Cantidad de donantes con enfermedades preexistentes: ", Contador_Enfermedad;
	Escribir "Cantidad de donantes con cancer: ", Contador_Cancer;
	
FinAlgoritmo
