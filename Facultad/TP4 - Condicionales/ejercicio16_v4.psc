Algoritmo ejercicio16
    Definir Mes Como Entero;
	
	Escribir "Ingrese el Mes: ";
    Leer Mes;
	
    Segun Mes Hacer
		1, 3, 5, 7, 8, 10, 12 : Escribir "El Mes ", Mes ," tiene 31 dias.";
		4, 6, 9, 11 : Escribir "El Mes ", Mes ," tiene 30 dias.";
		2 : Escribir "El Mes ", Mes ," tiene 28 dias.";
        De otro modo:
            Escribir "Mes fuera de rango.";
    FinSegun
FinAlgoritmo