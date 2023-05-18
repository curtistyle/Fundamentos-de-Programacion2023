//      En LinkedIn se registran los datos de sus usuarios. De cada uno se tiene:
//	    apellido y nombre, edad, profesión, área de desarrollo, si ha conseguido
//		trabajo por esta red e institución en la que se desarrolla. A fines estadísticos
//	    se desea calcular:
//		    a) Promedio de edad de los usuarios que desarrollan software.
//		    b) Porcentaje de usuarios que se desarrollan en el área sistemas o
//		       informática o software y entre ellos determinar además porcentaje de
//		       estudiantes.
//		    c) Indicar porcentaje de usuarios que han obtenido trabajo a través de esta
//		       red.
//		    d) Indicar además cantidad de personas que trabajan o estudian en
//		       universidades. (para este punto considerar si en institución comienzan
//			   declarando la palabra UNIVERSIDAD).

Algoritmo ejercicio4
	Definir Indice, Edad, Contador_Linkedin Como Entero;
	Definir Nombre, Apellido, Profesion, Area_Desarollo, Nombre_Institucion Como Cadena;
	Definir Acumulador_Edad_Software, Contador_Edad_Software, Contador_Sistemas, Contador_Areas Como Entero;
	Definir Contador_Estudiantes, Contador_Institucion Como Entero;
	Definir Opcion Como Caracter;
	Definir Estado Como Logico;
	
	Indice <- 0;
	Contador_Linkedin <- 0;
	Acumulador_Edad_Software <- 0;
	Contador_Edad_Software <- 0;
	Contador_Areas <- 0;
	Contador_Estudiantes <- 0;
	Estado <- Falso;
	
	
	Escribir "¿Quiere ingresar un nuevo usuario? (s/n).";
	Leer Opcion;
	
	Mientras ((Opcion = 's') o (Opcion = 'S')) Hacer
		Escribir " > Nombre: ";
		Leer Nombre;
		Escribir " > Apellido: ";
		Leer Apellido;
		Escribir " > Edad: ";
		Leer Edad;
		Escribir " > Profesion: ";
		Leer Profesion;
		Escribir " > Area de desarrollo: ";
		Leer Area_Desarollo;
		Escribir " > ¿Ha conseguido trabajo por LinkedId? (s/n): ";
		Leer Opcion;
		
		// Cuenta la cantidad de usuarios que consiguieron trabajo a travez de linkedin
		Si ((Opcion = 's') o (Opcion = 'S')) Entonces
			Contador_Linkedin <- Contador_Linkedin + 1;
		FinSi
		
		Escribir " > Nombre de la institucion en la que desarrolla software: ";
		Leer Nombre_Institucion;
		
		// Contador y acumulador para determinar el promedio de edad de los que desarrollan software
		Si ((Profesion = 'Desarrollo de software') o (Profesion = 'desarrollo de software')) Entonces
			Contador_Edad_Software <- Contador_Edad_Software + 1;
			Acumulador_Edad_Software <- Acumulador_Edad_Software + Edad;
		FinSi
		
		// Cuenta y determina la cantidad de usuarios trabajadores y usuarios estudiantes que estan en ciertas areas de desarrollos 
		// Usuarios trabajadores
		Segun Area_Desarollo Hacer
			'sistemas'    : Contador_Areas <- Contador_Areas + 1;
							Estado <- Verdadero;
			'informatica' : Contador_Areas <- Contador_Areas + 1; 
							Estado <- Verdadero;
			'software'    : Contador_Areas <- Contador_Areas + 1; 
							Estado <- Verdadero;
					FinSegun
		// Usuarios estudiantes
		Si (Estado = Verdadero) y ((Profesion = 'Estudiante') o (Profesion = 'estudiante')) Entonces
			Contador_Estudiantes <- Contador_Estudiantes + 1;
		FinSi
		Estado <- Falso;
		
		// Cuenta la cantidad de usuarios que trabajan en universidades
		Si ((Nombre_Institucion = 'Universidad') o (Nombre_Institucion = 'universidad')) Entonces
			Contador_Institucion <- Contador_Institucion + 1;
		FinSi
		
		Escribir "¿Quiere ingresar un nuevo usuario? (s/n).";
		Leer Opcion;
		
		Indice <- Indice + 1;
	FinMientras
	
	Si (Contador_Edad_Software > 0) Entonces
		Escribir "Promedio de edad de los usuarios que desarrollan software: ", Acumulador_Edad_Software / Contador_Edad_Software;
	FinSi
	
	Si (Contador_Areas > 0) Entonces
		Escribir "Porcentaje de usuarios que se desarrollan en el area de sistemas/informatica/software: ",(Contador_Areas * 100) / Indice,"%";
		Escribir "Porcentaje de estudiantes que se desarrollan en el arrea de sistemas/informatica/software: ", (Contador_Estudiantes * 100) / Contador_Areas,"%";
	FinSi
	
	Si (Contador_Linkedin > 0) Entonces
		Escribir "Porcentaje de usuarios que han obtenido trabajo a traves de Linkedin: ",(Contador_Linkedin * 100) / Indice;
	FinSi
	
	Si (Contador_Institucion > 0) Entonces
		Escribir "Porcentaje de estudiantes que trabajan en Universidades: ", (Contador_Institucion * 100) / Indice;
	FinSi
	
FinAlgoritmo
