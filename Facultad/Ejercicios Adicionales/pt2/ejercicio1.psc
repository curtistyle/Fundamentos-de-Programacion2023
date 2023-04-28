Algoritmo ejercicio1
	Definir Indice, Edad, Pythonizame, Pythonizame_Edad, Estudiante Como Entero;
	Definir Ninez, Adolescencia, Juventud, Adultez, Vejez Como Entero;
	Definir Estudiante_Ninez, Estudiante_Adolescencia, Estudiante_Juventud, Estudiante_Adultez, Estudiante_Vejez Como Entero;
	Definir Pagina, Ocupacion, Opcion Como Cadena;
	Definir Promedio Como Real;
	
	Indice <- 1;
	Ninez <- 0;
	Adolescencia <-0;
	Juventud <- 0;
	Adultez <- 0;
	Vejez <- 0;
	Pythonizame <- 0;
	Estudiante <- 0;
	Estudiante_Ninez <- 0;
	Estudiante_Adolescencia <- 0;
	Estudiante_Juventud <- 0;
	Estudiante_Adultez <- 0;
	Estudiante_Vejez <- 0;
	Opcion <- 's';
	
	Mientras (Opcion = 's') Hacer
		Escribir "Usuario (", Indice, "): ";
		
		Escribir "Ingrese la edad: ";
		Leer Edad;
		
		Escribir "Ingrese su Ocupacion: ";
		Leer Ocupacion;
		
		Escribir "Ingrese su Pagina Favorita: ";
		Leer Pagina;
		
		Si (Edad <= 11) Entonces
			Ninez <- Ninez + 1;
		SiNo
			Si (Edad >= 12) y (Edad <= 18) Entonces
				Adolescencia <- Adolescencia + 1;
			SiNo
				Si (Edad >= 19) y (Edad <= 30) Entonces
					Juventud <- Juventud + 1;
				SiNo
					Si (Edad >= 31) y (Edad <= 60) Entonces
						Adultez <- Adultez + 1;
					SiNo
						Vejez <- Vejez + 1;
					FinSi
				FinSi
			FinSi
		FinSi
		
		Si ((Pagina = 'Pythonizame') o (Pagina = 'pythonizame')) Entonces
			Pythonizame <- Pythonizame + 1;
			Pythonizame_Edad <- Pythonizame_Edad + Edad;
		FinSi
		
		Si (Ocupacion = 'estudiante') o (Ocupacion = 'Estudiante') Entonces
			Estudiante <- Estudiante + 1;
			Si (Edad <= 11) Entonces
				Estudiante_Ninez <- Estudiante_Ninez + 1;
			SiNo
				Si (Edad >= 12) y (Edad <= 18) Entonces
					Estudiante_Adolescencia <- Estudiante_Adolescencia + 1;
				SiNo
					Si (Edad >= 19) y (Edad <= 30) Entonces
						Estudiante_Juventud <- Estudiante_Juventud + 1;
					SiNo
						Si (Edad >= 31) y (Edad <= 60) Entonces
							Estudiante_Adultez <- Estudiante_Adultez + 1;
						SiNo
							Estudiante_Vejez <- Estudiante_Vejez + 1;
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
		
		Escribir "¿Quiere agregar a otro usuario?(s/n): ";
		Leer Opcion;
		Indice <- Indice + 1;
	FinMientras
	
	Indice <- Indice - 1;
	
	Escribir "Cantidad del seguidores por rango etario: ";
	Escribir " > Niñes: ", Ninez;
	Escribir " > Adolescencia: ", Adolescencia;
	Escribir " > Juventud: ", Juventud;
	Escribir " > Adultez: ", Adultez;
	Escribir " > Vejez: ", Vejez;
	Si (Ninez > Adolescencia) y (Ninez > Juventud) y (Ninez > Adultez) y (Ninez > Vejez) Entonces
		Escribir "El rango etario Niñes tiene mayor representatividad en la red social.";
	SiNo
		Si (Adolescencia > Ninez) y (Adolescencia > Juventud) y (Adolescencia > Adultez) y (Adolescencia > Vejez) Entonces
			Escribir "El rango etario Adolescencia tiene mayor representatividad en la red social.";
		SiNo
			Si ()
		FinSi
	FinSi
	
	Promedio <- Pythonizame_Edad / Pythonizame;
	Escribir "Cantidad de seguidosres de la pagina Pythonizame: ", Pythonizame ," y su promedio de edad es: ", Promedio,".";
	
	Escribir "Porcentaje de estudiantes en general: ", (Estudiante * 100) / Indice ,"%.";
	Escribir "Porcentaje de Estudiante por rango etario: ";
	Escribir " > Niñes: ", (Estudiante_Ninez * 100) / Indice;
	Escribir " > Adolescencia: ", (Estudiante_Adolescencia * 100) / Indice;
	Escribir " > Juventud: ", (Estudiante_Juventud * 100) / Indice;
	Escribir " > Adultez: ", (Estudiante_Adultez * 100) / Indice;
	Escribir " > Vejez: ", (Estudiante_Vejez * 100) / Indice;
	
FinAlgoritmo