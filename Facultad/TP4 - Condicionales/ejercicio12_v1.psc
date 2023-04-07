Algoritmo ejercicio12
    Definir Nombre1, Direccion1, Nombre2, Direccion2 Como Cadena;
    Definir Edad1, Edad2 Como Entero;
	
	Escribir "Ingrese los datos del primer socio: ";
	Escribir "Nombre: ";
	Leer Nombre1;
	Escribir "Direccion: ";
	Leer Direccion1;
	Escribir "Edad: ";
	Leer Edad1;
	
	Escribir "Ingrese los datos del primer socio: ";
	Escribir "Nombre: ";
	Leer Nombre2;
	Escribir "Direccion: ";
	Leer Direccion2;
	Escribir "Edad: ";
	Leer Edad2;
	
    Si (Edad1 < Edad2) Entonces
        Escribir Nombre1, "es el Socio mas Joven,  con la edad de ", Edad1, " años y direccion ", Direccion1;
    SiNo
        Escribir Nombre2, "es el Socio mas Joven,  con la edad de ", Edad2, " años y direccion ", Direccion2;
    FinSi    
FinAlgoritmo