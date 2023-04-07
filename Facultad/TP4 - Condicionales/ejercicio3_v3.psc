Algoritmo ejercicio3
	Definir Nombre Como Cadena;
    Definir Sueldo Como Real;
	
	Escribir "Ingrese el nombre del empleado: ";
    Leer Nombre;
	Escribir "Ingrese su sueldo: ";
	Leer Sueldo;
	
    Si (Sueldo > 30000) Entonces
        Escribir Nombre, " gana mas de $30000.";
    SiNo
        Si (Sueldo = 30000) Entonces
            Escribir Nombre, " gana $30000.";
        SiNo
            Si (Sueldo > 0) y (Sueldo < 30000) Entonces
                Escribir Nombre, " gana menos $30000.";
            SiNo
                Escribir "¡Error!, el sueldo ingresado no es valido.";
            FinSi
        FinSi
    FinSi
FinAlgoritmo
