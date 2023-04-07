Algoritmo ejercicio14
    Definir Nombre1, Nombre2, Nombre3 Como Cadena;
	
	Escribir "Ingrese el primer nombre: ";
	Leer Nombre1;
	Escribir "Ingrese el segundo nombre: ";
	Leer Nombre2;
	Escribir "Ingrese el tercer nombre:";
	Leer Nombre3;
	
    Si (Nombre1 = 'Mariana Rios') Entonces
        Escribir "Mariana Rios esta en la lista.";
    SiNo
        Si (Nombre2 = 'Mariana Rios') Entonces
            Escribir "Mariana Rios esta en la lista.";
        SiNo
            Si (Nombre3 = 'Mariana Rios') Entonces
                Escribir "Mariana Rios esta en la lista.";
            SiNo
                Escribir "No existe en la lista.";
			FinSi
		FinSi
	FinSi
FinAlgoritmo